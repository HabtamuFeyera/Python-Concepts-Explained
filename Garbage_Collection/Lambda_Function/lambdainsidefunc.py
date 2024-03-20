def myfunc(n):
    return lambda x: x * n

doubler = myfunc(4)
print(doubler(12))

tripler = myfunc(3)
print(tripler(6))