from change_to_list import *
from input_checks import *
from stack import *

def cal_expression(expr:str):
    """
    This function gets a mathematical expression as input, processes it,
    and calculates the result.

    Args:
           math expression (str): Mathematical expression to calculate
    return:
            the result of the expression
    """

    expr= check_input(expr)
    expr= change_unary(expr)
    expr = infix_to_postfix(expr)
    result = calculate_postfix(expr)

    return result


def main():
    print("Welcome to the Omega Calculator!")
    print("Here, you can calculate advanced mathematical expressions")
    print("To exit the calculator, simply type 'end'")
    expr = input("please enter an equation:")

    while expr != 'end':
        try:
            result= cal_expression(expr)
            print(f"the result is: {result}")

        except OverflowError:
            print("The expression's result is beyond the capacity for calculation")

        except Exception as e:
            print(e)
            print("try again")

        expr = input("enter an equation:")

if __name__ == "__main__":
    main()