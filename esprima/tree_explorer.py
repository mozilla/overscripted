import json
import esprima
import visitor



import visitor



####
# Port of estree-walk from Node

class Element:

    BLACKLISTEDKEYS = ['parent']

    def __init__(self, esprima_ast):
        self._ast = esprima_ast
        self._visitors = []

    def accept(self, visitor):
        self._visitors.append(visitor)

    def _step(self, node, queue):
        before = len(queue)

        # Enumerate keys for possible children
        for key in node.keys():
            if key in self.BLACKLISTEDKEYS:
                continue

            child = getattr(node, key)

            if child and hasattr(child, 'type') == True:
                child.parent = node
                queue.append(child)

            if isinstance(child, list):
                for item in child:
                    if hasattr(item, 'type') == True:
                        item.parent = node
                        queue.append(item)


        # Return whether any children were pushed
        return len(queue) != before

    def walk(self):
        queue = [self._ast]

        while len(queue) > 0:
            node = queue.pop()

            # Run visitors here
            for v in self._visitors:
                v.visit(node)

            if isinstance(node, esprima.nodes.Node):
                self._step(node, queue)


class MatchPropertyVisitor:
    def __init__(self, property_name, node_handler):
        self._property_name = property_name
        self._node_handler = node_handler

    def visit(self, node):
        if 'MemberExpression' == node.type and \
                node.property.type == 'Identifier' and \
                node.property.name == self._property_name:
            self._node_handler(node)

def main():
    print ("#" * 100)
    ast = esprima.parseScript(open('js/snowplow.js').read())

    el = Element(ast)

    def parent_type(node):
        return getattr(getattr(node, 'parent', None), 'type', None)

    visitor = MatchPropertyVisitor('colorDepth', lambda n: print("{}:{}".format(n.type, parent_type(n))))

    el.accept(visitor)

    el.walk()

main()
