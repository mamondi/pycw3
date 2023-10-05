diagram1 = int(input("diagram1: "))
diagram2 = int(input("diagram2: "))
diagram3 = int(input("diagram3: "))
target = int(input("target: "))
size = 16

act1 = size - int((size * ((diagram1/target)*100))/100)
act2 = size - int((size * ((diagram2/target)*100))/100)
act3 = size - int((size * ((diagram3/target)*100))/100)
for i in range(0, size):
    for j in range(0, size):
        if 3 <= j <= 5 and i != size-1:
            if i >= act1:
                print("*", end="")
            else:
                print(" ", end="")
        if 8 <= j <= 10 and i != size-1:
            if i >= act2:
                print("*", end="")
            else:
                print(" ", end="")
        if 13 <= j <= 16 and i != size-1:
            if i >= act3:
                print("*", end="")
            else:
                print(" ", end="")
        if j == 0:
            print("|", end="")
        elif 1 == size-1:
            print("==", end="")
        else:
            print(" ", end="")
    print()
