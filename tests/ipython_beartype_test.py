import ipython_beartype
import pytest

def test_smoke()->None:
    """Smoke test for the ipython_beartype package."""
    assert ipython_beartype.__version__ is not None, "Version should not be None"
    assert hasattr(ipython_beartype, "load_ipython_extension"), "Function should exist"