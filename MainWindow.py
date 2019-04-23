from MainWindow_ui import *
from TableModel import TableModel
from Parser import Parser
from Resolution import Resolution
import sys

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		self.parser = Parser()
		QtWidgets.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.connectEvents()
		self.iniTable()

	#Initialize the table process
	def iniTable(self):
		header = ['Paso', 'Clausula', 'Resultado']
		data = []
		table_model = TableModel(self, data, header)
		self.processTable.setModel(table_model)
		self.processTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

	def setDataTableProgres(self, data):
		header = ['Paso', 'Clausula', 'Resultado']
		table_model = TableModel(self, data, header)
		self.processTable.setModel(table_model)
		self.processTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

	#Conect the events of the buttons
	def connectEvents(self):
		self.borrarBtn.clicked.connect(self.clear)
		self.demostrarBtn.clicked.connect(self.runProcess)
		self.erroresBtn.clicked.connect(self.showErrors)

		self.actionAbrir_archivo.triggered.connect(self.openFileNameDialog)
		self.actionCerrar.triggered.connect(self.close)
		self.actionDemostrar.triggered.connect(self.runProcess)
		self.actionBorrar.triggered.connect(self.clear)


	def close(self):
		self.close()

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

	#Open a file dialog
	def openFileNameDialog(self):
		options = QtWidgets.QFileDialog.Options()
		options |= QtWidgets.QFileDialog.DontUseNativeDialog
		fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QtWidgets.QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
		if fileName:
			self.clear()
			file = open(fileName, 'r')
			
			with file:
				text = file.read()
				self.clausulasText.setPlainText(text)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	ui = MainWindow()
	ui.show()
	sys.exit(app.exec_())