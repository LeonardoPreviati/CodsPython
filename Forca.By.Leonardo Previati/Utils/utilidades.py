import os
class Limpar(object):

	def limpar(self):
		os.system('cls' if os.name == 'nt' else 'clear')
