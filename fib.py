"""

lru_cache не использовать

"""

cache = {0: 0, 1: 1}


def fib(num):
    # if num == 4:
    #     print(4)
    if num in cache:
        return cache[num]
    cache[num] = (fib(num - 1) + fib(num - 2))
    return cache[num]


fib(10)
# for i in range(1,9):
#     print(fib(i))
