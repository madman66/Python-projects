auction = {}

def bidding_process():
    
    while True:
        name = input("Enter your name : ")
        bid = int(input("How much would you like to bid : "))
        auction.update({name:bid})
        bidder_count = input("Are there more bidders : Enter yes if there are more bidders and no if there are not ").lower()
        
        if bidder_count == 'yes':
            continue
        elif bidder_count =='no':
             break 
        else: 
            print("Please enter a valid choice ")

def auction_winner(a):
    l1=[]
    for i in a:
        l1 =l1 + [a[i]]
    b = max(l1)
    for j in a:
        if a[j] ==b:
            print(j,"Has the highest bid at",b)

while True:
    print("Welcome to this Silent Auction")
    m = int(input("How many auctions do you want to run : "))
    for i in range(m):
        bidding_process()
        auction_winner(auction)
    print("Thank you for using our auction services. We hope you had a good time!")
    break 
