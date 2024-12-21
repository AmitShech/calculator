from exceptions import *
from const_variables import *


def is_empty(expression):
    """Remove whitespace and check if expression is empty."""
    expression = expression.replace(" ", "")
    expression = expression.replace("\t", "")
    if expression == "":
        raise EmptyInput()
    return expression

def parenthesis_balance(expression):
    """Check if parentheses are balanced."""
    count=0
    for i in range(len(expression)):
        char= expression[i]
        if char == '(':
            if expression[i+1]==')':
                raise IncorrectSyntax(f"Error: the parenthesis are empty ()")
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            raise UnbalanceParenthesis("Closing parenthesis ')' has no matching opening parenthesis")
    if count > 0:
        raise UnbalanceParenthesis("Error: Opening parenthesis '(' has no matching closing parenthesis")

def valid_chars(expression):
    """Validate the expression contain only valid chars."""

    for x in expression:
        if x not in VALID_CHARS:
            raise IncorrectSyntax(f"Error: {x} isn't a part of a mathematical expression")


def right_format(expression):
    """Validate the format of the mathematical expression."""


    if expression[0] in OP_FORMAT:
        if OP_FORMAT[expression[0]] in ['x_x','x_'] :
            raise IncorrectSyntax(f"Error: A value need to come before the operat {expression[0]} ")

    if expression[-1] in OP_FORMAT:
        if OP_FORMAT[expression[-1]] in ['x_x', '_x']:
            raise IncorrectSyntax(f"Error:A value need to come after the operat {expression[-1]} ")

    if expression[-1] == '-':
        raise IncorrectSyntax(f"Error: the operat {expression[-1]} need to come before a value")

    for i in range(len(expression)-1):
        x = expression[i]

        if x in OP_FORMAT:
            if OP_FORMAT[x] == 'x_x':
                if not (expression[i-1].isdigit() or  expression[i-1] in  ['!', '#',')','.'] ):
                    raise NotInFormat(expression[i-1],x)

                if not (expression[i+1].isdigit() or expression[i+1] in ['-','(','~','.']):
                    raise NotInFormat(x,expression[i+1])

            elif OP_FORMAT[x] == 'x_':
                if not (expression[i-1].isdigit() or expression[i-1] in ['!', '#','.',')']) :
                    raise NotInFormat(expression[i-1],x)
                if i < len(expression) - 1 and (expression[i + 1].isdigit() or expression[i + 1] in ['~', '(']):
                    raise NotInFormat(x, expression[i + 1])

            elif OP_FORMAT[x] == '_x':
                if not (expression[i-1] in BINARY_OP or expression[i-1]!='(') and i>0:
                    raise NotInFormat(expression[i-1],x)

                n=1
                after=""

                while (i+n) < len(expression) and expression[i + n] == '-':
                    after += expression[i+n]
                    n += 1
                after += expression[i + n]
                if (i+n) < len(expression) and not (expression[i+n].isdigit() or expression[i+n] in ['(','.'] ):
                    raise NotInFormat(x,after)

        if x == '(':
            if i>0 and not (expression[i-1] in OP_POWER or expression[i-1] == '('):
                raise NotInFormat(expression[i-1],x)

        if x == ')':
            if i< len(expression)-1 and not (expression[i + 1] in OP_POWER or expression[i + 1] == ')'):
                raise NotInFormat(x,expression[i + 1])


def check_input(expression: str) -> str:
    """
        Comprehensive input validation for mathematical expressions.

        Args:
            expression (str): Mathematical expression to validate

        Returns:
            str: Validated expression

        Raises:
            Various syntax and formatting exceptions
        """

    expression=is_empty(expression)
    parenthesis_balance(expression)
    valid_chars(expression)
    right_format(expression)

    return expression


def main():
    test_expressions = [
        "2+~3",
        "(~1+1)",
        "(3!)"
    ]

    for expr in test_expressions:
        try:
            print(expr)
            validated_expr = check_input(expr)
            print(f"Valid expression: {validated_expr}")
        except Exception as expr:
            print(f"Invalid expression: {expr.message}")


if __name__ == "__main__":
    main()


