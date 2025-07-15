![https://beartype.readthedocs.io](https://raw.githubusercontent.com/beartype/beartype-assets/main/banner/logo.png)

# ipython-beartype

IPython extension type-checking IPython environments with beartype.

## Installation

```console
pip install ipython_beartype
```

## Usage

Within an IPython / Jupyter notebook session, do the following:

```python
%load_ext ipython_beartype
%beartype
```

All the type annotations in the following cells will be type checked.

## Local Development / Testing

- Create and activate a virtual environment
- Run `pip install -e .[dev]` to do an editable install
- Run `pytest` to run tests

## Type Checking

Run `mypy .`

## Credits

Thanks to [knyazer](https://github.com/knyazer) and
[patrick-kidger](https://github.com/patrick-kidger) for building the `jaxtyping`
IPython extension, which was used as the base for this extension.

Also special thanks to [leycec](https://github.com/leycec) for creating beartype
and the IPython team.
