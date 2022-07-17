from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.


print(art.logo)
print("Welcome to the secret auction program!")

bidders = []

def add_bidder():
  name = input("What is your name? ")
  bid = int(input("What is your bid? $"))  
  new_bidder = {}
  new_bidder['name'] = name
  new_bidder['bid'] = bid
  bidders.append(new_bidder)

def check_winner():

  max_bid = 0
  winner = {}
  for bidder in bidders:
    if(bidder['bid'] > max_bid):
      winner = bidder
  print(f"Winner is {winner['name']} with {winner['bid']} bid value")

  

while True:
  add_bidder()
  
  status = input("Are there any other bidders? Type 'yes' or 'no'?\n")  

  if(status == 'no'):
    check_winner();
    break
  else:
    clear();





