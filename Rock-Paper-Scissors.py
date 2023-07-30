Yangyang Lian
07/12/2023
CS 10 Rock-Paper-Scissors

def determineWinner(user, computer):
user = user.lower()
computer = computer.lower()
if user == computer: 
print("It's a Tie!!!")
elif user == "rock": 
if computer == "scissor" or computer == "scissors": 
print("User Wins! Rock breaks Scissors!!") 
else: 
print("Computer Wins! Paper Covers Rock!!")
elif user == "paper":
if computer == "rock":
print("User Wins! Paper Covers Rock!!") 
else:
print("Computer Wins! Scissors Cut Paper!!") 
else: 
if computer == "rock":
print("Computer Wins! Rock breaks Scissors!!")
else: 
print("User Wins! Scissors Cut Paper!!") 

def userMove():
user = input("Please enter your move: Paper, Rock, or Scissors: ").lower()
return user

def computerMove():
moves = ["Rock", "Paper", "Scissors"]
return moves[random.randint(0, len(moves)-1)]

def main():
user = userMove()
computer = computerMove()
print("Computer's move is",computer)
if user == "rock" or user == "paper" or user == "scissors" or user == "scissor":
determineWinner(user, computer) 
else: 
print("Invalid move!!")

if __name__ == "__main__":
main() 
