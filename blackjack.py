##############
# Blackjack! #
##############

# To Do:
# - add dealer logic for multiple hits depending on score
# - add blackjack logic 
# - add soft 17 logic
# - add betting logic
# - add multiple players
# - add split logic
# - add double down logic
# - add insurance logic
# - add surrender logic
# - clean up card formatting

#############
# Libraries #
#############
import random
import time

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
print('Let\'s play Blackjack!\n')

# shuffle the deck
random.shuffle(deck)

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
    hit_input = input('Would you like a card? (y/n)\n')
    if hit_input == 'y':
        print('Player hits!\n')
        time.sleep(1)
        deal_card(1, player1)
        print('Player receives:', player1['cards'][-1])
        show_cards(player1)
        if calc_score(player1) > 21:
            print(f'Player busts with a score of {player1['score']}!\n')
            flag_hit = False
        else:
            continue
    else:
        print('Player stands!')
        time.sleep(1)
        # Show dealer's cards
        print('Dealer flips their card and shows:', {dealer['cards'][1]}, ' with a score of:', calc_score(dealer),'\n')
        # Dealer play their hand
        while calc_score(dealer) < 17:
            time.sleep(1)
            print('\nDealer hits!')
            time.sleep(1)
            deal_card(1, dealer)
            show_cards(dealer)
            if calc_score(dealer) > 21:
                print(f'Dealer busts with a score of {dealer['score']}!\n')
                flag_hit = False
                break
        if player1['score'] > dealer['score']:
            print(f'Player wins! (Dealer: {dealer['score']} vs. Player: {player1['score']})\n')
        elif player1['score'] == dealer['score']:
            print('Push!\n')
        elif dealer['score'] > 21:
            print(f'Player wins! (Dealer: {dealer['score']} vs. Player: {player1['score']})\n')
        else:
            print(f'Dealer wins! (Dealer: {dealer['score']} vs. Player: {player1['score']})\n')
        flag_hit = False