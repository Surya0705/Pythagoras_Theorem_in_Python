import math # Importing the math module for Square Root.

a = float(input("Enter the Measure of First Side: ")) # Taking the Measure of the First Side as Input from the User.
b = float(input("Enter the Measure of Second Side: ")) # Taking the Measure of the Second Side as Input from the User.

c = (a ** 2) + (b ** 2) # Adding the Squares of Both Sides as stated in the Pythagoras Theorem.
d = math.sqrt(c) # Finding the Square Root of 'c' to find the Measure of the Hypoteneuse.
print(f"Using the Pythagoras Theorem the Hypoteneuse[Third Side] will measure {d}.") # Printing the Result.