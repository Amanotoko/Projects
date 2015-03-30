#=============================================================================
#
# Author: Kai He - khe004@ucr.edu
#
# VSCLAB
#
# Last modified: 2015-03-28 17:27
#
# Filename: product_inventory.py
#
# Description: 
# **Product Inventory Project** - 
#	Create an application which manages an inventory of products. 
#	Create a product class which has a price, id, and quantity on hand. 
#	Then create an *inventory* class which keeps track of various products and can sum up the inventory value.
#
#=============================================================================

class Product:
	def __init__(self, pID, name, price, quantity):
		#Initialization
		self.pID = pID
		self.name = name
		self.price = price
		self.quantity = quantity

	def updatePrice(self, new_price):
		#update price
		if new_price > 0:
			self.price = new_price
		else:
			print "Error! Cannot update price to lower than or equal to zero."
	
	def updateQuantity(self, new_quantity):
		#update quantity
		if new_quantity >= 0:
			self.quantity = new_quantity
		else:
			print "Error! Cannot update quantity to lower than zero."
	
	def getQuantity(self):
		#get quantity
		return self.quantity
	
	def getPrice(self):
		#get price
		return self.price
	
	def viewProduct(self):
		#display the product's information
		print "Product ID: " + str(self.pID)
		print "Name: " + self.name
		print "Price: " + str(self.price)
		print "Quantity: " + str(self.quantity) + "\n"
	
class Inventory:
	def __init__(self):
		#Initialization
		self.listProduct=[]
		totalValue = 0
	
	def addProduct(self, product):
		#add new product
		self.listProduct.append(product)

	def removeProduct(self, product):
		#remove product
		self.listProduct.remove(product)
	
	def viewInventory(self):
		print "Inventory:"
		for p in self.listProduct:
			p.viewProduct()
	
	def viewValue(self):
		print "Inventory value:"
		totalValue = 0
		for p in self.listProduct:
			value = p.price * p.quantity
			print p.name + ":" + str(value)
			totalValue += value		
		print "Total value: " + str(totalValue)


if __name__ == '__main__':
	apple = Product(1, "apple", 2.20, 50)
	
	#test getQuantity and updateQuantity
	print apple.getQuantity()
	apple.updateQuantity(100)
	print apple.getQuantity()

	#test getPrice and updatePrice
	print apple.getPrice()
	apple.updatePrice(1.80)
	print apple.getPrice()
	
	#test viewProduct
	apple.viewProduct()
	
	pear = Product(2, "pear", 3.1, 30)
	banana = Product(3, "banana", 0.7, 150)

	inv = Inventory()
	inv.addProduct(apple)
	inv.addProduct(pear)
	inv.addProduct(banana)
	inv.viewInventory()	
	inv.viewValue()
