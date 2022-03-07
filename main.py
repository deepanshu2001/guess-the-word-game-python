# program to build guess the word game


import random

l=["python","programmer","java","algorithm","masters",'america']


word=random.choice(l)

name=input("Enter your name:")
print("Welcome "+name+" to the game")
print(f"The word is of {len(word)} letters!")
turn=5
while turn>0:
    guess=input("Enter a word :")
    if (guess!=word):
        print("Wrong guess")
        turn-=1
        print(f"You have {turn} guesses remaining!")
    else:
        print("Yo win")
        print(f"The word is {word}")
        break

if turn==0:
    print("You ran out of turns!")
    print("You Lose")



        


