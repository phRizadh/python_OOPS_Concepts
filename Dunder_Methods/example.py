# CLass Declaration
class Individual:
    
    # Dunder or Magic Method for object initiation
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

if __name__ == '__main__':
    # Creating the object instance to trigger __init__ method
    ind1 = Individual("Person1", 29, 'm')
    
    # Prints the object's memory address
    print(ind1)
    
    # Prints the object instance attribute/variable 'name'
    print(ind1.name)
