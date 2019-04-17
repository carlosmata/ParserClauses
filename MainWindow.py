from MainWindow_ui import *
from TableModel import TableModel
from Parser import Parser
from Resolution import Resolution
import sys

class MainWindow(QtWidgets.QDialog, Ui_Dialog):
	def __init__(self, parent=None):
		self.parser = Parser()
		QtWidgets.QDialog.__init__(self, parent)
		self.setupUi(self)
		self.connectEvents()
		self.iniTable()

	#Initialize the table process
	def iniTable(self):
		header = ['Paso', 'Clausula', 'Resultado']
		data = []
		table_model = TableModel(self, data, header)
		self.processTable.setModel(table_model)
		self.processTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

	def setDataTableProgres(self, data):
		header = ['Paso', 'Clausula', 'Resultado']
		table_model = TableModel(self, data, header)
		self.processTable.setModel(table_model)
		self.processTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

	#Conect the events of the buttons
	def connectEvents(self):
		self.borrarBtn.clicked.connect(self.clear)
		self.demostrarBtn.clicked.connect(self.runProcess)
		self.erroresBtn.clicked.connect(self.showErrors)

	def showErrors(self):
		errores = ""
		for error in self.parser.errors:
			errores = errores + error + "\n"
		
		QtWidgets.QMessageBox.about(self, 
						"Errores", 
						errores)

	#Clicked event for demostrarBtn
	def runProcess(self):
		self.erroresBtn.setVisible(False)
		self.resultadoLbl.setText("")
		text = self.clausulasText.toPlainText()
		clauses = self.parser.parse(text)
		
		data = []
		inconsistent = False
		
		if(clauses != None):
			#------------TODO apply resolution
			resolution = Resolution(clauses)
			inconsistent = resolution.applyResolution()
			clauses = resolution.getClauses()
			#-------------------------------------------

			iterator = 1
			for clause in clauses:
				clause.setId(iterator)
				data.append((clause.getId(), clause.toString(), clause.getResultado()))
				iterator = iterator + 1

			if(inconsistent):
				self.resultadoLbl.setText("Es incosistente")
			else: 
				self.resultadoLbl.setText("Es consistente")
		
		if(len(self.parser.errors) > 0):
			self.erroresBtn.setVisible(True)
			self.showErrors()
			self.resultadoLbl.setText("Error en entrada")

		self.setDataTableProgres(data)

	#Clicked event for borrarBtn
	def clear(self):
		self.clausulasText.setPlainText("")
		self.processTable.clearSpans()
		self.progressBar.setProperty("value", 0)
		self.resultadoLbl.setText(" Sin Entradas")
		self.clausulasLbl.setText("   ")
		self.erroresBtn.setVisible(False)
		self.iniTable()

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = MainWindow()
	ui.show()
	sys.exit(app.exec_())