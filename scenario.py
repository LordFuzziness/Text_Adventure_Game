from enum import Enum
import utility

# - By William Lim

class ScenarioIdentity:
	def __init__(self) -> None:
		self.value = 0

class ConType(Enum):
	EQUAL = 0
	LESS = 1
	GREATER = 2
	HAS_ITEM = 3
	GREATER_OR_EQUAL = 4
	LESS_OR_EQUAL = 5
	AND = 6
	OR = 7

class ConVal:
	def __init__(self, value) -> None:
		self.value = value

class Constraint:
	def __init__(self, player, item1:ConVal, constraint:ConType, item2:ConVal = None) -> None:
		"""
		item1 and item2 should be lists that contain only one item each
		"""
		self.type = constraint
		self.item1 = item1
		self.item2 = item2
		self.player = player
	
	def check(self) -> bool:
		match self.type:
			case ConType.EQUAL:
				if self.item1.value == self.item2.value:
					return True
				else:
					return False
			case ConType.GREATER_OR_EQUAL:
				if self.item1.value >= self.item2.value:
					return True
				else:
					return False
			case ConType.LESS_OR_EQUAL:
				if self.item1.value <= self.item2.value:
					return True
				else:
					return False
			case ConType.HAS_ITEM:
				if self.item1.value in self.player.inventory:
					return True
				else:
					return False
			case ConType.LESS:
				if self.item1.value < self.item2.value:
					return True
				else:
					return False
			case ConType.GREATER:
				if self.item1.value > self.item2.value:
					return True
				else:
					return False
			case ConType.AND:
				if self.item1.check() & self.item2.check():
					return True
				else:
					return False
			case ConType.OR:
				if self.item1.check() | self.item2.check():
					return True
				else:
					return False

class Scenario:
	def __init__(self, identifier:ScenarioIdentity, player_instance, prompt:str, actions:dict = {}, substitutions:dict = {}, triggers = []) -> None:
		"""
		The actions dictionary keys are what the player inputs and the values are the next scenario they will go to.

		for substitutions wrap {} arround the key you want to substitute in the prompt and then make the word inside the {}
		a key in your substitutions dictionary. the value should be the word you are substituting
		"""
		self.prompt = prompt
		self.actions = actions
		self.previous = None
		for key in self.actions.keys():
			self.actions[key].previous = self
		self.substitutions = substitutions
		self.player_instance = player_instance
		self.constraints = {}
		self.reward_constraints = {}
		self.rewards = {}
		self.triggers = triggers
		self.id = identifier.value
		identifier.value += 1

	def add_trigger(self, trigger):
		self.triggers.append(trigger)

	def set_action(self, action:str, scenario):
		self.actions[action] = scenario
		self.actions[action].previous = self

	def delete_action(self, action:str):
		del self.actions[action]

	def set_constraint(self, constraint, action):
		self.constraints[action] = constraint

	def set_reward_constraint(self, constraint, reward:str):
		self.reward_constraints[reward] = constraint

	def add_reward(self, reward:str, item):
		if reward not in self.rewards.keys():
			self.rewards[reward] = [item]
		else:
			self.rewards[reward].append(item)

	def delete_reward(self, reward:str):
		del self.rewards[reward]

	def run(self):
		utility.clear_screen()
		for trigger in self.triggers:
			trigger()
		for key, val in self.rewards.items():
			if (self.reward_constraints[key].check() if key in self.reward_constraints.keys() else True):
				self.player_instance.inventory.extend(val)

		prompt_msg = self.prompt
		for key, val in self.substitutions.items():
			prompt_msg = prompt_msg.replace("{"+ key +"}", val)\
		
		print(f"{prompt_msg}\n")
		print(f"Option:")
		for key in self.actions.keys():
			if (self.constraints[key].check() if key in self.constraints.keys() else True):
				print(f"{key}")
		print(self.player_instance.get_stats())
		player_input = ""
		while True:
			player_input = input(f"{self.player_instance.name}:").lower()
			if player_input not in self.actions.keys() & self.constraints[player_input].check() if player_input in self.constraints.keys() else False:
				print("That is not a valid action, please try again.")
			else:
				break
		self.actions[player_input].run()