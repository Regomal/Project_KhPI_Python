splits = 70
# ============= Task A =============
print("=" * splits)
print("Task A) Functions as Objects")


def apply_twice(func, x):
    return func(func(x))
def square(x):
    return x * x

functions = [lambda x: x + 1, abs, square]

for f in functions:
    print(f"func: {f.__name__} -> {apply_twice(f, -3)}")

# ============= Task B =============
print("=" * splits)
print("Task B) Sorting with Lambda")

people = [
("Alice", 25),
("Bob", 20),
("Carol", 30),
("Dave", 22)
]

print(f"Sorted by age: {sorted(people, key=lambda x: x[1])}")
print(f"Sorted by name: {sorted(people, key=lambda x: x[0])}")

# ============= Task C =============
print("=" * splits)
print("Task C) Function Factory")

def make_multiplier(k):
    def multiplier(x):
        return x * k
    return multiplier

times3 = make_multiplier(3)
print(f"Multiplier = 3 -> {times3(10)}")

times5 = make_multiplier(5)
print(f"Multiplier = 5 -> {times5(10)}")

# ============= Task D =============
print("=" * splits)
print("Task D) Closure Counter")

def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter()
print(c())
print(c())
print(c())

# ============= Task E =============
print("=" * splits)
print("Task E) Lambda vs def")

def square_def(x):
    return x ** 2

square_lambda = lambda x: x ** 2

print(f"def: {square_def(4)}, lambda: {square_lambda(4)}")
print(f"def == lambda : {square_def(4) == square_lambda(4)}")

# ============= Task F =============
print("=" * splits)
print("Task F) Functional Composition")

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = sum( (x ** 2 for x in filter(lambda x: x % 2 == 0, numbers)) )

print(f"Result: {result}")

