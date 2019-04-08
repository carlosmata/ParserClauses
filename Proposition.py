'''
	FILE: Proposition.py
	Class that represents a proposition in propositional logic
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:30 Marzo 2019
	-------------------------------------------------------------------
'''

class Proposition(object):
	
	def __init__(self, name, negative = False):
		self.name = name
		self.negative = negative

	# Get the name of the proposition
	def getName(self):
		return self.name

	# Set the negative value of the proposition
	def setNegative(self, negative):
		self.negative = negative

	# Show if the proposition is negative or not
	def isNegative(self, negative):
		return (self.negative == negative)

	# GEt the value of the negative attribute
	def getNegativeValue(self):
		return self.negative

	def toString(self):
		p = ""
		if(self.negative):
			p = p + "~"
		return p + self.name