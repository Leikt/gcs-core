"""
Base classes and component to build a gcs module.
"""
from __future__ import annotations

from typing import TypeVar, Type

T = TypeVar('T')

__all__ = ['add_child', 'HasName', 'HasDescription', 'HasChildren']


class HasName:
    """
    Provide the node with a name. This is also the base trait to use for all the nodes.
    """
    v_name: str

    def __init__(self, name: str):
        self.v_name = name


class HasChildren:
    """
    Allow the node to have children. If used, create a __init__ method calling this one HasChildren.__init__(self)
    """
    v_children: list

    def __init__(self):
        self.v_children = []


class HasDescription:
    v_description: str = ''

    def description(self: T, text: str) -> T:
        """
        Provide the node with a description.
        :param text: text of the description.
        :return: the node
        """
        self.v_description = text
        return self


def add_child(parent: HasChildren, klass: Type[T], name: str) -> T:
    """
    Create and add a child to the given parent node.
    :param parent: the parent node
    :param klass: the class of the child node
    :param name: name of the child node
    :return: the child node
    """
    child = klass(name)
    parent.v_children.append(child)
    return child
