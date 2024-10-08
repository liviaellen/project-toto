# Divide Function by Livia Ellen
This is a Python function named `divide_without_raising` that divides two numbers without raising errors when the denominator is zero. Instead, it returns infinity for positive numerators, negative infinity for negative numerators, and NaN (Not a Number) for a zero numerator.

The function is designed to handle all possible division scenarios, including positive and negative numbers, as well as zero. It is a useful tool for mathematical operations where division by zero is a possibility.

Example usage:
```python
from toto.divide2 import divide_without_raising

# Positive division
print(divide_without_raising(10, 2))  # Output: 5.0

# Division by zero with positive numerator
print(divide_without_raising(10, 0))  # Output: inf

# Division by zero with negative numerator
print(divide_without_raising(-10, 0))  # Output: -inf

# Division by zero with zero numerator
print(divide_without_raising(0, 0))  # Output: nan
```
This function is part of the `toto` package and can be imported and used as shown above.
