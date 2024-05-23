##name = input("What is your name?")
##letter = input("What is your favourite letter?")
##letter_count = 0
##vowel_count = 0
##for char in name:
##    if char == letter:
##        letter_count += 1
##    if char in "aeiouAEIOU":
##        vowel_count += 1
##print("You have", letter_count,"instances of your favourite letter", letter,"in your name!")
##print("You have", vowel_count, "vowels in your name.")
##print("The total length of your name is", len(name))

##age = 0
##while age < 100:
##    age += 1
##print(age)
##
###this print the number to add to get to yaey
##yay = int(input("what number u want start:"))
##yaey = int(input("ending number :"))
##var_counter = 0
##while yay < yaey:
##    var_counter += 1
##    yay+= 1
##print(var_counter)

###once
##num = 0
##while num != 2:
##    num += 2


##number_hippos = 1
##more_hippos = "yes"
##while more_hippos == "yes":
##    number_hippos += 1
##    print("You have", number_hippos, "hippos!")
##    more_hippos = input("Do you want another hippo?(yes):")
### how many times will this loop repeat? It depends on the user!
### it will add another hippo anytime they answer "yes"
### it will stop as soon as they answer anything other than "yes"

##name = "Rumplestiltskin"
##guess = "anaya"
##while guess != name:
##    print("I challenge you to guess my name!")
##    guess = input("Enter your guess: ")
##    if "anaya" == guess:
##        print("Wow! You got it!")
##    # stuck in this loop you guess correctly
### The only way this print is reached is if you get it right!
### if you always guess wrong, this loop could go forever

                                                                
##ada = 99
##while ada > 1000:
##    print("i in loop and so are you")
##print("anaya no no loop")
##
####adada = "hehe"
####awa = "real"
####while adada != awa:
####    print("bleep bloop")
##    
####while True:
####    print("bleepbloop FOREVER MUAHAHAHAHHAHAAAHFHAHBAHHAHAHHHNAHHAHAHAHAHHGAHAHBAHDAHBDHADHADHAHAHDHADHAHDH")
####
##while False:
##    print("i in loop")
##
##game_completed = True
##while not game_completed:
##    print("Keep playing!")
    
##dollars = 35
##while dollars < 20:
##    print("insufficient funds")
##    
##x = 100
##while x != 300:
##    x = x - 5
##guess = "x"
##secret_letter = "b"
##while guess != secret_letter:
##    print("Wrong letter! Guess again!") 
##    cheer = "yes"
##while cheer == "yes":
##    for i in range(3): 
##        print("Hip hip hooray!")
##        cheer = input("Would you like us to cheer for you again?")


###classwork ques
#1
##while True:
##    print("bleepbloop FOREVER MUAHAHAHAHHAHAAAHFHAHBAHHAHAHHHNAHHAHAHAHAHHGAHAHBAHDAHBDHADHADHAHAHDHADHAHDH")

#2
##while False:
##    print("loop")
##print("out loop")

#3/4
##secret_word = "tomato"
##nuess = "x"
##giveup = "yes"
##while nuess != secret_word:
##    guess = input("word?:")
##    if guess == secret_word: 
##        print("YAY!!")
##    else:
##        print("nope")
##        giveup = input("give up?:")
##        if giveup == "yes":
##            print("it was tomato haha!")
##        else:
##            print("okay, keep trying!")



#5
##while True:
##    number = int(input("enter a number:"))
##    if number % 2 == 0:
##        break
        
#5 bonus
##while True:
##   number = int(input("enter a number:"))
##   if number % 2 == 1:
##       break

#6
##for i in range(2,9):
##    print(i)
##fast = 2
##while fast <= 8:
##    print(fast)
##    fast+=1
##print("for loops are better for this because it has a range while while loops are very.. confusing!")

#6 bonus
##slow = 8
##while slow >= 2:
##    print(slow)
##    slow-=1

#7
##guess = int(input("Guess the number of marbles in the jar: "))
##number_of_marbles = 249
##while guess != number_of_marbles:
##    print("Incorrect guess! Try again!")
#logic error was the first line; they didn't make guess the number of marbles a string
#also probably THAT YOU HAVE TO restart the loop for new guesses
