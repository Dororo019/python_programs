# wrtie a recursive fibonacci function


def fib(n):
    """
    input: 
        n: int

    return:
        fibbonacci number for n
    """
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(10))

# fib(6) should return 5
# fib(10) should return 34
