'''
    FILE: Resoltion.py
    Algoritmo para aplicar el algoritmo de resulución en una lista de 
    clausulas
    -------------------------------------------------------------------
    Author: Carlos Antonio Mata Valdez
    Begin:12 Abril 2019
    -------------------------------------------------------------------
'''

class Resolution( object ):

	def __init__(self, clauses = []):
		self.clauses = clauses

	# Get the clauses of the class
	def getClauses(self):
		return self.clauses

	# Apply the principle of the resolution in all pair the clauses
	'''def applyResolution(self):
		new = []
		clauses = self.clauses
		while (True):
			for i in range(len(clauses)):
				for j in range(i + 1, len(clauses)):
					Ci = clauses[i]
					Cj = clauses[j]
					resolvents =  Ci.resolvent(Cj)
					if(self.hasEmptyClass(resolvents)):
						new = new + resolvents
						self.addClauses(new)
						return True
					new = new + resolvents
			if self.existClauses(new):
				return False
			#self.clauses = self.clauses + new
			self.addClauses(new)
			new = []'''

	# Apply the principle of the resolution in all pair the clauses
	def applyResolution(self):
		response = self.resolutionRecursive(self.clauses)
		self.addClauses(response[1])
		return response[0]

	# Resolution recursive 
	def resolutionRecursive(self, clauses):
		if(self.hasEmptyClass(clauses)):
			return [True, []]
		if(len(clauses) < 2):
			return [False, []]

		new = []
		for i in range(len(clauses)):
			for j in range(i + 1, len(clauses)):
				Ci = clauses[i]
				Cj = clauses[j]
				resolvents = Ci.resolvent(Cj)
				newList = self.getListWithoutClauses(clauses, Ci,Cj)
				newclauses = resolvents + newList
				new = new + resolvents

				response = self.resolutionRecursive(newclauses)
				
				if(response[0] == True):
					new = new + response[1]
					#new = resolvents + response[1]
					return [True, new]

		return [False, new]

	#Get a list without the clauses Ci and Cj
	def getListWithoutClauses(self, clauses, Ci, Cj):
		newList = []
		for k in range(len(clauses)):
			if(clauses[k] != Ci and clauses[k] != Cj):
				newList.append(clauses[k])
		return newList

	# Check if the clauses is inconsistent
	def isInconsistent(self):
		for clause in self.clauses:
			if(clause.isEmpty()):
				return True
		return False

	# Check if the clases in the parameters has the clause empty
	def hasEmptyClass(self, clauses):
		for clause in clauses:
			if(clause.isEmpty()):
				return True
		return False

	# Check if the newclauses exist in the clauses existents
	def existClauses(self, newclauses):
		for newclause in newclauses:
			if(not self.existClause(newclause)):
				return False
		return True

	def addClauses(self, newclauses):
		for newclause in newclauses:
			if(not self.existClause(newclause)):
				self.clauses.append(newclause)

	# Check if th
	def existClause(self, newclause):
		for clause in self.clauses:
			if(clause.isEquals(newclause)):
				return True
		return False

	# Return the max id number of the clauses
	def getMaxId(self):
		maxId = 0
		for clause in self.clauses:
			if(clause.getId() > maxId):
				maxId = clause.getId()

		return maxId
