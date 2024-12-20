

def palindrome(num: int) -> bool:
    rev = 0
    n = num
    while n > 0:
        rev = ( rev * 10 ) + (n % 10)
        n //= 10
    
    return rev == num

def add(a, b):
    return a + b

def greet(str):
    return f"Hello {str}"
