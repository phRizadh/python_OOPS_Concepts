# Decorator is used to modify the functional behavior of a specific function by wrapping it in another function.
# We create a script which creates a profile with a set of statistics. It's used to analyze duration and instances of the program executed.
# The same results are logged in a text file

import cProfile, pstats, io
from pstats import SortKey


def performance(main_func):
  def perf_wrapper(*args):
    
    # Behavior to decorated function. This remains active throughout the execution of the main_func -> main_function
    pr = cProfile.Profile()
    pr.enable()
    value = main_func(*args)
    pr.disable()
    s = io.StringIO()
    sortby = SortKey.CUMULATIVE
    ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
    
    # writing the program profile statistics to a text file
    with open('log_performance.txt', 'a+') as f:
      ps.print_stats()
      f.write(str(s.getvalue()))
    return value
  return perf_wrapper

# Function 1
# Decorate main_func -> main_function with the decorated function 'performance'
@performance
def main_function(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result
print(main_function(100000))

# Function 2
# Decorate main_func -> main_function2 with the decorated function 'performance'
@performance
def main_function2(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result
print(main_function2(200000))


