# We utilize the __add__ to approach a vector addition scenario

# Class Declaration
class Vectortype:
    
    # Dunder or Magic Method for object initiation
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    # addition of numeric values like a vector
    def __add__(self, vect):
        # Here we add the respective vectors' components
        return Vectortype(self.a + vect.a, self.b + vect.b)
    
    # this method is used to print the resultant object variable values in vector representation
    def __repr__(self):
        return f"a-> {self.a}, b-> {self.b}"

if __name__ == '__main__':
     # Creating the object instance 'vector1' to trigger __init__ method
     vector1 = Vectortype(50, 30)
    # Creating the object instance 'vector2' to trigger __init__ method
     vector2 = Vectortype(60, 50)
     # resultant vector after addition
     vector_result = vector1 + vector2
     # Print the resultant vector after addition
     print(vector_result)
