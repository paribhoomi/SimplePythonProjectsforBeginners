def logger(func):
    def wrapper(*args,**kwargs):
        print(f"Running {func.__name__}")
        result = func(*args,**kwargs)
        print(f"Finished{func.__name__}")
        return result
    return wrapper

@logger
def add(a,b):
    return a+b

print(add(5,3))