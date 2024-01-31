# Method-Level Code Smells

This document provides an overview of various method-level code smells often encountered in software development, along with examples in Python.

## Table of Contents
- [Dead Code](#dead-code)
- [Long Parameter List](#long-parameter-list)
- [Black Sheep](#black-sheep)
- [God Method](#god-method)
- [Oddball Solution](#oddball-solution)
- [Indentation Loss](#indentation-loss)

### Dead Code
Dead Code refers to portions of code that are never executed or accessed. Such code can lead to confusion and unnecessary complexity.

**Example:**
```python
def example_function():
    # Code that is never called
    unused_variable = 10
    print("Hello, World!")

# This function contains an unused variable, which is a form of dead code.
```

### Long Parameter List
Methods or functions with an excessively long list of parameters can be challenging to understand and maintain.

Example:

```python
Copy code
```

### Black Sheep
Black Sheep refers to a method that is significantly different from others in terms of its behavior or dependencies. More Information

```python
Copy code
```

### God Method
The God Method is a design smell where a single method performs multiple tasks and is often overly complex.

Example:

```python

class Processor:
    def __init__(self):
        self.data = []

    def process_data(self, file_name):
        # This method does too much, making it a 'God Method'
        file = open(file_name, 'r')
        lines = file.readlines()
        file.close()

        for line in lines:
            if 'error' in line:
                self.data.append(line)

        self.analyze_data()
        self.generate_report()

    def analyze_data(self):
        pass

    def generate_report(self):
        pass

```

### Oddball Solution
An "Oddball" solution is an unconventional approach to solving a problem, differing from the standard or accepted solutions.

Example:

```python
Copy code
def addition_1(n):
    # Summing numbers from 1 to n using a loop
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def addition_2(n):
    # Summing numbers using Gauss's formula
    total = (n * (n + 1)) // 2
    return total

n = 100
print("Sum (Function 1):", addition_1(n))
print("Sum (Function 2):", addition_2(n))
```

### Indentation Loss
Indentation Loss refers to inconsistencies in the indentation of code blocks, leading to reduced readability and potential errors.

Example:

python
Copy code
def control(a, b):
    if a > 0:
        print("a is positive")
    else:
        print("a is negative")
    if b > 0:
        print("b is positive")
    else:
        print("b is negative")
# The indentation is inconsistent, leading to possible confusion.
