from modelo.voo import Voo
from modelo.abstrato import Abstrato

class VooDao(Abstrato):

    def __init__(self, conexao):
        self.conexao = conexao



    def salvar(self, voo):
        sql = ""
        if voo.id == 0:
            sql = 'insert into voo(numero,origem, destino, lugares)values(?, ?, ?, ?)'
            self.conexao.execute(sql, (voo.numero,voo.origem, voo.destino, voo.lugares))
        else:
            sql = 'update voo set numero = ? ,origem = ? ,destino = ? ,lugares = ?  where id = ?'
            self.conexao.execute(sql, (voo.numero,voo.origem, voo.destino, voo.lugares, voo.id))
        self.conexao.commit()
    def pesquisar(self):
        sql = "select * from voo"
        resultado = self.conexao.execute(sql)
        self.lista = []
        for valor in resultado:
            voo = Voo(valor[0], valor[1], valor[2], valor[3], valor[4])
            self.lista.append(voo)
        return self.lista

    def alterar(self,param):
        sql = "select * from voo where id = ?"
        resultado = self.conexao.execute(sql, (param,) )
        for valor in resultado:
            voo = Voo(
                valor[0],valor[1],valor[2],valor[3],valor[4]
            )
            return voo



    def PesquisarNumero(self,parametro):
        sql = 'SELECT * from voo where numero = ?'
        resultado = self.conexao.execute(sql, (parametro,))
        lista1 = []

        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista1.append(voo)
        return lista1





    def PesquisarOrigem(self,parametro):
        sql = 'SELECT * from voo where origem = ?'
        resultado = self.conexao.execute(sql, (parametro,))
        lista = []
        for valor in resultado:

            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista.append(voo)
        return lista



    def PesquisarDestino(self,parametro):
        sql = 'SELECT * from voo where destino = ?'
        resultado = self.conexao.execute(sql, (parametro,))
        lista3 = []
        for valor in resultado:
            voo = Voo(valor[0],valor[1],valor[2],valor[3],valor[4])
            lista3.append(voo)
        return lista3


    def ConfirmarReserva(self,numero):
        r = "Voo Inexistente"
        self.cursor = self.conexao.execute ("select * from voo ")
        for coluna in self.cursor.fetchall():

            if numero == coluna[1]:
                x = int(coluna[4])
                if x > 0:
                    x = x - 1
                    r = "Voo confirmado"



                    self.conexao.execute("UPDATE  Voo SET lugares = ? WHERE numero = ?",(x,numero))
                    self.conexao.commit()

                else:
                    r = 'Voo lotado'

        return r












    def CancelarReserva(self,numero):
        r = "Voo Inexistente"
        self.cursor = self.conexao.execute ("select * from voo ")
        for coluna in self.cursor.fetchall():

            if numero == coluna[1]:
                x = int(coluna[4])
                if x >= 0:
                    x += 1
                    r = "Voo Cancelado"




                    self.conexao.execute("UPDATE  Voo SET lugares = ? WHERE numero = ?",(x,numero))
                    self.conexao.commit()

                else:
                    r = 'Voo lotado'

        return r







    def NumeroExistente(self,numero):
        b = ""
        self.cursor = self.conexao.execute ("select * from voo WHERE numero = ?",(numero,))
        for coluna in self.cursor:
            return False
            break
        return True
        #    if numero != coluna[1]:
        #        self.conexao.execute("UPDATE  Voo  WHERE numero = ?",(numero,))
        #        self.conexao.commit()
        #    else:
        #        b = "Numero invalido, digite outro !"

        #return b




    def excluir(self,id):
        r = "Voo Inexistente !!!"
        sql = "select * from voo where id = ?"
        resultado = self.conexao.execute(sql, (id,))
        for coluna in resultado:

            if id == coluna[0]:
                r = "Voo Deletado Com Sucesso !!!"
                self.conexao.execute("DELETE FROM Voo where id = ?",(id,))
                self.conexao.commit()
            else:
                r = "Voo Inexistente !!!"
        return r
