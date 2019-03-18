from ventana import *
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from Detector import passImg
#pyuic5 -x ventana.ui -o ventana_ui.py
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.fileName = ""
        self.setupUi(self)
        self.Seleccionar.clicked.connect(self.seleccionar)
        self.label_path.setText("'No has seleccionado un archivo aún'")
        self.pushButton.clicked.connect(self.analizar)
        
    def seleccionar(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        self.fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","JPG (*.jpg);;PNG (*.png)", options=options)
        if self.fileName != "":
            self.label_path.setText(self.fileName)
            self.estatus.setText("Estatus: Imagen seleccionada")

    def analizar(self):    
        if self.fileName != "":    
            print(self.fileName)
            if passImg(self.fileName):
                self.estatus.setText("Estatus: Imagen procesada")
            else:
                self.estatus.setText("EStatus: Esta imagen no se pudo procesar")
        else:
            self.estatus.setText("Estatus: Selecciona una imagen")

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()