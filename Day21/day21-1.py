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

def count_non_alergen_ingredients(alergen_to_word, foods):
    alergen_words = set()
    count = 0
    for alergen in alergen_to_word:
        alergen_words = alergen_words.union(alergen_to_word[alergen])
    for food in foods:
        ingredients, _ = seperate_ingredients_from_alergens(food)
        for ingredient in ingredients:
            if ingredient not in alergen_words:
                count += 1
    return count

def main():
    foods = InputReader.fetch_input_lines()
    alergen_to_word = map_alergens_to_words(foods)
    print(count_non_alergen_ingredients(alergen_to_word, foods))
main()
