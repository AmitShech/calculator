from tree_builder import*
OP_FORMAT={'+':'x_x','*':'x_x','/':'x_x','^':'x_x', '@':'x_x','$':'x_x',
           '&':'x_x','%':'x_x',"!":'x_',"#":'x_',"~":'_x'}

def is_empty(expression):
    """Remove whitespace and check if expression is empty."""
    expression = expression.replace(" ", "")
    if expression == "":
        raise EmptyInput()
    return expression

def parenthesis_balance(expression):
    """Check if parentheses are balanced."""
    count=0
    for char in expression:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            raise UnbalanceParenthesis("Closing parenthesis ')' has no matching opening parenthesis")
    if count > 0:
        raise UnbalanceParenthesis("Error: Opening parenthesis '(' has no matching closing parenthesis")

def valid_chars(expression):
    """Validate the expression contain only valid chars."""

    chars = set('0123456789.()-+!@#$%^&*/~')

    for i in range(len(expression)):
        x = expression[i]

        if x not in chars:
            raise IncorrectSyntax(f"Error: {x} isn't a part of a mathematical expression")


def right_format(expression):
    """Validate the format of the mathematical expression."""


    if expression[0] in OP_FORMAT:
        if OP_FORMAT[expression[0]] in ['x_x','x_'] :
            raise IncorrectSyntax(f"A value need to come before the operat {expression[0]} ")

    for i in range(len(expression)):
        x = expression[i]

        if x in OP_FORMAT:
            if OP_FORMAT[x] == 'x_x':
                if not (expression[i-1].isdigit() or  expression[i-1] in  ['!', '#',')','.'] ):
                    raise NotInFormat(expression[i-1],x)

                if not (expression[i+1].isdigit() or expression[i+1] in ['-','(','~','.']):
                    raise NotInFormat(x,expression[i+1])

            elif OP_FORMAT[x] == 'x_':
                if not (expression[i-1].isdigit()) or (expression[i-1] in ['!', '#',')','.']) :
                    raise NotInFormat(expression[i-1],x)

            elif OP_FORMAT[x] == '_x':
                n=1
                after=""

                while (i+n) < len(expression) and expression[i + n] == '-':
                    n += 1
                    after += expression[i+n]

                if not (expression[i+n].isdigit() or expression[i+n] in ['(','.']):
                    raise NotInFormat(x,after)


        if expression[-1] in OP_FORMAT:
            if OP_FORMAT[expression[-1]] in ['x_x', '_x']:
                raise IncorrectSyntax(f"A value need to come after the operat {expression[-1]} ")

        if expression[-1] == '-':
            raise IncorrectSyntax(f"the operat {expression[-1]} need to come before a value")

def check_input(expression: str) -> list:
    """
        Comprehensive input validation for mathematical expressions.

        Args:
            expression (str): Mathematical expression to validate

        Returns:
            str: Validated expression

        Raises:
            Various syntax and formatting exceptions
        """
    try:
        expression=is_empty(expression)
        parenthesis_balance(expression)
        valid_chars(expression)
        right_format(expression)
    except Exception as e:
            print(str(e))
    else:
        return expression


def main():
    test_expressions = [
        "6*4.8",
        "6*4.&8",
        "(3+4)*2",
        "3++4",
        "3+",
        "*3+4",
        "~-------(3)",
    ]

    for expr in test_expressions:
        try:
            validated_expr = check_input(expr)
            print(f"Valid expression: {validated_expr}")
        except Exception:
            print(f"Invalid expression: {expr}")


if __name__ == "__main__":
    main()


