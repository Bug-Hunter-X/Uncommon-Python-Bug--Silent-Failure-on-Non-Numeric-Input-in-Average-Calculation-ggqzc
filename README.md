# Uncommon Python Bug: Silent Failure on Non-Numeric Input in Average Calculation

This repository demonstrates a subtle bug in a Python function designed to calculate the average of a list of numbers. While the function correctly handles empty lists, it silently fails when provided with non-numeric input, leading to unexpected results.

The `calculate_average.py` file contains the buggy code, while `calculate_average_solution.py` provides a robust solution.  The issue highlights the importance of comprehensive error handling in numerical computations.

## Bug Report
The `calculate_average()` function does not perform any checks to ensure that the input list contains only numbers.  If a string or other non-numeric type is present, `sum()` will raise a `TypeError`. However, this error is not explicitly handled and may lead to unexpected behavior or crashes without clear error messages to the user.