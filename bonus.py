word="hello"
lives=7
while lives>=0:
    guess=input("what do you think the word is?:")
    if guess == word:
        print("yupeeppepepepepepe")
        break
    elif guess in word:
        print("right letter!")
        print(lives)
    else:
        print("keep going")
        lives-=1
        print(lives)
    
