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
