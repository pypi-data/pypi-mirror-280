# discover-plugins

[![PyPI - Version](https://img.shields.io/pypi/v/discover-plugins.svg)](https://pypi.org/project/discover-plugins)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discover-plugins.svg)](https://pypi.org/project/discover-plugins)

-----

## Rationale

`discover-plugins` is a utility to find installed plugins for a python environment.


## Installation

```console
pipx install discover-plugins
```

## Usage

By default, `discover-plugins` will look for plugins for the current python interpreter. You can specify the
interpreter to use with `--interpreter`.

You can filter plugins by `group`, `name` and `value`. To find all plugins related to `pytest` run:

```console
discover-plugins --group pytest11
```

Output:
```json
{
  "pytest11": [
    {
      "name": "pytest_httpx",
      "group": "pytest11",
      "value": "pytest_httpx"
    },
    {
      "name": "anyio",
      "group": "pytest11",
      "value": "anyio.pytest_plugin"
    },
    {
      "name": "pytest-aws-apigateway",
      "group": "pytest11",
      "value": "pytest_aws_apigateway.plugin"
    }
  ]
}

```

## License

`discover-plugins` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
