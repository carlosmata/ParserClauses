'''
	FILE: Lex.py
	Lexical analizer 
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:28 Marzo 2019
	-------------------------------------------------------------------
'''

from Token import Token as Token

class Lex( object ):
	
	def __init__(self, definitions):
		self.rules = definitions
		self.errors = []
	
	# Obtain a list of tokens of text
	def obtainTokens(self, text ):
		tokens = []
		begin = 0
		ends = len(text)
		rule = None
		band = False

		#get the tokens at the text 
		while(band != True):
			# find the next string
			substring = text[begin: ends]
			
			rule = self.getDefinition( substring )
			if rule != None:
				if (rule.getName() != "space" and 
					rule.getName() != "enter" and
					rule.getName() != "tab"): 
					tokens.append(Token(rule, substring))
				begin = ends
				ends = len(text)
				if begin == len(text): 
					break 		# se acabo la cadena
			else:
				ends = ends - 1
			
			if ends == begin: #no se encontro token
				self.errors.append("No se encontro definicion para " + substring)
				band = True
		
		if(band == True): # no se encontro definicion
			tokens = None

		return tokens
	
	# Obtain of rule that match with the expresion
	def getDefinition(self, string ):
		for rule in self.rules: 
			if rule.match(string): 
				return rule
		return None

