from typing import Optional
# Purpose:
# The `str_to_float` function attempts to convert a string to a floating-point number.
# If the string represents a valid number, it returns the float; otherwise, it returns None.

# Input:
# - A single string `s`, which is expected to represent a number.
# - The string can either be a valid number (e.g., '3.14', '42') or an invalid number (e.g., 'abc', '123abc').
# 
# Output:
# - If `s` can be successfully converted to a float, return the float representation of the string.
# - If `s` cannot be converted to a float (i.e., it is not a valid number), return None.
def str_to_float(s: str) -> Optional[float]:
    try:
        return float(s)
    except ValueError:
        return None

