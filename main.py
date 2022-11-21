import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Amount of wininng from slots
def check_winings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    # we loop Every row
    for line in range(lines):
        # We check whatever symbol is in the firs col of the current row
        # Becasue all the symbols need be the same
        symbol = columns[0][line]
        # ANd we need to check for that symbol
        for column in columns:
            symbol_to_check = column[line]
            if symbol == symbol_to_check:
                break
        else:
            winnings += values[symbol * bet]
            winning_lines.append(line + 1)
    
    return winnings, winning_lines
            

# Create sloth machine reels to spin
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
    columns = []
    # Generate a column for every single column that we have
    for _ in range(cols):
        # Picking random values for each row in our column
        column = []
        current_symbols = all_symbols[:]
        # Loop that number of values that we need to generate
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
        
    return columns
    
# Sloth machine 
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        
        print()
    
# To deposit in slot machine the amount of money
def deposit():
    # While the number is good it's will not break
    while True:
        amount = input("Depsit your money? $")
        # Check that number be valid example: 1, 2
        if amount.isdigit():
            # Convert
            amount = int(amount)
            # Greater than zero
            if amount >= 0:
                # And in the end if not good it will breaks
                break
            else:
                print("Must be greater than zero!")
        else:
            print("Please enter a number.")
    
    return amount

# Slot display lines
def get_number_of_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" +str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            # Choose between the lines
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")
    
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            # Choose between the Min and Max
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")
    
    return amount
    
def spin(balance):
    lines = get_number_of_lines()
      # to check if your bet amount is valid to your depost amount
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You don't have enough to bet that amount, yout current balance is: ${balance}")
        else:
            break
        
    print(f"You are betting ${bet} on ${lines} lines. Total bet is equal to: ${total_bet}")
    
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    
    winnings, winning_lines = check_winings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit)")
        if answer == "q":
            break
        balance += spin(balance)
    
    print(f"You left with ${balance}")
        
        
main()

        