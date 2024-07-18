import hashlib
from datetime import timedelta

from django.conf import settings
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from django.utils import timezone
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext


def make_signature_components(
    path: str,
    hostname: str,
    expires: int | None = None,
    scheme: str = "http",
) -> tuple[str, int, str]:
    """
    Make the components used to sign and verify the url.

    If `expires` is provided the components are called for the verification step.

    Otherwise expiry is calculated and returned
    """
    if not expires:
        expires = int(
            (
                timezone.now()
                + timedelta(seconds=getattr(settings, "PRESIGNED_URL_LIFETIME", 3600))
            ).timestamp()
        )
    host = f"{scheme}://{hostname}"
    url = f"{host.strip('/')}{path}"
    token = f"{url}{expires}{settings.SECRET_KEY}"
    hash = hashlib.shake_256(token.encode())
    # Django's base64 encoder strips padding and ascii-decodes the output
    signature = urlsafe_base64_encode(hash.digest(32))
    return url, expires, signature


def verify_signed_components(
    path: str, hostname: str, expires: int, scheme: str, token_sig: str
) -> bool:
    """
    Verify a presigned download URL.

    It tests against expiry and signature integrity
    raises a `ValidationError` if either test fails
    returns `True` otherwise.
    """
    now = timezone.now()
    host, expires, signature = make_signature_components(
        path, hostname, expires, scheme
    )

    if int(now.timestamp()) > expires:
        raise ValidationError(gettext("Presigned URL expired."))
    if not token_sig == signature:
        raise ValidationError(gettext("Invalid signature."))

    return True


def make_presigned_url(path: str, request: HttpRequest) -> str:
    """Make a presigned URL with `expires` and `signature` as the query paramters."""
    url, expires, signature = make_signature_components(
        path,
        request.get_host(),
        scheme=request.META.get("wsgi.url_scheme", "http"),
    )

    return f"{url}?expires={expires}&signature={signature}"


def verify_presigned_request(path: str, request: HttpRequest) -> bool:
    """Verify a presigned URL from `expires` and `signature` query parameters."""
    if token_sig := request.GET.get("signature"):
        return verify_signed_components(
            path=path,
            hostname=request.get_host(),
            expires=int(request.GET.get("expires", "-1")),
            scheme=request.META.get("wsgi.url_scheme", "http"),
            token_sig=token_sig,
        )

    return False
