class GCD:
    """
    create two variables and the main algorithm as a method

    """
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def euclidean_algorithm(self):
        # set the condition of iteration, the algorithm won't stop before reaching the answer
        while self.b != 0:
            print(f"a = {self.a}, b = {self.b}")

            remainder = self.a % self.b  # A = Q * B + R, This is R
            times = 0

            print(f" The remainder of {self.a} divider by {self.b} is {remainder}")

            # gcd(a,b) = gcd(b, r)
            self.a = self.b
            self.b = remainder
            times += 1

            # print current value, and how many times it calculates
            print(f"After {times} calculation, a = {self.a}, b = {self.b}")

        return f"{self.a} is the GCD of a and b"

    def __str__(self):
        """
        print the exact value of the method, which is GCD(a,b)
        not the memory address.
        :return: gcd(a,b)
        """
        return self.euclidean_algorithm()


GCD1 = GCD(100, 99)  # create the object and print the results
print(GCD1)
