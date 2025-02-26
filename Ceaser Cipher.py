import string
l1 = list(string.ascii_uppercase)
m = 1
l = 1

def encoder(a):
    global m
    a = a.upper()
    n = 0
    
    en = ""
    while len(a) >= m:
        
        for j in a:
            if j == ' ': continue
            else:
                n = l1.index(j)
                en = en + l1[n+1]
                m+=1
    m1=len(en)
    m1=int(m1/2)
    print(en[0:m1])
            
def decoder(a):
    global l
    a = a.upper()
    n = 0
    l = 1
    de = ""
    while len(a) >= l:
        
        for j in a:
            if j == ' ': continue
            else:
                n = l1.index(j)
                de = de + l1[n-1]
                l+=1
    l2 = len(de)
    
    print(de[0:l2])

encoder('hello world')
decoder('IFMMPXPSME')


while True:
    print("Welcome to the Ceaser Cipher. You can decode or encode messages using this code \n")
    a = input("Would you like to encode or decode a word or phrase : \n enter encode for encoding or decode for decoding and type exit to stop the program : \n").lower()
    if a == 'encode':
        b = input("Would you like to encode by moving a letter forward or backward : Enter forward to encode forward and enter backward for backwards encoding : \n").lower()
        if b == 'forward':
            encoder(input("Enter the phrase you want encoded : \n"))
        elif b == 'backwards':
            decoder(input("Enter the phrase you want encoded : \n"))
        else: print("Please enter a valid choice to use the encoding features \n")
    elif a == 'decode':
        b = input("Would you like to decode by moving a letter forward or backwards : Enter forward to decode forward and enter backward for backwards decoding : \n").lower()
        if b == 'backward':
            encoder(input("Enter the phrase you want decoded : \n"))
        elif b == 'backwards':
            decoder(input("Enter the phrase you want decoded : \n"))
        else: print("Please enter a valid choice to use the decoding features")
    elif a == 'exit':
        break
    else:
        print('Please choose a valid option')
    

    
