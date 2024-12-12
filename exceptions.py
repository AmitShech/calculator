class RootToNegative(Exception):
    def __init__(self,message="Error: cant calculate root to a negative number"):
        self.message = message
        super().__init__(message)

class NegativeInFactorial(Exception):
    def __init__(self, message="Error: cant calculate factorial to a negative number"):
        self.message = message
        super().__init__(message)

class FloatInFactorial(Exception):
    def __init__(self,message="Error: cant calculate factorial to a decimal number"):
        self.message = message
        super().__init__(message)

class DivisionByZero(Exception):
    def __init__(self,message="Error: Cannot divide by zero"):
        self.message = message
        super().__init__(message)

