'''
	FILE: Definition.py
	Class that represents a lexical definition 
	-------------------------------------------------------------------
	Author: Carlos Antonio Mata Valdez
	Begin:28 Marzo 2019
	-------------------------------------------------------------------
'''
import re

class Definition( object ):
	
	def __init__(self, name , expresion):
		self._name = name
		self._expresion = expresion

	# Get the name of Token
	def getName( self ):
		return self._name
	
	# Get the expresion of rule
	def getExpresion( self ):
		return self._expresion
	
	# Set the expresion of rule
	def setExpresion( self, expresion ):
		self._expresion = expresion
	
	# Match the text with the definition
	def match( self, text ):
		cads = re.findall(self._expresion, text)
		
		if(cads != None and len(cads) > 0 and cads[0] == text): 
			return True
		return False

