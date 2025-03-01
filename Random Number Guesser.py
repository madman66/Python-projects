
from random import randint

def RandomNumberGuesser():
    a = randint(0,100)
    t= 0
    
    difficulty = input("Welcome to this random number guesser game, enter 'easy' for easy difficulty and 'hard' for hard difficulty : ").lower()
    
    if difficulty == 'easy':
        
        print("Welcome to the random nbumber guesser, in easy more you have 10 attempts to get the answer right" )
        
        for i in range(10):
            print("this is attempt number ", i+1, ' you have ',9-i,' attempts left')
            guess = int(input("Enter your guess"))
            
            if guess == a:
                print("YOU WIN!")
                break
            
            elif guess < a:
                print('Too Low,Try again')
            
            elif guess > a:
                print("Too high, try again")
            
        print("You have run out of attempts and YOU LOSE")
                
    elif difficulty == 'hard':
        
        print("Welcome to the random nbumber guesser, in hard more you have 5 attempts to get the answer right" )
        
        for i in range(5):
            print("this is attempt number ", i+1, ' you have ',4-i,' attempts left')
            guess = int(input("Enter your guess"))
            
            if guess == a:
                print("YOU WIN!")
                break
            
            elif guess < a:
                print('Too Low,Try again')
            
            elif guess > a:
                print("Too high, try again")
            
        print("You have run out of attempts and YOU LOSE")
               
    else:
        print("Choose the correct difficulty option")

RandomNumberGuesser()
