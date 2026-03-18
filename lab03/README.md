# LAB03: Functions as Objects, Lambda, Closures

LAB03 is a university lab project used to explore Python functions as first-class objects, demonstrating an understanding of core language concepts.

The project covers and demonstrates:

- Functions as objects
- Lambda expressions
- Closures
- Basic functional composition

---

# Requirements

- Python 3.10+ (or specify the Python version used)

---

# Repository Structure

```text
lab03/
├── README.md           → this file
├── requirements.txt    → external dependencies if used (may be empty)
├── src/
│   └── main.py         → source code containing your implementation of the tasks
└── report/
    └── answers.md      → short explanations requested in the tasks
```

# Implemented Tasks

All tasks are executed sequentially from the main script.

## Task A: Functions as Objects

Demonstrates how to apply a given function two times using `apply_twice(func, x)`.

## Task B: Sorting with Lambda

Sorts a list of people by age and by name using lambda expressions with `sorted`.

## Task C: Function Factory

Implements a `make_multiplier(k)` function that returns another function to multiply its argument by `k`.

## Task D: Closure Counter

Implements a counter using closures to store the internal state.

## Task E: Lambda vs def

Creates two equivalent implementations of the same functionality (e.g., a function that squares a number) using `def` and `lambda`.

## Task F: Functional Composition

Creates a small processing pipeline for a list of numbers to keep only even numbers, square them, and compute the sum using lambda and generator expressions.

---

# Execution

All code should be executed from the root directory of the project.

Command:

    python src/main.py

*(Use `python3` instead of `python` depending on your environment).*

Output includes:

- Demonstrations of the required functionality
- Correct results printed for all tasks running without errors

---

# Important Notes

- Short explanations requested in the tasks and answers to theoretical questions (e.g., what it means that functions are first-class objects, the difference between `def` and a lambda expression, closures) are located in `report/answers.md`.
- Estimated work time: 2-3 hours.