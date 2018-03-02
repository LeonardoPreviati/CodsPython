import sqlite3
from pattern.conexaoFactoryPattern import ConexaoFactoryPattern

class ConexaoFactory(ConexaoFactoryPattern):
    def __init__(self):
        self.conexao = sqlite3.connect('elegebd.db')
        self.criarTabelas()
        self.inicializarDados()



    def getconexao(self):
        return self.conexao

    def criarTabelas(self):
        self.conexao.execute('''CREATE TABLE IF NOT EXISTS TANQUE
        (COD INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, CAPACIDADE
         REAL NOT NULL, TIPO TEXT NOT NULL, CARGA REAL NOT NULL,
         COR TEXT NOT NULL)''')

    
        self.conexao.execute('''CREATE TABLE IF NOT EXISTS USUARIO
        (COD INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        LOGIN TEXT NOT NULL, SENHA TEXT NOT NULL)''')

    def inicializarDados(self):
        sql = "SELECT * FROM Usuario"
        resultado = self.conexao.execute(sql)
        lista = []
        for i in resultado:
            lista.append(i[1])
        if "admin" in lista:
            return 0
        else:
            self.conexao.execute('''INSERT into USUARIO
                (LOGIN,SENHA)values('admin','admin')''')      




