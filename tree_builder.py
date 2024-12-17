from Tree import *
from calculation import *
from exceptions import *

OP_POWER = {'-': 1, '+': 1, '*': 2, '/': 2, ';': 2.5, '^': 3, '@': 5, '$': 5, '&': 5, '%': 4, '~': 6, '!': 6, '#':6}

def is_closed(expression:list) -> bool:
    """the func check if th exp start and end with the same parentheses"""
    count=0
    for char in expression[1:len(expression)-1]:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count < 0:
            return False
    return count == 0


def find_min(expression: list, start: int, end: int) -> int:
    """The function finds the operator with the lowest precedence"""
    min_op = '0'
    min_index = -1
    count = 0

    for i in range(start,end+1):
        x=expression[i]
        if x == "(":
            count += 1
        elif x == ")":
            count -= 1
        elif count == 0 and x in OP_POWER:
            if min_op == '0' or OP_POWER[x] <= OP_POWER[min_op]:
                min_op = x
                min_index = i

    return min_index


def build_tree(expression: list, root: TreeNode, start: int, end: int) -> TreeNode:
    """the func build the tree that represent the expression
            Args:
                expression (list): A list of characters representing a mathematical expression.
                root (TreeNode): The root node of the binary tree, which will be modified to represent the expression.
                start (int): The starting index of the current sub-expression within the list.
                end (int): The ending index of the current sub-expression within the list.

            Returns:
                TreeNode: The root of the binary tree that represents the given expression.

            Raises:
                IncorrectSyntax: If the parentheses are unbalanced or the expression is invalid,
                an exception is raised."""

    if start > end:
        root.set_value('0')
        return root

    if start == end:
        root.set_value(expression[start])
        return root

    #remove parentheses if needed
    while expression[start] == "(" and expression[end] == ")" and is_closed(expression[start:end + 1]):
        start += 1
        end -= 1
        # raise an error if parentheses aer empty
        if start > end:
            raise IncorrectSyntax("Syntax Error: parentheses '()' are empty")

    #split the expression by the weakest operand.
    min_op = find_min(expression,start, end)

    if min_op==-1:
        root.set_value(expression[start])
        return root

    root.set_value(expression[min_op])
    build_tree(expression, root.get_left(), start, min_op - 1)
    build_tree(expression, root.get_right(), min_op + 1, end)
    return root

def calculate_tree(root: TreeNode)-> float:
    """
    calculate the tree expression
    Args:
        root (TreeNode): The root node of the binary tree representing the expression.

    Returns:
        float: The result of the evaluated expression. If the result is a whole number,
        it is returned as an integer.

    Raises:
        IncorrectSyntax: If a leaf node's value cannot be converted to a number,
        an exception is raised with an error message.
        """

    #stopping condition
    if root.is_leaf():
        try:
            num=float(root.get_value())
        except Exception as e:
            raise IncorrectSyntax(f" invalid syntax, {root.get_value()} isn't a number")
        else:
            return num
    else:
        op1=calculate_tree(root.get_left())
        op2=calculate_tree(root.get_right())

        cal= Operation[root.get_value()](op1, op2)
        result= cal.result()

        if int(result)==result:
            return int(result)

        return result


def main():
    expression =  ['2', '-', '8','*','(', '-', '(', '3', '+', '4', ')', ')']

    try:
        root = TreeNode()
        root = build_tree(expression, root, 0, len(expression)-1)
        result= calculate_tree(root)
    except Exception as e:
        print(e.message)
    else:
        print(f"the result is: {result}")


if __name__ == "__main__":
    main()

