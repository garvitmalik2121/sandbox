MINIMUM_LENGTH = 6
def main():
    password = input("Enter password")
    while len(password) < MINIMUM_LENGTH:
        print("Invalid Input")
        password = input("Enter password")
    for stars in range(len(password)):
        print("*", end="")
main()