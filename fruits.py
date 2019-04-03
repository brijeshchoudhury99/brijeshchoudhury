fruits = ["banana","apple","cherry"]
print(fruits)
for x in fruits:
    print(x)
if "mango" in fruits:
    print("yes apple is in the list")
else:
    print("no it is not in the list")
    print(len(fruits))
fruits.append("orange")
print(fruits)
fruits.insert(1, "orange")
print(fruits)
fruits.remove("banana")
print(fruits)

