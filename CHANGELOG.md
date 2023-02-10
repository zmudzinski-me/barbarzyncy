# Changelog

## [Unreleased]

- Add optional Mailhog support for the local and K8S environments.

## [2019.05.31]

- Use Gitlab CI instead of Jenkins
- Add Helm chart for Kubernetes deployment

## [2019.05.15]

- Switch to [Calendar Versioning](https://calver.org/), as this tool is supposed to be used once per project, with no upgrade path in mind.
- The format to use from now onwards is `YYYY.0M.0D`.
- Update to Python 3.7.3.
- Update to Django 2.2.
- Update `Pipfile.lock` with recent versions of dependencies.
- Install dependencies to a virtualenv owned by application user, instead of global site-packages.
- Split out `CHANGELOG.md` file

## [0.0.1] - 2019-03-28

- Initial release.
- Use Python 3.6.8 and Django 2.1.
- Add linting and autoformatting via `isort`, `black`, `flake8`, `mypy`.
- Include support for <https://pypi.mrx.gd> PyPI index and wheelstore.
- Use `Pipenv` as package manager.
- Setup `pytest` configured with `coverage`, `freezegun` and `django` plugins, and `factory_boy` for creating test model instances.
- Define Python project structure, where application code lives in `src/`, and tests are in `tests/`.
- Create Django REST framework-centric template.
- Include `djoser`, `django-cors-headers`, `django-rest-swagger`, `django-storages`, `django-rest-framework-simplejwt`, `sentry-sdk`, `psycopg2`, `django-debug-toolbar` as dependencies.
- Use `django-environ` for accessing env vars.
- Include Jenkins support.
- Create `docker-compose` files for local and CI environments.
- Include AWS support by `django-storages` and tweaking `uwsgi.ini` to work with AWS ALB.

[Unreleased]: https://gitlab.com/merixstudio/pts/django-project-template/compare/2019.05.15...master
[2019.05.15]: https://gitlab.com/merixstudio/pts/django-project-template/tree/2019.05.15
[0.0.1]: https://gitlab.com/merixstudio/pts/django-project-template/tree/0.0.1
