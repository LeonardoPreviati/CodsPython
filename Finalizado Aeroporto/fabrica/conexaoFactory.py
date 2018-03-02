import sqlite3
class ConexaoFactory(object):
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.tabelaaeroporto()
        self.tabelavoos()
        self.tabelapassageiro()


    def getconexao(self):
        return self.conexao

    def tabelaaeroporto(self):
        self.conexao.execute("CREATE TABLE IF NOT EXISTS AEROPORTO(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NOME TEXT NOT NULL, SIGLA TEXT NOT NULL)")

    def tabelavoos(self):
        self.conexao.execute("CREATE TABLE IF NOT EXISTS VOO(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,NUMERO TEXT NOT NULL, ORIGEM TEXT NOT NULL, DESTINO TEXT NOT NULL, LUGARES INTEGER NOT NULL)")

    def tabelapassageiro(self):
        self.conexao.execute("CREATE TABLE IF NOT EXISTS PASSAGEIRO(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, NOME TEXT NOT NULL, CPF TEXT NOT NULL, IDADE INTEGER NOT NULL)")
