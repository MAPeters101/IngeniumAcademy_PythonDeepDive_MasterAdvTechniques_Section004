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


if __name__ == '__main__':
    greet('Alice')