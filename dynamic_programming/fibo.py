def fibonacci(n):
    if (n <= 0):
        return 0
    elif (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_memoize(n, cache=[]):
    if (len(cache) == 0):
        cache = [0]*(n+1)

    if (n <= 0):
        return 0
    elif (n == 1 or n == 2):
        return 1

    if (cache[n-1] < 1):
        result1 = fibonacci_memoize(n - 1, cache)
        cache[n - 1] = result1
    
    if (cache[n-2] < 1):
        result2 = fibonacci_memoize(n - 2, cache)
        cache[n-2] = result2

    
    cache[n] = cache[n-2] + cache[n-1]

    return cache[n]

def fib_bottom_up(n):
    if (n <= 0):
        return 0
    elif (n == 1 or n == 2):
        return 1

    cache = [0]*(n + 1)
    cache[1] = 1
    cache[2] = 1

    for i in range(3, n + 1):
        cache[i] = cache[i - 1] + cache[ i - 2]

    return cache[n]

n = 10
print(fibonacci(n))
n = 3
print(fibonacci(n))
n = 10
print(fibonacci(n))


n = 10
print(fibonacci_memoize(n))
n = 3
print(fibonacci_memoize(n))
n = 1000
print(fibonacci_memoize(n))


n = 10
print(fib_bottom_up(n))
n = 3
print(fib_bottom_up(n))
n = 100000
print(fib_bottom_up(n))
