#1
for i in range(1,12):
    print("---------------------------------------------------------------------------------------------\n|",end=' ')
    for j in range(1,11):
        print(i*j, end="|\t")
    print()
print("---------------------------------------------------------------------------------------------")
#2
star=1
while True:
    wa=input("would u like to start drawing a triangle??? ")
    if wa == 'y':
        star+=1
        for i in range(1,star):
            print("*"*i,end="\n")
    else:
        print("bye:))")
        break
        
