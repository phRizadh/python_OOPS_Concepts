"""

Usually while generating a set of elements, it returns the actual set of elements itself.
But 'Generator' function returns an iterator, instead of actual set of elements,
that produces a sequence of values when iterated over using 'yield' statement.

"""

# Below is a primitive way of generating fibonacci series. This causes performance issues while generating the series for a large set 

"""
def f_series(n):
    a = 0
    b = 1
    print(b)
    for x in range(2, n):
        c = a + b
        print(c)
        a = b
        b = c
f_series(100)
"""

# Above example can be demonstrated in a simpler and efficient way using the generator function with the help of yield statement
def f_series():
    a, b = 0, 1
    while True:
      yield b
      a, b = b, a + b
    
# The Generator instead of returning the results, creates an iterator to be used when needed. 
f_gen = f_series()

# The type of 'f_gen' as can be seen here is a class of type 'Generator'. 
"""
print(type(f_gen))
"""
# The the generator can be iterated as shown below. It returns the results 1,1,2. Using the next statement it returns the next value in the iterator.
"""
print(next(f_gen))
print(next(f_gen))
print(next(f_gen))
"""
# It can be iterated with in a simpler way if we need a specific set of elements
"""
[next(f_gen) for i in range(10)]
"""
# If we need a specific value from a set
"""
list([next(f_gen) for i in range(10)])[4]
"""



