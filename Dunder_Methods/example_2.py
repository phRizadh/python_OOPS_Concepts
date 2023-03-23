# Class Declaration
class Individual:
    
    # Dunder or Magic Method for object initiation
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    # this method is used to print the object variables' values     
    def __repr__(self):
        return self.name
    
    # used to add/concatenate with respective object variable, depending on the datatype. Here we concatenate with lastname
    def __add__(self, lastname):
        return self.name + lastname
      
if __name__ == '__main__':
    # Creating the object instance to trigger __init__ method
    ind1 = Individual("Person1", 29, 'm')
    
     # Prints the value of variable 'name' concatenated with 'lastname' for the instance 'ind1' 
    print(ind1 + ' lastname1')
