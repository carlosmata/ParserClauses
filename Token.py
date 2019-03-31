'''
	FILE: Token.py
	Class that represents a token in a analizer lexical 
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:28 Marzo 2019
	-------------------------------------------------------------------
'''

class Token(object):
	
	def __init__(self, expresion, value):
		self._value = value
		self._rule = expresion

	# Get the name of Token
	def getName(self):
		return self._rule.getName()
	
	# Get the value of Token
	def getValue(self):
		return self._value
	
	# Set the value of Token
	def setValue(self, value ):
		self._value = value

	# Say if the sender name is equals to the name of the token
	def Equals(self, tokenname ):
		return (tokenname ==  self.GetName())
