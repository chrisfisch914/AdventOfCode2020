import re
import sys
sys.path.append("..")
from input_reader import InputReader

def initalize_decks(lines):
    player1_cards = []
    player2_cards = []
    for card in lines[0].split("\n")[1:]:
        player1_cards.append(int(card))
    for card in lines[1].split("\n")[1:]:
        player2_cards.append(int(card))
    return player1_cards, player2_cards

def calcualte_score(winning_deck):
    multiplier = len(winning_deck)
    sum = 0
    while(len(winning_deck) > 0):
        sum += multiplier * winning_deck.pop(0)
        multiplier -= 1
    return sum

def cards_to_key(player1_cards, player2_cards):
    key = "Player1: "
    for card in player1_cards:
        key += str(card) + " "
    key += "Player2: "
    for card in player2_cards:
        key += str(card) + " "
    return key

def player1_wins(player1_cards, value1, value2):
    player1_cards.append(value1)
    player1_cards.append(value2)

def player2_wins(player2_cards, value1, value2):
    player2_cards.append(value2)
    player2_cards.append(value1)

def initalize_new_deck(deck, count):
    new_deck = []
    for i in range(count):
        new_deck.append(deck[i])
    return new_deck

def recursive_combat(player1_cards, player2_cards):
    memo = {}
    while len(player1_cards) > 0 and len(player2_cards) > 0:
        if cards_to_key(player1_cards, player2_cards) in memo:
            return 1, player1_cards
        memo[cards_to_key(player1_cards, player2_cards)] = True
        value1 = player1_cards.pop(0)
        value2 = player2_cards.pop(0)
        if len(player1_cards) < value1 or len(player2_cards) < value2:
            if value1 > value2:
                player1_wins(player1_cards, value1, value2)
            else:
                player2_wins(player2_cards, value1, value2)
        else:
            new_player1_cards = initalize_new_deck(player1_cards, value1)
            new_player2_cards = initalize_new_deck(player2_cards, value2)
            winner, _ = recursive_combat(new_player1_cards, new_player2_cards)
            if winner == 1:
                player1_wins(player1_cards, value1, value2)
            else:
                player2_wins(player2_cards, value1, value2)
    if len(player1_cards) > 0:
        return 1, player1_cards
    else:
        return 2, player2_cards

def main():
    lines = InputReader.fetch_input_seperated_by_empty_lines()
    player1_cards, player2_cards = initalize_decks(lines)
    _, winning_deck = recursive_combat(player1_cards, player2_cards)
    print(calcualte_score(winning_deck))

main()