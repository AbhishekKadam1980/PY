#types of crust
#normal, Pan fried, cheese crust, thin crust
#types of toppings
#olives, avocado, mushrooms, chiken tikka, cheese, veggies, paneer tikka, golden delight

pizza_types={'crust':{'Normal-Crust','Pan-Fried','Cheese-Crust','Thin-Crust',},'Toppings':{'olives','avocado','mushrooms','chicken-tikka','extra-cheese','extra-veggies','paneer-tikka','Golden-Delight',}}
print ("WELCOME TO PIZZA HUT")
message = ("\t"+"How can we excite you today??")
print(message.title())
print("\nSELECT THE TYPE OF CRUST"+"\n1. Normal-Crust"+"\n2. Pan-Fried"+"\n3. Cheese-Crust"+"\n4. Thin-Crust")
base_selection = input("PLEASE ENTER YOUR CHOICE: ")

#for crust in pizza_types:
#if selection in pizza_types['crust']:
#    print("\nOK!!,"+ selection +"Pizza base")
#else:
#    print("Please select a crust from the list")
None == '0'
#empty == '" "'
#while base_selection is not None:

 if base_selection == '1':
    print("\nOK!! "+"Normal-Crust base selected")
 elif base_selection == '2':
    print("\nOK!! "+"Pan-Fried base selected")
 elif base_selection == '3':
    print("\nOK!! "+"Cheese-Crust base selected")
 elif base_selection == '4':
    print("\nOK!! "+"Thin-Crust")
 else:
    print("\n"+"Please select a base from the above list")

 print("Pizza base selected,Lets get the toppings sorted!! ")
 print("\nSELECT THE TYPE OF TOPPINGS"+"\n1. olives"+"\n2. avocado"+"\n3. mushrooms"+"\n4. chiken tikka"+"\n5. cheese"+"\n6. veggies"+"\n7. paneer tikka"+"\n8. golden delight")
 pizza_toppings={'olives','avocado','mushrooms','chiken tikka','cheese','veggies','panner tikka','golden delight'}
topping_selection = input("\n"+"PLEASE ENTER THE TOPPINGS OF YOUR CHOICE: ")
#for topping_selection in pizza_toppings:
if topping_selection == '1':
        print("\n"+"olives")
elif topping_selection == '2':
        print("\n"+"avocado")
elif topping_selection == '3':
        print("\n"+"mushrooms")
elif topping_selection == '4':
        print("\n"+"chiken tikka")
elif topping_selection == '5':
        print("\n"+"cheese")
elif topping_selection == '6':
        print("\n"+"veggies")
elif topping_selection == '7':
        print("\n"+"paneer tikka")
elif topping_selection == '8':
        print("\n"+"golden delight")
else:
    multiple_toppings = input("Do you want to select multiple toppings?(Y/N)")
    if multiple_toppings == 'Y':
        print("SELECT THE TYPE OF TOPPINGS: ")








