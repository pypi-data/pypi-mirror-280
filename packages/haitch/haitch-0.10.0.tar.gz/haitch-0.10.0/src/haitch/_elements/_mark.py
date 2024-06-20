from __future__ import annotations

from typing import Mapping, NewType

from typing_extensions import Unpack

from haitch._attrs import AttributeValue, GlobalAttrs
from haitch._elements._element import Element
from haitch._typing import Child

MarkElement = NewType("MarkElement", Element)
"""A `<mark>` element."""


def mark(
    *children: Child,
    extra_attrs: Mapping[str, AttributeValue] = {},
    **attrs: Unpack[GlobalAttrs],
) -> MarkElement:
    """Represents text which is marked or highlighted for reference or notation purposes.

    <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark>
    """
    el = Element("mark")(**attrs, **extra_attrs)(*children)
    return MarkElement(el)
