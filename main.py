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

    try:
        """
        keep the program iterative 
        use try except to show error message when the user input is invalid(number or string)
        """
        x = int(input("Please enter the first number:\n "))
        y = int(input("Please enter the second number:\n"))

        if x < 0 or y < 0:
            print("Only non-negative integers are allowed. Please try again.")
            continue

        gcd_instance = GCD(x, y)
        print(gcd_instance)

    except ValueError:
        print("Invalid input! Please enter an integer.")  # error message
