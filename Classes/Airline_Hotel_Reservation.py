#=============================================================================
#
# Author: Kai He - khe004@ucr.edu
#
# VSCLAB
#
# Last modified: 2015-03-29 21:07
#
# Filename: Airline_Hotel_Reservation.py
#
# Description: 
#	Create a reservation system which books airline seats or hotel rooms. 
#	It charges various rates for particular sections of the plane or hotel. 
#	Example, first class is going to cost more than coach. 
#	Hotel rooms have penthouse suites which cost more. 
#	Keep track of when rooms will be available and can be scheduled.
#
#=============================================================================

class Seat:
	def __init__(self):
		self.avail = True
		self.name = ""
	
	def bookSeat(self, name):
		if self.avail == True:
			self.avail = False
			self.name = name
			return True
		else:
			print "This seat is not available."
			return False

	def cancelSeat(self):
		self.avail = True
		self.name = ""

class SeatSection:
	def __init__(self, section, num, price):
		#initializtion
		self.section = section
		self.num = num
		self.availNum = num
		self.price = price
		self.seatlist = []
		#self.seatlist = [Seat()] * self.num # doesn't work because it called Seat() once and made self.num copies
		self.seatlist = [Seat() for n in range(self.num)] # called Seat() self.num times
		#for i in range(self.num):
		#	self.seatlist.append(Seat()) # can work
	
	def updateNum(self, new_num):
		#update number
		if new_num >= 0:
			self.num = new_num
			self.availNum = num
			#self.seatlist = [s] * self.num
		else:
			print "Error! Cannot update seat number to negative one"
	
	def updatePrice(self, new_price):
		#update price
		if new_price >= 0:
			self.price = new_price
		else:
			print "Error! Cannot update seat price to negative one"
	
	def getNumber(self):
		return self.num

	def getAvailNum(self):	
		return self.availNum

	def getPrice(self):
		return self.price

	def book(self, name, sID):
		if sID < self.num:
			if self.seatlist[sID].bookSeat(name):
				self.availNum -= 1
		else:
			print "Error! This seat ID is out of range!"
	
	def cancel(self, sID):
		if sID < self.num:
			self.seatlist[sID].cancelSeat()
			self.availNum += 1
		else:
			print "Error! This seat ID is out of range!"
		
	def viewSection(self):
		print "Section: " + self.section
		print "Total number: " + str(self.num)
		print "Available number: " + str(self.availNum)
		print "Price: " + str(self.price) + "\n"
	
	def viewStatus(self):
		for idx in range(self.num):
			if self.seatlist[idx].avail == False:
				print "Seat ID: " + str(idx)
				print "Customer Name: " + self.seatlist[idx].name + "\n"

class AirlineSeat:
	def __init__(self):
		self.sectionlist = []

	def addSection(self, section):
		self.sectionlist.append(section)
	
	def removeSection(self, section):
		self.sectionlist.remove(section)

	def viewStatus(self):
		for sec in self.sectionlist:
			sec.viewSection()
			sec.viewStatus()
	
	def book(self, name, sectionID, seatID):
		self.sectionlist[sectionID].book(name, seatID)

	def cancel(self, sectionID, seatID):
		self.sectionlist[sectionID].cancel(seatID)
		

if __name__ == '__main__':
	ss1 = SeatSection("Top", 10, 1000.00)
	ss2 = SeatSection("Eco", 100, 400.00)

	Air1 = AirlineSeat()
	Air1.addSection(ss1)
	Air1.addSection(ss2)

	Air1.viewStatus()

	Air1.book("John", 0, 2)
	Air1.book("Mike", 0, 3)
	Air1.book("Amy", 1, 3)
	Air1.book("Lucy", 1, 33)

	Air1.viewStatus()
	
	Air1.cancel(0,2)

	Air1.viewStatus()
	
