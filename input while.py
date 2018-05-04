#we use the input() fuction to accept user input
#we can use the while loop to keep programs running as long as a certain condition remains true
message = input("\ninput:" )
message += "\nthanks"
#building a multi line string prompt
#the += operator appends the  string at the end of the line after the input
print("This is what Python understood:-->"+"\t\n"+message.title())
name = input("Enter your name please:")
print("Hello "+name.title())
#using int() to accept numerical input
age = input("How old are you?:")
age = int(age)
print("Whoa ur"+" "+ str(age)+"?" )
print("thats real cool" )
#introducing while loops,The loop will continue as long as a certain condtion remains true
current_number = 1
while current_number <=5:
    print(current_number)
current_number = current_number + 1
    current_number += 1

#using a while loop example with
#using a flag with a break
#a flag acts as a signal to a program which tells it to either carry on or stop
#a break is used to control which lines are executed and which lines are not, A break statement can be used in any of pythons loops
#while True:
    city =input("Type the name of city here:")
     if city == 'quit':
         break
     else:
        print("id love to visit "+city.title())
#using continue in a loop
  current_number = 0
 while current_number<10:
         current_number += 1
         if current_number % 2 == 0:
         continue
    print(current_number)
#moving items from one list to another
unconfirmed_users =['abhishek','sumit','prashant','mayur']
confirmed_users = [ ]
while unconfirmed_users :
    current_user = unconfirmed_users.pop()
   print("Verifying user "+current_user.title())
    confirmed_users.append(current_user)
print(confirmed_users)
#removing specific items from a list
pets =['dogs','cats','snakes','birds']
print (pets)
while 'cats' in pets:
    pets.remove('cats')
print(pets)
#filling a dictionary with user input
responses = {}
polling_active = True
while polling_active:
    name = input("Name:")
    response = input("Political affiliation:")
    responses[name] = response
    repeat = input("Would you like to keep the poll live?(yes/no)")
    if repeat == 'no':
        polling_active = False
print(responses)






