# Eksempel på hvordan en task-dekorator i prinsippet fungerer i Prefect:
import functools

class Task:
    def __init__(self, func):
        self.func = func
        self.run_count = 0

    def __call__(self, *args, **kwargs):
        self.run_count += 1
        print(f"Running task '{self.func.__name__}', run count: {self.run_count}")
        return self.func(*args, **kwargs)

def task(func):
    task_instance = Task(func)

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return task_instance(*args, **kwargs)
    return wrapper

@task
def example_task(x, y):
    return x + y

print(example_task(1, 2)) 
print(example_task(5, 3))


# 2. Utvider funskjonaliteten til task-dekoratoren ved å legge til retries og retry_delay_seconds:
# import functools
# import time

# class Task:
#     def __init__(self, func, retries=0, retry_delay_seconds=0):
#         self.func = func
#         self.retries = retries
#         self.retry_delay_seconds = retry_delay_seconds
#         self.run_count = 0

#     def __call__(self, *args, **kwargs):
#         self.run_count += 1
#         print(f"Running task '{self.func.__name__}', run count: {self.run_count}")
#         for attempt in range(1, self.retries + 2):
#             try:
#                 result = self.func(*args, **kwargs)
#                 return result
#             except Exception as e:
#                 if attempt <= self.retries:
#                     print(f"Error: {e}. Retrying in {self.retry_delay_seconds} seconds... (Attempt {attempt}/{self.retries})")
#                     time.sleep(self.retry_delay_seconds)
#                 else:
#                     print(f"Task '{self.func.__name__}' failed after {self.retries} retries.")
#                     raise

# def task(retries=0, retry_delay_seconds=0):
#     def decorator(func):
#         task_instance = Task(func, retries=retries, retry_delay_seconds=retry_delay_seconds)

#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             return task_instance(*args, **kwargs)

#         return wrapper
#     return decorator

# @task(retries=3, retry_delay_seconds=1)
# def unreliable_function():
#     import random
#     if random.choice([True, False]):
#         raise ValueError("Random failure!")
#     return "Success!"

# print(unreliable_function())

# 3. Logikken kan også ligge i wrapper-funksjonen: 
# import functools
# import time

# def task(retries=0, retry_delay_seconds=0):
#     def decorator(func):
#         run_count = 0
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             nonlocal run_count
#             run_count += 1
#             print(f"Running task '{func.__name__}', run count: {run_count}")
#             for attempt in range(1, retries + 2):
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     if attempt <= retries:
#                         print(f"Error: {e}. Retrying in {retry_delay_seconds} seconds... (Attempt {attempt}/{retries})")
#                         time.sleep(retry_delay_seconds)
#                     else:
#                         print(f"Task '{func.__name__}' failed after {retries} retries.")
#                         raise
#         return wrapper
#     return decorator

# @task(retries=3, retry_delay_seconds=1)
# def unreliable_function():
#     import random
#     if random.choice([True, False]):
#         raise ValueError("Random failure!")
#     return "Success!"

# print(unreliable_function())

# Lær mer om dekoratorer her: https://realpython.com/primer-on-python-decorators/