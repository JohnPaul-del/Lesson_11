class DivisionZero(ZeroDivisionError):
    def __init__(self, msg):
        self.msg = msg


try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 0:
        raise DivisionZero("Math Error! Division by zero is not allowed")
except ValueError:
    print("Only numbers")
except DivisionZero as err:
    print(err)
else:
    print(f"{a/b}")
