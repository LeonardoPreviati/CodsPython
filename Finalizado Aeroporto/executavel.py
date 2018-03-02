from modelo.aeroporto import Aeroporto
from modelo.voo import Voo
from modelo.passageiro import Passageiro


from fabrica.conexaoFactory import ConexaoFactory



from dao.aeroportoDao import AeroportoDao
from dao.vooDao import VooDao
from dao.passageiroDao import PassageiroDao




conn = ConexaoFactory().getconexao()



#numlist = []
aeroportoDao = AeroportoDao(conn)
vooDao = VooDao(conn)
passageiroDao = PassageiroDao(conn)




while True:


    print("--- (1) Cadastrar: ")
    print("--- (2) Pesquisar tudo: ")
    print("--- (3) Deletar: ")
    print("--- (4) Alterar: ")
    print("--- (5) Pesquisar por ID: ")
    print("--- (6) Pesquisar/Voo/Categoria: ")
    print("--- (7) Confirmar Reserva: ")
    print("--- (8) Cancerlar Reserva")
    print("--- (0) Sair: ")

    opcao = input()








    if opcao == "1":
        while True:
            print("--- (1) Aeroporto: ")
            print("--- (2) Voo: ")
            print("--- (3) Passageiro: ")
            print("--- (4) Menu: ")
            opcao2 = input()



            if opcao2 == '1':


                    nome = input("Informe o nome: ")
                    if (len(nome)) < 1:
                        print("Digite pelo menos 1 caracter para informar o nome do aeroporto")

                    else:
                        if(aeroportoDao.NomeExistente(nome.upper())):

                            sigla = input("Informe a sigla: ")
                            if (len(sigla)) < 1:
                                print("Digite pelo menos 1 caracter para informar a sigla do aeroporto")
                            else:

                                aeroporto = Aeroporto(0,nome,sigla)
                                aeroportoDao.salvar(aeroporto)
                                print("Dados Salvos Com Sucesso !!! ")
                                break
                        else:
                            print("Nome do aeroporto já cadastrado")



            if opcao2 == '2':

                numero = input("Informe o número do Voo: ")
                #voo = vooDao.NumeroExistente(numero)
                if (len(numero)) < 1:
                    print("Digite pelo menos 1 caracter para informar o numero do voo")
                else:

                    #print(voo)
                    if(vooDao.NumeroExistente(numero)):
                        origem = input("Informe a origem: ")
                        if (len(origem)) < 1:
                            print("Digite pelo menos 1 caracter para informar a origem do voo")
                        else:
                            destino = input( "Informe o destino: ")
                            if (len(destino)) < 1:
                                print("Digite pelo menos 1 caracter para informar o destino do voo")
                            else:
                                while True:
                                    try:
                                        lugares = int(input("Informe os lugares: "))
                                        break
                                    except:
                                        print("Digite apenas números !!!")
                                if lugares == 0:
                                    lugares = 15
                                    voo = Voo(0,numero,origem,destino,lugares)
                                    vooDao.salvar(voo)
                                    print("Dados Salvos Com Sucesso !!! ")
                                    break
                                else:
                                    voo = Voo(0,numero,origem,destino,lugares)
                                    vooDao.salvar(voo)
                                    print("Dados Salvos Com Sucesso !!! ")
                                    break
                    else:
                        print("numero do voo ja cadastrado")





            if opcao2 == '3':
                nome = input("Informe o seu nome: ")
                if (len(nome)) < 1:
                    print("Digite pelo menos 1 caracter para informar o seu nome")
                else:
                    cpf = input("Informe o seu cpf: ")
                    if (len(cpf)) < 11:
                        print("Digite pelo menos 11 caracters para informar o seu cpf")
                    else:
                        while True:
                            try:
                                idade = int(input("Informe a sua idade: "))
                                break
                            except:
                                print("Digite apenas números !!!")
                        passageiro = Passageiro(0,nome,cpf,idade)
                        passageiroDao.salvar(passageiro)
                        print("Dados Salvos Com Sucesso !!! ")
                        break

            if opcao2 == '4':
                print("Voltando ao Menu...")
                break


            if opcao2 != '1' or opcao2 != '2' or opcao2 != '3' or opcao2 != '4':
                print("Digite apenas (1), (2), (3), (4) !!!")



    elif opcao == '2':
        listaAeroporto = aeroportoDao.pesquisar()
        print("")
        print("AEROPORTO(S)")
        if(len(listaAeroporto)==0):
            print("AEROPORTOS INEXISTENTES")
        for aeroporto in listaAeroporto:
            print(
                "ID:",aeroporto.id,"\nNOME:",aeroporto.nome,
                "\nSIGLA:",aeroporto.sigla
            )
            print("")


        listaVoo = vooDao.pesquisar()

        print("")
        print("VOO(S)")
        if(len(listaVoo)==0):
            print("VOOS INEXISTENTES")
        for voo in listaVoo:

            print(
                "ID:",voo.id,"\nNUMERO:",voo.numero,"\nORIGEM:",voo.origem,
                "\nDESTINO:",voo.destino,"\nLUGARES:",voo.lugares
            )
            print("")



        listaPassageiro = passageiroDao.pesquisar()
        print("")
        print("PASSAGEIRO(S)")
        if(len(listaPassageiro)==0):
            print("PASSAGEIROS INEXISTENTES")
        for passageiro in listaPassageiro:
            print(
                "ID:",passageiro.id,"\nNOME:",passageiro.nome,
                "\nCPF:",passageiro.cpf,"\nIDADE:",passageiro.idade
            )

            print("")



    elif opcao == '3':
        while True:
            print("--- Qual deseja excluir ---")
            print("--- (1) Aeroporto: ")
            print("--- (2) Voo: ")
            print("--- (3) Passageiro: ")
            print("--- (4) Menu: ")
            opcao = input()


            if opcao == "1":
                while True:
                    try:
                        parametro = int(input("Informe o ID do Aeroporto:"))
                        break
                    except:
                        print("Informe somente números")

                a = aeroportoDao.excluir(parametro)
                print(a)
                break


            if opcao == "2":
                while True:
                    try:
                        parametro = int(input("Informe o ID do Voo:"))
                        break
                    except:
                        print("Informe somente números")
                b = vooDao.excluir(parametro)
                print(b)
                break


            if opcao == "3":
                while True:
                    try:
                        parametro = int(input("Informe o ID do Passagerio:") )
                        break
                    except:
                        print("Informe somentes números")
                c = passageiroDao.excluir(parametro)
                print(c)
                break


            if opcao == '4':
                print("Voltando ao Menu...")
                break

            if opcao != "1" or opcao != "2" or opcao != "3" or opcao != "4":
                print("Digite apenas (1), (2), (3), (4) !!!")



    elif opcao == '4':
        while True:
            print("--- Qual deseja alterar ---")
            print("--- (1) Aeroporto: ")
            print("--- (2) Voo: ")
            print("--- (3) Passageiro: ")
            print("--- (4) Menu: ")
            opcao2 = input()
            if opcao2 == "1":
                while True:
                    try:
                        idaero = int( input("Informe o ID do Aeroporto: "))
                        break
                    except:
                        print("Digite apenas números !!!")
                aeroporto = aeroportoDao.alterar(idaero)
                if(aeroporto!=None):
                    print("**Dados do Aeroporto**")

                    print("**** ID: ",aeroporto.id)
                    print("**** NOME: ",aeroporto.nome)
                    print("**** SIGLA: ",aeroporto.sigla)



                    nome = input("Informe o nome do Aeroporto: ")
                    if (len(nome)) < 1:
                        print("Digite pelo menos 1 caracter para informar o nome do aeroporto")
                    else:
                        sigla = input("Informe a sigla: ")
                        if (len(sigla)) < 1:
                            print("Digite pelo menos 1 caracter para informar a sigla do aeroporto")
                        else:
                            aeroporto = Aeroporto(idaero,nome,sigla)
                            aeroportoDao.salvar(aeroporto)
                            print("Dados Salvos")
                            break
                else:
                    print("Aeroporto Inexistente !!!")
                    break


            if opcao2 == "2":
                while True:
                    try:
                        idvoo = int( input("Informe o ID do Voo: "))
                        break
                    except:
                        print("Digite apenas números !!!")
                voo = vooDao.alterar(idvoo)
                if(voo!=None):
                    print("**Dados do Voo**")
                    print("**** ID: ",voo.id)
                    print("*** NÚMERO ",voo.numero)
                    print("**** ORIGEM: ",voo.origem)
                    print("**** DESTINO: ",voo.destino)
                    print("**** LUGARES: ",voo.lugares)

                    numero = input("Informe o novo número: ")
                    if (len(numero)) < 1:
                        print("Digite pelo menos 1 caracter para informar o número do voo")
                    else:
                        origem = input("Informe a nova origem: ")
                        if (len(origem)) < 1:
                            print("Digite pelo menos 1 caracter para informar a origem do voo")
                        else:
                            destino = input("Informe o novo destino: ")
                            if (len(destino)) < 1:
                                print("Digite pelo menos 1 caracter para informar o destino do voo")
                            else:
                                while True:
                                    try:
                                        lugares = int(input("Informe os lugares: "))
                                        break
                                    except:
                                        print("Digite apenas números !!!")

                                voo = Voo(idvoo,numero,origem,destino,lugares)
                                vooDao.salvar(voo)
                                print("Dados Salvos")
                                break
                else:
                    print("Voo Inexistente !!!")
                    break


            if opcao2 == "3":
                while True:
                    try:
                        passageiroid = int( input("Informe o ID do Passageiro: "))
                        break
                    except:
                        print("Digite apenas números !!!")
                passageiro = passageiroDao.alterar(passageiroid)
                if(passageiro!=None):
                    print("**Dados do Passageiro**")
                    print("**** ID: ",passageiro.id)
                    print("**** NOME: ",passageiro.nome)
                    print("**** CPF: ",passageiro.cpf)
                    print("**** IDADE: ",passageiro.idade)

                    nome = input("Digite o novo nome: ")
                    if (len(nome)) < 1:
                        print("Digite pelo menos 1 caracter para informar o nome do passageiro")
                    else:
                        cpf = input("Digite o novo cpf: ")
                        if (len(cpf)) < 11:
                            print("Digite pelo menos 11 caracters para informar o cpf do passageiro")
                        else:
                            while True:
                                try:
                                    idade = int(input("Digite a sua nova idade: "))
                                    break
                                except:
                                    print("Digite apenas números !!!")
                            passageiro = Passageiro(passageiroid,nome,cpf,idade)
                            passageiroDao.salvar(passageiro)
                            print("Dados Salvos")
                            break
                else:
                    print("Passageiro Inexistente !!!")
                    break
            if opcao2 == "4":
                print("Voltando ao Menu...")
                break


            if opcao2 != "1" or opcao2 != "2" or opcao2 != "3" or opcao2 != "4":
                print("Digite apenas (1), (2), (3), (4) !!!")











    elif opcao == '5':
        while True:
            print("--- Qual deseja pesquisar---")
            print("--- (1) Aeroporto: ")
            print("--- (2) Voo: ")
            print("--- (3) Passageiro: ")
            print("--- (4) Menu: ")
            opcao1 = input()


            if opcao1 == "4":
                print("Voltando ao Menu...")
                break




            if opcao1 == "1":
                while True:
                    try:
                        idaeroportos = int( input("Informe o ID do Aeroporto: "))
                        break
                    except:
                        print("Digite apenas números !!!")
                aeroporto = aeroportoDao.alterar(idaeroportos)
                if(aeroporto!=None):
                    print("**Dados do Aeroporto**")
                    print("**** ID: ",aeroporto.id)
                    print("**** NOME: ",aeroporto.nome)
                    print("**** SIGLA: ",aeroporto.sigla)
                else:
                    print("Aeroporto Inexistente !!!")
                break


            elif opcao1 == "2":
                while True:
                    try:
                        voosid = int( input("Informe o ID do Voo: "))
                        break
                    except:
                        print("Digite apenas números !!!")
                voo = vooDao.alterar(voosid)
                if(voo!=None):
                    print("**Dados do Voo**")
                    print("**** ID: ",voo.id)
                    print("**** NÚMERO ",voo.numero)
                    print("**** ORIGEM: ",voo.origem)
                    print("**** DESTINO: ",voo.destino)
                    print("**** LUGARES: ",voo.lugares)
                else:
                    print("Voo Inexistente !!!")
                break


            elif opcao1 == "3":
                while True:
                    try:
                        passageiroids = int( input("Informe o ID do Passageiro: "))
                        break
                    except:
                        print("Digite apenas números !!!")
                passageiro = passageiroDao.alterar(passageiroids)
                if (passageiro!=None):
                    print("**Dados do Passageiro**")
                    print("**** ID: ",passageiro.id)
                    print("**** NOME: ",passageiro.nome)
                    print("**** CPF: ",passageiro.cpf)
                    print("**** IDADE: ",passageiro.idade)
                else:
                    print("Passageiro Inexistente !!!")
                break




            elif opcao1 != "1" or opcao1 != "2" or opcao1 != "3" or opcao1 != "4":
                print("Digite apenas (1), (2), (3), (4) !!!")




    elif opcao == '6':
        while True:
            print("--- Por qual opção deseja pesquisar ---")
            print("--- (1) Numero: ")
            print("--- (2) Origem: ")
            print("--- (3) Destino: ")
            print("--- (4) Menu: ")

            opcao = input()
            listar = []




            if opcao == "1":
                numeros = input("Informe o número do Voo: ")
                procurar = vooDao.PesquisarNumero(numeros.capitalize())

                for voo in procurar:
                    if (procurar!=None):
                        print("**Dados do Voo**")
                        print("**** ID: ",voo.id)
                        print("**** NÚMERO ",voo.numero)
                        print("**** ORIGEM: ",voo.origem)
                        print("**** DESTINO: ",voo.destino)
                        print("**** LUGARES: ",voo.lugares)
                        break
                    else:
                        print("Número Inexistente")
                        break


            elif opcao == "2":
                voosid = input("Informe a origem do voo: ")
                voos = vooDao.PesquisarOrigem(voosid.capitalize())
                #print(len(voos))
                for voo in voos:
                    if (voos!=None):
                        print("**Dados do Voo**")
                        print("**** ID: ",voo.id)
                        print("**** NÚMERO ",voo.numero)
                        print("**** ORIGEM: ",voo.origem)
                        print("**** DESTINO: ",voo.destino)
                        print("**** LUGARES: ",voo.lugares)
                        break
                    else:
                        print("Origem Inexistente")
                        break






            elif opcao == "3":
                voosid = input("Informe o destino do voo: ")
                destinar = vooDao.PesquisarDestino(voosid.capitalize())
                #print(len(voos))
                for voo in destinar:
                    if (destinar!=None):
                        print("**Dados do Voo**")
                        print("**** ID: ",voo.id)
                        print("**** NÚMERO ",voo.numero)
                        print("**** ORIGEM: ",voo.origem)
                        print("**** DESTINO: ",voo.destino)
                        print("**** LUGARES: ",voo.lugares)
                        break
                    else:
                        print("Destino Inexistente")
                        break




            elif opcao == "4":
                print("Voltando ao Menu...")
                break

            elif opcao != "1" or opcao != "2" or  opcao != "3" or  opcao != "4":
                print("Digite apenas (1), (2), (3), (4) !!!")

    elif opcao == "7":



        numero = (input("Informe o número do Voo: "))
        voo = vooDao.ConfirmarReserva(numero)
        print(voo)







    elif opcao == "8":

      numero = (input("Informe o número do Voo: "))
      voo = vooDao.CancelarReserva(numero)
      print(voo)





    elif opcao == '0':
        print("O programa foi finalizado...")
        break
    else:
        print("Opção Inválida!")
