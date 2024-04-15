import tkinter as tk
from Function import FuncApp


class MainWindow:
    # constructor
    def __init__(self):
        self.__mainRoot = tk.Tk()
        self.__funx = FuncApp()

    # iniciador de la ventana principal
    def initWindow(self):
        self.__mainRoot.geometry(self.__funx.determinarPosicion(1200, 700))
        self.__mainRoot.mainloop()

