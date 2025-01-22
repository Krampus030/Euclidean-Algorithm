class GCD:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def equal_to_0(self):
        if self.a == 0:
            return f"The GCD of {self.a} and {self.b} is {self.b}"
        if self.b == 0:
            return f"The GCD of {self.a} and {self.b} is {self.a}"


    def euclidean_algorithm(self):
        while self.b != 0:
            print(f"a = {self.a}, b = {self.b}")

            remainder = self.a % self.b

            print(f" The remainder of {self.a} divider by {self.b} is {remainder}")

            self.a = self.b
            self.b = remainder

            print(f"After one calculation, a = {self.a}, b = {self.b}")

        return f"{self.a} is the GCD of a and b"

    def __str__(self):
        return self.euclidean_algorithm()


GCD1 = GCD(100,99)
print(GCD1)