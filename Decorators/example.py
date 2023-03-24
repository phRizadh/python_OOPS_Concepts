# Decorator is used to modify the functional behavior of a specific function by wrapping it in another function.
# We demonstrate decorators with a simple example: displays time taken to execute 2 different function

import time, math
def exec_time(main_func):
      
  # Decorator Function
  def exec_wrapper(*args):
    before_exec = time.time()
    value = main_func(*args)
    after_exec = time.time()
    func_name = main_func.__name__
    print(f'Main function -> {func_name} took {after_exec - before_exec} seconds to execute')
    return value
  return exec_wrapper

@exec_time
def main_function1(x):
  print(math.factorial(x))
main_function1(20)

@exec_time
def main_function2(x):
  print(math.factorial(x))
main_function2(30)
