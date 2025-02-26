from random import randint


def blackjack():

    cards= [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,9,9,9,9,10, 10,10,10,10,10,10,10,10,10,10,10,]
    player = []
    dealer = []
    t=0
    ps=0
    ds=0
    
    
    for i in range(2):
        
        a = len(cards)-1
        x =  randint(0,a)
        player.append(cards[x])
        cards.pop(x)
    
    for i in range(1):
        
        a = len(cards)-1
        x =  randint(0,a)
        dealer.append(cards[x])
        cards.pop(x)
    
    print(player,'\n',sum(player))
    print(dealer,'\n')

    while t==0:
        y = input('Enter "y" if you want to be delt another card and "n" to not get delt another card').lower()

        if y == 'y':
            for i in range(1):
                a = len(cards)-1
                x =  randint(0,a)
                player.append(cards[x])
                cards.pop(x)
            ps=sum(player)
            
            for i in range(1):
                a = len(cards)-1
                x =  randint(0,a)
                dealer.append(cards[x])
                cards.pop(x)   
            ds=sum(dealer) 
            print(player)
            print(dealer)
            print(ps)
            print(ds)
            t=1    
            
        elif y =='n':
            for i in range(1):
                a = len(cards)-1
                x =  randint(0,a)
                dealer.append(cards[x])
                cards.pop(x)
            print(player)
            print(dealer)  
            ps=sum(player)
            ds=sum(dealer)
            print(ps)
            print(ds)
            t=1
        else:
            print('Enter a correct input')
    if ps == 21:
        print("YOU WIN")
    elif ds == 21:
        print("YOU LOSE")
    elif ps < 21 and ps > ds:
        print("YOU WIN")
    elif ps > 21:
        print("YOU LOSE")
    elif ps < 21 and ds > ps:
        print("YOU LOSE")
        




    
blackjack()