from abc import abstractmethod,ABC 

class UsuarioDaoPattern(ABC): 

	@abstractmethod
	def save(self):
		pass

	@abstractmethod
	def alterar(self):
		pass
	
	@abstractmethod
	def getLista(self):
		pass
		
	@abstractmethod
	def getListaPesquisa(self):
		pass
		
	@abstractmethod
	def excluir(self):
		pass

	@abstractmethod
	def LoginExistente(self):
		pass
	
	@abstractmethod
	def LoginExistenteEntrar(self):
		pass