
# import sqrt function to use for the distance formula
from math import sqrt

# global Constants to restrict the maximum x and y values that a person object
# can have.
MAX_X = 1000
MAX_Y = 800

class Item:
    # initialize the class
    # class, x, and y are all given default values if a value is not given
    def __init__(self, name = "player 1", x = 0, y =0):
        self.name = name
        self.x = x
        self.y = y
        self.size = 1
        
    # Use the string magic function to print out a specific lay out when an object is called
    def __str__(self):
        return (f"Person({self.name}):\tsize = {self.size},\tx = {self.x}\ty = {self.y}")

    # Changes the value of the x and y coordinate plane to allow for the a perosn to move with
    # a default value of one or a given value
    def goLeft(self,value=1):
        self.x -= value
    def goRight(self,value=1):
        self.x += value
    def goUp(self,value=1):
        self.y -= value
    def goDown(self,value=1):
        self.y += value
        
    # gets the distance of objects using the euclidean distance formula
    def getDistance(self, other):
        total = float(sqrt((self.y - other.y)**2 + (self.x - other.x)**2))
        return total
    
    # Getter and setter utilizing the decorators to make things easier
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,value):
        # checks if the length of the name is at least two
        if(len(value) >= 2):
            self._name = value
        else:
            # renames to "player 1" if needs aren't met
            self._name = "player 1"
            
    # Getter and setter utilizing the decorators to make things easier
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self,value):
        # simple range check to make sure entered
        # values are between the max x and 0 inlcusive
        if(value > MAX_X):
            # if exceeding, x is set to the max
            self._x = MAX_X
        elif(value < 0):
            # if less than 0, x is set to 0
            self._x = 0
        else:
            self._x = value
            
    # Getter and setter utilizing the decorators to make things easier
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self,value):
        # simple range check to make sure entered
        # values are between the max y and 0 inlcusive
        if(value > MAX_Y):
            #if exceeding, y is set to the max
            self._y = MAX_Y
            
        elif(value < 0):
            #if less than 0, y set to 0
            self._y = 0
            
        else:
            self._y = value
            
    # Getter and setter utilizing the decorators to make things easier
    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self,value):
        # checks that the size value given is greater than 1 inclusive
        if(value >= 1):
            self._size = value
            
        else:
            #keeps the value as 1 and the value is not changed
            pass
    