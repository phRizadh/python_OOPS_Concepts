# Using the example with a decorator, here argument is passed using sys.argv via command line

# Arguments are always in list and accessed by indexing first element in the list is always the python file name.

import cProfile, pstats, io, sys
from pstats import SortKey

# sys.argv[0] - > example.py hence we pass the second element at index 1 - > sys.argv[1] as text filename to log report

filename = sys.argv[1]

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
    
    # writing the program profile statistics to a text file. Here the 'filename' value is given via command line
    with open(filename, 'a+') as f:
      ps.print_stats()
      f.write(str(s.getvalue()))
    return value
  return perf_wrapper

# Decorate main_func -> main_function with the decorated function 'performance'
@performance
def main_function(x):
    result = 1
    for i in range(1, x):
        result *= i
    return result
print(main_function(100000))

# python parsing.py log_performance.txt
