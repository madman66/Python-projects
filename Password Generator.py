import random
l1=['a ','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','q','w','e','r','t','y','u','i','o','p'] 
l2=['A','S','D','F','G','H','J','K','L','Q','W','E','R','T','Y','U','I','O','P','Z','X','C','V','B','N','M']
L3=['1','2','3','4','5','6','7','8','9','0']
L4 =['!','@','#','$','%','&','_','-',]
l5=[]
g = ""
x = int(input("How many letters should the password have : "))
a,b,c,d= int(input("How many lower case characters do you want in the password : ")),int(input("How many upper case characters do you want in the password : ")),int(input("How many numbers do you want in the password : ")),int(input("How many special characters do you want in the password : "))
while len(l5) != x:
    for i in range(a):
        l5.append(l1[random.randint(0,25)])
    for i in range(b):
        l5.append(l2[random.randint(0,25)])
    for i in range(c):
        l5.append(L3[random.randint(0,9)])
    for i in range(d):
        l5.append(L4[random.randint(0,7)])
l5=random.sample(l5,len(l5))
for i in l5:
    g = g + i

print("The password generated for you is : ",g)



    

      
