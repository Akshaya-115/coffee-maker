MENU = {
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

quarters = 0.25
dimes = 0.10
nickles = 0.05
pennies = 0.01


'''continue_ = True
while continue_:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "report":
        print(resources)
        continue

    if coffee not in MENU:
        print("Invalid input.")
        continue


    enough = True
    for item in MENU[coffee]["ingredients"]:
         if MENU[coffee]["ingredients"][item] > resources.get(item, 0):
            print(f"sorry not enough resources to make {coffee}")
            enough = False
            break
    if not enough:
        continue

    print("Please insert coins.")
    q = int(input("how many quarters?:"))
    d = int(input("how many dimes?:"))
    n = int(input("how many nickles?:"))
    p = int(input("how many pennies?:"))
    total = quarters * q + dimes * d + nickles * n + pennies * p
    change = 0
    cost = MENU[coffee]["cost"]

    if total > cost:
        change += total - cost
        print("here is your change", round(change, 2))
        print(f"here is your {coffee}")
        for item in MENU[coffee]["ingredients"]:
            resources[item] -= MENU[coffee]["ingredients"][item]
    elif total == cost:
        print(f"here is your {coffee}")
        for item in MENU[coffee]["ingredients"]:
            resources[item] -= MENU[coffee]["ingredients"][item]
    else:
        print("sorry you don't have enough money, Money refunded.")'''




# 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
#this is the new comment

continue_ = True
while continue_:
    coffee = input("What would you like? (espresso/latte/cappuccino)").lower()
    if coffee == "report":
        print(resources)
        #continue
    # if coffee not in MENU:
    #     print("invalid choice")
    #     continue
    else:
        enough = True

        for item in MENU[coffee]["ingredients"]:
            if MENU[coffee]["ingredients"][item] > resources.get(item, 0):
                print(f"sorry not enough resources to make {coffee}")
                enough = False
                break
        if not enough:
            continue

        print("Please insert coins.")
        q = int(input("how many quarters?:"))
        d = int(input("how many dimes?:"))
        n = int(input("how many nickles?:"))
        p = int(input("how many pennies?:"))
        total = quarters * q + dimes * d + nickles * n + pennies * p
        change = 0
        if coffee == "espresso":
            if total > 1.5:
                change += total - MENU["espresso"]["cost"]
                print("here is your change", change)
                print("here is your cappuccino")
                for item in MENU["espresso"]["ingredients"]:
                    resources[item] -= MENU["espresso"]["ingredients"][item]

            elif total == 1.5:
                print("here is your cappuccino")
                for item in MENU["espresso"]["ingredients"]:
                    resources[item] -= MENU["espresso"]["ingredients"][item]

            else:
                print("sorry you dont have enough money,Money refunded")

        elif coffee == "latte":
            if total > 2.5:
                change += total - MENU["latte"]["cost"]
                print("here is your change", change)
                print("here is your latte")
                for item in MENU["latte"]["ingredients"]:
                    resources[item] -= MENU["latte"]["ingredients"][item]

            elif total == 2.5:
                print("here is your latte")
                for item in MENU["latte"]["ingredients"]:
                    resources[item] -= MENU["latte"]["ingredients"][item]

            else:
                print("sorry you dont have enough money,Money refunded")

        else:
            if total > 3.0:
                change += total - MENU["cappuccino"]["cost"]
                print("here is your change", change)
                print("here is your cappuccino")
                for item in MENU["cappuccino"]["ingredients"]:
                    resources[item] -= MENU["cappuccino"]["ingredients"][item]

            elif total == 3.0:
                print("here is your cappuccino")
                for item in MENU["cappuccino"]["ingredients"]:
                    resources[item] -= MENU["cappuccino"]["ingredients"][item]

            else:
                print("sorry you dont have enough money,Money refunded")
    if coffee=="off":
        continue_=False