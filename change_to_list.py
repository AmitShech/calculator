from exceptions import *
from const_variables import *



def change_unary(expression:str) ->list:
    """
            Replaces the string into a list and separates the different types of minuses

            Args:
                expression (str): string to reverse

            Returns:
                expr (list): expression in list format

            Raises:
                syntax and formatting exception with the minus
           """
    i = 0
    expr = []
    sign = ""
    soger=0

    while i < len(expression):

        if expression[i].isdigit() or expression[i] == '.':
            num = sign
            while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                num += expression[i]
                i += 1
            expr.append(num)
            sign = ""
            continue


        elif expression[i] == '-':

            if i == 0 or expression[i - 1] in ['(', ';']:
                count = 0
                while i < len(expression) and expression[i] == '-':
                   count += 1
                   i += 1
                if count % 2 == 1:
                    expr.append(';')
                continue


            elif OP_FORMAT.get(expression[i - 1], None) in ['x_x', '_x'] or expression[i - 1]=='-':
                count = 0
                sign = ""
                while i < len(expression) and expression[i] == '-':
                    count += 1
                    i += 1

                if expression[i] in OP_FORMAT:
                    raise IncorrectSyntax(f" invalid syntax, after a sign minus cant come operat")

                if count % 2 == 1:
                    sign = "-"
                    if expression[i] == '(':
                        expr.append('(')
                        expr.append('~')
                        sign = ""
                        soger=1

                continue

            else:
                expr.append(expression[i])

        else:
            expr.append(expression[i])

        if expression[i] == '(' and soger >0:
            soger+=1

        if expression[i] == ')':
            if soger == 2:
                expr.append(')')
                soger=0
            else:
                soger-=1

        i += 1

    return expr


def main():

    test_expressions = [
        "2--(3+4)"
    ]

    for expr in test_expressions:
        print(f"Original: {expr}")
        print(f"Processed: {change_unary(expr)}\n")


if __name__ == "__main__":
    main()