def return_decorator(func):
    def wrapper(*args, **kwargs):
        print("Running function...")
        result = func(*args, **kwargs)
        print("Function finished.")
        return result
    return wrapper

@return_decorator
def multiply(a, b):
    return a * b

print(multiply(3, 4))
