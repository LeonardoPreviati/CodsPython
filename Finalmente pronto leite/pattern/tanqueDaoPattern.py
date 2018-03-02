from abc import abstractmethod,ABC 

class TanqueDaoPattern(ABC):

	@abstractmethod
	def save(self):
		pass

	@abstractmethod
	def alterar(self):
		pass


	@abstractmethod
	def getTanque(self):
		pass
		
	@abstractmethod
	def getLista(self):
		pass
		
	@abstractmethod
	def getListaPesquisaCapacidade(self):
		pass

	@abstractmethod
	def getListaPesquisaTipo(self):
		pass

	@abstractmethod
	def getListaPesquisaCor(self):
		pass

	@abstractmethod
	def getListaPesquisaCarga(self):
		pass
		
	@abstractmethod
	def excluir(self):
		pass
		
	@abstractmethod
	def setCarga(self):
		pass	

	@abstractmethod
	def getCarga(self):
		pass									