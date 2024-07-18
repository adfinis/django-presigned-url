import pytest
from django.core.exceptions import ValidationError
from django.http import HttpRequest
from freezegun import freeze_time

from django_presigned_url.presign_urls import (
    make_presigned_url,
    verify_presigned_request,
)


@pytest.fixture(autouse=True, scope="session")
def setup_django():
    import django
    from django.conf import settings

    settings.configure(
        USE_TZ=True,
        SECRET_KEY="foobar",
        ALLOWED_HOSTS=["example.com"],
        # package setting
        PRESIGNED_URL_LIFETIME=3600,
    )
    django.setup()


@pytest.fixture
def req():
    req = HttpRequest()
    req.META["HTTP_HOST"] = "example.com"
    return req


@freeze_time("2024-02-02")
def test_make_presigned_url(req):
    presigned = make_presigned_url("/download/1", req)
    assert (
        presigned
        == "http://example.com/download/1?expires=1706835600&signature=yI7rCgdttNzH6hhgzawcc5Y-VWiFM4RZ-amlZyV-jKI"
    )


@freeze_time("2024-02-02")
def test_verify_presigned_request(req):
    req.GET = {
        "expires": "1706835600",
        "signature": "yI7rCgdttNzH6hhgzawcc5Y-VWiFM4RZ-amlZyV-jKI",
    }
    assert verify_presigned_request("/download/1", req)


def test_verify_unsigned_request(req):
    req.GET = {}
    assert not verify_presigned_request("/download/1", req)


@freeze_time("2024-02-02")
@pytest.mark.parametrize(
    "query_params,error_text",
    [
        (
            {
                "expires": "1706749200",
                "signature": "KumiLhKy-Qw_9Tm89hnPJCdRnFF78Su1cxYB_TVVqIM",
            },
            "Presigned URL expired.",
        ),
        (
            {
                "signature": "KumiLhKy-Qw_9Tm89hnPJCdRnFF78Su1cxYB_TVVqIM",
            },
            "Presigned URL expired.",
        ),
        (
            {
                "expires": "1706835600",
                "signature": "gimme",
            },
            "Invalid signature.",
        ),
    ],
)
def test_verify_presigned_request_error(req, query_params, error_text):
    req.GET = query_params
    with pytest.raises(ValidationError) as exception:
        verify_presigned_request("/download/1", req)
    assert error_text in str(exception.value)
