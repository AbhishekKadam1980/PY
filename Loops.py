#The for loop
#note:- syntax of the python for loop contains a colon at the end of the for loop statement
#the space preceding the print statement after the for loop is necessary and the statement does not execute if the space is not given,This is called indentation
magicians = ['david','carolina','angela']
for magician in magicians:
 print(magician.title()+" "+"That was a great trick")
 print("I can't wait to see your next trick"+ "\t"+magician.upper() +"\n")
#the below line will not be included in the for loop because it is not indented
print("Thank you"+"\t"+magicians[0]+"\t"+magicians[1]+"\t"+magicians[2]+"\t"+"for the best magic show ever")

#making numerical lists
#using the range function, However note that the range function will not print the last value specified by you in the range function parameters
for value in range(1,5):
    print(value)

#using range to make a list of numbers
#the result is a list of numbers which you will specify in the range fuction
numbers = list(range(1,5))
print(numbers)

#making a list of even numbers using the list(range()) function
#in the range function we specify the start value/end value and the amount that has to be incremented to the start value
even_numbers = list(range(2,20,2))
print(even_numbers)

#making a list of odd numbers using the list(range()) function
 odd_numbers = list(range(1,20,2))
 print(odd_numbers)

#creating a list of squares
squares =[]
for values in range(1,11):
    squares.append(values**2)
print(squares)

#basic statistics with numbers
digits = [1,2,3,4,5,6,7,8]
sum = sum(digits)
min = min(digits)
max = max(digits)
print(sum)
print(min)
print(max)

#list comprehension
#combines the for loop and creation of new elements in one line and automatically appends each new element to the list
squares = [values**2 for values in range(1,11)]
print(squares)

#list comprehension for cubes of the first 10 numbers
cubic = [cube ** 3 for cube in range(1, 10)]
print(cubic)

#odd_numbers = list(range(1,20,2))
#print(odd_numbers)
#we use the for loop directly for printing individual numbers
for odd_numbers in list(range(1,20,2)):
    print(odd_numbers)
print("This is a list of odd numbers between 1 and 20")

#slicing a list
#we can select the number of elements to be printed from the list using the index number of that particular element
#do remember that python stops one short of the element that we specify last in the index positions
players = ['charles','martina','michael','eli']
print(players[0:2])
#even if we dont specify the stating index position it is automatically taken as 0
print(players[:4])
#looping through a slice
print("the first three players on my team are:")
for player in players[:3]:
    print(player)

#copying a list using a slice
first_team = players[:]
print(first_team)


#tuples
#a tuple is a list of items which cannot change
#a value which cannot change is reffered to as immutable in python, An immutable list is called as a tuple
dimensions =(20,50)
print(dimensions[0])
print(dimensions[1])
#listing all the values in a tuple
for dimension in dimensions:
    print(dimension)
#we can however overwrite values in a tuple, but cant append a tuple




