# GeometryBackendSdkPython

[ShapeDiver](https://www.shapediver.com/) is a cloud platform for building online applications
based on parametric 3D files made with [Rhinoceros 3D](https://www.rhino3d.com/) and
[Grasshopper](https://www.grasshopper3d.com/).

Using the **ShapeDiver Geometry Backend API** allows access to ShapeDiver models without using the
**ShapeDiver Viewer**. This SDK provides functionality to communicate with the Geometry Backend API
**version 2**, and includes type hints describing request and response data objects. See the
[API documentation](https://sdeuc1.eu-central-1.shapediver.com/api/v2/docs/) for more details.

## Making Changes & Contributing

Most of the code in this repository has been generated via the
[OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator). The specification of the
Geometry Backend API version 2 can be found in the
[ShapeDiver OAS](https://github.com/shapediver/OpenApiSpecifications/blob/main/geometry_backend_v2.yaml)
repository. Additionally, we have added wrappers and utility functions to improve overall
usability.

### Prerequisites

This project is written in _Python 3_ and uses version **3.9.x**. For Unix systems, we recommend
[pyenv](https://github.com/pyenv/pyenv) to install and manage multiple Python versions. Once
installed, run the following commands:

```bash
pyenv install -v 3.9
pyenv global 3.9
```

Additionally, we use some tools for various tasks. We recommend
[pipx](https://github.com/pypa/pipx) to install Python applications in isolation. Once installed,
run the following commands:

```bash
pipx install pre-commit
pipx install twine
pipx install tox
pipx install pyscaffold
```

Project-specific commands are handled via [just](https://github.com/casey/just), so install this
tool as well. To get an overview of all available commands, run `just --list`.

### Setup

This project makes use of [virtual environments](https://docs.python.org/3/library/venv.html) to
manage Python packages. Run the following commands to create a new virtual environment (`.venv`)
and to install all dependencies:

```bash
just setup
source .venv/bin/activate
pre-commit install
```

It is a good idea to update the hooks to the latest version via `pre-commit autoupdate`.

## Generate Code

To re-generate the code from the
[ShapeDiver OAS](https://github.com/shapediver/OpenApiSpecifications/blob/main/geometry_backend_v2.yaml)
file, you need to install version 7 of the
[OpenAPI Generator](https://github.com/OpenAPITools/openapi-generator?tab=readme-ov-file#1---installation).
We recommend installing it as a global NPM package:

```bash
npm i -g openapi-generator
```

Afterwards, update the local file `./oas_spec.yaml` and generate the new code via
`just generate <version>`. The _version_ argument represents the respective Git tag from
[ShapeDiver OAS](https://github.com/shapediver/OpenApiSpecifications/tags). For instance, use
version "1.0.0" when targeting the Git tag "gb_v2@1.0.0".

## Release

To release new versions of this package, create the file `~/.pypirc` with the following content:

```txt
[distutils]
index-servers =
  pypi
  testpypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = <token of main user>

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = <token of test user>
```

Afterwards, run `just release <version>` to build, publish, and commit a new version of the Python
package. The _version_ argument represents the new version of the package.

## Note

This project has been set up using _PyScaffold 4.5_. See [PyScaffold](https://pyscaffold.org/) for
details and additional information.
