#Importamos nuestra interfaz
from View.Calendario import Ui_MainWindow
#Importamos la Libreria a utilizar
from PyQt5 import QtCore,QtWidgets
#Importamos el query
from DB.Connection import Seleccion_Fechas,Eliminar_Evento
class Calendario(QtWidgets.QMainWindow,Ui_MainWindow):
    #Inicialiamos la clase 
    def __init__(self):
        super().__init__()
        #Para que se pueda mostrar la ventana
        self.setupUi(self)
        #Boton de Agregar
        self.btn_Agregar.clicked.connect(self.Abrir_Agregar)
        self.btn_Modificar.clicked.connect(self.Abrir_Modificar)
        #Configuramos la fecha
        self.fecha = "2022-04-03"
        self.Calendario.selectionChanged.connect(self.Obtener_Fecha)
        #!Configuramos la tabla        
        self.Confugurar_Tabla()
        self.Datos_Tabla(Seleccion_Fechas())
        #boton para eliminar
        self.btn_Eliminar.clicked.connect(self.Elimiar_Fecha)
        #Boton para actualizar
        self.btn_Actualizar.clicked.connect(lambda: self.Datos_Tabla(Seleccion_Fechas()))
    #Metodo para abrir la ventana de Agregar
    def Abrir_Agregar(self):
        self.hide()
        from Clases.Agregar import Agregar
        window = Agregar(self,self.fecha)
        window.show()
    def Abrir_Modificar(self):
        from Clases.Modificar import Modificar
        selected_row = self.Table.selectedItems()
        if selected_row:
            book_id = int(selected_row[0].text())
            self.hide()
            window = Modificar(self, book_id)
            window.show()
        #Limpiamos la columna seleccinada
        self.Table.clearSelection()
        
    #Obtenemos la fecha del calendario 
    def Obtener_Fecha(self):
        fecha_Seleccionada = self.Calendario.selectedDate()
        fecha_String = str(fecha_Seleccionada.toPyDate())
        self.fecha = fecha_String

    #!Configuramos la tabla
    def Confugurar_Tabla(self):
        columnas = ("Id","Fecha","Hora","Horario","Descripcion")
        #Numero de columnas
        self.Table.setColumnCount(len(columnas))
        #Nombre de las columnas
        self.Table.setHorizontalHeaderLabels(columnas)
        #Metodo para poder seleccionar
        self.Table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        #Tamaño de las columnas 
        self.Table.setColumnWidth(0,50)
        self.Table.setColumnWidth(1,80)
        self.Table.setColumnWidth(2,60)
        self.Table.setColumnWidth(3,60)
        self.Table.setColumnWidth(4,190)
        self.Table.setShowGrid(True)
        #Hacemos mas anchas las filas
        self.Table.verticalHeader().setDefaultSectionSize(70)
    #Datos de la Tabla
    def Datos_Tabla(self,data):
        #Configuramos las filas
        self.Table.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for(index_cell, cell) in enumerate(row):
                self.Table.setItem(index_row, index_cell,QtWidgets.QTableWidgetItem(str(cell)))
    
    def Elimiar_Fecha(self):
        fila = self.Table.selectedItems()
        if fila:
            id_fila = int(fila[0].text())
            if Eliminar_Evento(id_fila):
                self.Datos_Tabla(Seleccion_Fechas())
    