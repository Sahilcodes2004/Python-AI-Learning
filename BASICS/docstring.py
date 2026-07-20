#docsrings is used to add cooments or for future rememberance of logic

def increment(n):
    """Increment a number"""
    return n+1
print(increment(3))
print(increment.__doc__)
#annotations

def decre(n: int)->int:
    return n-1
print(decre(7))
#docstring are written just after the fuction name or just above the function body 