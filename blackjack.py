##############
# Blackjack! #
##############

# To Do:
# - Add dealer logic for multiple hits depending on score

#############
# Libraries #
#############
import random

#############
# Variables #
#############

deck = []
dealer = {'name': 'Dealer', 'type': 'dealer', 'cards': [], 'score': 0}
player1 = {'name': 'Player', 'type': 'player', 'cards': [], 'score': 0}
players = [dealer, player1]

# Create deck of cards
suits = ['C', 'D', 'H', 'S']
cards = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']

# start a new deck and add cards to deck list
def new_deck():
    for suit in suits:
        x = 0
        for card in cards:
            deck.append(cards[x] + ':' + suit)
            # print(cards[x], ':', suit)
            x += 1

# start a new deck        
new_deck()
print('Let\'s play Blackjack!')
# print('Base deck \n', deck, '\nTotal cards:', len(deck))

# shuffle the deck
random.shuffle(deck)
# print('Shuffled deck \n', deck, '\nTotal cards:', len(deck))

# deal a card
# variables indicate how many cards to deal and who to deal to
def deal_card(num_cards: int, deal_to: str):
    x = 0
    while x < num_cards:
        card = deck[0]
        deck.remove(card)
        deal_to['cards'].append(card)
        x += 1

deal_card(2, player1)
deal_card(2, dealer)
# print('Deck after dealing a card \n', deck, '\nTotal cards:', len(deck))

# for i in players:
#     print(f'{i['name']} cards:', i['cards'], 'total cards:', len(i['cards']))

# calculate score
def calc_score(player: str):
    score = 0
    for card in player['cards']:
        card_value = card.split(':')
        if card_value[0] in ['K', 'Q', 'J']:
            score += 10
        elif card_value[0] == 'A':
            if score + 11 > 21:
                score += 1
            else:
                score += 11
        else:
            score += int(card_value[0])
    player['score'] = score
    return score

# show cards for a selected player or 'all' for all players
def show_cards(player: str):
    if player=='all':
        for i in players:
            print(f'{i['name']} cards:', i['cards'], 'total cards:', len(i['cards']), 'score:', calc_score(i))
    else:
        print(f'{player['name']} cards:', player['cards'], 'total cards:', len(player['cards']), 'score:', calc_score(player))

# show dealers first card
print('Dealer shows:', dealer['cards'][0])

# show player their own cards
show_cards(player1)

# Ask player if they want a card
flag_hit = True
while flag_hit == True:
    hit_input = input('Would you like a card? (y/n)')
    if hit_input == 'y':
        print('player hits!')
        deal_card(1, player1)
        show_cards(player1)
        if calc_score(player1) > 21:
            print(f'Player busts with a score of {player1['score']}!')
            flag_hit = False
        else:
            continue
    else:
        print('player stands!')
        show_cards('all')
        if player1['score'] > dealer['score']:
            print('Player wins!')
        elif player1['score'] == dealer['score']:
            print('Push!')
        else:
            print('Dealer wins!')
        flag_hit = False