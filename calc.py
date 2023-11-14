def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")



while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    start = input("input: ")

    if start == "a" or start == "A":
        print("Addition")
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        add(a, b)
    elif start == "b" or start == "B":
        print("Subtraction")
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        add(a, b)
    elif start == "c" or start == "C":
        print("Multiplication")
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        add(a, b)
    elif start == "d" or start == "D":
        print("Division")
        a = int(input("Enter First Number"))
        b = int(input("Enter Second Number"))
        add(a, b)
    elif start == "e" or start == "E":
        print("Exiting...")
        quit()