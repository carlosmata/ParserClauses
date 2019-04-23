'''
	FILE: Clause.py
	Class that represents a clause in propositional logic
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:30 Marzo 2019
	-------------------------------------------------------------------
'''

class Clause(object):
	
	def __init__(self, id = 0):
		self.id = id
		self.propositions = []
		self.used = False

		#test
		self.parent1 = None
		self.parent2 = None

	def hadUsed(self):
		return self.used

	def setUsed(self, value):
		self.used = value

	#test
	def addParents(self, parent1,  parent2):
		self.parent1 = parent1
		self.parent2 = parent2

	# Set a new proposition to the clause
	def addProposition(self, proposition):
		if(self.getProposition(proposition.getName(), proposition.getNegativeValue()) == None):
			self.propositions.append(proposition)

	# Clear the list of propositions
	def clearList(self):
		clear(self.propositions)

	# Get the List of propositions
	def getPropositions(self):
		return self.propositions

	# Get a proposition of the clause
	def getProposition(self, name, negative):
		for p in self.propositions:
			if(p.getName() == name and p.isNegative(negative)):
				return p
		return None

	# Get the value of the member resultado
	def getResultado(self):
		res = "Hipótesis"
		if (self.parent1 != None and self.parent2 != None):
			res = "Resolución " + str(self.parent1.getId()) + " y " + str(self.parent2.getId())
		return res

	# Get the Id of the Clause
	def getId(self):
		return self.id

	# Set a new Id
	def setId(self, id):
		self.id = id

	# Transform the clause in a string
	def toString(self):
		if(len(self.propositions) == 0):
			return "{ [] }"

		c = "{"
		for prop in self.propositions:
			c = c + prop.toString() + ","

		return c[:-1] + "}"

	# Check if the clase is empty
	def isEmpty(self):
		if(len(self.propositions) == 0):
			return True

	# Check if the clause is equal to another clause
	def isEquals(self, otherclause):
		if(len(self.propositions) != len(otherclause.getPropositions())):
			return False

		for proposition in otherclause.getPropositions():
			if(not self.haveProposition(proposition)):
				return False
		return True

	#Check if the clause has a proposition
	def haveProposition(self, proposition):
		for p in self.propositions:
			if(p.isEqual(proposition)):
				return True
		return False

	#Check if the clause has a opposite proposition
	def haveOpposite(self, proposition):
		for p in self.propositions:
			if(p.isOpposite(proposition)):
				return True
		return False

	def resolvent(self, otherclause):
		resolvents = []

		for p in self.getPropositions():
			if(otherclause.haveOpposite(p)):
				newclause = Clause()

				for p1 in self.getPropositions():
					if(p1.getName() != p.getName()):
						newclause.addProposition(p1)
				for p2 in otherclause.getPropositions():
					if(p2.getName() != p.getName()):
						newclause.addProposition(p2)

				newclause.addParents(self, otherclause)
				resolvents.append(newclause)

		return resolvents





