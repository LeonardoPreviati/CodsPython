class Voo(object):

    def __init__(self, id,numero, origem, destino, lugares):
        self.id = id
        self.numero = numero
        self.origem = origem
        self.destino = destino
        self.lugares = lugares

    def __str__(self):
        return "Número: " + self.numero + " Origem: "+ self.origem + " Destino: "+ self.destino + " Nlugares: "+ str(self.lugares)

    #Não da certo pois ele adiciona 15 lugares quando chega a 0 e seria somente quando digitado 0, por isso existe um teste no executável que faz essa tarefa !!!
    """@property
    def lugares(self):
        return self._lugares
    @lugares.setter
    def lugares(self, value):
        if value <= 0 :
            self._lugares = 15
        else:
            self._lugares = value"""



    @property
    def origem(self):
        return self._origem
    @origem.setter
    def origem(self, value):
        self._origem = value.capitalize()



    @property
    def destino(self):
        return self._destino
    @destino.setter
    def destino(self, value):
        self._destino = value.capitalize()
