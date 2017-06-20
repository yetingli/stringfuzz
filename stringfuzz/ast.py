import string

'''
The AST is a list of ASTNodes.
'''

__all__ = [
    'ASTNode',
    'LiteralNode',
    'BoolLitNode',
    'IntLitNode',
    'StringLitNode',
    'SortNode',
    'SettingNode',
    'IdentifierNode',
    'ArgsNode',
    'ExpressionNode',
    'ConcatNode',
    'AtNode',
    'LengthNode',
]

# data structures
class ASTNode(object):
    pass

class LiteralNode(ASTNode):
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return 'Literal<{}>'.format(self.value)

class BoolLitNode(LiteralNode):
    def __repr__(self):
        return 'BoolLit<{}>'.format(self.value)

class IntLitNode(LiteralNode):
    def __repr__(self):
        return 'IntLit<{}>'.format(self.value)

class StringLitNode(LiteralNode):
    def __len__(self):
        return len(self.value)

    def __repr__(self):
        return 'StringLit<{!r}>'.format(self.value)

class SortNode(ASTNode):
    def __init__(self, sort):
        self.sort = sort

    def __repr__(self):
        return 'Sort<{}>'.format(self.sort)

class SettingNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Setting<{}>'.format(self.name)

class IdentifierNode(ASTNode):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Id<{}>'.format(self.name)

class ArgsNode(ASTNode):
    def __repr__(self):
        return 'Args<()>'

class ExpressionNode(ASTNode):
    def __init__(self, symbol, body):
        assert symbol is not None
        self.symbol = symbol
        self.body   = body

    def __repr__(self):
        contents = ' '.join(map(repr, [self.symbol] + self.body))
        return 'Expr<{}>'.format(contents)

class SpecificExpression(ExpressionNode):
    def __init__(self, symbol, body):
        super(SpecificExpression, self).__init__(symbol, body)

    def __repr__(self):
        contents = ' '.join(map(repr, self.body))
        return '{}<{}>'.format(self.symbol, contents)

class ConcatNode(SpecificExpression):
    def __init__(self, a, b):
        super(ConcatNode, self).__init__('Concat', [a, b])

class AtNode(SpecificExpression):
    def __init__(self, a, b):
        super(AtNode, self).__init__('At', [a, b])

class LengthNode(SpecificExpression):
    def __init__(self, a):
        super(LengthNode, self).__init__('Length', [a])