# django-presigned-url

Generate presigned urls for django.

## Getting started

### Installation

**Requirements**
- poetry

### Usage
Install `django-presigned-urls` in your django project and import the relevant functions.

```sh
poetry add django_presigned_urls
```

```python
from django_presigned_url.presign_urls import (
    make_presigned_url,
    verify_presigned_request,
)

make_presigned_url(reverse("file-download"), request)
verify_presigned_request(reverse("file-download"), request)
```


### Configuration
You can configure `django-presigned-urls` with your django settings.

- `PRESIGNED_URL_LIFETIME`: how long the url is valid in seconds (default: 3600)

