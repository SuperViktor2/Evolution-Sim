#from models.Being import Being
from singleton import used_ids
#from singleton import couples



import functions.functions as f
#import random
#import sys
#import os


first_gen = f.first_gen()
global used_ids

print("Creating 1st generation:")
init_pairs = f.generate_pairs(first_gen)
current_pairs = []

for pair in init_pairs:
	for individual in pair:
		print(individual.gene(), end=" ")
	print()
print("-----------")

user_choice = input("Create next generation? (Press enter for yes or type no)").lower()

while user_choice != "no":


    parents_to_use = current_pairs if current_pairs else init_pairs

    new_gen = f.new_gen(parents_to_use)

    for child in new_gen:
        parents = f.find_parents(child, parents_to_use)
        if len(parents) == 2:
            print(f"{child.gene()} <- {parents[0].gene()} {parents[1].gene()}")

    print("---- Making pairs ----")

    current_pairs = f.generate_pairs(new_gen)

    for pair in current_pairs:
        for individual in pair:
            print(individual.gene(), end=" ")
        print()

    user_choice = input("Create next generation? (Press enter for yes or type no)").lower()