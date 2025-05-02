Menu = ("soda", "water", "juice", "milk", "coffee", "tea")
price = 9
name= input("please enter your name")

if name == "Ben" or name== "Silvia" or name == "Loki":    
    evil_status = input("are you evil? (yes/no)")
    good_deeds = int(input("how many good deeds have you done today?"))
    if evil_status.lower() == "yes" and good_deeds < 4:
       print("evil " + name + " you are not welcome here, please leave")
       exit()
    else:
        print("ooh, so you are one of the good Bens, welcome to our hotel")   
else:
    print("hello " + name + " welcome to our hotel")
print("we have the following drinks available " + str(Menu) + "\n" )
drink = input("what can we offer you?")
if drink == "soda":
    price = 5
elif drink == "water":
    price = 2
elif drink == "juice":
    price = 3
elif drink == "milk":
    price = 4
elif drink == "coffee":
    price = 6
elif drink == "tea":
    price = 3
else:
    print("sorry we don't have that drink available")
    exit()              

num = int(input("how many drinks do you want?"))
totalprice = price * num
print(drink + "\n" + str(num) + "\n" + str(totalprice))
print(name + " thank you for you order. You total is: $"   + str(totalprice))

print("Hello " + name + ", your " + str(num) + " drink(s) will be ready in a few minutes")