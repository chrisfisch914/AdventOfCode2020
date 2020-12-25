import re
import sys
sys.path.append("..")
from input_reader import InputReader
import pprint

printer = pprint.PrettyPrinter()

def clean_alergens(alergens):
    for index, alergen in enumerate(alergens):
        if "," in alergen or ")" in alergen:
            alergens[index] = alergen[:-1]
    return alergens

def seperate_ingredients_from_alergens(food):
    split_food = food.split(" (contains ")
    ingredients = split_food[0].split(" ")
    alergens = clean_alergens(split_food[1].split(" "))
    return ingredients, alergens

def map_alergens_to_words(foods):
    alergen_to_word = {}
    for food in foods:
        ingredients, alergens = seperate_ingredients_from_alergens(food)
        for alergen in alergens:
            if alergen in alergen_to_word:
                alergen_to_word[alergen] = alergen_to_word[alergen].intersection(set(ingredients))
            else:
                alergen_to_word[alergen] = set(ingredients)
    return alergen_to_word

def swap_keys_and_values(matches):
    new_matches = {}
    for key in matches:
        new_matches[matches[key]] = key
    return new_matches

def match_alergen_to_word(alergen_to_word):
    matches = {}
    keep_going = True
    while keep_going:
        keep_going = False
        for alergen in alergen_to_word:
            if len(alergen_to_word[alergen]) == 1:
                for word in alergen_to_word[alergen]:
                    matches[word] = alergen
            else:
                keep_going = True
                remove_set = set()
                for word in alergen_to_word[alergen]:
                    if word in matches:
                        remove_set.add(word)
                alergen_to_word[alergen] = alergen_to_word[alergen].difference(remove_set)
    return swap_keys_and_values(matches)

def print_canonical_list(alergen_to_word):
    result = ""
    for alergen in sorted(alergen_to_word.keys()):
        result += alergen_to_word[alergen]
        result += ","
    print(result[:-1])

def main():
    foods = InputReader.fetch_input_lines()
    alergen_to_words = map_alergens_to_words(foods)
    alergen_to_word = match_alergen_to_word(alergen_to_words)
    print_canonical_list(alergen_to_word)
main()
