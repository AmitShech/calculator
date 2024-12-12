class TreeNode:

    def __init__(self, value=None):
        self._value = value
        self._left = None
        self._right = None

    def set_value(self, value):
        self._value = value

    def set_left(self, value):
        if self._left is None:
            self._left = TreeNode(value)
        else:
            self._left.set_value(value)

    def set_right(self, value):
        if self._right is None:
            self._right = TreeNode(value)
        else:
            self._right.set_value(value)

    def get_value(self):
        return self._value

    def get_left(self):
        if self._left is None:
            self._left=TreeNode()
        return self._left

    def get_right(self):
        if self._right is None:
            self._right=TreeNode()
        return self._right

    def is_leaf(self) -> bool:
        return self._left is None and self._right is None

    def is_empty(self) -> bool:
        return self._value is None

    def print_infix(self) -> object:
        if not self.is_empty():
            self.get_left().print_infix()
            print(f"{self._value} ")
            self.get_right().print_infix()
        else:
            return

    def print_prefix(self) -> object:
        if not self.is_empty():
            print(f"{self._value} ")
            self.get_left().print_prefix()
            self.get_right().print_prefix()
        else:
            return
