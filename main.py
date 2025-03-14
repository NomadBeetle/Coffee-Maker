# Prints the report on the resources left
def print_report():
    for r in resources:
        unit = "ml" if r != "coffee" else "g"
        print(f"{r.title()} : {resources[r]}{unit}")
    print(f"Money : ${money:.2f}")


# Function to check resource availability
def check_resources(order):
    scarcity = [i for i in MENU[order]["ingredients"] if resources[i] < MENU[order]["ingredients"][i]]
    return scarcity


# Function to process coins and return total money inserted
def process_payment():
    print("Please insert coins.")
    try:
        quarters = int(input("How many quarters? : ")) * coins["quarter"]
        dimes = int(input("How many dimes? : ")) * coins["dime"]
        nickels = int(input("How many nickels? : ")) * coins["nickel"]
        pennies = int(input("How many pennies? : ")) * coins["penny"]
        return round(quarters + dimes + nickels + pennies, 2)
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return process_payment()


# Function to make coffee and deduct resources
def make_coffee(order):
    global money
    order_cost = MENU[order]["cost"]
    money_paid = process_payment()

    if money_paid >= order_cost:
        change = round(money_paid - order_cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")

        # Update resources
        for ingredient in MENU[order]["ingredients"]:
            resources[ingredient] -= MENU[order]["ingredients"][ingredient]

        money += order_cost
        print(f"Here is your {order}. Enjoy! ☕")
    else:
        print("Sorry, that's not enough money. Money refunded.")


# Coffee Menu and Resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24},
        "cost": 3.0
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}
coins = {
    "penny": 0.01,
    "dime": 0.10,
    "nickel": 0.05,
    "quarter": 0.25
}
money = 0

# Main Code
while True:
    order = input("What would you like? (espresso/latte/cappuccino) : ").lower()

    if order == "report":
        print_report()

    elif order == "off":
        confirm = input("Are you sure you want to turn off the machine? (yes/no): ").lower()
        if confirm == "yes":
            print("Shutting down the coffee machine. ☕👋")
            break

    elif order == "refill":
        for key in resources:
            while True:
                try:
                    addition = int(input(f"Add {key} (ml/g): "))
                    if addition < 0:
                        print("Enter a positive number.")
                    else:
                        resources[key] += addition
                        break
                except ValueError:
                    print("Invalid input! Enter a valid number.")
        print("Resources refilled!")

    elif order in MENU:
        scarcity = check_resources(order)
        if not scarcity:
            make_coffee(order)
        else:
            print(f"Sorry, there's not enough {', '.join(scarcity)}.")

    else:
        print("Invalid Input! Please enter a valid option.")
