from Tree import *
from calculation import *
from exceptions import *

OP_POWER = {'-': 1, '+': 1, '*': 2, '/': 2, '^': 3, '@': 5, '$': 5, '&': 5, '%': 4, '~': 6, '!': 6}

def is_closed(expression):
    #the func check if th exp start and end with the same parentheses
    count=0
    for char in expression[1:-1]:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


def find_min(expression):
    #The function finds the operator with the lowest precedence
    min_op = '0'
    min_index = -1
    count = 0

    for i, x in enumerate(expression):
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1
        elif count == 0 and x in OP_POWER:
            if min_op == '0' or OP_POWER[x] <= OP_POWER[min_op]:
                min_op = x
                min_index = i

    return min_index


def build_tree(expression: str, root: TreeNode) -> TreeNode:
    #the func build the tree that represent the expression

    #remove parentheses if needed
    if expression[0] == '(' and expression[-1] == ')':
        if is_closed(expression):
            expression = expression[1:-1]

    #split the expression by the weakest operand.
    min_op = find_min(expression)

    if min_op == -1:
        root.set_value(expression)
        return root
    else:
        root.set_value(expression[min_op])
        first_part, second_part = expression[:min_op], expression[(min_op + 1):]

        if first_part == '':
            first_part = '0'
        if second_part == '':
            second_part = '0'
        build_tree(first_part, root.get_left())
        build_tree(second_part, root.get_right())
        return root

def calculate_tree(root: TreeNode)-> float:
    #caculate the tree expression
    if root.is_leaf():
        return root.get_value()
    else:
        op1=calculate_tree(root.get_left())
        op2=calculate_tree(root.get_right())
        try:
            cal= Operation[root.get_value()](op1, op2)
            result= cal.result()
        except Exception as e:
            print(e.message)
        else:
            return result


def main():
    expression = "((3+2)-(6*8))"

    root = TreeNode()
    root = build_tree(expression, root)
    result= calculate_tree(root)
    print(f"the result is: {result}")
    # root.print_infix()
    # print("--------------")
    # root.print_prefix()

main()
