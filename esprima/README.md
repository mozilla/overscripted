The tree_visitor.py class implements two classes which can be used in
a visitor pattern to inspect the Esprima AST tree for a given
Javascript source file.

Roughly, there is an Element class which accepts Visitor instances.

The code is very rough at this point, but minimally works to walk the
tree.

I've also added a visitor.py module which I found that may be helpful
in evolving our tree walker to do richer inspection and transformation
of the source tree.
