##e = 5
##a = 2
##
###1 exakple
##print(e < a)
##
###2 examplee
##print(a > e)
##
###3/ exa,p;e
##print(e == a)
##
##
##x = float(input("enter a x:"))
##y = float(input("enter a y:"))
##
##print("x greater than y?", x > y)
##print("is y greater than x?", y>x)
##print("is x equal to y?", x==y)
##print("is x not equal to y??", x != y )
##
##
##
##xx = "apple"
##print("is apple in xx?", "apple" in xx)
###returns true bc a sequence with the value "apple" is in the string
##
##xxx = "apple"
##print("is pineapple in xxx?", "pineapple" not in xxx)
###return true bc a sequence with the value "pineapple" is not in the string
##
##aa = 5
##b=5
##c = 3
##print("is aa b?", aa is b) #returns true bc aa is the same thing as b
##print("is aa c?", aa is c) #return false bc aa is not the same thing as c
##print("is aa not c?", aa is not c)#returns true bc aa is not c


#ride the roller coaster
age = 10
height = 5

#this is a boolean expression meaning older than 8 and more than 4 ft in height
print("are you enough to ride?", (age > 8) and (height >4), "! alright, hop on")




#waht are booleans 
##ay = 6
##et = 6
##aau =3
##aee = 5
##print("booleans are:", ay is et, aau is aee, "replies" )
##print("logical operaters are symbols and sometimes 'and' or 'or'. for example these are the symbols: <,>,==, != ")
##print("membership operaters are to test if a sequence is presented is inside a object")
##print("identity operaters are used to compare object, not if they are equal but if tehy are the same object with the same ram location")
##print("the 2 equal signs are this: = is to set a value and == is to compare values")
##print("every logical answer is a boolean expression")
##print("the difference between and and or is simple and is when you need two statements to be correct and or is when you only need one statment to be correct for it to say true")
##print((5*2) - 1 ==8 +1)
##print(13 - 6!=(3*2) + 1)
##print(3*(2-1) == 4 -1)
##print((1+1 == 2) and (2+2==4))
##print((3==8)or(3>4))
##print((9+5 <=15) or (7!=4+3))
##print((1<9)and(5!=6))
##print((4*2<=8)and(7-1==6))
##
##
##vowels = "aeiou"
##letter = input("enter a letter:")
##print("vowel: ",letter in vowels)
##print("consonant:", letter not in vowels)
##
##first = input("enter your first name:")
##last = input("enter your last name:")
##a = "a"
##
##print("a inside first name", a in first)
##print("a inside last name?", a in last)


#hangman game

word="newyork"
print("this is a hangman game, here is the topic: cities")
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)
l = input("enter a letter:")
print("in word", l in word)


w = input("whats the word(no spaces):")
print("is that the word?", w==word)

