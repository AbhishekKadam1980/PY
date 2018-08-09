#A function is a named block of code which is designed to perform a particular task

#DEFINING A FUNCTION
def greet_user():
    """print a simple greeting to the user, This is called a docstring"""
    print("Hello!!")
#CALLING A FUNCTION
greet_user()


#PASSING INFORMATION TO A FUNCTION
def greet_user(username):
    print("Hello "+ username.title()+ "!!")
greet_user('abhishek')

#ARGUMENTS AND PARAMETERS
#in the previous example "username" is a parameter and "abhishek" is a argument


#EXCERCISE 1
def display_message():
    print("Currently we are learning about functions")
display_message()

#EXCERCISE 2
def favourite_book(title):
    print("One of my favourite books is "+ title.title()+" !! ")
favourite_book('kite runner')

#PASSING ARGUMENTS
#POSITIONAL ARGUMENTS WHICH NEED TO BE IN THE SAME ORDER
#KEYWORD ARGUMENTS WHICH DO NOT NEED TO BE SPECIFIED IN A PARTICULAR ORDER


#EXAMPLE OF POSITIONAL ARGUMENTS
def describe_animal(animal_type,pet_name):
    print("I have a "+ animal_type +" named "+pet_name)
describe_animal('dog','foxy')

#A FUNCTION CAN BE CALLED MULTIPLE TIMES WITH DIFFERENT ARGUMENTS
#A KEYWORD ARGUMENT IS ALWAYS A NAME VALUE PAIR

#EXAMPLE OF KEYWORD ARGUMENTS
describe_animal(animal_type='cat',pet_name='Guddu')

#DEFAULT VALUES
#NOTE THAT THE DEFAULT VALUE HAS TO BE SPECIFIED LAST TO AVOID POSITIONAL ARGUMENT ERRORS
#IF WE PROVIDE A EXPLICIT VALUE THEN PYTHON WILL OVERWRITE THE DEFAULT VALUE

def describe_vehicle(brand,number_of_wheels,category='car'):
    print(brand+" "+ number_of_wheels+" " + category )
describe_vehicle(brand='buick',number_of_wheels='4')
describe_vehicle('chevrolet','4')

#EXCERCISE 3
def make_shirt(message,size = 'Large'):
    print("size "+size+ " Tshirt with "+ message +" printed on it ")
#keyword argument call
make_shirt(size='XL',message='" MAGIC IS AN ABOMINATION "')
#positional argument call
make_shirt('xl','wp gaben')

#EXCERCISE 4
def describe_country(city,country):
    print(city.title()+" is in "+ country.title())
describe_country('panjim','goa')


#RETURN VALUES
#THE RETURN STATEMENT TAKES A VALUE FROM INSIDE THE FUNCTION AND RETURNS IT BACK TO THE LINE THAT CALLED THE FUNCTION

#RETURNING A SIMPLE VALUE
def get_formatted_name(first_name,last_name):
    """takes a first name and a last name and returns a nearly formatted name"""
    full_name = first_name + " " + last_name
    return full_name.title()
#WE NEED TO PROVIDE A VARIABLE WHERE THE RETURN VALUE CAN BE STORED
musician = get_formatted_name('jimi','hendrix')
print(musician)


#MAKING AN ARGUMENT OPTIONAL
#MAKE SURE TO SPECIFY DEFAULT OR OPTIONAL ARGUMENT VALUES IN THE END OF THE FUNCTION TO AVOID POSITIONAL ARGUMENT ERRORS
def get_optional_middle_name(first_name,last_name,middle_name=''):
    if middle_name:
     full_name = first_name.title()+" "+ middle_name.title()+" "+ last_name.title()
    else:
     full_name = first_name.title()+" " + last_name.title()
    return full_name
actor = get_optional_middle_name('Ranbir','kapoor')
director = get_optional_middle_name('sanjay','Bhansali','leela')
print(actor)
print(director)


#RETURNING A DICTIONARY
#def build_person(first_name,last_name,age=''):
 #   person = {"first":first_name,"last":last_name}
  #  if age:
   #     person[age] = age
   # return person
#citizen_1 = build_person('Abhishek','Kadam')
#print(citizen_1)
#citizen_2 = build_person('Shubham','Kadam','23')
#print(citizen_2)

