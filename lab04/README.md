# LAB04: Higher-Order Functions, map/filter, Decorators

LAB04 is a university lab project designed to practice using higher-order functions and to understand how functions can
be used to transform behavior.

The project covers and demonstrates:

- Higher-order functions (functions as arguments and return values)
- Functional transformations using map and filter
- Differences between map/filter and comprehensions
- Decorators and how they modify function behavior
- Decorators with arguments
- Basic caching techniques using decorators

---

## Requirements

- Python 3.10+

---

## Environment Setup

To ensure the project runs cleanly and doesn't conflict with your system Python packages, it is highly recommended to
use a virtual environment.

**1. Create a virtual environment:**
Open your terminal in the root of the project (the `lab04` folder) and run:

    python -m venv venv

*(Use `python3` instead of `python` depending on your OS).*

**2. Activate the virtual environment:**

- On **Windows**:

  venv\Scripts\activate

- On **macOS / Linux**:

  source venv/bin/activate

**3. Install dependencies:**
Once the virtual environment is active, install the required packages (even if the file is currently empty, this is a
good practice):

    pip install -r requirements.txt

---

## Repository Structure

    lab04/
    ├── README.md           → this file
    ├── requirements.txt    → external dependencies if used (may be empty)
    ├── src/
    │   └── lab04.py         → source code containing the implementation of the tasks
    └── report/
        └── answers.md      → short explanations requested in the tasks

---

## Implemented Tasks

All tasks are executed sequentially from the main script.

- **Task A: Higher-Order Function**
  Implements an `apply(func, data)` function to process lists without using the built-in map.
- **Task B: map**
  Uses map to square numbers and convert them to strings.
- **Task C: filter**
  Uses filter to keep only even numbers and numbers greater than 10.
- **Task D: map/filter vs comprehension**
  Solves the same filtering and squaring task using both map+filter and list comprehensions to compare approaches.
- **Task E: Simple Decorator**
  Implements a `@call_counter` decorator that counts and prints how many times a function has been executed.
- **Task F: Decorator with Arguments**
  Implements a `@prefix("text")` decorator that prepends specific text to the returned result of a function.
- **Task G: Caching Decorator**
  Implements a `@cache` decorator to store previously computed results, demonstrating performance improvements on a
  recursive function.

---

## Execution

Ensure your virtual environment is activated, then run the code from the root directory of the project.

Command:

    python src/lab04.py

Output includes:

- Programs running without errors
- Correct results and demonstrations of the required functionality

---

## Important Notes

- Short explanations and answers to theoretical questions are located in `report/answers.md`.
- Estimated work time: 2-3 hours.