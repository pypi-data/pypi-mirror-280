# klabmodels

Kodelab data models for AI product suite

### Build Instructions

#### Install Required tools

`pip install setuptools wheel`

#### Build the Package

```
pip install build
python -m build
```

#### Upload package

```
pip install twine
twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

### Usage

#### Create a GitHub Personal Access Token

1. Go to GitHub > Settings > Developer settings > Personal access tokens.
2. Generate a new token with write:packages and read:packages scopes.

#### Configure pip to Use GitHub Packages

Create or edit ~/.pip/pip.conf to include your GitHub Packages URL:

```
[global]
extra-index-url = https://<GITHUB_USERNAME>:<GITHUB_TOKEN>@pypi.github.com/<GITHUB_USERNAME>

```

### Import the package

` pip install klabmodels`
