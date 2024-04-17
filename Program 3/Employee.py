#####################################################################
# author: Zachary Truxillo      
# date: 4/16/2024        
# description:  Creates a simple employee parent class which shows off the use 
# of inheritance and child classes. Also uses an abstract method to show off use of that concept.
#####################################################################

# import the abc library to make abstract classes
from abc import ABC, abstractmethod

######################################################################
# An employee class. Its constructor takes the first name, last name and
# pay. It also has email and position as instance variables. It contains
# a single abstract method i.e. applyRaise, and a createEmail function
# that creates an appropriate email address from the employee's first
# and last names.
######################################################################
class Employee(ABC):
    def __init__(self,firstname,lastname,pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay
        # calls function which follows a set path of making a default email
        self.email = self.createEmail()
        self.position = None
    
    @property
    def firstname(self):
        return self._firstname
    @firstname.setter
    def firstname(self,value):
        # account for errors users might make in creating name
        value = value.strip()
        value = value.capitalize()
        # corrects the rest of the name to follow a format, 
        # also confirming the number of characters in name
        if(len(value) > 1):
            value = value[0] + value[1:].lower()

        self._firstname = value
    
    @property
    def lastname(self):
        return self._lastname
    @lastname.setter
    def lastname(self,value):
        #account for errors users might make in creating name
        value = value.strip()
        value = value.capitalize()
        # corrects the rest of the name to follow a format, 
        # also confirming the number of characters in name
        if(len(value)>1):
            value = value[0] + value[1:].lower()

        self._lastname = value
    
    
    @property
    def pay(self):
        return self._pay
    @pay.setter
    def pay(self,value):
        # account for users who put a pay below 20000
        if(value>=20000):
            self._pay = value
        else:
            self._pay = 20000
            
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,string):
        # confirm the email is correct
        if ("@latech.edu" in string):
            self._email = string
        # correct the error otherwise
        else:
            self._email = self.createEmail()
            
    @property
    def position(self):
        return self._position
    @position.setter
    def position(self,string):
        self._position = string     
            
    # follow format of how email is supposed to look        
    def createEmail(self):
        return (f"{self.firstname.lower()}.{self.lastname.lower()}@latech.edu")
    
    # uses abstract method to stop users from giving employee 
    # a raise and not specific type of employee
    @abstractmethod
    def applyRaise(self,rate):
        raise NotImplementedError
        '''Can not give an Employee a raise'''
        
    
    def __str__(self):
        s = f"{self.lastname}, {self.firstname} ({self.email})"     
        return s   
        
        


######################################################################
# A faculty class is a subclass of the Employee class above. Its
# constructor receives both names as well as the position. The Faculty
# class also overrides the applyRaise function by multiplying the pay by
# the rate provided as an argument. It also slightly tweaks the __str__
# function in the super class.
######################################################################
class Faculty(Employee):
    def __init__(self,firstname,lastname,position):
        super().__init__(firstname,lastname,pay = 50000)
        self.position = position
        
    def applyRaise(self,rate):
        # account for users who put in incorrect rate
        if(rate > 0):
            self.pay *= rate
        else: 
            pass
    
    # fix string function to also show what position the faculty is in    
    def __str__(self):
        return super().__str__() + f" -- {self.position}"
        
        

######################################################################
# A Staff class is a subclass of the Employee class above. Its
# constructor only receives both names. It also overrides the applyraise
# function but adding the increase (provided as the argument) to the
# pay. It doesn't change anything else from the Employee class.
######################################################################
class Staff(Employee):
    def __init__(self,firstname,lastname):
        super().__init__(firstname,lastname,pay = 40000)
        
    def applyRaise(self,rate):
        if(rate > 0):
            self.pay += rate
        else:
            pass
        

