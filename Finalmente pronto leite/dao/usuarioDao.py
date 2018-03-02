from pattern.usuarioDaoPattern import UsuarioDaoPattern
from models.usuario import Usuario
from factory.conexaoFactory import ConexaoFactory
class UsuarioDao(UsuarioDaoPattern):
	def __init__(self,conexao):
		self.conexao = conexao

	def save(self,usuario):
		sql = ""
		if usuario.cod == 0:
			sql = 'insert into usuario(login,senha)values(?,?)'
			self.conexao.execute(sql,(usuario.login,usuario.senha))
		else:
			sql = 'update usuario set login = ?, senha = ? where cod = ?'
			self.conexao.execute(sql,(usuario.login,usuario.senha,usuario.cod))
		self.conexao.commit()
		#pass

	def alterar(self,cod):
		sql = "SELECT * FROM usuario where cod = ?"
		resultado = self.conexao.execute(sql,(cod,))
		for valor in resultado:
			usuario = Usuario(valor[0],valor[1],valor[2])
			return usuario





	def getLista(self):
		#Retorna todos os usuarios menos senhas

		sql = "SELECT * from usuario"
		resultado = self.conexao.execute(sql)
		self.lista = []
		for valor in resultado:
			usuario = Usuario(valor[0],valor[1],valor[2])
			self.lista.append(usuario)
			
		return self.lista

		#pass


	def getListaPesquisa(self,paramCod):
		#Pesquisar o nome do carinha
		sql = "SELECT * from usuario where cod =?"
		resultado = self.conexao.execute(sql,(paramCod,))
		for codes in resultado:
			usuario = Usuario(codes[0],codes[1],codes[2])
			#listaCod.append(tanque)
			return usuario




	def excluir(self,cod):
		r = "Usuario Inexistente"
		sql = "SELECT * FROM usuario where cod = ?"
		resultado = self.conexao.execute(sql,(cod,))
		for coluna in resultado:
			if cod == coluna[0]:
				r = "Usuario Excluido Com Sucesso"
				self.conexao.execute("DELETE FROM Usuario where cod =?",(cod,))
				self.conexao.commit()
			else:
				r = "Usuario Inexistente"
		return r



	def LoginExistente(self,login):
	    self.cursor = self.conexao.execute ("select * from usuario WHERE login = ? ",(login,))
	    for coluna in self.cursor:
	        return False
	        break
	    return True


	def LoginExistenteEntrar(self,login):
	    self.cursor = self.conexao.execute ("select * from usuario WHERE login = ? ",(login,))
	    for coluna in self.cursor:
	        return True
	        break
	    return False


	def SenhaExistente(self,senha):
		self.cursor = self.conexao.execute("select * from usuario WHERE senha = ?",(senha,))
		for coluna in self.cursor:
			return True
			break
		return False
