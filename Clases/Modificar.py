from doctest import debug_script
from PyQt5 import QtWidgets,QtCore
from View.Modificar import Ui_MainWindow
from DB.Connection import Insertar_Fecha,Seleccionar_Id,Actualizar_Fecha
from Clases.Compartido import ComBoxs

class Modificar(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None,id=None):
        self.id = id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Window)
        #Mostramos los datos en la interfaz
        self.Datos()
        #Configuramo el ComBoxs
        self.Horario.addItems(ComBoxs())
        #Boton Para salir
        self.btn_Salir.clicked.connect(self.Regresar)
        #Boton de Insertar
        self.btn_Agregar.clicked.connect(self.Modificar_Fecha)


    def Datos(self):
        data = Seleccionar_Id(self.id)
        fecha = data[1].split('-')
        tiempo = QtCore.QDateTime(int(fecha[0]),int(fecha[1]),int(fecha[2]),9,30)
        self.Fecha.setDateTime(tiempo)
        self.Des.setText(data[4])
        #Modificarmps el QTImeEdit
        hora = data[2].split(":")
        time = QtCore.QTime()
        time.setHMS(int(hora[0]),int(hora[1]),int(hora[2]))
        self.Hora.setTime(time)

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

    def Modificar_Fecha(self):
        Fecha = self.Fecha.date() 
        Fecha = str(Fecha.toPyDate())
        Hora = self.Hora.time()
        Hora= str(Hora.toPyTime())
        Hors = self.Horario.currentText()
        Des = self.Des.toPlainText()
    
        #Comprobamos el llenado de datos
        if self.Llenado():
            datos = (Fecha,Hora,Hors,Des)
            if Actualizar_Fecha(self.id,datos):
                self.Limpiar()

