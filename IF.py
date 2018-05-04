#Pythons if statement allows you to examine the current state of a program and respond appropriately to that state
#checking for equality(==)
#cars =['audi','bmw','subaru','toyota']
#for car in cars:
 #   if car =='bmw':
  #      print(car.upper())
   # else:
    #    print(car.title())
#different types of tests
#conditional tests : evaluate a statement and check whether it is true or false
#note the == sign to test conditionality , It is also called as the equality operator

#ignoring case sensitivity by using the lower method, This does not change the state of the original variable which is stored

#car.lower() == 'audi'

#checking for inequality(!=)
#understand that we are using the inequality sign literally here
#requested_toppings = "Mushroom"
#if requested_toppings != 'anchovies':
 #   print("I would like mushrooms on my Pizza")
#else:
 #   print("Thank you ironman")

#numerical comparisions(==,!=,>,>=,<,<=)
#answer = 42
#if answer != 42:
 #   print("well ur wrong")
#else:
 #   print("Correct answer")

#using AND to check multiple conditions
#and returns true only if both the check conditions are true
#age_0 = 22
#age_1 = 18
#age_0 >= 21 and age_1 >= 21


#using or to check multiple conditions
#or expression  returns true even if one of the check conditions is true
#age_0 = 22
#age_1 = 18
#age_0 >= 21 or age_1 >= 21


#checking whether a value is in a list using the in keyword
#requested_toppings = ['mushrooms','onions','pineapple']
#if 'mushrooms' in requested_toppings == True:


#checking whether a use is not in a list

#banned_users = ['andrew','carolina','david']
#user = ('maria')
#if user not in banned_users:
 # print(user.title()+" "+"welcome to the forum")

#boolean expressions
#a boolean value is either true or false

#core if statements
#the simplest if statement looks like if conditional_test: do something
#age = 19
#if age >=18:
 #   print("Yes you can vote")
#if else statements
#else:
 #   print("you are not eligible to vote")

#the if-elif-else loop
#used to test more than 2 possible situations
#note that this loop is efficient to test only one condition for true, The moment one test passes python just skips the rest of the tests
#age = 19
#if age  <4:
   # print("pay 4 dollars")
#note that we can use multiple elif blocks in this type of loop to test a number of conditions
#elif age < 18:
 #   print("Pay 18 dollars")
#elif age <28:
 #   print("pay 28 dollars")
#note that the else block is not compulsory
#else:
 #   print("get lost asshole")


#testing multiple conditions to be true
#if you want only one block of code to run to test true for one conditional statement then use a if-elif-else statement
#otherwise use a series of if statements
#requested_toppings=['mushrooms','extra cheese']
#if 'mushrooms' in requested_toppings:
 #   print("Adding mushrooms")
#if 'pepperoni' in requested_toppings:
#    print("Adding pepperoni")
#if 'extra cheese' in requested_toppings:
 #   print("Adding extra cheese")
#print("\n Finished making your pizza")


#using if statements with lists
#requested_toppings = ['mushrooms','pizza','extra cheese','pepperoni','bacon','prawns']
#for requested_topping in requested_toppings:
 #   if requested_topping == 'prawns':
  #      print("sorry we are out of prawns")
   # else:
    #    print(requested_topping)

#checking that a list is not empty
#requested_toppings = ['cheese']
#if requested_toppings:
 #   for requested_topping in requested_toppings:
  #      print(requested_topping.title()+" Added")
   #     print("\nFinished making your pizza")
#else:
 #   print("\tPlain pizza?")

#using multiple lists
available_toppings=['mushrooms','olives','peppers','pepperoni','pineapple','cheese']
requested_toppings=['mushrooms','frenchfries','jalapeno']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(requested_topping.title()+" Added")
        print("\tEnjoy your pizza")
    else:
        print("\nSorry the requested topping is not available")
print("Thanks")







