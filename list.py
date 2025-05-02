camping_stuff  =  "tent, sleeping bag, water, raspberry pi, coffee, knife, ethernet cable, flash drive, beard oil,marshmallows"

camping_list = ["tent", "sleeping bag", "water", "raspberry pi",
                  "coffee", "knife", "ethernet cable", "flash drive",
                  "beard oil", "marshmallows"]
print(type(camping_list))

me = camping_list[4]
print(me)

camp_site = ["crystal lake", "mountain view", 10, False]

you= camping_list[-1]
print(you)

camping_list.extend([".","!"]) 
camping_list = camping_list + []

camping_list.insert(0, "sunscreen")
camping_list.insert(-3, "toilet paper")
camping_list.remove("!")
print(camping_list.pop(0))
camping_list[1] = "chunk"
print(camping_list)

atuple = ("tent", "sleeping bag", "water", "raspberry pi")
atuple[0] = "berry"
print(atuple)