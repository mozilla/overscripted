"""Trasnforms AST dictionary into a tree of Node objects."""
import abc
from collections import OrderedDict
from typing import Any, Dict, Generator, List, Union


class UnknownNodeTypeError(Exception):
    """Raised if we encounter a node with an unknown type."""
    pass


class Node(abc.ABC):
    """Abstract Node class which defines node operations"""
    @abc.abstractproperty
    def fields(self) -> List[str]:
        """List of field names associated with this node type, in canonical order."""

    def __init__(self, data: Dict[str, Any]) -> None:
        """Sets one attribute in the Node for each field (e.g. self.body)."""
        for field in self.fields:
            setattr(self, field, objectify(data.get(field), parent=self))

    def dict(self) -> Dict[str, Any]:
        """Transform the Node back into an Esprima-compatible AST dictionary."""
        result = OrderedDict({'type': self.type})  # type: Dict[str, Any]
        for field in self.fields:
            val = getattr(self, field)
            if isinstance(val, Node):
                result[field] = val.dict()
            elif isinstance(val, list):
                result[field] = [x.dict() for x in val]
            else:
                result[field] = val
        return result

    def traverse(self) -> Generator['Node', None, None]:
        """Pre-order traversal of this node and all of its children."""
        yield self
        for field in self.fields:
            val = getattr(self, field)
            if isinstance(val, Node):
                yield from val.traverse()
            elif isinstance(val, list):
                for node in val:
                    yield from node.traverse()

    @property
    def type(self) -> str:
        """The name of the node type, e.g. 'Identifier'."""
        return self.__class__.__name__


def objectify(data: Union[None, Dict[str, Any], List[Dict[str, Any]]], parent=None) -> Union[
        None, Dict[str, Any], List[Any], Node]:
    """Recursively transform AST data into a Node object."""
    if not isinstance(data, (dict, list)):
        # Data is a basic type (None, string, number)
        return data

    if isinstance(data, dict):
        if 'type' not in data:
            # Literal values can be empty dictionaries, for example.
            return data
        # Transform the type into the appropriate class.
        node_class = globals().get(data['type'])
        if not node_class:
            raise UnknownNodeTypeError(data['type'])
        return node_class(data)
    else:
        # Data is a list of nodes.
        return [objectify(x) for x in data]


# --- AST spec: https://github.com/estree/estree/blob/master/es5.md ---
# pylint: disable=missing-docstring,multiple-statements


class Identifier(Node):
    @property
    def fields(self): return ['name']


class Literal(Node):
    @property
    def fields(self): return ['value', 'regex']


class Program(Node):
    @property
    def fields(self): return ['body']


# ========== Statements ==========


class ExpressionStatement(Node):
    @property
    def fields(self): return ['expression']


class BlockStatement(Node):
    @property
    def fields(self): return ['body']


class EmptyStatement(Node):
    @property
    def fields(self): return []


class DebuggerStatement(Node):
    @property
    def fields(self): return []


class WithStatement(Node):
    @property
    def fields(self): return ['object', 'body']


# ----- Control Flow -----


class ReturnStatement(Node):
    @property
    def fields(self): return ['argument']


class LabeledStatement(Node):
    @property
    def fields(self): return ['label', 'body']


class BreakStatement(Node):
    @property
    def fields(self): return ['label']


class ContinueStatement(Node):
    @property
    def fields(self): return ['label']


# ----- Choice -----


class IfStatement(Node):
    @property
    def fields(self): return ['test', 'consequent', 'alternate']


class SwitchStatement(Node):
    @property
    def fields(self): return ['discriminant', 'cases']


class SwitchCase(Node):
    @property
    def fields(self): return ['test', 'consequent']


# ----- Exceptions -----


class ThrowStatement(Node):
    @property
    def fields(self): return ['argument']


class TryStatement(Node):
    @property
    def fields(self): return ['block', 'guardedHandlers', 'handlers', 'handler', 'finalizer']


class CatchClause(Node):
    @property
    def fields(self): return ['param', 'body']


# ----- Loops -----


class WhileStatement(Node):
    @property
    def fields(self): return ['test', 'body']


class DoWhileStatement(Node):
    @property
    def fields(self): return ['body', 'test']


class ForStatement(Node):
    @property
    def fields(self): return ['init', 'test', 'update', 'body']


class ForInStatement(Node):
    @property
    def fields(self): return ['left', 'right', 'body']


# ========== Declarations ==========


class FunctionDeclaration(Node):
    @property
    def fields(self): return ['id', 'params', 'body']


class VariableDeclaration(Node):
    @property
    def fields(self): return ['declarations']


class VariableDeclarator(Node):
    @property
    def fields(self): return ['id', 'init']



# ========== Expressions ==========


class ThisExpression(Node):
    @property
    def fields(self): return []


class ArrayExpression(Node):
    @property
    def fields(self): return ['elements']


class ObjectExpression(Node):
    @property
    def fields(self): return ['properties']


class Property(Node):
    @property
    def fields(self): return ['key', 'value', 'kind']


class FunctionExpression(Node):
    @property
    def fields(self): return ['id', 'params', 'body']


class UnaryExpression(Node):
    @property
    def fields(self): return ['operator', 'prefix', 'argument']


class UpdateExpression(Node):
    @property
    def fields(self): return ['operator', 'argument', 'prefix']


class BinaryExpression(Node):
    @property
    def fields(self): return ['operator', 'left', 'right']


class AssignmentExpression(Node):
    @property
    def fields(self): return ['operator', 'left', 'right']


class LogicalExpression(Node):
    @property
    def fields(self): return ['operator', 'left', 'right']


class MemberExpression(Node):
    @property
    def fields(self): return ['object', 'property', 'computed']


class ConditionalExpression(Node):
    @property
    def fields(self): return ['test', 'consequent', 'alternate']


class CallExpression(Node):
    @property
    def fields(self): return ['callee', 'arguments']


class NewExpression(Node):
    @property
    def fields(self): return ['callee', 'arguments']


class SequenceExpression(Node):
    @property
    def fields(self): return ['expressions']
