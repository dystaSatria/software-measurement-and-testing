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

# Example missing. In practice, this would be a method with a long list of parameters.
Black Sheep
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
