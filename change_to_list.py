from tree_builder import*


def change_unary(expression):
    """
            Replaces the string into a list and separates the different types of minuses

            Args:
                expression (str): string to reverse

            Returns:
                expr (list): expression in list format

           """
    i = 0
    expr = []
    sign = ""

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
                #     count += 1
                #     i += 1
                # if count % 2 == 1:
                    expr.append(';')
                    i += 1
                continue


            elif expression[i - 1] in OP_POWER:
                count = 0
                sign = ""
                while i < len(expression) and expression[i] == '-':
                    count += 1
                    i += 1
                if count % 2 == 1:
                    sign = "-"
                continue
            else:
                expr.append(expression[i])

        else:
            expr.append(expression[i])
        i += 1

    return expr


def main():

    test_expressions = [
        "-5+3",
        "3+-5",
        "(-5)*2",
        "--7",
        "5-3"
    ]

    for expr in test_expressions:
        print(f"Original: {expr}")
        print(f"Processed: {change_unary(expr)}\n")


if __name__ == "__main__":
    main()