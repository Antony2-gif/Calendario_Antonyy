#Libreia a utilizar
from PyQt5 import QtWidgets
from Clases.Calendar import Calendario

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana = Calendario()
    ventana.show()
    app.exec_()
