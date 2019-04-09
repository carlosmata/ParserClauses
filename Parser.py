'''
    FILE: Parser.py
    Analizador sintactivo de la calculadora 
    -------------------------------------------------------------------
    Author: Carlos Antonio Mata Valdez
    Begin:28 Marzo 2019
    -------------------------------------------------------------------
'''
from Definition import Definition as Definition
from Lex import Lex as Lex
from Proposition import Proposition
from Clause import Clause

class Parser( object ):

	def __init__(self):
		self.errors = []
		self._tokens = None
		self._currenttoken = None
		self.definitions = [
							Definition("negativo", "[~]"),
							Definition("coma", "[,]"),
							Definition("etiqueta", "[a-zA-Z][a-zA-Z0-9_]*"),
							Definition("llaveizq", "[{]"),
							Definition("llaveder", "[}]")
							]
		self.definitions.append(Definition("enter", "\\n"))
		self.definitions.append(Definition("space", " "))
		self.definitions.append(Definition("tab", "\\t"))
		self.lexer = Lex(self.definitions)

	# Show error and out of program
	def errorparse(self):
		if self._currenttoken != None:
			self.errors.append("Existe un error en la sintaxis: token: " + 
					self._currenttoken.getName() + 
					" valor: " + 
					self._currenttoken.getValue())
		else:
			self.errors.append("Existe un error en la sintaxis: incompleta o erronea")
		return None

	# Match the current token with the name sender
	def match(self, nametoken):
		if self._currenttoken != None and self._currenttoken.getName() == nametoken:
			if(len(self._tokens) > 0):
				self._currenttoken = self._tokens.pop(0)
			else:
				self._currenttoken = None
			return True
		else:
			self.errorparse()
			return False

	# Begin the parse
	def parse( self, text ):
		del self.errors[:]
		if(text != None and text != ""):
			self._tokens = self.lexer.obtainTokens( text )

			if(self._tokens != None):
			#Aplicamos reglas de gramatica
				self._currenttoken = self._tokens.pop(0)
				clauses = self.S([])

				if(len(self._tokens) != 0): #No se terminaron los tokens-->error sintactico
					self.errors.append("Error en sintaxis, no se consumieron todos los tokens")
					return []
				else:
					return clauses
			else:
				self.errors.append("Existe un error en la entrada, no se reconocen algunos símbolos: Error léxico")
				return []
		else:
			self.errors.append("Entrada vacía")
			return []

#-----------------------Gramatica------------------------------------------
	#Rule S -> C Cp
	def S( self , listClauses):
		return self.Cp( self.C(listClauses) )

	#Rule Cp -> coma S | Epsilon
	def Cp( self, listClauses):
		if self._currenttoken == None:
			return listClauses
		elif self._currenttoken.getName() == "coma":
			self.match("coma")
			return self.S(listClauses)
		else:
			self.errorparse()
			return []

	#Rule C -> llaveIzq A llaveDer
	#Return puede devolver error
	def C( self, listClauses):
		if self._currenttoken == None:
			self.errorparse()
			return []

		elif self._currenttoken.getName() == "llaveizq":
			self.match("llaveizq")
			clause = Clause()
			res = self.A(clause)
			if(res != None and self.match("llaveder") ):
				listClauses.append(clause)
			return listClauses
		else:
			self.errorparse()
			return []

	#Rule A -> etiqueta Ap | negacion etiqueta Ap
	def A( self, clause ):
		if self._currenttoken == None:
			return self.errorparse()

		#Preposicion normal
		elif self._currenttoken.getName() == "etiqueta":
			name = self._currenttoken.getValue()
			self.match("etiqueta")
			clause.addProposition(Proposition(name))
			return self.Ap(clause)
		#Preposicion con negacion
		elif self._currenttoken.getName() == "negativo":
			self.match("negativo")
			if(self._currenttoken.getName() == "etiqueta"):
				name = self._currenttoken.getValue()
				proposition = Proposition(name)
				clause.addProposition(Proposition(name, True))

			self.match("etiqueta")
			return self.Ap(clause)
		else:
			return self.errorparse()

	#Rule Ap -> coma A | Epsilon
	def Ap( self, clause):
		if self._currenttoken == None:
			return clause
		elif self._currenttoken.getName() == "coma":
			self.match("coma")
			return self.A(clause)
		else:
			return clause
#-------------------------------------------------------------------

