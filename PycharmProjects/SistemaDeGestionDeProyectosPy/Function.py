import time
import tkinter as tk
from funcionesSQL import DataBaze


class FuncApp:
    # constructor
    def __init__(self):
        self.__funDB = DataBaze()
        self.__texto = None

    # Getters...
    @property
    def getNombreUsuario(self):
        return self.__nombreUsuario

    @property
    def getCargoUsuario(self):
        return self.__cargoUsuario

    # la posicion de la ventana
    def determinarPosicion(self, tamano_X, tamano_Y):
        info = tk.Tk()
        window_PantallaW = info.winfo_screenwidth()
        window_PantallaH = info.winfo_screenheight()
        posX = (window_PantallaW - tamano_X) / 2
        posY = (window_PantallaH - tamano_Y) / 2
        info.destroy()
        geometria = str(tamano_X) + "x" + str(tamano_Y) + "+" + str(int(posX)) + "+" + str(int(posY))

        return geometria

    # Funcion para el boton de agregar usuarios(+)
    def aggUsuarios(self):
        root = tk.Tk()
        root.geometry(FuncApp.determinarPosicion(self, 400, 200))
        # Frame que contendra el verificado de agregar usuario
        # (solo si la clave ingresada tiene el autorizado
        # se podra agregar el usuario)
        frameDeVerificacion = tk.Frame(root, width=400, height=200)
        # texto de bienvenida(ejem : que diga que tiene que ingresar una clave)
        textoXDXD = "Hola!!\n" + "Solo los usuarios autorizados pueden agregar nuevos usuarios!!"
        texto_Bienvenido = tk.Label(frameDeVerificacion, text=textoXDXD)
        texto_Bienvenido.place(x=30, y=90)
        # caja de texto que sera donde se reciba la clave
        caja_de_clave = tk.Entry(root, width=15)
        caja_de_clave.config(show="*", justify="center")
        caja_de_clave.config(font=(None, 14))
        caja_de_clave.place(x=75, y=140)
        # Boton de verificar
        boton_Verificar = tk.Button(frameDeVerificacion, text="Verificar")
        boton_Verificar.config(font=("Comic Sans", 10))
        boton_Verificar.place(x=250, y=139)
        frameDeVerificacion.pack()
        root.mainloop()
