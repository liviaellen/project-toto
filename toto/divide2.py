# toto/divide.py
def divide_without_raising(x: float, y: float) -> float:
    '''
    divides x by y, but instead of raising errors when y equals 0, returns:
    - inf if x positive
    - -inf if x negative
    - nan if x equals 0
    '''
    if y == 0:
        if x > 0:
            return float('inf')  # Return inf for positive x
        elif x < 0:
            return float('-inf')  # Return -inf for negative x
        else:
            return float('nan')  # Return nan for x equals 0
    return x / y  # Perform the division if y is not zero

if __name__ == "__main__":
    # Example test cases
    print(divide_without_raising(10, 2))   # Expected output: 5.0
    print(divide_without_raising(10, 0))   # Expected output: inf
    print(divide_without_raising(-10, 0))  # Expected output: -inf
    print(divide_without_raising(0, 0))    # Expected output: nan
