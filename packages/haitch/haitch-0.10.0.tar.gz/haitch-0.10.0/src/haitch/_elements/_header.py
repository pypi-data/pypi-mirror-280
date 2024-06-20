from __future__ import annotations

from typing import Mapping, NewType

from typing_extensions import Unpack

from haitch._attrs import AttributeValue, GlobalAttrs
from haitch._elements._element import Element
from haitch._typing import Child

HeaderElement = NewType("HeaderElement", Element)
"""A `<header>` element."""


def header(
    *children: Child,
    extra_attrs: Mapping[str, AttributeValue] = {},
    **attrs: Unpack[GlobalAttrs],
) -> HeaderElement:
    """Represents introductory content, typically a group of introductory or nav aids.

    It may contain some heading elements but also a logo, a search form, an author name,
    and other elements.

    <https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header>
    """
    el = Element("header")(**attrs, **extra_attrs)(*children)
    return HeaderElement(el)
