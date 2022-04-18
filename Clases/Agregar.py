from PyQt5 import QtCore, QtWidgets
from View.Agregar import Ui_MainWindow
from DB.Connection import Insertar_Fecha,Seleccion_Fechas
from Clases.Compartido import ComBoxs
class Agregar(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,fecha = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.Window)
        #Configuramos el QDateEdit
        fecha = fecha.split('-')
        tiempo = QtCore.QDateTime(int(fecha[0]),int(fecha[1]),int(fecha[2]),9,30)
        self.Fecha.setDateTime(tiempo)
        #Configuramo el ComBoxs
        self.Horario.addItems(ComBoxs())
        #Boton Para salir
        self.btn_Salir.clicked.connect(self.Regresar)
        #Boton de Insertar
        self.btn_Agregar.clicked.connect(self.Insertar_Datos)

    #Metodo para regresar a la ventan principla
    def Regresar(self):
        self.parent().show()
        self.close()

    #Verificamos que se Hayan llenado los campos  
    def Llenado(self):
        Fecha = self.Fecha.date() 
        Fecha = str(Fecha.toPyDate())
        Hora = self.Hora.time()
        Hora= str(Hora.toPyTime())
        Hors = self.Horario.currentText()
        Des =  self.Des.toPlainText()
        errores = 0
        if Hora == "00:00:00":
            errores += 1
        if Des == "":
            errores += 1
        return (errores == 0)
    
    #Limpiamos los datos
    def Limpiar(self):
        Fecha = self.Fecha.clear() 
        Hora = self.Horario.clear()
        Des =  self.Des.clear()

    def Insertar_Datos(self):
        Fecha = self.Fecha.date() 
        Fecha = str(Fecha.toPyDate())
        Hora = self.Hora.time()
        Hora= str(Hora.toPyTime())
        Hors = self.Horario.currentText()
        Des = self.Des.toPlainText()
    
        #Comprobamos el llenado de datos
        if self.Llenado():
            datos = (Fecha,Hora,Hors,Des)
            if Insertar_Fecha(datos):
                self.Limpiar()
                self.parent().show()
                self.close()



