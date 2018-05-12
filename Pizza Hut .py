#OPENING BANNER

print ("WELCOME")
message = ("\t"+"How can we excite you today!!")
print(message.title())

#PIZZA SIZE SELECTION

print("\n\t1. SMALL"+"\n\t2. MEDIUM"+"\n\t3. LARGE")
while True :
    pizza_size = input("\n PLEASE SELECT THE BASE SIZE : ")
    size = ['SMALL','MEDIUM','LARGE']
    pizza_size_dump = [ ]
    if pizza_size == '1':
        print("\n\tOK " + size[0] + " BASE SELECTED.")
        pizza_size_dump.append(size[0])
    elif pizza_size == '2':
        print("\n\tOK " + size[1] + " BASE SELECTED.")
        pizza_size_dump.append(size[1])
    elif pizza_size == '3':
        print("\n\tOK " + size[2] + " BASE SELECTED.")
        pizza_size_dump.append(size[2])
    else:
        print("\nPLEASE SELECT A VALID OPTION FROM THE LIST")
        continue
    break

#BASE SELECTION USING IF-ELIF-ELSE LOOP

print("\nSELECT THE TYPE OF CRUST"+"\n\t1. Normal-Crust"+"\n\t2. Pan-Fried"+"\n\t3. Cheese-Crust"+"\n\t4. Thin-Crust")
while True :
    base_selection = input("\nPLEASE ENTER YOUR CHOICE: ")
    pizza_base = ['Normal-Crust', 'Pan-Fried', 'Cheese-Crust', 'Thin-Crust']
    pizza_base_dump = []
    if base_selection == '1':
        print("\nOK!! " + pizza_base[0] + " base selected")
        pizza_base_dump.append(pizza_base[0])
    elif base_selection == '2':
        print("\nOK!! " + pizza_base[1] + " base selected")
        pizza_base_dump.append(pizza_base[1])
    elif base_selection == '3':
        print("\nOK!! " + pizza_base[2] + " base selected")
        pizza_base_dump.append(pizza_base[2])
    elif base_selection == '4':
        print("\nOK!! " + pizza_base[3] + " base selected")
        pizza_base_dump.append(pizza_base[3])
    else:
        print("\n" + "Please select a base from the above list")
        print("\ntry again.")
        continue
    break

#TOPPING SELECTION USING WHILE LOOP

print("\nSELECT THE TYPE OF TOPPINGS"+"\n\t1. olives"+"\n\t2. avocado"+"\n\t3. mushrooms")
pizza_toppings = ['olive', 'avocado', 'mushroom']
list = []
while True :
    pizza_topping_1 = input("\nPlease select a topping: ")
    if pizza_topping_1 == '1':
        print("ok " + pizza_toppings[0] + " selected")
        list.append(pizza_toppings[0])
    elif pizza_topping_1 == '2':
        print("ok " + pizza_toppings[1] + " selected")
        list.append(pizza_toppings[1])
    elif pizza_topping_1 == '3':
        print("ok " + pizza_toppings[2] + " selected")
        list.append(pizza_toppings[2])
    else:
        print("please select a valid topping option")
        continue
    break
choice = input("\nSelect an additional pizza topping ?(Y/N) : ")
choice_1 = 'Y'
choice_2 = 'y'
choice_3 = 'N'
choice_4 = 'n'
while choice not in (choice_1,choice_2,choice_3,choice_4):
    print("PLEASE SELECT Y or N"+"\n Try again")
    choice = input("\nSelect an additional pizza topping ?(Y/N) : ")
    continue
    break
else:
    while choice in (choice_1, choice_2):
        pizza_topping_2 = input("\nselect another topping from the list: ")
        if pizza_topping_2 == pizza_topping_1:
            print("\nTopping already selected, Please choose another one.")
            continue
            break
        elif pizza_topping_2 == '1':
            print("ok " + pizza_toppings[0] + " selected")
            list.append(pizza_toppings[0])
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
            print("\nDELICIOUS PIZZA ON THE WAY")
            break
        elif pizza_topping_2 == '2':
            print("ok " + pizza_toppings[1] + " selected")
            list.append(pizza_toppings[1])
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
            print("\nDELICIOUS PIZZA ON THE WAY")
            break
        elif pizza_topping_2 == '3':
            print("ok " + pizza_toppings[2] + " selected")
            list.append(pizza_toppings[2])
            print("\n" + list[0] + " and " + list[1] + " toppings")
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " and " + list[1] + " TOPPINGS")
            print("\nDELICIOUS PIZZA ON THE WAY!!")
            break
    else:
        while choice in (choice_3, choice_4):
            print("\nSELECTED ITEMS IN YOUR LIST ARE:")
            print("\n1." + pizza_size_dump[0] + " BASE")
            print("\n2." + pizza_base_dump[0]+" Pizza")
            print("\n3." + list[0] + " TOPPINGS")
            print("\nDELICIOUS PIZZA ON THE WAY!!")
            break


#CONFIRM ORDER
confirm_choice=input("\nDo you want to make any changes to your order(Y/N)??")
confirm_options_1 = 'Y'
confirm_options_2 = 'y'
confirm_options_3 = 'N'
confirm_options_4 = 'n'
while confirm_choice in (confirm_options_3,confirm_options_4) and list[1] == True:
        print("\n" + pizza_size_dump[0]+" " + pizza_base_dump[0]+" Pizza")
        print("\nORDER CONFIRMED.")
#else:
 ##          change_choice=input("\nPlease select what you would like to change: "+"\n\t1. BASE SIZE"+"\n\t2. BASE TYPE"+"\n\t3. TOPPINGS")
   #           change_option_1 = '1'
    #          change_option_2 = '2'
     #         change_option1_1 = '3'
      #        continue
       #       break





