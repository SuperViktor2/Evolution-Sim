import sys
import random

sys.path.insert(1, '/Users/viktorgoles/Desktop/Evolution/models')
sys.path.insert(2, '/Users/viktorgoles/Desktop/Evolution')

from Being import Being
from singleton import used_ids
from singleton import couples



global used_ids


def mate(prt1, prt2):

	parent_gen = prt1.generation
	
	if ((prt1.sex == "F") & (prt2.sex == "M")) | ((prt1.sex == "M") & (prt2.sex == "F")): #check if different sex

		while True:
			p1_tag = str(prt1.id)[:3]
			p2_tag = str(prt2.id)[:3]
			unique_suffix = f"{random.randint(0, 99):02}"

			new_id = p1_tag + p2_tag + unique_suffix
			
			if new_id not in used_ids:

				new_height = prt1.give_genes() * prt2.give_genes() #new height is a product of parent's passed height
				new_being = Being(new_id)	#make a new being
				new_being.height = round(new_height, 2) #set new beings height so it is not a default value
				new_being.generation = parent_gen + 1
				used_ids.add(new_id)
				break

		#print("Pairing successful")
		return new_being
	else:
		print("Beings not compatible")


def first_gen():
	first_gen = []

	for i in range(random.randint(10,15)):

		while True:
			new_id = random.randint(0,99999999)
			if new_id not in used_ids:
				new_being = Being(new_id)
				new_being.sex = "F"
				first_gen.append(new_being)
				used_ids.add(new_id)

				break

	for i in range(random.randint(10,15)):
		while True:
			new_id = random.randint(0,99999999)
			if new_id not in used_ids:
				new_being = Being(new_id)
				new_being.sex = "M"
				first_gen.append(new_being)
				used_ids.add(new_id)

				break
	return first_gen
'''
	for being in first_gen:
		print(being.gene())
	print("---")
	print(len(used_ids))
'''

def generate_pairs(list_of_objects):

	pairs = []
	males = []
	females = []
	x = 0

	for obj in list_of_objects:
		if obj.sex == "M":
			males.append(obj)
		if obj.sex == "F":
			females.append(obj)

	for i, male in enumerate(males):
	        current_pair = [male]
	        
	        if i < len(females):
	            current_pair.append(females[i])
	        pairs.append(current_pair)

	if len(females) > len(males):
		leftover_females = females[len(males):]
		for fem in leftover_females:
			pairs.append([fem])

	for pair in pairs:
		if len(pair) == 2:
			x+=1
			couples.append(pair)

	print(f"Generated {x} pairs")
	return pairs

def new_gen(list_of_pairs):
	new_gen = []
	x = 0
	y = []

	for pair in list_of_pairs:
		if len(pair) == 2:
			beta = get_beta_random()
			y.append(beta)
			for i in range(0, beta):
				offspring = mate(pair[0], pair[1])
				new_gen.append(offspring)
				x += 1
	print(f"Generated {x} offsprings")
	print(y)
	return new_gen

def find_parents(child):
	child_id = str(child.id)
	parents = []

	for couple in couples:		
		if (
			(child_id[:3] == str(couple[0].id)[:3]) or 
			(child_id[:3] == str(couple[1].id)[:3]) and 
			(child_id[-1] == str(couple[0].generation - 1))
		):
			parents.append(couple[0])
			parents.append(couple[1])
	return parents
#-------------------------------------------------------------------
def get_beta_random():

    raw_val = random.betavariate(1, 10)
    scaled_val = 1 + (raw_val * 14)
    
    return round(scaled_val)

#-------------------------------------------------------------------

if __name__ == "__main__":

	pairs = generate_pairs(first_gen())

	for pair in pairs:
		for individual in pair:
			print(individual.gene(), end=" ")
		print()

	print("-----------")

	new_gen = new_gen(pairs)
	for being in new_gen: print(being.gene())

	print("-------")
	for parent in find_parents(new_gen[0]):
		print(parent.gene())