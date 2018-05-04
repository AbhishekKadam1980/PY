
#a list is a collection of items in a particular order
bicycles=['mongoose','atlas','hero','Being human','mozilla','schwinn']
print (bicycles)

#accessing individual items in a list
#in any list the index position starts at 0 and not 1
#by asking for the -1 position allways the last element in the list is returned, likewise -2 shows secondlast element and -3 shows thirdlast element

print(bicycles[-1])
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print(bicycles[4])

#we can call individual elements from a list by specifying the index position
print("bicycle"+" "+ bicycles[0].title())


#changing adding and removing elements from a list
bicycles[2] = "Ranger swing"
print(bicycles[2])

#appending elements to a list
bicycles.append('Shewtacycles')
print(bicycles)

#append method makes it easy to build lists dynamically, we can name a list first and then we can go on adding elements in the list as we like
#appending a list can also include incrementing or decrementing numeric values
motorcycles = [ ]
motorcycles.append('KTM')
motorcycles.append('Yamaha')
motorcycles.append('hero')
print(motorcycles)

#inserting elements into a list, We allways need to keep in mind that a list index starts from 0 and not 1
#we can specify the position at which we want to insert the new element
motorcycles.insert(0,'ducati')
print(motorcycles)

#removing elements from a list
del motorcycles[0]
print(motorcycles)

#using the pop() method, to pop the last element in the list,can be used to find the last item we bought in the grocery list
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

#popping items from a selected position from the list
#once we pop an element from the list it will no longer reflect in the list at the next print
first_owned = motorcycles.pop()
print (first_owned)
print(motorcycles)


#IF WE WANT TO PERMANENTLY REMOVE AN ITEM FROM THE LIST AND NEVER USE IT AGAIN WE USE THE DEL METHOD
#IF WE MAY WANT TO USE THE ELEMENT WE REMOVE AGAIN WE USE THE POP METHOD

#removing an item by value
print(motorcycles)
motorcycles.remove('KTM')

#now the list shows as an empty list
print(motorcycles)

#organize lists according to preference
#sorting a list permanently with the sort() method, The sort() method will permanently sort list entries alphabetically
#to calculate the length we need to first assign a variable to store the value of length in
cars = ['bmw','audi','mercedes','porsche','jaguar']
length = len(cars)
print(length)
cars.sort()
print(cars)

#to sort in reverse order we user sort(reverse=True)
cars.sort(reverse=True)
print(cars)

#sorting a list temporarily with a sorted() function
#Note the syntax of the sorted function as it does pose a problem usually
#sorted sorts the given data alphabetically
print(cars)
print(sorted(cars))

#using sorted reverse, Make a note of the syntax
print(sorted(cars,reverse=True))

#printing a list in reverse order, simply reverses the whole list
cars.reverse()
print(cars)

#finding the length of the list
len(cars)



