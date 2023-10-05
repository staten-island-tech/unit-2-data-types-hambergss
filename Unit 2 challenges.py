# integers and floats

x = 8
y = float(8)
print(x,y)

# tip calculator

bill = float(input("Enter your bill: "))
tip = int(input("Enter your tip: "))

print(bill)
print(tip)
print(bill + tip)

# challenge on creating a function that determines if a number is odd or even

x = int(input("Enter a number: "))

if x%2 == 0:
    print("It is Even")
else:
    print("It is Odd")

# challenge on creating a function to accept a "bill" value and offer a tipe of 0%, 15%, 20%, or 25% depending on if the service was "bad, okay, good, or great".

x = input("Enter your bill amount: ")
y = input("Enter how your service was; bad, okay, good, great: ")

if y == "bad":
    print("Your tip is 0%, Sorry about the service.")
elif y == "okay":
    print("Your tip is 15%, Thank you, please come again!")
elif y == "good":
    print("Your tip is 20%, Thank you, please come again!")
elif y == "great":
    print("Your tip is 25%, Thank you, please come again!")
else:
    print("Sorry I don't understand.")

# challenge finding all the factors of a number

x = int(input("Enter a number: "))
def print_factors(x):
    print("The factors of",x,"are: ")
    for i in  range(1, x + 1):
        if x % i == 0:
            print(i)

num = x
print_factors(num)

# challenge to find the greatest common factor between 2 numbers

x = int(input("Enter an integer: "))
y = int(input("Enter another integer: "))

r = x%y
q = int(x/y)

