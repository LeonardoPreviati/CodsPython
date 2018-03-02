
class Usuario(object):
    def __init__(self,cod,login,senha):
        self.cod = cod
        self.login = login
        self.senha = senha
        
    def __str__(self):
    	return self.cod + self.login + self.senha