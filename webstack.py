import sys
from win import MainW


from PyQt4 import QtCore, QtGui

def main():
	app = QtGui.QApplication(sys.argv)
	
	window = QtGui.QMainWindow()
	
	MainWin = MainW.create()
	MainWin.setupUi(window)
	
	window.show()
	
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()
