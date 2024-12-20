from calculation import *
from exceptions import *
from const_variables import *


def infix_to_postfix(infix: str) -> list:
    """Convert an infix mathematical expression to postfix notation.

    Args:
        infix (str): The infix expression to be converted.

    Returns:
        list: A list representing the postfix expression.
    """
    stack=[]
    postfix=[]

    for x in infix:

        if x == '(':
            stack.append('(')

        elif x == ')':
            while stack and stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()

        elif x in OP_POWER:
            while stack and stack[-1] != '(' and OP_POWER[stack[-1]] >= OP_POWER[x]:
                postfix.append(stack.pop())
            stack.append(x)

        else:
            postfix.append(x)

    while stack:
        postfix.append(stack.pop())

    return postfix


def calculate_postfix(expr:list):
    """Evaluate a postfix expression and return the result.
    Args:
        expr (list): The postfix expression as a list of operands and operators.

    Returns:
        int or float: The result of evaluating the postfix expression.

    Raises:
        IncorrectSyntax: If the expression has invalid syntax or contains invalid numbers."""
    stack = []

    if len(expr)==1:
        try:
            return float(expr[0])
        except Exception as e:
            raise IncorrectSyntax(f" invalid syntax, {expr[0]} isn't a number")

    for i in range(len(expr)):
        x=expr[i]

        if x not in OP_POWER:
            stack.append(x)

        else:
            if x in BINARY_OP:
                opend2=stack.pop()
                opend1=stack.pop()

            elif x in UNARY_OP:
                opend1 = stack.pop()
                opend2=None

            cal = Operation[x](opend1, opend2)
            result = cal.result()
            stack.append(result)

    result=stack.pop()

    if int(result) == result:
        return int(result)

    return result


def main():
    # expression = input('Enter infix expression ')
    expression=['123','#','-','2']
    print('infix notation: ', expression)
    expr=infix_to_postfix(expression)
    print('postfix notation: ',expr)
    result=calculate_postfix(expr)
    print(f"the result is {result}")


if __name__ == "__main__":
    main()