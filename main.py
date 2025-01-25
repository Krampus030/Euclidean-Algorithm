class GCD:
    """
    create two variables and the main algorithm as a method

    """

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def euclidean_algorithm(self):
        times = 0
        # set the condition of iteration, the algorithm won't stop before reaching the answer
        while self.b != 0:
            print(f"a = {self.a}, b = {self.b}")

            remainder = self.a % self.b  # A = Q * B + R, This is R

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


while True:
    """
    keep the program iterative 
    """
    x = int(input("Please enter the first number here.\n "))
    y = int(input("Please enter the second number here.\n "))

    if x >= 0 and y >= 0:
        GCD1 = GCD(x, y)  # only if the inputs are validated, create the object and print the results
        print(GCD1)
    else:
        print("Your input is not valid, please try again")  # error message
