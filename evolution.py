#from models.Being import Being
from singleton import used_ids
from singleton import couples



import functions.functions as f
#import random
#import sys
#import os


first_gen = f.first_gen()
global used_ids

pairs = f.generate_pairs(first_gen)

for pair in pairs:
	for individual in pair:
		print(individual.gene(), end=" ")
	print()
print("-----------")

new_gen = f.new_gen(pairs)

for child in new_gen:
	parents = f.find_parents(child)
	p1_gene = parents[0].gene()
	p2_gene = parents[1].gene()
	print(child.gene(), "<-", p1_gene, p2_gene)

	print("This is a test")

'''
for i, being in enumerate(new_gen):
	print(being.gene(), "<-", pairs[i][0].gene(), pairs[i][1].gene())
'''

#stop = False

#while not stop:



#user_choice = input("New generation?").lower()

#if user_choice == "no":
	#stop = True
	#break
#else:
	#del first_gen[:]
	#print('\n'*100)




'''

try:
	print(being3.gene())
except AttributeError:

	pass
'''



