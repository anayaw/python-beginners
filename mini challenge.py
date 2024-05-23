###1
##for num in range(1,101):
##    if num %3 == 0 and num %5 == 0:
##        print("fizzbuzz")
##    elif num %3==0:
##        print("fizz")
##    elif num %5==0:
##        print("buzz")
##    else:
##        print(num)
##(❁´◡`❁)
###2
##stars = 0
##for k in range(10):
##    for i in range(8):
##        print(" "*i*i,end='*\n')
##    for j in range(8, 0, -1):
##        print(" "*j*j,end="*\n")
    
#3
monei = float(input("WRITE MONEY:"))
print(monei)
toonie = 0
while monei >= 2:
    monei-=2
    toonie+=1
    
loonie = 0
while monei >= 1:
    monei-=1
    loonie+=1
    
quarter = 0
while monei >= 0.25:
    monei-=0.25
    quarter+=1

dime = 0
while monei >= 0.10:
    monei-=0.10
    dime+=1

nickel = 0
while monei >= 0.5:
    monei-=0.05
    nickel+=1

print(toonie,"toonie",  loonie,"loonie", quarter, "quarter", dime,  "dime",  nickel, "nickel")