#USING A FUNCTION WITH A WHILE LOOP
#def get_formatted_credentials(f_name,l_name):
   # full_name = f_name+" "+ l_name
   # return full_name.title( )
#while True:
   # print("\nPlease tell me your name")
   # print("\nType q to quit at any time ")
   # f_name = input("First_name: ")
   # if f_name == 'q':
    #    break
    #l_name = input("Last_name: ")
    #if l_name == 'q':
      #  break
    #format_name = get_formatted_credentials(f_name,l_name)
    #print("Hello "+format_name)

#EXCERCISE 5
#while True:
 #     print("\nPlease fill out the following details\nEnter q to exit at any time")
  #    artist_name = input("\n Please enter the name of the artist : ")
   #   if artist_name == 'q' or 'Q':
    #      break
     # else
      #    continue
      #album_title = input("\n Please enter the name of the album : ")
      #if album_title == 'q' or 'Q':
       #   break
      #num_track = input("\n Please enter the number of tracks : ")
      #if num_track == 'q' or 'Q':
      #    break
      #if (artist_name or album_title or num_track) not in ('q' or 'Q'):
       #   def make_album(artist_name, album_title, num_track=''):
        #      data = {"artist": artist_name, "album": album_title, "number of tracks": num_track}
         #     return data
          #music = make_album(artist_name, album_title, num_track)
          #print(music)
      #else:
       #   #if (artist_name or album_title or num_track) in ('q' or 'Q'):
        #     print("EXIT, BYE")
         #    exit()
          #   break


#PASSING A LIST
def greet_users_list(names):
    """print a simple message to each user in the list"""
    for name in names:
        message = " Hello " + name.title()
        print(message)
usernames = ['hannah','sarah','linda']
greet_users_list(usernames)

#MODIFYING A LIST IN A FUNCTION
def print_models(unprinted_designs,completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("\nPrinting model: "+ current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    print("\n The following models have been completed")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['Iphone Case','Robot Pendant','Dog']
completed_models = [ ]

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

#PREVENTING A FUNCTION FROM MODIFYING A LIST
#INSTEAD OF SENDING THE ORIGINAL LIST WE CAN SEND A COPY OF THE LIST TO THE FUNCTION

print_models(unprinted_designs[:],completed_models)

#EXCERCISE 7
def show_magicians (magician_names):
    for name in magician_names:
        print("Hello "+ name)
magician_names = ['jim','jack','trevor']
show_magicians(magician_names)

#EXCERCISE 8
def make_great(magician_names):
    for name in magician_names:
        print("The Great "+ name)
magician_names = ['jim','jack','trevor']
make_great(magician_names)

#EXCERCISE 9
#magician_names_new = [ ]
#make_great(magician_names[:])
#for names in magician_names:
#    names.append(magician_names_new)
#print(magician_names_new)

#PASSING AN ARBITRARY NUMBER OF ARGUMENTS
#THE * PARAMETER MAKES A EMPTY TUPLE CALLED TOPPINGS
#THIS SYNTAX WORKS NO MATTER HOW MANY ARGUMENTS ARE BEING PASSED TO THE FUNCTION
def make_pizza_unlimited(*toppings):

#MIXING POSITIONAL AND ARBITARY ARGUMENTS
#THE PARAMETER WHICH ACCEPTS ARBITARY ARGUMENTS HAS TO BE PLACED LAST IN THE FUNCTION CALL LIST
#def make_pizza(size, *toppings):
    """summarize the pizza that we are about to make"""
 #   print("\nMaking a " + str(size) + " - inch pizza with the following toppings :")
  #  for topping in toppings:
   #     print("\n"+topping)

#USING ARBITARY KEYWORD ARGUMENTS
#WE CAN PASS AS MANY NAME VALUE PAIRS AS WE WANT USING **
def build_user_database(first,last,**user_info):
    """build a dictionary containing everything we know about the user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key]=value
        return profile

#THIS FUNCTION CALL ACCEPTS A NAME VALUE PAIR IN THE END AND WE CAN DEFINE N NUMBER OF NAME VALUE PAIRS
test = build_user_database('abhishek','kadam',location = 'princeton')
print(test)






























