#!/usr/bin/env python3
# --------------------( LICENSE                            )--------------------
# Copyright (c) 2014-2025 Beartype authors.
# See "LICENSE" for further details.

'''
**ipython-beartype,** an IPython extension type-checking IPython environments
with :mod:`beartype`.
'''

# ....................{ IMPORTS                            }....................
from beartype.claw._ast.clawastmain import BeartypeNodeTransformer
from beartype import BeartypeConf
from IPython.core.interactiveshell import InteractiveShell

# ....................{ GLOBALS                            }....................
__version__ = '0.3.0'
'''
Human-readable package version as a ``.``-delimited string.

For :pep:`8` compliance, this specifier has the canonical name ``__version__``
rather than that of a typical global (e.g., ``VERSION_STR``).

Note that this is the canonical version specifier for this package. Indeed, the
top-level ``pyproject.toml`` file dynamically derives its own ``version`` string
from this string global.

See Also
--------
pyproject.toml
   The Hatch-specific ``[tool.hatch.version]`` subsection of the top-level
   ``pyproject.toml`` file, which parses its version from this string global.
'''

# ....................{ PLUGINS                            }....................
def load_ipython_extension(ipython: InteractiveShell) -> None:

    # The import is local to avoid degrading import times when the magic is
    # not needed.
    from IPython.core.magic import line_magic, Magics, magics_class

    @magics_class
    class IPythonBeartypeMagics(Magics):
        @line_magic("beartype")  # type: ignore
        def register_ipython_beartype(self, line: str) -> None:
            # remove old BeartypeNodeTransformers, if present
            assert self.shell is not None
            self.shell.ast_transformers = list(
                filter(
                    lambda x: not isinstance(x, BeartypeNodeTransformer),
                    self.shell.ast_transformers,
                )
            )

            # add new one
            self.shell.ast_transformers.append(
                BeartypeNodeTransformer(
                    module_name_beartype="x.py",
                    conf_beartype=BeartypeConf(),
                )
            )

    ipython.register_magics(IPythonBeartypeMagics)
