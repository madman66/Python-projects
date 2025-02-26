import random
l1 = [
    "action", "banana", "beauty", "breeze", "broken", "burden", "camera", "casual", "choice", "chorus",
    "coffee", "combat", "cotton", "danger", "desire", "detect", "divide", "dragon", "easily", "editor",
    "empire", "escape", "excuse", "fabric", "famous", "father", "frozen", "gather", "golden", "gravel",
    "hammer", "honest", "hunter", "income", "island", "jacket", "jungle", "kidney", "ladder", "lawyer",
    "legend", "linear", "luxury", "magnet", "manner", "marble", "mentor", "moment", "monkey", "mother",
    "muscle", "mystic", "nectar", "notion", "object", "orange", "oxygen", "packet", "pastor", "pebble",
    "phrase", "planet", "plenty", "pocket", "prefer", "prison", "public", "puzzle", "quaint", "racing",
    "random", "refine", "replay", "rescue", "retail", "reward", "rhythm", "rocket", "safety", "sailor",
    "sample", "savage", "school", "script", "singer", "silver", "spirit", "stolen", "stream", "subtle",
    "tablet", "target", "temple", "thirst", "timber", "tongue", "trophy", "urgent", "vacant", "vector",
    "velvet", "vision", "wealth", "window", "writer", "yellow", "zephyr", "zigzag", "zodiac", "zombie"
]
chosen_word = random.choice(l1) 
print(chosen_word)


t = 0 # loop avariable
g = 0 #ascii variable
def alpha_check():
    global t,g
    a2 = 0 #guess index x
    a1 = 0 #word index y
    guess = input("Enter a word :").lower()
    if chosen_word == guess:
        print("You Guessed the word \n YOU WIN")
        t = 1
        g = 0
        
    else:
        for i in range(6):
            if guess[a2] ==chosen_word[a2]:
                print("The letter ",chosen_word[a1]," is present in the ",a1+1,'th position')
                g +=1
                a1+=1
                a2+=1
def ascii():
    global g
    if g == 1:
        print("""
      +---+
      |   |
          |
          |
          |
          |
    =========
    """, "\n You have 5 attempts left")
    elif g ==2:
        print("""
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """, "\n You have 4 attempts left")
    elif g ==3:
        print("""
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """, "\n You have 3 attempts left")
    elif g == 4:
        print("""
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """, "\n You have 2 attempts left")
    elif g ==6:
        print("""
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """, "\n You have 1 attempt left")
    elif g ==7:
        print("""
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """, "\n GAME OVER")
    
        
while t!=1:
    alpha_check()
    ascii()
