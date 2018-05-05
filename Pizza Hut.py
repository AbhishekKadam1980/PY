#OPENING BANNER
print ("\nWELCOME TO PIZZA HUT")
message = ("\n\t"+"How can we excite you today??")
print(message.title())

#PIZZA BASE SIZE SELECTION
base_size = ['small','medium','large']
print("\nSELECT PIZZA SIZE")
print("\n\t1. SMALL"+"\n\t2. MEDIUM","\n\t3. LARGE")
base_choice = input("\nPLEASE ENTER YOUR CHOICE: ")
if base_choice == '1':
   print("OK "+base_size[0].upper()+" BASE SELETED")
elif base_choice == '2':
   print("OK "+base_size[1].upper()+" BASE SELECTED")
elif base_choice == '3':
   print("OK "+base_size[2].upper()+" BASE SELECTED")
else:
        print("PLEASE SELECT A VALID BASE OPTION ,TRY AGAIN")
        exit( )

#BASE SELECTION USING IF-ELIF-ELSE LOOP

print("\nSELECT THE TYPE OF CRUST"+"\n\t1. Normal-Crust"+"\n\t2. Pan-Fried"+"\n\t3. Cheese-Crust"+"\n\t4. Thin-Crust")
base_selection = input("\nPLEASE ENTER YOUR CHOICE: ")
pizza_base = ['Normal-Crust','Pan-Fried','Cheese-Crust','Thin-Crust']
if base_selection == '1':
   print("\nOK!! "+pizza_base[0]+" base selected")
elif base_selection == '2':
   print("\nOK!! "+pizza_base[1]+" base selected")
elif base_selection == '3':
   print("\nOK!! "+pizza_base[2]+" base selected")
elif base_selection == '4':
   print("\nOK!! "+pizza_base[3]+" base selected")
else:
   print("\n"+"Please select a base from the above list")
   print("Sorry,try again.")
   exit()

#TOPPING SELECTION USING WHILE LOOP

print("\nSELECT THE TYPE OF TOPPINGS"+"\n\t1. olives"+"\n\t2. avocado"+"\n\t3. mushrooms")
pizza_toppings=['olives','avocado','mushrooms']
pizza_topping_1 = input("\nPlease select a topping: ")
count = 0
list = [ ]
if pizza_topping_1 == '1':
   print("ok "+pizza_toppings[0]+" selected")
   list.append(pizza_toppings[0])
elif pizza_topping_1 == '2':
     print("ok " + pizza_toppings[1] + " selected")
     list.append(pizza_toppings[1])
elif pizza_topping_1 == '3':
     print("ok " + pizza_toppings[2] + " selected")
     list.append(pizza_toppings[2])
choice = input("\nSelect an additional pizza topping ?(Y/N) : ")
if choice == 'Y':
   pizza_topping_2 = input("\nselect another topping from the list: ")
   count = count + 1
   if pizza_topping_2 == '1':
       print("ok " + pizza_toppings[0] + " selected")
       list.append(pizza_toppings[0])
   elif pizza_topping_2 == '2':
       print("ok " + pizza_toppings[1] + " selected")
       list.append(pizza_toppings[1])
   elif pizza_topping_2 == '3':
       print("ok " + pizza_toppings[2] + " selected")
       list.append(pizza_toppings[2])
   print("\n\nOK "+list[0]+" and "+list[1]+" topping")
   print("\nwe can only load so much goodness on one base!!")
   print("\nDELICIOUS PIZZA ON THE WAY")
else :
    print("OK DELICIOUS PIZZA ON THE WAY")






