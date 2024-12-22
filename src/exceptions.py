
"""input errors:"""

class EmptyInput (Exception):
    def __init__(self):
        self.message = f"Error: empty expression entered"
        super().__init__(self.message)

class UnbalanceParenthesis (Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class IncorrectSyntax (Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)

class NotInFormat (Exception):
    def __init__(self,op1,op2):
        self.message = f"Error: syntax error, {op1} {op2} is an invalid sequence"
        super().__init__(self.message)

"""--------------------------------------------------
    Calculation errors: """

class RootToNegative(Exception):
    def __init__(self, message="Error: cant calculate root to a negative number"):
        self.message = message
        super().__init__(message)

class NegativeInFactorial(Exception):
    def __init__(self, message="Error: cant calculate factorial to a negative number"):
        self.message = message
        super().__init__(message)

class FloatInFactorial(Exception):
    def __init__(self, message="Error: cant calculate factorial to a decimal number"):
        self.message = message
        super().__init__(message)

class NegativeInSum(Exception):
    def __init__(self, message="Error: cant sum a negative number"):
        self.message = message
        super().__init__(message)

class DivisionByZero(Exception):
    def __init__(self, message="Error: Cannot divide by zero"):
        self.message = message
        super().__init__(message)

class SumOfDigitsEError(Exception):
    def __init__(self, message="Error: cannot calculate sum for numbers represented with 'e'"):
        self.message = message
        super().__init__(message)
