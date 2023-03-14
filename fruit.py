import random
fruits = ("Orange", "Apple", "Pear")
looping = True


def print_fruit(userinput):    
        frn = int(userinput)
        print("\n" - fruits[frn-1] + "coming right up! \n")

while looping:

    print("------------------")
    print("\n FruitMachine \n")

    i=1

    for fruit in fruits:
        print(str(1)+": "+fruit)

    fruits = input("Pick the fruit you want: ")
    print_fruit(fruits)


    go = input("Do you want to chose another fruit? y/n ")
    print("\n")

    if (go == "n"):
        break

print("--------------------")
print("You get one more fruit ")
randomFruit = random.randint(1,3)
print_fruit(randomFruit)    
    