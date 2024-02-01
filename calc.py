print("Hello world!")

def add(num1,num2):
    sum = num1 + num2
    return sum

def sub(num1,num2):
    difference = num1 - num2
    return difference
def prod(num1,num2):
    product = num1 * num2
    return product
def div(num1,num2):
    division = num1/num2
    return division

print("Welcome to the basic calculator")
print("Due to some development issues, this calculator can only handle small basic\n calucations between two numbers.")

print("First number")
fig1 = int(input("Enter the first number here: "))

print("Second number")
fig2 = int(input("Enter the second number here: "))

Choice = input("Here choose what kind of arithmetic operations you would like to\n calculate from the options below: ")
print("Addition")
print("Subtraction")
print("Product")
print("Division")

if Choice == "Addition":
    print(add(fig1,fig2))
elif Choice == "Subtraction":
    print(sub(fig1,fig2))
elif Choice == "Product":
    print(prod(fig1,fig2))
else:
    print(div(fig1,fig2))


