#############################
## DECORATORS W/ ARGUMENTS ##
#############################
def repeat(num):
    def decorator_repeat(func):
        def wrapper(*args, **kwargs):
            for _ in range(num):
                func(*args, **kwargs)
        return wrapper
    return decorator_repeat

@repeat(num=3)
def greet(name):
    print(f"Hello {name}")


#################################
## DECORATORS W/ RETURN VALUES ##
#################################
def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}({args}, {kwargs}) returned {result}")
        return result
    return wrapper

@debug
def add(a, b):
    return a+ b


if __name__ == '__main__':
    # greet('Alice')

    print(add(2, b=3))