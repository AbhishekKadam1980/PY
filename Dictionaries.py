#a simple dictionary
#a dictionary in python is a collection of key value pairs,each key is connected to a value
#a key value pair is a set of values which conatains a key and a value bound to that key which can be retreived at any time
#python does not care about the order in which we input the key value pairs
alien_0 = {'color':'green','points':5}

#adding values to a dictionary alternately and also modifying some values
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print (alien_0)
alien_0['color'] = 'yellow'
print(alien_0['color'])

#removing key value pairs, a deleted key value pair is deleted permanently
del alien_0['points']

# a dictionary of similar objects
favourite_languages = {'jen' : 'python','sarah' : 'c','edward' : 'ruby','Abhishek': 'pY'}
print(favourite_languages['sarah']+ '" language"' +" i guess sarah knows that")

#looping through all key pair values in a dictionary
#the method items returns a list of key value pairs
user_0 = {'username':'efermi','first':'efraim','last':'fermi'}
for key, value in user_0.items():
    print("\nkey:"+ key)
    print("value: "+ value)

#using a for loop and items method to loop through an entire dictionary
favourite_languages = {'jen' : 'python','sarah' : 'c','edward' : 'ruby','Abhishek': 'pY'}
print(favourite_languages['sarah']+ '" language"' +" i guess sarah knows that")
for name, languages in favourite_languages.items():
    print(name.title()+" "+languages.title())

#looping through all the keys in the dictionary using the keys() method
for name in favourite_languages.keys():
    print(name.title())

#favourite_languages = {'jen' : 'python','sarah' : 'c','edward' : 'ruby','Abhishek': 'pY'}
#favourite_languages = {'jen' : 'python','sarah' : 'c','edward' : 'ruby','Abhishek': 'pY','piyush':'python'}
friends = ['phil','sarah']
for name in favourite_languages.items():
    print(name)
if name in friends :
  print("hi"+ name.title() +"your favourite language is" + favourite_languages[name].title())

#looping through keys in order using the sorted function
for name in sorted(favourite_languages.keys()): print(name)

#looping through all values in a dictionary using the values() method
#this method does not check for repeats
print("The following languages have been mentioned:")
for languages in favourite_languages.values():
   print(languages.title())

#to make the set of chosen items in the list to be unique use the set method,any duplicate entries will be removed
for language in set(favourite_languages.values()):
   print(language.title())

#nesting
#you can nest a set of dictionaries inside a list , and a list of items inside a dictionary  or even a dictionary inside another dicitonary
#a list of dictionaries


#we define an empty list
aliens=[]
#we use a for loop to specify a repeat task using the range method, The method tells pyhton how many times the loop will repeat
for alien_number in range(30):
    #we define an element called new alien and append it to the aliens list
    new_alien = {'color':'green','points':5,'speed':'slow'}
    aliens.append(new_alien)
    for alien in aliens[:5]:
        print(alien)
        print("......................................................................")
        print(str(len(aliens)))

    # a list in a dictionary
# notice that we have included a list in the dictionary
 pizza_specifics = {'crust':['Thick','Thin','Pan','cheese crust'],'toppings':['mushrooms','cheese','chicken-tikka'],}
 print("You can choose from the following list of crusts")
 for crusts in pizza_specifics['crust']:
     print("\t"+crusts.title())
 for topping in pizza_specifics['toppings']:
   print("\t"+topping.title())

pizza_specifics = {'crust':'thick','toppings':['mushrooms','cheese','chicken-tikka'],}
print("You ordered a "+ pizza_specifics['crust'] +" crust pizza with the following toppings")
for topping in pizza_specifics['toppings']:
   print("\t"+topping.title())


#a dictionary in a dictinoary
users = {
    'aeinstein':{'first':'albert','last':'einstein','location':'princeton',},
    'mcurie':{'first':'marie','last':'curie','location':'paris',}
}
for username, user_info in users.items():
    print("\nUsername "+ username)
    full_name = user_info['first']+" "+user_info['last']
    location = user_info['location']
    print("\nFullname:" + full_name.title())
    print("\nLocation:"+ location.title())











