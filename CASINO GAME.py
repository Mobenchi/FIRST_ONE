import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 10

ROW = 3
COL = 3
symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5
}
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}
def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines 
def get_machine_slot_spin(rows ,cols ,symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()
def deposit():
    while True:
        balance = input("enter amout that you want to deposit? $")
        if balance.isdigit():
            balance = int(balance)
            if balance > 0:
                break
            else:
                print("the amout must be greater than 0")
                continue
        else:
            print("please enter a number not a letter or a symbole")
            continue
    return balance
def numbers_of_lines_():
    while True:
        lines = input("enter the number of lines that you want to bet in (1-"+ str(MAX_LINES) +")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("the amout must be in (1-"+ str(MAX_LINES) +")")
                continue
        else:
            print("please enter a number in (1-"+ str(MAX_LINES) +")")
            continue
    return lines
def get_bet():
    while True:
        amount = input("enter amout that you want to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET :
                break
            else:
                print(f"the bet must be greater than ${MIN_BET} - ${MAX_BET}")
                continue
        else:
            print("please enter a number not a letter or a symbole")
            continue
    return amount
def spin(wallet_balance):
    lines_numbers = numbers_of_lines_()
    while True:
        bet = get_bet()
        total_bet = bet * lines_numbers
        if total_bet > wallet_balance :
            print(f"you do not have enough money to bet with, your current balance is ${wallet_balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines_numbers} lines . total bet is equal to : ${total_bet}")
    slots = get_machine_slot_spin(ROW, COL, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winning(slots, lines_numbers, bet, symbol_value) 
    print(f"you won ${winnings}")
    print("you won on thr line", *winning_lines)
    return winnings - total_bet
def main():
    wallet_balance = deposit()
    while True:
        print(f"your current balance is ${wallet_balance}")
        spinning = input("press enter to play (q to quit).")
        if spinning == "q":
            break
        wallet_balance += spin(wallet_balance)
    print(f"you left with ${wallet_balance}")


    
main()

