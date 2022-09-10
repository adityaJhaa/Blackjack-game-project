############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
endgame=False
import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
                   

def intro():
  global carddeck
  carddeck=[11,2,3,4,5,6,7,8,9,10,10,10]
  a=random.choice(carddeck)
  b=random.choice(carddeck)
  global userlist
  userlist=[a,b]
  global sum1
  
  sum1=sum(userlist)
  x=0
  for i in userlist:
    if sum1>21 and i==carddeck[0]:
      userlist[x]==1
    x+=1
  c=random.choice(carddeck)
  d=random.choice(carddeck)
  global complist
  complist=[c,d]
  global sum2
  
  sum2=sum(complist)
  x=0
  for i in complist:
    if sum2>21 and i==carddeck[0]:
      complist[x]==1
    x+=1
def displayscore():
  print(f"User cards : {userlist} and total score:{sum1}")
  print(f"computer's first card:{complist[0]}")
def winner():
  if sum1==sum2:
    print("Draw")
  elif sum1>21:
    print("You lose")
    #come here back after want to play more function
  elif sum2>sum1:
    print("You lose")
  else:
    print("You won")
  
  
def display_complist():
  print(complist)

  
def core():
  choice=input("y for pass and n for taking one more card")
  if choice=="y":
    displayscore()
    display_complist()
    winner()
  if choice=="n":
    global sum1
    global sum2
    m=random.choice(carddeck)
    n=random.choice(carddeck)
    sum1+=m
    sum2+=n
    userlist.append(m)
    complist.append(n)
    while sum2<17:
      y=random.choice(carddeck)
      sum2+=y
      complist.append(y)
    displayscore()
    display_complist()
    winner()
def endorcont():
  global endgame
  
  choice=input("want to continue or end(y/n")
  if choice=="y":
    game()
  else:
    endgame=True
  
def game():
  while not endgame:
    print(logo)
    intro()
    displayscore()
    core()
    endorcont()
game() 
      
    
    
  
