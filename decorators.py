# Prøv å komme på en god oppgave som kan løses med en decorator.


# Start med å vise at Prefect i stor grad bruker dekoratorer.

# Kanskje det er mulig å vise hvordan en task eller flow fungerer med pseudokode?

from functools import wraps

class Task:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        # Simulating task logic (e.g., logging, retries, tracking)
        print(f"Running task: {self.func.__name__}")
        try:
            result = self.func(*args, **kwargs)
            print(f"Task {self.func.__name__} completed successfully.")
            return result
        except Exception as e:
            print(f"Task {self.func.__name__} failed with error: {e}")
            raise

def task(func):
    """
    A decorator to transform a function into a Prefect-like task.
    """
    # Use functools.wraps to preserve the original function's metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Wrap the function in the Task class
        return Task(func)(*args, **kwargs)
    
    return wrapper

# Usage
@task
def example_task(x, y):
    return x + y

# Simulate running the task
if __name__ == "__main__":
    result = example_task(5, 10)
    print(f"Task result: {result}")
