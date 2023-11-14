def main():
    name = input("Enter your name: ")
    print("Hi, Welcome " + name)
    print("")

    email_input = input("Enter your Email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ", username)
    print("Domain : ", domain)
    print("Extension : ", extension)

while True:
    main()