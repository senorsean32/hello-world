
# coding: utf-8

# In[1]:

from IPython.display import clear_output
import random


# In[2]:

class Deck(object):
    init_deal = True
    
    def __init__(self):
        self.cards = {'Two': 2,
               'Three': 3,
               'Four': 4,
               'Five': 5,
               'Six': 6,
               'Seven': 7,
               'Eight': 8,
               'Nine': 9,
               'Jack': 10,
               'Queen': 10,
               'King': 10,
               'Ace': 11}
    
    def deal(self):
        self.init_deal = False
        return random.choice(self.cards.items())


# In[3]:

class User(object):
    hand = []
    hand_total = 0
    
    def receive_card(self, cardIn):
        self.cardIn = cardIn
        self.hand.append(self.cardIn)
        self.hand_total = self.hand_total + self.cardIn[1]
            
    def reset_cards(self):
        self.hand = []
        self.hand_total = 0


# In[4]:

class Player(User):
    
    def __init__(self, money = 100):
        self.money = money
        
    def adjust_money(self, amount):
        self.money = self.money + amount
        total = self.money
        return total
        
    def place_bet(self):
        print "Your cash: " + str(player.money)
        return int(raw_input('What is your wager? \n'))


# In[5]:

# Global Vars
dealer = User()
player = Player()
deck = Deck()
wager = 0
playing = False
result = "blank"


# In[6]:

def game_intro():
    print "Welcome to my crappy BlackJack game!"
    print "I hope you already know the rules. I'm too lazy to type them out"
    print "----------------------------------------------------------------"


# In[7]:

def gameplay():
    # Set up game and initial deal
    global dealer, player, deck, wager, playing
    
    # Reset the hands
    dealer.reset_cards()
    player.reset_cards()
    
    # Clear screen
    clear_output()
    
    # Prompt player to enter wager amount
    print "Your current bankroll = " + str(player.money)
    wager = int(raw_input("Please enter your wager for this hand\n"))
    
    # Deal cards to dealer
    dealer.receive_card(deck.deal())
    dealer.receive_card(deck.deal())
    
    # Deal cards to player
    player.receive_card(deck.deal())
    player.receive_card(deck.deal())
    
    playing = True
    game_display()
    player_input()


# In[8]:

def show_hands():
    global dealer, player
    
    # Print out the name value for each card tuple
    print "Dealer's hand: "
    for tuple in dealer.hand:
        print tuple[0]
    print "Dealer hand total: " + str(dealer.hand_total) 
    
    print " "

    print "Player's hand: "
    for tuple in player.hand:
        print tuple[0]
    print "Your hand total: " + str(player.hand_total)  


# In[9]:

def game_display():
    # Display the game state info
    global dealer, player, wager, playing, result
    
    # Clear screen
    clear_output()
    
    # Print current wager amount
    print "Bankroll: " + str(player.money - wager) + " Wager: " + str(wager)
    print " "
    
    # Display current hands
    show_hands()
       
    if playing:
        player_input()
    else:
        print result
        raw_input("Press ENTER to continue")
        gameplay()


# In[10]:

def player_input():
    ''' Read user input, lower case it just to be safe'''
    plin = raw_input("Press Hit, Stand or Quit\n").lower()
    
    
    if plin == 'h':
        hit()
    elif plin == 's':
        stand()
    elif plin == 'q':
        game_exit()
    else:
        print "Invalid Input...Enter h, s, or q: "
        player_input()


# In[11]:

def hit():
    # Handle the player card logic
    global player, result, playing, wager

    player.receive_card(deck.deal())
    
    p_total = player.hand_total
    
    if p_total == 21:
        result = "You hit 21, dude! You win this hand!"
        playing = False
        player.money += wager
    elif p_total > 21:
        result = "You busted, fool!"
        playing = False
        player.money -= wager

    game_display()


# In[12]:

def stand():
    # Handle the CPU card logic
    global dealer, player, wager, playing, result
    d_total = dealer.hand_total
    
    while d_total < 17:
        dealer.receive_card(deck.deal())
        d_total = dealer.hand_total
        continue
    
    d_total = dealer.hand_total
    p_total = player.hand_total
    
    if d_total == p_total:
        result = "It was a push"
    elif d_total > 21:
        result = "The dealer busted! What an idiot!! You won this hand"
        player.money += wager
    elif d_total < p_total:
        result = "You won this hand!"
        player.money += wager
    elif d_total > p_total:
        result = "Haha! The dealer won, sucker!"
        player.money -= wager
    
    playing = False
    game_display()


# In[ ]:

def game_exit():
    print "Thanks for playing!"
    exit()


# In[ ]:

game_intro()
gameplay()


# In[ ]:

"""
1. Welcome message-
2. Show bankroll and ask for wager-
3. Deal 2 cards to the player and the dealer
4. If either has BJ, declare winner and handle money. Reset cards and go to STEP 2.
5. If not BJ, prompt player for HIT or STAND
6. If BJ, player wins, gets money. Reset cards and go to STEP 2.
7. If BUST, player loses, loses money. Reset cards and go to STEP 2.
8. If HIT, give new card and check for BJ or BUST
9. If BJ, go to STEP 6. If BUST, go to STEP 7. If not BJ or BUST, deal 1 card, go to STEP 5.
10. If STAND, dealer HITs until WIN or BUST. 
11. If Player wins, gets money. Reset cards and go to STEP 2.
12. If Dealer wins, player loses money. Reset cards and go to STEP 2.
13. If player is out of money, GAME OVER
"""
game_start()


# In[ ]:



