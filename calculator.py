class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


if __name__ == '__main__':
    calculator = Calculator()
    print("5 + 3 =", calculator.add(5, 3))
    print("9 - 2 =", calculator.subtract(9, 2))
    print("4 * 6 =", calculator.multiply(4, 6))
    print("8 / 2 =", calculator.divide(8, 2))

