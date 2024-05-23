#STUDENT VERSION

# Here are all your hangman drawings
hangman0 = '''
  +---+
  |   |
      |
      |
      |
      |
========='''

hangman1 = '''
  +---+
  |   |
  O   |
      |
      |
      |
========='''
hangman2 = '''
  +---+
  |   |
  O   |
  |   |
      |
      |
========='''
hangman3 = '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
========='''
hangman4 = '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
========='''
hangman5 = '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
========='''
hangman6 = '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='''

# S1 - ask for user's name and word to guess
player1 = input("what's your name,player 1: ")
player2 = input("what's your name, player 2: ")
full_answer = input("player 1 what is the word?: ")
# S2 - initialize important variables
wrongl = ""
correctl = ""
lives = 6 
while lives > 0: # S7
    # S3
    for char in full_answer:
        if char in correctl:
            print(char, end=" ")
        else:
            print("_",end=" ")
    print()
    
    #S4
    if lives == 6: 
        print(hangman0)
    elif lives == 5:
         print(hangman1)
    elif lives == 4:
        print(hangman2)
    elif lives == 3:
        print(hangman3)
    elif lives == 2:
        print(hangman4)
    elif lives == 1:
        print(hangman5)
    elif lives == 0:
        print(hangman6)
    
    # S5
    guessl=input("guess a letter or word: ")
   #S6
    if guessl in full_answer:
        if guessl == full_answer:
            print("you did it! ")
            correctl += guessl
            print("and you had a remaning of", lives, "lives :)")
            break
        else:
            if guessl in correctl:
                print("you already GUESSED IT >:(")
                print("ALSOO, it was a correct letter sooo..")
                print("you only have",lives, 'LIVES :0')
            else:
                print("correct letter!")
                print("you only have",lives, 'LIVES :0')
                correctl += guessl
    else:
        if guessl in wrongl:
            print("you already GUESSED IT >:(")
            print("COME ON! u guessed it alr!")
            print("you only have",lives, 'LIVES :0')
        else:
            print("keep trying, WRONG GUESS")
            wrongl += guessl
            lives -= 1
            print("you only have",lives, 'LIVES :0')

  # S9, S10 and S11   
if lives == 0:
    print("its ok", player1, "try again!")
else:
    print( "you won!", player1)



