class Aeroporto(object):
      def __init__(self, id, nome, sigla):
        self.id = id
        self.nome = nome
        self.sigla = sigla

      voos = []
      def adicionarVoo(self,voo):
        self.voos.append(voo)

      @property
      def nome(self):
          return self._nome
      @nome.setter
      def nome(self, value):
          self._nome = value.upper()



      @property
      def sigla(self):
          return self._sigla
      @sigla.setter
      def sigla(self, value):
          self._sigla= value.capitalize()