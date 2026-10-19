## Task 1: Execution Counter Closure 
def make_counter(start_value=0):
    count = start_value

    def counter():
        nonlocal count
        count += 1
        return count

    return counter



counter = make_counter(start_value=10)
print(counter())  
print(counter()) 

##Task 2: Execution Time & Metadata Logger Decorator

from functools import wraps
import time

def log_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Running [{func.__name__}]... Executed in {execution_time:.2f} seconds.")
        return result

    return wrapper
@log_execution
def example_function(n):
    """Calculates the sum of numbers up to n."""
    total = sum(range(n))
    time.sleep(1)  
    return total

print("Result:", example_function(1000000))

##Task 3: Access Control / Password Required Decorator 
def require_role(allowed_role="admin"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            user_role = kwargs.get("user_role")

            if user_role == allowed_role:
                return func(*args, **kwargs)
            else:
                print("Permission Denied: User is not an admin.")

        return wrapper

    return decorator

@require_role(allowed_role="admin")
def sensitive_action(user_role):
    print("Action executed successfully!")

sensitive_action(user_role="admin")  
sensitive_action(user_role="user")  