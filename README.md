# Coffee Machine Program

This is a terminal-based Coffee Machine program written in Python. It simulates a simple vending machine where users can order coffee, manage resources, and handle payments.

## Features
- **Order Processing**: Users can order espresso, latte, or cappuccino.
- **Resource Management**: The program checks if enough resources are available before making a drink.
- **Coin Handling**: Users insert coins, and the machine calculates total payment.
- **Change Dispensing**: If excess money is inserted, the machine returns change.
- **Report Generation**: The machine can display the remaining resources and total earnings.
- **Refill Option**: Allows maintainers to refill the machine's resources.
- **Shutdown Option**: Maintainers can turn off the machine.

## How to Run
1. Clone the repository:
   ```sh
   git clone https://github.com/NomadBeetle/Coffee-Maker.git
   cd Coffee-Maker
   ```
2. Run the program:
   ```sh
   python coffee_machine.py
   ```

## Commands
- `espresso`, `latte`, `cappuccino` – Order a coffee.
- `report` – Display remaining resources and money earned.
- `refill` – Add more water, milk, or coffee.
- `off` – Shut down the machine.

## Example Interaction
```
What would you like? (espresso/latte/cappuccino) : latte
Please insert coins.
How many quarters? : 10
How many dimes? : 0
How many nickels? : 0
How many pennies? : 0
Here is $0.50 in change.
Here is your latte. Enjoy! ☕
```

## Author
**Made by Azaan Ahmed**
- [GitHub](https://github.com/NomadBeetle)
- [LinkedIn](https://www.linkedin.com/in/azaan-ahmed-a738b4332/)
- [LeetCode](https://leetcode.com/u/NomadBeetle/)
