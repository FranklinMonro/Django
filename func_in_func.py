def hello(name='franco'):
    print("The hello() function has been run!")

    def greet():
        return "This string is inside greet()"

    def welcome():
        return "This string is inside welcome()"

    if name == "jose":
        return greet
    else:
        return welcome


x = hello()

print(x())
