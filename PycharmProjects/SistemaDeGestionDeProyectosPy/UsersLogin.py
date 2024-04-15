import time
import asyncio
import tkinter as tk
from Function import FuncApp
from funcionesSQL import DataBaze
from MainWindow import MainWindow


class LoginSystem:
    # Constructor
    def __init__(self):
        self.funx = FuncApp()
        self.funDB = DataBaze()
        self.__nombreUsuario = None
        self.__cargoUsuario = None
        self.__root = tk.Tk()

    # Funcion que se encargara de determinar el acceso al programa
    def trueAcceso(self, _clave):
        if self.funDB.verificarUsuarios(_clave):
            tupla = self.funDB.getDatos
            self.__nombreUsuario = tupla[0]
            self.__cargoUsuarioUsuario = tupla[2]
            self.__root.destroy()
            nuevaVentana  = MainWindow()
            nuevaVentana.initWindow()
        else:
            print("acceso denegado")

    # Logo
    def MostrarLogo(self):
        root = tk.Tk()
        root.geometry(self.funx.determinarPosicion(600, 350))
        frame = tk.Frame(master=root)
        img = tk.PhotoImage(file="Resource/image/loginTheme.png")
        img_label = tk.Label(frame, image=img)
        img_label.pack()
        frame.pack()
        root.overrideredirect(True)
        root.mainloop()

    # Vetana del login
    async def mostrarVentaLogin(self):

        self.__root.geometry(self.funx.determinarPosicion(600, 550))
        frameImg = tk.Frame(self.__root)
        img = tk.PhotoImage(file="Resource/image/loginManagmetnProyect.png")
        img_label = tk.Label(frameImg, image=img)
        img_label.pack()
        """Botoness"""

        """
        # Boton salir
        botonSalir = tk.Button(frameImg, text="X")
        botonSalir.config(width=4, bg="#08101E", fg="WHITE")
        botonSalir.config(font=(None, 11))
        botonSalir.config(border=False)
        botonSalir.bind("<Leave>", lambda event: botonSalir.config(bg="#08101E"))
        botonSalir.bind("<Enter>", lambda event: botonSalir.config(bg="RED"))
        botonSalir.bind("<Button-1>", lambda event: root.quit())
        botonSalir.place(x=560, y=0)
        """

        # Boton para ingresar
        botonIngresar = tk.Button(frameImg, text="Ingresar")
        botonIngresar.config(fg="#91B5C1", bg="#0F1F38")
        botonIngresar.config(border=False, font=("Comic Sans MS", 12))
        botonIngresar.bind("<Leave>", lambda event: botonIngresar.config(bg="#0F1F38", fg="#91B5C1"))
        botonIngresar.bind("<Enter>", lambda event: botonIngresar.config(bg="#00D7ED", fg="#0F1F38"))
        botonIngresar.bind("<Button-1>", lambda event: LoginSystem.trueAcceso(self, cajaTextoPassword.get()))
        botonIngresar.place(x=400, y=310)
        """
        Botones (labels/textos) que se conportan
        Como botones
        """
        # boton/Label Cambiar Contrasena
        boton_LabelCambiarPass = tk.Label(frameImg, text="Cambiar Contrasena")
        boton_LabelCambiarPass.config(fg="#BAAF88", bg="#08101E")
        boton_LabelCambiarPass.config(font=("Comic Sans MS", 12))
        boton_LabelCambiarPass.place(x=359, y=365)
        boton_LabelCambiarPass.bind("<Leave>", lambda event: boton_LabelCambiarPass.config(fg="#BAAF88"))
        boton_LabelCambiarPass.bind("<Enter>", lambda event: boton_LabelCambiarPass.config(fg="#06F6D3"))
        # Boton plus
        botonMas = tk.Button(frameImg, text="+")
        botonMas.config(font=("Comic Sans MS", 16))
        botonMas.config(width=3)
        botonMas.config(fg="#06F6D3", bg="#08101E")
        botonMas.config(border=False)
        botonMas.bind("<Leave>", lambda event: botonMas.config(fg="#06F6D3", bg="#08101E"))
        botonMas.bind("<Enter>", lambda event: botonMas.config(bg="#00D7ED", fg="#0F1F38"))
        botonMas.bind("<Button-1>", lambda event: self.funx.aggUsuarios())
        botonMas.place(x=285, y=500)
        """Textos"""
        # texto password
        textPassword = tk.Label(frameImg, text="Password:")
        textPassword.config(bg="#08101E", fg="#91B5C1")
        textPassword.config(font=("Comic Sans MS", 12))
        textPassword.place(x=315, y=240)
        """sub texto"""
        corporationText = tk.Label(frameImg, text="CORPORATION")
        corporationText.config(bg="#08101E", fg="WHITE")
        corporationText.config(font=(None, 16))
        corporationText.place(x=362, y=170)
        """sub texto autor"""
        autorText = tk.Label(frameImg, text="@Diego Borges")
        autorText.config(bg="#08101E", fg="#BAAF88")
        autorText.config(font=("Comic Sans MS", 10))
        autorText.place(x=500, y=525)
        # Caja de texto para la clave
        cajaTextoPassword = tk.Entry(frameImg, show="*")
        cajaTextoPassword.config(width=20, bg="#08101E")
        cajaTextoPassword.config(border=False, fg="#91B5C1")
        cajaTextoPassword.config(justify="center")
        cajaTextoPassword.config(font=(None, 16))
        cajaTextoPassword.place(x=320, y=265)
        frameImg.pack()
        # root.overrideredirect(True)
        self.__root.mainloop()

    # iniciaself.__r accion
    async def accionAsyncrona(self):
        tarea_1 = asyncio.create_task(self.funDB.crearData())
        tarea_2 = asyncio.create_task(LoginSystem.mostrarVentaLogin(self))
        await asyncio.gather(tarea_1, tarea_2)

    # Funcion asincrona numero 2(La del titulo al empezar)
    async def cerrarVentanaEnLoopp(self):
        pass
