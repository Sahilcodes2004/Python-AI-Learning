#docsrings is used to add cooments or for future rememberance of logic

def increment(n):
    """Increment a number"""
    return n+1
print(increment(3))
#annotations

def decre(n: int)->int:
    return n-1
print(decre(7))