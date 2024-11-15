# 1. Hvis man legger til et argument i den dekorerte funksjonen, vil det gi en feilmelding.
def simple_decorator(func):
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@simple_decorator
def say_hello(text):
    print(text)

say_hello("Hello!")

# 2. Dette kan løses med å bruke *args og **kwargs i wrapper-funksjonen:
# def decorator_with_args(func):
#     def wrapper(*args, **kwargs):
#         print(f"Function called with args: {args}, kwargs: {kwargs}")
#         return func(*args, **kwargs)
#     return wrapper

# @decorator_with_args
# def add(a, b, c):
#     return a + b + c

# print(add(2, 3, c=4))

# 3. Så vårt opprinnelige eksempel blir slik:
# def simple_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before the function is called.")
#         func(*args, **kwargs)
#         print("After the function is called.")
#     return wrapper

# @simple_decorator
# def say_hello(text):
#     print(text)

# say_hello("Hello!")