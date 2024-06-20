from __future__ import annotations

import html
from typing import Iterable, Mapping

from haitch._attrs import AttributeValue, serialize_attribute
from haitch._typing import Child, Html, SupportsHtml


class Element:
    """Lazily built HTML Element.

    An Element represents a Document Object Model (DOM) with optional
    attributes and children. Render the HTML to string by invoking the
    `__str__` method.
    """

    def __init__(self, tag: str, unsafe: bool = False) -> None:
        """Initialize element by providing a tag name, ie. "a", "div", etc."""
        self._tag = tag
        self._unsafe = unsafe
        self._attrs: Mapping[str, AttributeValue] = {}
        self._children: Iterable[Child] = []

    def __call__(self, *children: Child, **attrs: AttributeValue) -> Element:
        """Add children and/or attributes to element.

        Provide attributes, children, or a combination of both:

        >>> import haitch as H
        >>> H.img(src="h.png", alt="Letter H")
        >>> H.h1("My heading")
        >>> H.h1(style="color: red;")("My heading")
        """
        if children:
            self._children = [*self._children, *children]

        if attrs:
            self._attrs = {**self._attrs, **attrs}

        return self

    def __str__(self) -> Html:
        """Renders the HTML element as a string."""
        return self._render()

    def _render(self) -> Html:
        attrs_ = "".join(serialize_attribute(k, v) for k, v in self._attrs.items())
        children_ = "".join(self._render_child(child) for child in self._children)

        if self._tag == "fragment":
            return Html(children_)

        html_str = "<%(tag)s%(attrs)s>%(children)s</%(tag)s>" % {
            "tag": self._tag,
            "attrs": attrs_,
            "children": children_,
        }

        if self._tag == "html":
            return Html("<!doctype html>" + html_str)

        return Html(html_str)

    def _render_child(self, child: Child) -> str:
        if child is None or child is False:
            return ""

        elif isinstance(child, str):
            return child if self._unsafe else html.escape(child)

        elif isinstance(child, SupportsHtml):
            return child._render()

        elif isinstance(child, Iterable):
            return "".join(str(nested_child) for nested_child in child)

        raise ValueError(f"Invalid child type: {type(child)}")
