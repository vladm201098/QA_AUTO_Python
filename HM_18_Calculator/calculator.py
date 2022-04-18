class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def is_valid(a, b):
        assert all(isinstance(number, (float, int)) for number in (a, b)), \
            "Вы ввели первое или второе число с другим типом данных."

    def sum(self, a, b):
        return a + b

    def diff(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("The divisor must not be zero")
        return a / b