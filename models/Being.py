import random

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
#BOLD = "\033[1m"
RESET = "\033[0m" # Always use this to stop the color!

class Being:

	def __init__(self, id_num):
		self.id = id_num
		self.height = round(random.uniform(0.5, 1.5), 2) #default random values
		self.sex = random.choice(['M', 'F']) #default random values
		self.generation = 0
		#self.parents = mum + dad

	def gene(self):
		gene = (
			f"{RED}{self.id:0>8}{RESET}"
			f"{GREEN}{self.sex}{RESET}"
			f"{YELLOW}{self.height:0<4}{RESET}"
			f"{BLUE}{self.generation}{RESET}"
			)
		return gene #its just height and sex in one string

	def give_genes(self):
		mutation = random.uniform(0.9, 1.1)
		pass_height = self.height * mutation  #height that a being gives is similar to its own

		return pass_height


if __name__ == "__main__":
	being = Being(1)
	print(being.gene())