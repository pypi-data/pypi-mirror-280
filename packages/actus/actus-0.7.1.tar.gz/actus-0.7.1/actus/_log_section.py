import sys as _sys
from traceback import TracebackException as _TracebackException

import colex as _colex

from ._highlighting import highlight as _highlight
from ._style import Style as _Style
from ._annotations import (
    FileLike as _FileLike,
    SupportsStr as _SupportsStr
)


class LogSection:
    def __init__(
        self,
        label: str,
        /,
        *,
        style: _Style | None = None,
        suppress_color: bool = False,
        fd: _FileLike[str] | None = None,
        suppress_output: bool = False,
        left_deco: str = "[",
        right_deco: str = "]",
        label_end: str = " ",
        indent_size: int = 2,
        indent_filler: str = " ",
        indent_deco: str = " ",
        indent_delimiter: str = " "
    ) -> None:
        self._label = label
        self._style = style or _Style()
        self._suppress_color = suppress_color
        self._fallback_fd: _FileLike[str] = fd or _sys.stdout
        self._suppress_output = suppress_output
        self._left_deco = left_deco
        self._right_deco = right_deco
        self._label_end = label_end
        self._indent_size = indent_size
        self._indent_filler = indent_filler
        self._indent_deco = indent_deco
        self._indent_delimiter = indent_delimiter
        self._indent_level = 0
    
    def __enter__(self):
        self.indent()
        return self
    
    def __exit__(
        self,
        exc_type: type | None,
        _exc_value: Exception | None,
        _traceback: _TracebackException | None
    ) -> bool:
        self.dedent()
        return exc_type is None
    
    def indent(
        self,
        indent_count: int = 1,
        /,
        deco: str | None = None
    ):
        self._indent_level += indent_count
        if deco is not None:
            self.set_indent_deco(deco)
        return self
    
    def dedent(
        self,
        dedent_count: int = 1,
        /,
        deco: str | None = None
    ):
        self._indent_level = max(0, self._indent_level - dedent_count)
        if deco is not None:
            self.set_indent_deco(deco)
        return self
    
    def dedent_all(self, /, deco: str | None = None):
        self._indent_level = 0
        if deco is not None:
            self.set_indent_deco(deco)
        return self

    def set_style(self, style: _Style | None, /):
        # `None` will set `_style` to a fresh `Style()`
        self._style = style or _Style()
        return self

    def get_style_copy(self) -> _Style:
        # This is to prevent mutating a LogSection,
        # when mutating the reference to its style
        return _Style(
            label=self._style.label,
            text=self._style.text,
            highlight=self._style.highlight,
            indent=self._style.indent
        )
    
    def set_fd(self, fd: _FileLike[str] | None, /):
        # `None` will set `_fallback_fd` to `sys.stdout`
        self._fallback_fd = fd or _sys.stdout
        return self
    
    def set_left_deco(self, left_deco: str, /):
        self._left_deco = left_deco
        return self
        
    def set_right_deco(self, right_deco: str, /):
        self._right_deco = right_deco
        return self
    
    def set_label_end(self, label_end: str, /):
        self._label_end = label_end
        return self

    def set_indent_size(self, size: int, /):
        self._indent_size = size
        return self

    def set_indent_filler(self, filler: str, /):
        self._indent_filler = filler
        return self
    
    def set_indent_deco(self, deco: str, /):
        self._indent_deco = deco
        return self

    def set_indent_delimiter(self, delimiter: str, /):
        self._indent_delimiter = delimiter
        return self
    
    def disable_color(self):
        self._suppress_color = True
        return self
    
    def enable_color(self):
        self._suppress_color = False
        return self
    
    def disable_output(self):
        self._suppress_output = True
        return self
    
    def enable_output(self):
        self._suppress_output = False
        return self
    
    def __call__(
        self,
        *values: _SupportsStr,
        sep: str = " ",
        end: str = "\n",
        fd: _FileLike[str] | None = None,
        flush: bool = True
    ):
        if self._suppress_output:
            return self
        if self._suppress_color:
            body = _highlight(sep.join(map(str, values)), style=None)
        else:
            body = _highlight(sep.join(map(str, values)), style=self._style)
        if self._indent_level == 0:
            header = self._left_deco + self._label + self._right_deco
            if self._suppress_color:
                content = header + self._label_end + body
            else:
                content = _colex.colorize(header, self._style.label) + self._label_end + body
        else:
            indent_suffix = self._indent_deco + self._indent_delimiter
            indent_chars = self._indent_size * self._indent_level
            indentation = indent_suffix.rjust(indent_chars, self._indent_filler)
            if self._suppress_color:
                content = indentation + body
            else:
                content = _colex.colorize(indentation, self._style.indent) + body
        final_fd = fd or self._fallback_fd
        final_fd.write(content + end)
        if flush:
            final_fd.flush()
        return self
