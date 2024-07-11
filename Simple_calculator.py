# Task : Design a simple calculator with basic arithmetic operations.

def sum(a, b):
    return a + b
def difference(a, b):
    return a - b
def product(a, b):
    return a * b
def division(a, b):
    return a / b

n1 = eval(input("Enter first number: "));
n2 = eval(input("Enter second number: "));

print("Select the operation : ")
print("1. Sum")
print("2. Difference")
print("3. Product")
print("4. Division")

while(True):
    choice = int(input("Enter the choice from (1/2/3/4):"))
    if choice in (1,2,3,4):
        if choice == 1:
            print(n1, "+", n2, "=", sum(n1, n2))
            break
        elif choice == 2:
            print(n1, "-", n2, "=", difference(n1, n2))
            break
        elif choice == 3:
            print(n1, "*", n2, "=", product(n1, n2))
            break
        elif choice == 4:
            print(n1, "/", n2, "=", division(n1, n2))
            break
    else:
        print("Invalid input")
exit()

            