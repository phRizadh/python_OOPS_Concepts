# Funtion 1 takes parameter: param_1 and it should be of integer type 
# and the return value should also be an interger type

def function_1(param_1: int) -> int:
    return param_1 + 25
  
# Funtion 2 serves takes parameter: param_2 which is the return value of Function 1 and it should be an integer

def function_2(param_2: int):
    print(param_2)

function_2(function_1(20))
