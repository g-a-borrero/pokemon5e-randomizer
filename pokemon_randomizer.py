import random
import copy
import json

class Pokemon:
	with open("meta.json") as f:
		json_file = json.load(f)
	pokemon = json_file["pokemon"]
	abilities = json_file["abilities"]
	moves_list = json_file["moves"]
	def __init__(self):
		self.name = Pokemon.pokemon[random.randint(0, len(Pokemon.pokemon)-1)]
		self.ability = Pokemon.abilities[random.randint(0, len(Pokemon.abilities)-1)]
		self.moves = {"Starting": [],"2": [], "6": [], "10": [], "14": [], "18": []}
		temp_moves = copy.deepcopy(Pokemon.moves_list)
		for i in ["Starting", "Starting", "2", "2", "6", "6", "6", "6", "10", "10", "10", "14", "14", "18"]:
			self.moves[i].append(temp_moves.pop(random.randint(0, len(temp_moves)-1)))
	def __str__(self):
		return("Pokemon: " + self.name + "\nAbility: " + self.ability + "\n**Moves**\n" + "\n".join([k + ": " + ", ".join(v) for k,v in self.moves.items()]))
	def get_pokemon(self):
		return(self.name)
	def get_moves(self):
		return("\n".join([k + ": " + ", ".join(v) for k,v in self.moves.items()]))
	def get_ability(self):
		return(self.ability)

if __name__ == "__main__":
	print(Pokemon())
