'''
	FILE: Clause.py
	Class that represents a clause in propositional logic
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:30 Marzo 2019
	-------------------------------------------------------------------
'''

class Clause(object):
	
	def __init__(self, resultado = "Hipotesis"):
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

	def toString(self):
		c = "{"
		for prop in self.propositions:
			c = c + prop.toString() + ","

		return c[:-1] + "}"

