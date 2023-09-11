class Nothing(object):
    def __init__(self, x):
        self.x = x

#Class blueprint for more instances of this class object
class Coordinate(object):
    
    #Calling this function only when you create an instance of this class object from this blueprint 
    ##self refers to the new instance... sort of a placeholder
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #Defining a method to get distance by Euclides formula
    def distance(self, other):
        x_diff_sq = (self.x - other.x) ** 2
        y_diff_sq = (self.y - other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
    
    #Defining a method that changes print behaviour for any instance of Coordinate blueprint
    def __str__(self):
        return "<" + str(self.x) + ", " + str(self.y) + ">"
    


#Creating two objects from Coordinate blueprint
##Data attributes from an instance are called instance variables
c = Coordinate(3, 4)
zero = Coordinate(0, 0)

#Using c's distance method to calculate distance from zero
##Both ways are equal
print(c.distance(zero))
print(Coordinate.distance(c, zero))

#Checking if __str__ method works
print(c)

#isinstance() works to check if foo instance comes from bar blueprint
print(isinstance(c, Nothing))


if __name__ == "__main__":
    print("HELLO")