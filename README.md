# ipython-beartype

IPython extension type-checking IPython environments with beartype.

## Installation

```bash
pip install ipython_beartype
```

## Usage

Within an IPython / Jupyter notebook session, do the following:

```console
%load_ext ipython_beartype
%beartype
```

All the type annotations in the following cells will be type checked.

## Local Development / Testing

- Create and activate a virtual environment
- Run `pip install -r requirements-dev.txt` to do an editable install
- Run `pytest` to run tests

## Type Checking

Run `mypy .`

## Create and upload a package to PyPI

Make sure to bump the version in `setup.cfg`.

Then run the following commands:

```bash
rm -rf build dist
python setup.py sdist bdist_wheel
```

Then upload it to PyPI using [twine](https://twine.readthedocs.io/en/latest/#installation):

```bash
twine upload dist/*
```

## Credits

Thanks to [knyazer](https://github.com/knyazer) and
[patrick-kidger](https://github.com/patrick-kidger) for building the `jaxtyping`
IPython extension, which was used as the base for this extension.

Also special thanks to [leycec](https://github.com/leycec) for creating beartype
and the IPython team.
