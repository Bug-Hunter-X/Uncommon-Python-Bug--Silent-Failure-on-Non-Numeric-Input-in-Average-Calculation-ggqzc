def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0  # Handle empty or non-numeric list
    return sum(numeric_numbers) / len(numeric_numbers)
    #Alternatively: use numpy.mean()
    #import numpy as np
    #return np.mean(numeric_numbers) 