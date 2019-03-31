'''
	FILE: Clause.py
	Class that represents a clause in propositional logic
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:30 Marzo 2019
	-------------------------------------------------------------------
'''

class Clause(object):
	
	def __init__(self):
		self.propositions = []

	# Set a new proposition to the clause
	def addProposition(self, proposition):
		if(self.getProposition(proposition.getName(), proposition.getNegativeValue()) == None)
			self.propositions.append(proposition)

	# Clear the list of propositions
	def clearList(self):
		clear(self.propositions)

	# Get the List of propositions
	def getPropositions(self):
		return self.propositions

	# Get a proposition of the clause
	def getProposition(name, negative):
		for p in propositions:
			if(p.getName() == name and p.isNegative(negative)):
				return p
		return None