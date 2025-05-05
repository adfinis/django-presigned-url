# CHANGELOG


## v0.1.1 (2025-05-05)

### Bug Fixes

- **request**: Use request.scheme to determine the scheme of the request
  ([`344d5bc`](https://github.com/adfinis/django-presigned-url/commit/344d5bc7c0c98669e53ffa945e57185e061c606d))

Previously, we used `wsgi.url_scheme` on `request.META` which is being set by the WSGI server
  (gunicorn, uwsgi, hurricane etc.) and seems to be unreliable as the value differs depending on the
  used server.

### Build System

- Add build command to semantic release
  ([`85fec71`](https://github.com/adfinis/django-presigned-url/commit/85fec718805b7bd006cc04448299bf46f6b037da))

- Add github action release script
  ([`3b9eff7`](https://github.com/adfinis/django-presigned-url/commit/3b9eff7dc28e749e871f32636ec01a835b4af75d))

### Chores

- **deps**: Bump django from 5.0.7 to 5.1.1
  ([`969ea66`](https://github.com/adfinis/django-presigned-url/commit/969ea66e80ea7b43be7afbf555ca9bbead14259d))

Bumps [django](https://github.com/django/django) from 5.0.7 to 5.1.1. -
  [Commits](https://github.com/django/django/compare/5.0.7...5.1.1)

--- updated-dependencies: - dependency-name: django dependency-type: direct:production

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump django from 5.1.1 to 5.1.4
  ([`ac7a0ff`](https://github.com/adfinis/django-presigned-url/commit/ac7a0ff6bde42a67e04414d72c29bec6c850a20e))

Bumps [django](https://github.com/django/django) from 5.1.1 to 5.1.4. -
  [Commits](https://github.com/django/django/compare/5.1.1...5.1.4)

--- updated-dependencies: - dependency-name: django dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump django from 5.1.4 to 5.1.6
  ([`1e45a6b`](https://github.com/adfinis/django-presigned-url/commit/1e45a6bbe6b3e45dc407e55442eb748b5511fcd1))

Bumps [django](https://github.com/django/django) from 5.1.4 to 5.1.6. -
  [Commits](https://github.com/django/django/compare/5.1.4...5.1.6)

--- updated-dependencies: - dependency-name: django dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps**: Bump django from 5.1.6 to 5.1.8
  ([`59e3f8e`](https://github.com/adfinis/django-presigned-url/commit/59e3f8e2fdce0beeaa7237000b80afbd3a6134e0))

Bumps [django](https://github.com/django/django) from 5.1.6 to 5.1.8. -
  [Commits](https://github.com/django/django/compare/5.1.6...5.1.8)

--- updated-dependencies: - dependency-name: django dependency-version: 5.1.8

dependency-type: direct:production

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump pytest from 8.2.2 to 8.3.4
  ([`7f5f3d5`](https://github.com/adfinis/django-presigned-url/commit/7f5f3d5391f83364a3fd861f780c34f558b57866))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.2.2 to 8.3.4. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.2.2...8.3.4)

--- updated-dependencies: - dependency-name: pytest dependency-type: direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump pytest from 8.3.4 to 8.3.5
  ([`a4127e8`](https://github.com/adfinis/django-presigned-url/commit/a4127e83339a53bc5492d9f72255d9a2de24ef4f))

Bumps [pytest](https://github.com/pytest-dev/pytest) from 8.3.4 to 8.3.5. - [Release
  notes](https://github.com/pytest-dev/pytest/releases) -
  [Changelog](https://github.com/pytest-dev/pytest/blob/main/CHANGELOG.rst) -
  [Commits](https://github.com/pytest-dev/pytest/compare/8.3.4...8.3.5)

--- updated-dependencies: - dependency-name: pytest dependency-type: direct:development

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump python-semantic-release from 9.15.1 to 9.19.1
  ([`2971ddc`](https://github.com/adfinis/django-presigned-url/commit/2971ddc64fa79665ac854b5f2ef793bf07c95677))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.15.1 to 9.19.1. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.rst)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.15.1...v9.19.1)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump python-semantic-release from 9.19.1 to 9.21.0
  ([`c52d39b`](https://github.com/adfinis/django-presigned-url/commit/c52d39b5084d2ff148fd1dda8d383cf4db631063))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.19.1 to 9.21.0. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.rst)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.19.1...v9.21)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump python-semantic-release from 9.8.5 to 9.8.8
  ([`1eeb022`](https://github.com/adfinis/django-presigned-url/commit/1eeb022cd5e8a9fa8c52773e741e5e4fab0969e9))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.8.5 to 9.8.8. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.5...v9.8.8)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:development

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump python-semantic-release from 9.8.8 to 9.15.1
  ([`3be07ad`](https://github.com/adfinis/django-presigned-url/commit/3be07adc3703203a92cc47b8ce498dff06d9376a))

Bumps [python-semantic-release](https://github.com/python-semantic-release/python-semantic-release)
  from 9.8.8 to 9.15.1. - [Release
  notes](https://github.com/python-semantic-release/python-semantic-release/releases) -
  [Changelog](https://github.com/python-semantic-release/python-semantic-release/blob/master/CHANGELOG.md)
  -
  [Commits](https://github.com/python-semantic-release/python-semantic-release/compare/v9.8.8...v9.15.1)

--- updated-dependencies: - dependency-name: python-semantic-release dependency-type:
  direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump ruff from 0.5.2 to 0.5.3
  ([`ea92300`](https://github.com/adfinis/django-presigned-url/commit/ea9230034d985edcc28a95286df24740b3d5ac16))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.5.2 to 0.5.3. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.2...0.5.3)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:development

update-type: version-update:semver-patch ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump ruff from 0.5.3 to 0.6.4
  ([`4afa0cf`](https://github.com/adfinis/django-presigned-url/commit/4afa0cf5bfe1fb74d092354f193058aec7c6da95))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.5.3 to 0.6.4. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.5.3...0.6.4)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump ruff from 0.6.4 to 0.9.6
  ([`480e354`](https://github.com/adfinis/django-presigned-url/commit/480e354b3eec6bac3ed0d8742d29789e83cd9eef))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.6.4 to 0.9.6. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.6.4...0.9.6)

--- updated-dependencies: - dependency-name: ruff dependency-type: direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>

- **deps-dev**: Bump ruff from 0.9.6 to 0.11.8
  ([`38d321f`](https://github.com/adfinis/django-presigned-url/commit/38d321f8fa4dff72fa5ed6b41fd4d83eb54699ca))

Bumps [ruff](https://github.com/astral-sh/ruff) from 0.9.6 to 0.11.8. - [Release
  notes](https://github.com/astral-sh/ruff/releases) -
  [Changelog](https://github.com/astral-sh/ruff/blob/main/CHANGELOG.md) -
  [Commits](https://github.com/astral-sh/ruff/compare/0.9.6...0.11.8)

--- updated-dependencies: - dependency-name: ruff dependency-version: 0.11.8

dependency-type: direct:development

update-type: version-update:semver-minor ...

Signed-off-by: dependabot[bot] <support@github.com>


## v0.1.0 (2024-07-19)

### Chores

- Add GPLv3 license
  ([`881420a`](https://github.com/adfinis/django-presigned-url/commit/881420a645c1f389278165a6e165b8c878228cb1))

- Add python semantic release
  ([`f64b54c`](https://github.com/adfinis/django-presigned-url/commit/f64b54c04851bef5ff2f9196e1397e5f7f98239c))

### Features

- Implement django-presigned-url
  ([`f47dc85`](https://github.com/adfinis/django-presigned-url/commit/f47dc8581d6d36e9bdb82ba4bdba3e0fefb50b54))
