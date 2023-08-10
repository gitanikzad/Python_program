import random
name=input("Enter you name?")
# list=["Ana", "Sara", 'Gita', "Arash"]
list=[]
list=name.split(",")
# print(list)
x=random.randint(0,(len(list)-1))

#print(list)
print(f"{list[x]} should pay for lunch")
