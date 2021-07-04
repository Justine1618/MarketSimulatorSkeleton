class Inventory:
	currentLevel = 0
	def AddToInventory(self):
		currentLevel += 1
	def RemoveFromInventory(self):
		#want to add a check to see if inventory is empyt first
		currentLevel -= 1
