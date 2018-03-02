from modelo.aeroporto import Aeroporto
from modelo.abstrato import Abstrato

class AeroportoDao(Abstrato):

    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, aeroporto):
        sql = ""
        if aeroporto.id == 0:
            sql = 'insert into aeroporto(nome, sigla)values(?, ?)'
            self.conexao.execute(sql, (aeroporto.nome, aeroporto.sigla))
        else:
            sql = 'update aeroporto set nome = ? ,sigla = ?  where id = ?'
            self.conexao.execute(sql, (aeroporto.nome, aeroporto.sigla, aeroporto.id))
        self.conexao.commit()
    def pesquisar(self):
        sql = "select * from aeroporto"
        resultado = self.conexao.execute(sql)
        self.lista = []
        for valor in resultado:
            aeroporto = Aeroporto(valor[0], valor[1], valor[2])
            self.lista.append(aeroporto)
        return self.lista

    def alterar(self,id):

        sql = "select * from aeroporto where id = ?"
        resultado = self.conexao.execute(sql, (id,))
        for valor in resultado:
            aeroporto = Aeroporto(valor[0],valor[1],valor[2])
            return aeroporto












    def excluir(self,id):
        r = "Aeroporto Inexistente !!!"
        sql = "select * from aeroporto where id = ?"
        resultado = self.conexao.execute(sql, (id,))
        for coluna in resultado:

            if id == coluna[0]:
                r = "Aeroporto Deletado Com Sucesso !!!"
                self.conexao.execute("DELETE FROM Aeroporto where id = ?",(id,))
                self.conexao.commit()
            else:
                r = "Aeroporto Inexistente !!!"
        return r






    def NomeExistente(self,nome):
        b = ""
        self.cursor = self.conexao.execute ("select * from aeroporto WHERE nome = ?",(nome,))
        for coluna in self.cursor:
            return False
            break
        return True
