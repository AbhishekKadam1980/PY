#OBJECT ORIENTED PROGRAMMING
#ANY FUNCTION WHICH IS A PART OF A CLASS IS CALLED A METHOD


#CREATING A SIMPLE CLASS

# PYTHON RUNS THE __INIT__ METHOD FIRST WHENEVER A NEW INSTANCE OF THE DOG CLASS IS MADE
# THE __ MAKES SURE THAT PYTHON DOES NOT MIX UP USER DEFINED AND SYSTEM DEFINED METHODS
# EVERY METHOD CALL ASSOCIATED WITH A CLASS AUTOMATICALLY PASSES THE SELF ARGUMENT
#SELF GIVES THE

class Dog():
    #EVERY METHOD CALL ASSOCIATED WITH A CLASS AUTOMATICALLY PASSES SELF WHICH IS A REFERENCE TO THE INSTANCE ITSELF
    #SELF GIVES THE INDIVIDUAL INSTANCE ACCESS TO THE ATTRIBUTES AND METHODS IN THAT CLASS
    #IT IS THE __INIT__ METHOD IN PARTICULAR WHICH WILL CREATE AN INSTANCE
    def __init__(self, name, age):
    #ANY VARIABLE PREFIXED WITH SELF IS AVAILABLE TO EVERY METHOD IN THE CLASS
        self.name = name
        self.age = age
    def sit(self):
        print(self.name.title()+" is now sitting")
    def roll(self):
        print(self.name.title()+" has just rolled over")


#MAKING AN INSTANCE FROM A CLASS
my_dog = Dog('willie',6)
print("My dogs name is "+ my_dog.name.title()+".")
print("My dog is "+ str(my_dog.age) +" years old.")

#ACCESSING ATTRIBUTES
my_dog.name

#CALLING METHODS
my_dog.sit()
my_dog.roll()

#WE CAN CREATE AS MANY INSTANCES OF A CLASS AS WE WANT
#IT DOES NOT MATTER IF WE GIVE THE SAME DATA IN THE CLASS PARAMETERS, ALL WE NEED TO DO IS GIVE THE
# INSTANCE A UNIQUE VARIABLE NAME

#EXCERCISE 1

class Restaurant():
    def __init__(self,name,cusine):
        self.name = name
        self.cusine = cusine

    def describe_restaurant(self):
        print("Welcome to "+self.name.title())
        print("We serve delicious "+self.cusine.title()+" cusine")

    def open_restaurant(self):
        print("WE ARE NOW OPEN")

restaurant = Restaurant('Casalobo','goan')
restaurant.describe_restaurant()
restaurant.open_restaurant()







