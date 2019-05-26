from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from Detector import passImg
import cv2
import imutils
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        
        self.master = master
        self.pack(fill=BOTH, expand=1)
        titulo = Label(self,text="Detector de personas",font=("Arial Bold", 25)).grid(row=1,column=1)
        instruccion1 = Label(self,text="Instrucciones",font=("Arial Bold", 18)).grid(sticky=W, padx=5,row=2,column=1)
        instruccion2 = Label(self,text="1. Presiona el botón", font=("Arial",14)).grid(sticky=W, padx=5,row=3,column=1)
        instruccion3 = Label(self,text="2. Busca una imagen", font=("Arial",14)).grid(sticky=W, padx=5,row=4,column=1)
        seleccionar = Button(self, text="Selecciona una imagen", bg="skyblue", command=self.selectImagen).grid(row=5,column=1)
        
        self.cantidadPersonasText = Label(self,text="Personas encontradas:",font=("Arial Bold", 12)).grid(row=2,column=2)                
        self.cantidadPersonas=Label(self,text="0",font=("Arial Bold", 12)).grid(row=3,column=2)

        # self.tituloImg1 = Label(self,text="Imagen Original",font=("Arial Bold", 12)).grid(row=6,column=1)
        # self.load = Image.open("bg.jpg")
        # self.render = ImageTk.PhotoImage(self.load)
        # self.original = Label(self, image=self.render)
        # self.original.image = self.render        
        # self.original.grid(row=7,column=1)

        self.tituloImg2 = Label(self,text="Imagen Resultado",font=("Arial Bold", 12)).grid(row=8,column=0)
        self.load = Image.open("bg2.jpg")
        self.render = ImageTk.PhotoImage(self.load)
        self.resultado = Label(self, image=self.render)
        self.resultado.image = self.render        
        self.resultado.grid(row=7,column=2)

    # def cargarOriginal(self, path="bg.jpg"):
    #     self.original.image=""
    #     self.load = cv2.imread(path)
    #     self.load=cv2.cvtColor(self.load, cv2.COLOR_BGR2RGB)
         
    #     height, width, channels = self.load.shape
    #     if(width>800 or height>800):
    #         self.load=self.changeSize(self.load)
        
    #     self.load = Image.fromarray(self.load)
    #     self.render = ImageTk.PhotoImage(self.load)
    #     self.original = Label(self, image=self.render)
    #     self.original.image = self.render        
    #     self.original.grid(row=6,column=1)
    #     imagenDibujada, personas = passImg(path)
    #     self.cantidadPersonas=Label(self,text=str(personas),font=("Arial Bold", 12)).grid(row=3,column=2)
    #     self.cargarResultado(imagenDibujada)

    def cargarResultado(self, image):
        self.resultado.image=""
        self.load = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        height, width, channels = self.load.shape
        if(width>800 or height>800):
            self.load=self.changeSize(self.load)
        self.load = Image.fromarray(self.load)
        
        self.render = ImageTk.PhotoImage(self.load)
        self.resultado = Label(self, image=self.render)
        self.resultado.image = self.render        
        self.resultado.grid(row=6,column=2)
    
    def selectImagen(self):
        self.path = filedialog.askopenfilename(initialdir = ".",title = "Selecciona tu imagen",filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("jpg files","*.jpg")))
        if len(self.path)>0:
            #self.cargarOriginal(self.path)
            imagenDibujada, personas = passImg(self.path)
            self.cantidadPersonas=Label(self,text=str(personas),font=("Arial Bold", 12)).grid(row=3,column=2)
            self.cargarResultado(imagenDibujada)
        else:
            print("Debes seleccionar una imagen")

    def changeSize(self,imagen):
        height, width, channels = imagen.shape
        if width>1000 or height>1000:
            w = int(imagen.shape[1] / 3.0)
            imagen = imutils.resize(imagen, width=w)
        elif width>1000 or height>1000:
            w = int(imagen.shape[1] / 2.0)
            imagen = imutils.resize(imagen, width=w)
        elif width>600 or height > 600: 
            w = int(imagen.shape[1] / 1.3)
            imagen = imutils.resize(imagen, width=w) 
        return imagen
            
root = Tk()
app = Window(root)

root.wm_title("Tkinter window")
root.geometry("900x900")
root.mainloop()