import sys
from Utils.utilidades import Limpar
limpeza = Limpar()
#Até poderia ter feito com variáveis normais, sem lista, professor... Mas deu acaso de eu fazer assim. Não repare muito no nome das listas, kkkkk.
#O cod ficou grande, na verdade pelo fato de eu fazer a parte de não dar erro em inputs, ou seja, o usuário poder digitar apenas letras.
#Sendo assim poderia ter ficado menor o código, tenho certeza kkkk, mas que nada, o que importa é a lógica, que nem sempre é boa, mas que serviu para funcionar :D!

class Forca(object):

    letraSalva= []
    letras = []
    ajuda = []
    salvar = []
    mais = [1]
    letraExistente = []
    lista3 = []
    aux = []
    saida = []
    gambiarra = []
    desafiante = ""
    competidor = ""
    chave = ""
    dica1 = ""
    dica2 = ""
    dica3 = ""
    informe = ""
    contador = 0
    historico = ""
    compar = "1234567890'@#$%¨&*()-_=+[]{^}^;:.,\|?°/ª§º´~`"

    def amig(self):

        print("------INICIALIZANDO O JOGO ------")
        while True:
            valido = True

            self.desafiante = input(str("Digite o seu nome desafiante: "))
            if (len(self.desafiante)) < 1:
                print("")
                print("Digite o seu nome corretamente !!!")
                a.amig()
            else:
                for letra in self.desafiante:
                    for comp in self.compar:
                        if(letra==comp):
                            valido = False
                            break
                    if(valido==False):
                        break
                if valido:
                    break
                else:
                    print("Digite somente letras !!!")
                    a.amig()

        while True:
            valido = True

            self.competidor = input("Digite o seu nome competidor: ")
            if (len(self.competidor)) < 1:
                print("")
                print("Digite o seu nome corretamente !!!")
                a.amig()
            else:
                for letra in self.competidor:
                    for comp in self.compar:
                        if(letra==comp):
                            valido = False
                            break
                    if(valido==False):
                        break
                if valido:
                    break
                else:
                    print("Digite somente letras !!!")
                    a.amig()
        limpeza.limpar()
        while True:
            valido = True

            self.chave = input("Digite a palavra chave: ")
            if (len(self.chave)) < 1:
                print("")
                print("Digite o seu nome corretamente !!!")
                a.amig()
            else:
                for letra in self.chave:
                    for comp in self.compar:
                        if(letra==comp):
                            valido = False
                            break
                    if(valido==False):
                        break
                if valido:
                    break
                else:
                    print("Digite somente letras !!!")
                    a.amig()
        self.aux.append(self.chave)
        for i in range(len(self.chave)):
            self.saida.append("*")

        while True:
            valido = True

            self.dica1 = input("Digite a primeira dica: ")
            if (len(self.dica1)) < 1:
                print("")
                print("Digite o seu nome corretamente !!!")
                a.amig()
            else:

                for letra in self.dica1:
                    for comp in self.compar:
                        if(letra==comp):
                            valido = False
                            break
                    if(valido==False):
                        break
                if valido:
                    break
                else:
                    print("Digite somente letras !!!")
                    a.amig()
        self.gambiarra.append(self.dica1)

        while True:
            valido = True

            self.dica2 = input("Digite a segunda dica: ")
            if (len(self.dica2)) < 1:
                print("")
                print("Digite o seu nome corretamente !!!")
                a.amig()
            else:

                for letra in self.dica2:
                    for comp in self.compar:
                        if(letra==comp):
                            valido = False
                            break
                    if(valido==False):
                        break
                if valido:
                    break
                else:
                    print("Digite somente letras !!!")
                    a.amig()
        self.gambiarra.append(self.dica2)

        while True:
            valido = True

            self.dica3 = input("Digite a terceira dica: ")
            if (len(self.dica3)) < 1:
                print("")
                print("Digite o seu nome corretamente !!!")
                a.amig()
            else:
                for letra in self.dica3:
                    for comp in self.compar:
                        if(letra==comp):
                            valido = False
                            break
                    if(valido==False):
                        break
                if valido:
                    break
                else:
                    print("Digite somente letras !!!")
                    a.amig()

        self.gambiarra.append(self.dica3)
        limpeza.limpar()
        a.amig2()

    def amig2(self):
        print("Numero de letras da palavra chave: ",len(self.chave)*"*","\n------ Jogar - 1 /Solicitar Dica - 2 -------")

        while True:
            try:
                opcao = input()
                break
            except:
                print("Digite apenas '1' ou '2' para continuar !!!")

        if opcao == "1":
            a.Opcao()

        if opcao == "2":
            a.Dicas()

        if opcao != "1" or opcao != "2":
            print("Digite apenas os valores '1', ou '2' para prosseguir !!!")
            print("")
            a.amig2()

    def Opcao(self):
        while True:
            valido = True
            informe = input("Informe uma letra: ")
            for letra in informe:
                for comp in self.compar:
                    if(letra==comp):
                        valido = False
                        break
                if(valido==False):
                    break
            if valido:
                break
            else:
                print("Digite somente letras !!!")

        if (len(informe)) < 1:
            print("")
            print("Digite a uma letra pelo menos !!!")
            a.Opcao()

        if (len(informe)) > 1 or (len(informe)) < 0:
            print("Digite apenas uma letra !!!")
            a.Opcao()

        if informe in self.letraExistente:
           print("Impossível digitar a mesma letra, digite outra por gentileza !!!")
           a.Opcao()

        if (len(informe)) == 1:
            contador = 0
            AUX = str(self.aux)

            if informe not in AUX:
                self.lista3.append(1)
                #print("errou")
                if (len(self.lista3))== 1:
                    print("Erro 1:",informe)
                    print("O")
                    self.letraExistente.append(informe)
                    a.amig2()

                if (len(self.lista3))== 2:
                    print("Erro 2:",informe)
                    print("O\n|")
                    self.letraExistente.append(informe)
                    a.amig2()

                if (len(self.lista3))== 3:
                    print("Erro 3:",informe)
                    print(" O ")
                    print("\|/")
                    self.letraExistente.append(informe)
                    a.amig2()

                if (len(self.lista3))== 4:
                    print("Erro 4:",informe)
                    print(" O ")
                    print("\|/")
                    print("/ \ ")
                    self.letraExistente.append(informe)
                    a.amig2()

                if (len(self.lista3))== 5:
                    print("Erro 5:",informe)
                    del self.letras[:]
                    del self.ajuda[:]
                    del self.salvar[:]
                    self.mais = [1]
                    del self.letraExistente[:]
                    del self.lista3[:]
                    del self.aux[:]
                    del self.saida[:]
                    del self.gambiarra[:]
                    del self.lista3[:]
                    self.dica1 = ""
                    self.dica2 = ""
                    self.dica3 = ""

                    c ="Palavra: ",self.chave," - Vencedor Desafiante: ",self.desafiante," - Perdedor Competidor: ",self.competidor
                    semAspas = (''.join(c))
                    print(semAspas)
                    b = str(semAspas)
                    self.historico += semAspas + "\n"
                    arquivo = open('jogo.txt','a')
                    arquivo.write(b + "\n")
                    arquivo.close()

                    while True:
                        print("\n\n\nHistórico de partidas\n",self.historico)
                        self.contador += 1
                        print("Número de partidas jogadas",self.contador)
                        print("Para Jogar Novamente Digite (1)\nPara Sair Digite (2):")
                        while True:
                            try:
                                opcao1 = input()
                                break
                            except:
                                print("Digite apenas os valores '1', ou '2' para prosseguir !!!")

                        if opcao1 == "1":
                            a.amig()
                            a.amig2()

                        if opcao1 == "2":
                            print("O Jogo Está Sendo Finalizado :( ...")
                            sys.exit()

                        if opcao1 != "1" or opcao1 != "2":
                            print("Digite Apenas Os Valores '1' ou '2'")

            else:

                for letra in self.chave:
                    if letra == informe:
                        self.saida[contador] = letra
                        self.letras.append(1)
                        self.letraExistente.append(informe)
                    contador += 1

                if (len(self.letras)) < (len(self.chave)):
                    print("Acertou")
                    print(''.join(self.saida))
                    a.amig2()
                    a.Opcao()

                if (len(self.letras)) == (len(self.chave)):
                    del self.letras[:]
                    del self.ajuda[:]
                    del self.salvar[:]
                    self.mais = [1]
                    del self.letraExistente[:]
                    del self.lista3[:]
                    del self.aux[:]
                    del self.saida[:]
                    del self.gambiarra[:]
                    del self.lista3[:]
                    self.dica1 = ""
                    self.dica2 = ""
                    self.dica3 = ""

                    c = "Palavra: ",self.chave," - Vencedor Competidor: ",self.competidor," - Perdedor Desafiante: ",self.desafiante
                    semAspas = (''.join(c))
                    print(semAspas)
                    b = str(semAspas)
                    self.historico += semAspas + "\n"
                    arquivo = open('jogo.txt','a')# escreva o conteúdo criado anteriormente nele.
                    arquivo.write(b + "\n")
                    arquivo.close()
                    while True:
                        print("\n\n\nHistórico de partidas\n",self.historico)
                        self.contador += 1
                        print("Número de partidas jogadas",self.contador)
                        print("Para Jogar Novamente Digite (1)\nPara Sair Digite (2):")
                        while True:
                            try:
                                opcao1 = input()
                                break
                            except:
                                print("Digite apenas os valores '1', ou '2' para prosseguir !!!")

                        if opcao1 == "1":
                            a.amig()
                            a.amig2()

                        if opcao1 == "2":
                            print("O Jogo Está Sendo Finalizado :( ...")
                            sys.exit()

                        if opcao1 != "1" or opcao1 != "2":
                            print("Digite Apenas Os Valores '1' ou '2'")

    def Dicas(self):
        print("----Dica----")
        if len(self.mais) == 1:
            print(self.gambiarra[0])
            self.mais.append(1)
            a.Opcao()
            a.amig2()

        if len(self.mais) == 2:
            print(self.gambiarra[1])
            self.mais.append(1)
            a.Opcao()
            a.amig2()

        if len(self.mais) == 3:
            print(self.gambiarra[2])
            self.mais.append(1)
            a.Opcao()
            a.amig2()

        if len(self.mais) > 3:
            print("Você já visualizou todas as suas dicas !!!")
            a.amig2()

a = Forca()
a.amig()
a.amig2()
a.Opcao()
a.Dicas()
