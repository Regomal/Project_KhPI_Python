# ============= Task A =============
print("=" * 50)
print("Task A) Higher-Order Function")

def apply(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

lst = [1, 2, 3]
print(f"List: {lst}")
print(f"apply(lambda x: x * x, {lst}) -> {apply(lambda x: x * x, lst)}")

print("=" * 50, end = "\n\n")


# ============= Task B =============
print("=" * 50)
print("Task B) map")

lst = [1, 2, 3]
print(f"List: {lst}")
print(f"Squared -> Strings: {list(map(str, list(map(lambda x: x**2, lst))))}")

print("=" * 50, end = "\n\n")


# ============= Task C =============
print("=" * 50)
print("Task C) filter")

lst = [5, 10, 15, 20]
print(f"List: {lst}")
print(f"%2 == 0: {list(filter(lambda x: x % 2 == 0, lst))}")
print(f">10: {list(filter(lambda x: x > 10, lst))}")

print("=" * 50, end = "\n\n")


# ============= Task D =============
print("=" * 50)
print("Task D) map/filter vs comprehension")

lst = [1, 2, 3, 4, 5, 6]
print(f"Original list: {lst}")

res_1 = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, lst)))
res_2 = [x**2 for x in lst if x % 2 == 0]

print(f"map + filter: {res_1}")
print(f"list comprehension: {res_2}")

print(f"Is equal -> {res_1 == res_2}")

print("=" * 50, end = "\n\n")


# ============= Task E =============
print("=" * 50)
print("Task E) Simple Decorator")

def call_counter(func):
    cnt = 0
    def wrapper(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print(f"call #{cnt}")
        return func(*args, **kwargs)
    return wrapper

@call_counter
def fun():
    return 42

for _ in range(3):
    fun()

print("=" * 50, end = "\n\n")


# ============= Task F =============
print("=" * 50)
print("Task F) Decorator with Arguments")

def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"{text}: {func(*args, **kwargs)}"
        return wrapper
    return decorator

@prefix("INFO")
def get_data():
    return "data"

print(get_data())

print("=" * 50, end = "\n\n")


# ============= Task G =============
print("=" * 50)
print("Task G) Caching Decorator")


def cache(func):
    storage = {}
    def wrapper(*args):
        if args in storage:
            return storage[args]
        result = func(*args)
        storage[args] = result
        return result
    return wrapper

def count_calls_G(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1      # as it turns out, `nonlocal` doesn't play well with recursion
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper


@count_calls_G
def tribonacci(n):
    if n < 0: return -1
    elif n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 1
    else: return tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)


@count_calls_G
@cache
def tribonacci_cache(n):
    if n < 0: return -1
    elif n == 0: return 0
    elif n == 1: return 1
    elif n == 2: return 1
    else: return tribonacci_cache(n - 1) + tribonacci_cache(n - 2) + tribonacci_cache(n - 3)

import time
n = 25
print(f"Steps {n}: ")

start = time.time()
res_1 = tribonacci(n)
time_1 = time.time() - start
print(f"without cache: result={res_1}, time={time_1} sec, calls={tribonacci.calls}")

start = time.time()
res_2 = tribonacci_cache(n)
time_2 = time.time() - start
print(f"with cache: result={res_2}, time={time_2} sec, calls={tribonacci_cache.calls}")

print("\n")

print("""Steps 30: 
without cache: result=29249425, time=10.159270286560059 sec, calls=56843233
with cache: result=29249425, time=0.0 sec, calls=85""")

print("=" * 50, end = "\n\n")