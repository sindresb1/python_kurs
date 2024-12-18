def simple_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()