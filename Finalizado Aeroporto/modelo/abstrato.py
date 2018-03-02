from abc import abstractmethod,ABC

class Abstrato(ABC):
    @abstractmethod

    def salvar(self):
        pass
    @abstractmethod
    def excluir(self):
        pass
    @abstractmethod
    def alterar(self):
        pass
    @abstractmethod
    def pesquisar(self):
        pass
