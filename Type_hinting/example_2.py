# The type of agrument and its elements are stored as alias in 'List_Elements'

List_Elements = list[int]

# Passing 2 parameters, one is a scaling factor for the list elements
# other parameter is the list. The output expected is also a list

def function_scaling(param: int, list_elements: List_Elements) -> list:
    # looping through each list elements to scale it up by a factor: param    
    return [param*i for i in list_elements]

new_list = function_scaling(2, [4, 5, 6])

print(new_list)
