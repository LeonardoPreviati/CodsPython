from pattern.tanqueDaoPattern import TanqueDaoPattern
from models.tanque import Tanque

class TanqueDao(TanqueDaoPattern):
	def __init__(self,conexao):
		self.conexao = conexao

	def save(self,tanque):
		sql = ""
		if tanque.cod == 0:
			sql = 'insert into tanque(capacidade,tipo,cor,carga)values(?,?,?,?)'
			self.conexao.execute(sql,(tanque.capacidade,tanque.tipo,tanque.cor,tanque.carga))
		else:
			sql = 'update tanque set capacidade = ?, tipo = ?, cor = ?, carga = ? where cod = ?'
			self.conexao.execute(sql,(tanque.capacidade,tanque.tipo,tanque.cor,tanque.carga,tanque.cod))
		self.conexao.commit()


	def alterar(self,cod):
		sql = "SELECT * FROM tanque where cod = ?"
		resultado = self.conexao.execute(sql,(cod,))
		for valor in resultado:
			tanque = Tanque(valor[0],valor[1],valor[2],valor[3],valor[4])
			return tanque















	def getTanque(self,paramCod):

		#mostrar por cod o tanque
		sql = "SELECT * from tanque where cod =?"
		resultado = self.conexao.execute(sql,(paramCod,))
		#listaCod = []
		for codes in resultado:
			tanque = Tanque(codes[0],codes[1],codes[2],codes[3],codes[4])
			#listaCod.append(tanque)
			return tanque













	def getLista(self):
		#Mostrar tudo o que a na lista
		sql = "SELECT * from tanque"
		resultado = self.conexao.execute(sql)
		self.lista = []
		for valor in resultado:
			tanque = Tanque(valor[0],valor[1],valor[2],valor[3],valor[4])
			self.lista.append(tanque)
		return self.lista


	def getListaPesquisaCapacidade(self,paramCapacidade):
		#pesquisar por categorias(cor,tipo,capacidade)

		sql = 'SELECT * from tanque where capacidade = ?'
		resultado = self.conexao.execute(sql,(paramCapacidade,))
		listaCapacidade = []
		for capacidades in resultado:
			tanque = Tanque(capacidades[0],capacidades[1],capacidades[2],capacidades[3],capacidades[4])
			listaCapacidade.append(tanque)
		return listaCapacidade





	def getListaPesquisaTipo(self,paramTipo):
		#pesquisar por categorias(cor,tipo,capacidade)
		sql = "SELECT * FROM tanque where tipo=?"
		resultado = self.conexao.execute(sql,(paramTipo,))
		listaTipo = []
		for tipos in resultado:
			tanque = Tanque(tipos[0],tipos[1],tipos[2],tipos[3],tipos[4])
			listaTipo.append(tanque)
		return listaTipo


	def getListaPesquisaCor(self,paramCor):
		#pesquisar por categorias(cor,tipo,capacidade)
		sql = "SELECT * FROM tanque where cor =?"
		resultado = self.conexao.execute(sql,(paramCor,))
		listaCor = []
		for cores in resultado:
			tanque = Tanque(cores[0],cores[1],cores[2],cores[3],cores[4])
			listaCor.append(tanque)
		return listaCor


	def getListaPesquisaCarga(self,paramCarga):
		#pesquisar por categorias(cor,tipo,capacidade)
		sql = "SELECT * FROM tanque where carga = ?"
		resultado = self.conexao.execute(sql,(paramCarga,))
		listaCarga = []
		for cargas in resultado:
			tanque = Tanque(cargas[0],cargas[1],cargas[2],cargas[3],cargas[4])
			listaCarga.append(tanque)
		return listaCarga






	def excluir(self,cod):
		r = "Tanque Inexistente"
		sql = "SELECT * FROM tanque where cod = ?"
		result = self.conexao.execute(sql,(cod,))
		for colunar in result:
			if cod == colunar [0]:
				r = "Tanque Excluido Com Sucesso"
				self.conexao.execute("DELETE  FROM Tanque where cod = ?",(cod,))
				self.conexao.commit()
			else:
				r = "Tanque Inexistente"

		return r












	def setCarga(self,cod,DEPOSITAR):
		#BOTAR LEITE NOS TANQUES
		#pass
		r = "Tanque Inexistente"
		self.cursor = self.conexao.execute("SELECT * FROM tanque")
		for coluna in self.cursor.fetchall():




			if cod == coluna[0]:

				CAPACIDADE = float(coluna[1])#Y
				CARGA = float(coluna[3])#X
				TIPO = str(coluna[2])#Z
				COR = str(coluna[4])



				if TIPO == "Cru":








					if DEPOSITAR > 0:

						if (DEPOSITAR + CARGA) > CAPACIDADE:
							r = "Depósito não pode ser realizado, ultrapassando em ",DEPOSITAR + CARGA - CAPACIDADE,"litro(s) a carga máxima do tanque",COR

						if CARGA < CAPACIDADE:
							if (DEPOSITAR + CARGA) <= CAPACIDADE:
								CARGA += DEPOSITAR
								r = "Deposito Efetivado Com Sucesso. O Tanque",COR,"Esta Com",CARGA,"Litro(s) De Leite. Capacidade Atual",CAPACIDADE
								self.conexao.execute("UPDATE Tanque SET carga = ? WHERE cod = ?",(CARGA,cod))
								self.conexao.commit()

							else:
								r = "Depósito não pode ser realizado, ultrapassando em ",DEPOSITAR + CARGA - CAPACIDADE,"litro(s) a carga máxima do tanque",COR



						if CARGA > CAPACIDADE:

							r = "Depósito não pode ser realizado, ultrapassando em ",DEPOSITAR + CARGA - CAPACIDADE,"litro(s) a carga máxima do tanque",COR

					else:
						r = "Digite apenas valores maiores que zero para informar o deposito"








				if TIPO == "Pasteurizado":
					#(print)Era Necessário Professor, pelo fato de ele não retornar a mensagem se não fizesse isso.
					aux = (CAPACIDADE * 9) /10
					CAPACIDADE = aux
					if DEPOSITAR > 0:

						if (DEPOSITAR + CARGA) > CAPACIDADE:
							r = "Depósito não pode ser realizado, ultrapassando em ",DEPOSITAR + CARGA - CAPACIDADE,"litro(s) a carga máxima do tanque",COR

						if CARGA < CAPACIDADE:
							if (DEPOSITAR + CARGA) <= CAPACIDADE:# or DEPOSITAR + CARGA > CAPACIDADE:
								CARGA += DEPOSITAR
								r = "Deposito Efetivado Com Sucesso. O Tanque",COR,"Esta Com",CARGA,"Litro(s) De Leite. Capacidade Atual",CAPACIDADE
								self.conexao.execute("UPDATE Tanque SET carga = ? WHERE cod = ?",(CARGA,cod))
								self.conexao.commit()

							else:
								r = "Depósito não pode ser realizado, ultrapassando em ",DEPOSITAR + CARGA - CAPACIDADE,"litro(s) a carga máxima do tanque",COR



						if CARGA > CAPACIDADE:
							r = "Depósito não pode ser realizado, ultrapassando em ",DEPOSITAR + CARGA - CAPACIDADE,"litro(s) a carga máxima do tanque",COR

					else:
						r = "Digite apenas valores maiores que zero para informar o deposito"
		return r
















	def getCarga(self,cod,RETIRAR):
		#PEGAR O LEITE DOS TAXO
		#BOTAR LEITE NOS TANQUES
		#pass
		r = "Tanque Inexistente"
		self.cursor = self.conexao.execute("SELECT * FROM tanque")
		for coluna in self.cursor.fetchall():



			if cod == coluna[0]:
				CAPACIDADE = float(coluna[1])
				TIPO = str(coluna[2])
				CARGA = float(coluna[3])
				COR = str(coluna[4])
				aux = (CAPACIDADE * 9) /10
				CAPACIDADE = aux

				if TIPO == "Cru":


					if RETIRAR <= CARGA and RETIRAR <= aux: #and RETIRAR + CARGA <= CAPACIDADE:# and RETIRAR <= CAPACIDADE:

						CARGA -= RETIRAR
						r = "você acabou de retirar",RETIRAR,"litro(s). Atualmente pode retirar ainda ",CARGA ,"litro(s) de leite."
						self.conexao.execute("UPDATE Tanque SET carga = ? WHERE cod = ?",(CARGA,cod))
						self.conexao.commit()

					if RETIRAR > CARGA or RETIRAR > aux:
						r = "Retirada não pode ser realizada, ultrapassando em",RETIRAR - CARGA,"litro(s) a carga máxima do tanque",COR



					if RETIRAR <= 0:
						r = "Retirada não pode ser realizada, pois não foram fornecidos valores"


					#if RETIRAR <= CARGA:
						#r = "Retirada não pode ser realizada, ultrapassando em",RETIRAR - CARGA,"litro(s) a carga máxima do tanqu2e",COR







				if TIPO == "Pasteurizado":
					CAPACIDADE = float(coluna[1])
					TIPO = str(coluna[2])
					CARGA = float(coluna[3])
					COR = str(coluna[4])
					aux = (CAPACIDADE * 9) /10
					CAPACIDADE = aux


					if RETIRAR <= CARGA and RETIRAR <= CAPACIDADE: #RETIRAR <= CAPACIDADE: #and RETIRAR + CARGA <= CAPACIDADE:# and RETIRAR <= CAPACIDADE:

						CARGA -= RETIRAR
						r = "você acabou de retirar",RETIRAR,"litro(s). Atualmente pode retirar ainda ",CARGA ,"litro(s) de leite."
						self.conexao.execute("UPDATE Tanque SET carga = ? WHERE cod = ?",(CARGA,cod))
						self.conexao.commit()

					if RETIRAR > CAPACIDADE:
						r = "Retirada não pode ser realizada, ultrapassando em",RETIRAR - CARGA,"litro(s) a carga máxima do tanque",COR

					if CARGA == 0 and RETIRAR > 0:
						r = "Retirada não pode ser realizada, ultrapassando em", RETIRAR - CARGA,"litro(s) a carga máxima do tanque",COR



					if RETIRAR <= 0:
						r = "Retirada não pode ser realizada, pois não foram fornecidos valores"
		return r
