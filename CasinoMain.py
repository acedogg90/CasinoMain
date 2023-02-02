#Max number of lines cannot exceed 3
import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

#Values set for wheels and rows for the wheels

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}
 
def get_slot_machine_spin(rows, cols, symbols):
  pass1

#Depost amount to start 

def deposit():
  while True:
    amount = input("What woudl you like to depost? $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Amount must be grater than $0.")
    else:
      print("Please enter a number.")

  return amount
  
def get_number_of_lines():
  while True:
    lines = input("Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Please enter a valid number of lines.")
    else:
      print("Please enter a number.")

  return lines

def get_bet():
    while True:
        amount = input("What woudl you like to bet on each line? $ ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET<= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount
#Main is set to all continued betting.

def main():
  balance = deposit()
  lines = get_number_of_lines()
  while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
  
  total_bet = bet * lines
  print(f"You are betting ${bet} on {lines} lines. Total Bet is equal to: ${total_bet}")
  


main()