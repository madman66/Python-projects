t = 0
while t!=1:
    print ('''        /`-._      _,
          /      `-._(  \
         /           \\  \
        /             \\  \`-._
       /           .   \\  \    `-._
      /           :).   \\  \        `-.
     /           ./;.    \\  \         /
    /           .;'       \\  \       /
   /   .        .          \\  \     /
  /  .; ):.   __________    \\  \   /
 /   . :" '  |~~_~__ _  |    \\(_) /
/       '    ) (_=__=_) (     \(.`/
`-._         |-_________|        /
     `-._                       /
          `-._                 /
               `-._           /
                    `-._     /
                         `-./''')
    print(" Welcome to columbia\n","Your long and ardeous journy has lead you to pablo escobar's house")
    a = input(" You're at a crossroad, do you wanna explore the room on the lef tor the right? \n enter left to enter the room on the left, or right to enter the room on the right : ")
    if a == "left" or a =="Left" or  a =="LEFT":
        print(" You've made it into Escobar's hidden safe room ")
        z = input( " There is a strange button on the safe do you want to press it?\n If yes type yes or no if you're deciding not to touch the button : ")
        if z =="yes" or z == "YES" or z == "Yes":
            print("the room exploded and you are dead")
            print('''     _           _             
                | |         (_)            
  _____  ___ __ | | ___  ___ _  ___  _ __  
 / _ \ \/ / '_ \| |/ _ \/ __| |/ _ \| '_ \ 
|  __/>  <| |_) | | (_) \__ \ | (_) | | | |
 \___/_/\_\ .__/|_|\___/|___/_|\___/|_| |_|
          | |                              
          |_|''')
            print("You've somehow ended up back at the enterance of the mansion forced to go through the same incidents as before untill you find the treasure or give up")
        elif z =="no" or z == "NO" or z == "No":
            print("Nothing happens for a while and you get bored the leave the mansion with filled with extreme sadness and on the way out slip on a bananna peel and fall down breaking your head and passing away in as funny circumstance")
            print('''_  /)
                 mo / )
                 |/)\)
                  /\_
                  \__|=
                 (    )
                 __)(__
_________+______/      \______+__________
  __--   |       R.I.P.       |-_-- __
_-- -    | ___ __________ ___ |
-_-- __  || | | | {|    /| | || __---  -_
 --__-   || | | | {|   /|| | ||--        -
         || | | | {|  /||| | ||__--
 __-- -__|| | | | {| |}||| | ||--   __--
         ||_|_|_|_{| |}|||_|_||  -__
 --__-  -|| | | | {& |}||/ | ||---   __--
         || | | | {| |}|/| | ||-__
--   __--|| | | | {| |}/|| | ||__-- -__
  --     || | | | {| &}||| | ||   __
---   __-|| | | | {| |}||| | ||_---__-  --
 -  -_   || | | | {| |}||| | || --
 __ejm 97|| | | | {| |}||| | ||_--__-   _---
_________||_|_|_|_{| |}|||_|_||______________
                     |}|/
                     |}/
                     |/''')
            print("You've somehow ended up back at the enterance of the mansion forced to go through the same incidents as before untill you find the treasure or give up")
        else:
            print("Please enter a valid choice!")
            print("You've somehow ended up back at the enterance of the mansion forced to go through the same incidents as before untill you find the treasure or give up")

    elif a =="right" or a =="RIGHT" or a == "Right":
        print("You've successfully made it into the real vault there is a keypad and a sticky note with the numbers 011249 written on it")
        x = input(" Are you brave enough to enter the number you see on the keypad? or are you entering a code of your own choosing? \n if thats the case enter yes and no if you're entering a custom code : ")
        if x =="yes" or x =="YES" or x =="Yes":
            print("The code was a security lock code and the mansion is in lockdown and you are stuck in here for eternity")
            print("You've somehow ended up back at the enterance of the mansion forced to go through the same incidents as before untill you find the treasure or give up")
            print('''  _________________________
     ||   ||     ||   ||
     ||   ||, , ,||   ||
     ||  (||/|/(\||/  ||
     ||  ||| _'_`|||  ||
     ||   || o o ||   ||
     ||  (||  - `||)  ||
     ||   ||  =  ||   ||
     ||   ||\___/||   ||
     ||___||) , (||___||
    /||---||-\_/-||---||\
   / ||--_||_____||_--|| \
  (_(||)-| S123-45 |-(||)_)''')
        elif x =="no" or x=="NO" or x=="No":
            for i in range(5):
                q = int(input("enter a six digit code : "))
                if q == 696969:
                    print("you have successfully opened the vault and gotten all the riches left behind for yourself and successfully left the mansion multitudes richer than when you entered")
                    t = 1
                    break
                elif q != 696969:
                    h = 4 - i
                    print("The code you entered was incorrect.")
                    print("you have "+str(h)+ " attempts left")
                
        else:
            print("Please enter a valid option!")

    
    else:
        print("Please enter as valid option!!")


                
    
            

