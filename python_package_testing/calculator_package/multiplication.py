def multiply_two_numbers(a,b):
    """Multiply two numbers and return the result"""
    return a*b

def multiply_multiple_numbers(*args):
    """Multiply multiple numbers and return the result"""
    result = 1
    for num in args:
        result*=num
    return result