from Inventory import Inventory

class MarketInterface:
	buyInventory = Inventory()
	sellInventory = Inventory()
	moneyInventory = Inventory()
	requestedLevel = 5
	yesterdaysPrice = 10 #I don't really want to set this value to zero
	wasOrderCompleted = False
	def PlaceBuyOrder(self):
		pass
	def PlaceSellOrder(self):
		pass
	def AdjustPrice(self):
		pass
