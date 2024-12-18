# 1. Man bør også være oppmerksom på at decorated funksjoner ikke returnerer noe uten at det er spesifisert i wrapper-funksjonen.
def simple_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before the function is called.")
        func(*args, **kwargs)
        print("After the function is called.")
    return wrapper

@simple_decorator
def say_hello(text):
    print(text)
    return text

hello = say_hello("Hello!")
print(hello)

# 2. Vi kan løse dette ved å returnere funksjonen i wrapper-funksjonen:
# def simple_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before the function is called.")
#         func(*args, **kwargs)
#         print("After the function is called.")
#         return func(*args, **kwargs)
#     return wrapper

# @simple_decorator
# def say_hello(text):
#     print(text)
#     return text

# hello = say_hello("Hello!")
# print(hello)

# 3. Det er litt unødvendig å kalle funksjonen to ganger, så vi kan lagre resultatet i en variabel:
# def simple_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before the function is called.")
#         result = func(*args, **kwargs)
#         print("After the function is called.")
#         return result
#     return wrapper

# @simple_decorator
# def say_hello(text):
#     print(text)
#     return text

# hello = say_hello("Hello!")
# print(hello)
