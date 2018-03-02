from modelo.passageiro import Passageiro
from modelo.abstrato import Abstrato

class PassageiroDao(Abstrato):

    def __init__(self, conexao):
        self.conexao = conexao

    def salvar(self, passageiro):
        sql = ""
        if passageiro.id == 0:
            sql = 'insert into passageiro(nome, cpf, idade)values(?, ?, ?)'
            self.conexao.execute(sql, (passageiro.nome, passageiro.cpf, passageiro.idade))
        else:
            sql = 'update passageiro set nome = ? ,cpf = ? ,idade = ?  where id = ?'
            self.conexao.execute(sql, (passageiro.nome, passageiro.cpf, passageiro.idade, passageiro.id))
        self.conexao.commit()
    def pesquisar(self):
        sql = "select * from passageiro"
        resultado = self.conexao.execute(sql)
        self.lista = []
        for valor in resultado:
            passageiro = Passageiro(valor[0], valor[1], valor[2], valor[3])
            self.lista.append(passageiro)
        return self.lista

    def alterar(self,parametros):
        sql = "select * from passageiro where id = ?"
        resultado = self.conexao.execute(sql, (parametros,) )
        for valor in resultado:
            passageiro = Passageiro(
                valor[0],valor[1],valor[2],valor[3]
            )
            return passageiro





    def excluir(self,id):
        r = "Passageiro Inexistente !!!"
        sql = "select * from passageiro where id = ?"
        resultado = self.conexao.execute(sql, (id,))
        for coluna in resultado:

            if id == coluna[0]:
                r = "Passageiro Deletado Com Sucesso !!!"
                self.conexao.execute("DELETE FROM Passageiro where id = ?",(id,))
                self.conexao.commit()
            else:
                r = "Passageiro Inexistente !!!"
        return r
