from change_to_list import *
from input_checks import *
from stack import *


def main():
    """
    This function gets a mathematical expression as input, processes it,
    and calculates the result.

            return:
                None : print the result of the expression

    """
    print("Welcome to the Omega Calculator!")
    print("Here, you can calculate advanced mathematical expressions")
    print("To exit the calculator, simply type 'end'")
    expr=input("please enter an equation:")

    while expr != 'end':
        try:
            expr= check_input(expr)
            expr= change_unary(expr)
            expr = infix_to_postfix(expr)
            result = calculate_postfix(expr)

            print(f"the result is: {result}")

        except OverflowError:
            print("The expression's result is beyond the capacity for calculation")

        except Exception as e:
            print(e.message)
            print("try again")


        expr=input("enter an equation:")

if __name__ == "__main__":
    main()