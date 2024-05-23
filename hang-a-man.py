word= "hello"
life = 7
while life>=0:
    guess = input("enter a word/letter:")
    if guess == word:
        print("yaey")
        break
    else: 
        if guess in word:
            print("lifes:", life)
            print("yipeeeee")
        else:
            life -= 1
            print("lifes:", life)
            print("keep going :))) :DDDDDDDD :<<<< :PPP :>>> ")
