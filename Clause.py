'''
	FILE: Clause.py
	Class that represents a clause in propositional logic
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:30 Marzo 2019
	-------------------------------------------------------------------
'''

class Clause(object):
	
	def __init__(self, id = 0, resultado = "Hipotesis"):
		self.id = id
		self.propositions = []
		self.resultado = resultado

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

	# Set the value of the member resultado
	def setResultado(self, resultado):
		self.resultado = resultado

	# Get the value of the member resultado
	def getResultado(self):
		return self.resultado

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

	#Apply the principle of the resolution with one proposition
	#and return a new clause
	'''def resolvent(self, proposition):
		newclause = Clause()
		for p in self.propositions:
			print(proposition.toString() + ":" +p.toString())
			if(not proposition.isOpposite(p)):
				newclause.addProposition(p)
		return newclause'''

	def resolvent(self, otherclause, maxid):
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

				newclause.setId(maxid)
				newclause.setResultado("Resolucion de "+ 
											str(self.getId()) + 
											" y " + 
											str(otherclause.getId()))
				resolvents.append(newclause)
				maxid = maxid + 1

		#for otherp in otherclause.getPropositions():
		#	if(not self.haveOpposite(otherp)):
		#		newclause.addProposition(otherp)
		return resolvents, maxid





