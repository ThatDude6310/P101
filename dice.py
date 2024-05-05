import random
play = "y"

edge = "-----------------"
layout = "| {:^3}  {:^3}  {:^3} |"

while play == "y":
    roll = random.randint(1,6)

    if roll == 1:
        print(edge)
        print(layout.format("","",""))
        print(layout.format("","O",""))
        print(layout.format("","",""))
        print(edge)

    if roll == 2:
        print(edge)
        print(layout.format("","O",""))
        print(layout.format("","",""))
        print(layout.format("","O",""))
        print(edge)

    if roll == 3:
        print(edge)
        print(layout.format("","",""))
        print(layout.format("O","O","O"))
        print(layout.format("","",""))
        print(edge)

    if roll == 4:
        print(edge)
        print(layout.format("O","","O"))
        print(layout.format("","",""))
        print(layout.format("O","","O")) 
        print(edge)

    if roll == 5:
        print(edge)
        print(layout.format("O","","O"))
        print(layout.format("","O",""))
        print(layout.format("O","","O"))  
        print(edge)

    if roll == 6:
        print(edge)
        print(layout.format("O","","O"))
        print(layout.format("O","","O"))
        print(layout.format("O","","O"))  
        print(edge)
    
    play = input("Do you want to roll again (y/n)")