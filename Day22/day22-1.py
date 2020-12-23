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

def combat(player1_cards, player2_cards):
    while len(player1_cards) > 0 and len(player2_cards) > 0:
        value1 = player1_cards.pop(0)
        value2 = player2_cards.pop(0)
        if value1 > value2:
            player1_cards.append(value1)
            player1_cards.append(value2)
        else:
            player2_cards.append(value2)
            player2_cards.append(value1)
    if len(player1_cards) > 0:
        return player1_cards
    else:
        return player2_cards

def main():
    lines = InputReader.fetch_input_seperated_by_empty_lines()
    player1_cards, player2_cards = initalize_decks(lines)
    winning_deck = combat(player1_cards, player2_cards)
    print(calcualte_score(winning_deck))

main()