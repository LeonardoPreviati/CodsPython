
class Tanque(object):
    def __init__(self,cod,capacidade,tipo,carga,cor):
        self.cod = cod
        self.capacidade = capacidade
        self.tipo = tipo
        self.carga = carga
        self.cor = cor 


    def __str__(self):
    	return "Número do taxo" + self.cod + "Capacidade" + (str(self.capacidade)) + "Tipo" + self.tipo + "Carga" + self.carga + "Cor" + self.cor