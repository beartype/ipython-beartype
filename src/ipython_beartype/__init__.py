"""IPython extension type-checking IPython environments with beartype."""

from beartype.claw._ast.clawastmain import BeartypeNodeTransformer
from beartype._conf.confcls import BeartypeConf
from IPython.terminal.interactiveshell import TerminalInteractiveShell


def load_ipython_extension(ipython: TerminalInteractiveShell) -> None:
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

    ipython.register_magics(IPythonBeartypeMagics)  # type: ignore[no-untyped-call]
