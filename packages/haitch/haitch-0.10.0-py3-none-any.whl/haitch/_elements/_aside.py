from __future__ import annotations

from typing import Mapping, NewType

from typing_extensions import Unpack

from haitch._attrs import AttributeValue, GlobalAttrs
from haitch._elements._element import Element
from haitch._typing import Child

AsideElement = NewType("AsideElement", Element)
"""An `<aside>` element."""


def aside(
    *children: Child,
    extra_attrs: Mapping[str, AttributeValue] = {},
    **attrs: Unpack[GlobalAttrs],
) -> AsideElement:
    """Represents a portion of a document whose content is only indirectly related.

    Asides are frequently presented as sidebars or call-out boxes.

    <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside>
    """
    el = Element("aside")(**attrs, **extra_attrs)(*children)
    return AsideElement(el)
