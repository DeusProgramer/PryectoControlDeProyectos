import asyncio
import sqlite3


class DataBaze:
    # Constructor
    def __init__(self):
        self.__datos = None

    @property
    def getDatos(self):
        return self.__datos

    # Crear data base
    async def crearData(self):
        querY = "create table if not exists Users (usuario TEXT, clave TEXT, cargo TEXT)"
        try:
            conx = sqlite3.connect("Resource/data/dateStorage/XXCVVB.db")
            conx.execute(querY)
            conx.commit()
            conx.close()
        except:
            pass

    # Verificar clave en base de datos
    def verificarUsuarios(self, _clave):
        querY = "select * from Users"
        conx = sqlite3.connect("Resource/data/dateStorage/XXCVVB.db")
        hola = conx.execute(querY)
        datos = hola.fetchall()
        for tupla in datos:
            if _clave == tupla[1]:
                self.__datos = tupla
                return True
        return False

    # agregar usuarios a la base de datos
    def aggUsuarios(self, _usuario, _clave, _cargo):
        try:
            conx = sqlite3.connect("Resource/data/dateStorage/XXCVVB.db")
            querY = "insert into Users (usuario, clave, cargo) values (?, ?, ?)"
            conx.execute(querY, (_usuario, _clave, _cargo))
            conx.commit()
            conx.close()
        except:
            pass
