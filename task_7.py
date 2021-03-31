class ComplexNumber:
    def __init__(self, num_1, num_2):
        self.num_1 = num_1
        self.num_2 = num_2

    def get_complex_num(self):
        return complex(self.num_1, self.num_2)

    def __add__(self, other):
        self.sum_1 = self.num_1 + other.num_1
        self.sum_2 = self.num_2 + other.num_2
        return complex(self.sum_1, self.sum_2)

    def __mul__(self, other):
        self.mul_1 = self.num_1 * other.num_2 - self.num_2 * other.num_1
        self.mul_2 = self.num_2 * other.num_1 + self.num_1 * other.num_2
        return complex(self.mul_1, self.mul_2)


a = ComplexNumber(3, -3)
b = ComplexNumber(4, 3)
print(f"First complex: {a.get_complex_num()}\nSecond complex: {b.get_complex_num()}"
      f"\nSum of complex: {a + b}\nMul of complex: {a * b}")
