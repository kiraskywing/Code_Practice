class Calculator:
    """
    @param a, b: Two integers.
    @param operator: A character, +, -, *, /.
    """
    def calculate(self, a, operator, b):
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            return a / b