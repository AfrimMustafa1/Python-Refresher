# Python Refresher Assignment

## Overview

This repository contains two Python scripts demonstrating fundamental programming concepts:

1. **Echo Simulation (`echo.py`)** - Simulates an echo effect with repeated fading text.
2. **Fibonacci Sequence (`fib.py`)** - Implements a recursive Fibonacci function with performance optimization using decorators.

## 1. Echo Simulation (`echo.py`)

The `echo.py` script defines a function that simulates a mountain echo by repeating a given text with a fading effect.

### Implementation:
```python
def echo(text: str, repetitions: int = 3) -> str:
    """Imitate a real-world echo."""
    output = []
    for i in range(repetitions):
        output.append(text[:len(text) - i])
    return "\n".join(output)

if __name__ == "__main__":
    text = input("Yell something at a mountain: ")
    print(echo(text))
```

### Example Usage:
```bash
$ python echo.py
Yell something at a mountain: Helloooo
Helloooo
Hellooo
Helloo
```

---

## 2. Fibonacci Sequence (`fib.py`)

The `fib.py` script calculates the nth Fibonacci number using a recursive approach. It utilizes two decorators:

- `@lru_cache` to store previously computed values for optimization.
- `@timer` to measure execution time for each function call.

### Implementation:
```python
from functools import lru_cache
import time

def timer(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print(f"Finished in {end - start:.6f}s: fib({n}) = {result}")
        return result
    return wrapper

@lru_cache
@timer
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    fib(100)
```

### Example Output:
```bash
Finished in 0.000001s: fib(0) = 0
Finished in 0.000002s: fib(1) = 1
Finished in 0.000003s: fib(2) = 1
Finished in 0.000004s: fib(3) = 2
Finished in 0.000005s: fib(4) = 3
...
Finished in 0.083417s: fib(100) = 354224848179261915075
```

---

## 3. Execution Time Plot

The script records execution times and can generate a plot similar to the following:

![Execution Time Plot](execution_time_plot.png)

The x-axis represents `n` in Fibonacci number calculation, and the y-axis represents time in seconds.

---

## Submission Requirements

- The repository includes:
  - `echo.py`
  - `fib.py`
  - A properly formatted `README.md`
  - Screenshot images of code and output
  - A plot of execution time for `fib(n)`
- The `README.md` should document the assignment with explanations and images.

---

### Author:
**[Afrim Mustafa]**  
*University of Iowa - CS:3980 - Spring 2025*
