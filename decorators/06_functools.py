# 1. Når man dekorerer en funksjon, vil funksjonen som dekorerer den overskrive metadata som navn og docstring.
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        result = func(*args, **kwargs)
        print("After the function is called.")
        return result
    return wrapper

@simple_decorator
def say_hello(text):
    """Veldig nyttig docstring."""
    print(text)
    return text

print(say_hello.__name__)
print(say_hello.__doc__)

# 2. Dette kan løses ved å bruke functools.wraps fra functools-modulen:
# import functools

# def simple_decorator(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Before the function is called.")
#         result = func(*args, **kwargs)
#         print("After the function is called.")
#         return result
#     return wrapper

# @simple_decorator
# def say_hello(text):
#     """Veldig nyttig docstring."""
#     print(text)
#     return text

# print(say_hello.__name__)
# print(say_hello.__doc__)
