def decorator_with_args(func):
    def wrapper(*args, **kwargs):
        print(f"Function called with args: {args}, kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper

@decorator_with_args
def add(a, b, c):
    return a + b + c

print(add(2, 3, c=4))
