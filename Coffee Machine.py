menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


# TODO: 2 check if resources are enough
def resource_checker(ingredients):
    is_enough=True
    for i in ingredients:
        if ingredients[i] >= resources[i]:
            print(f"Sorry there is not enough {i}.")
            is_enough = False

    return is_enough

# TODO: 3 process coins

def coin_process():
    quarters = int(input("How many quarters are you entering : "))*0.25
    dimes =int(input("How many dimes are you entering : "))*0.10
    nickles = int(input("How many nickles are you entering : "))*0.05
    pennies = int(input("How many pennies are you entering : "))*0.01
    total = quarters+dimes+nickles+pennies
    return total

def transaction(money,cost):
    if money > cost:
        change = round(money - cost, 2)
        print(f"Here is ${change} change")
        global profit
        profit += cost
        return True
    else:
        print("sorry! that's not enough money😒. Money refunded ")
        return False

def make_coffee(drink_name, order_ingredients):

    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")

while True:
    # TODO: 1 print report of all resources
    order = input("What would you like to order? we have \n1.Espresso \n2.latte \n3.cappuccino \nEnter 'off' to switch the machine off \nEnter report to see the current resource level : ").lower()
    if order == 'report':
        for i in resources:
            print(i, ':', resources[i])
    elif order == 'off':
        print("Thank You")
        break
    else:
        drink = menu[order]
        if resource_checker(drink["ingredients"]):
            payment = coin_process()
            if transaction(payment, drink['cost']):
                make_coffee(order, drink["ingredients"])















