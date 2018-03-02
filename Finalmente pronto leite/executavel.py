from models.tanque import Tanque
from models.usuario import Usuario
from utils.utilidades import Extra
import sys

from factory.conexaoFactory import ConexaoFactory

from dao.tanqueDao import TanqueDao
from dao.usuarioDao import UsuarioDao


conn = ConexaoFactory().getconexao()

tanqueDao = TanqueDao(conn)
usuarioDao = UsuarioDao(conn)



os = Extra()


while True:





    print("--- (1) Logar como um usuario: ")
    print("--- (0) Sair: ")



    opcao = input()

    if opcao == '0':
        print("Saindo Do Sistema...")
        break







    if opcao == '1':

        while True:
            os.limpar()

            login = input("Informe o seu login:")

            if usuarioDao.LoginExistenteEntrar(login):
                senha = input("Informe sua senha: ")
                if usuarioDao.SenhaExistente(senha):
                    print("Entrando No Sistema !!!")











                    while True:

                        os.limpar()

                        print("--- (1) Cadastrar Tanque: ")
                        print("--- (2) Cadastrar Usuario: ")
                        print("--- (3) Pesquisar Todos/Tanques/Usuarios: ")
                        print("--- (4) Pesquisar por categorias do Tanque: ")
                        print("--- (5) Pesquisar por Cod/Tanque/Usuario: ")
                        print("--- (6) Excluir Por Cod/Tanque/Usuario: ")
                        print("--- (7) Deposito/Retirar De Um Tanque: ")
                        print("--- (8) Alterar/Tanque/Usuario: ")
                        print("--- (0) Sair: ")
                        opcao = input()



                        if opcao == '1':
                            while True:




                                while True:


                                    try:
                                        capacidade = float(input("Digite a capacidade do tanque: "))
                                        break
                                    except(ValueError):
                                        print("Digite apenas números !!!")




                                if capacidade < 0:
                                    capacidade = capacidade * (-1)
                                    tipo = input("Digite 1 - Pasteurizado 2 - Cru: ")


                                    if tipo == "1":
                                        tipo = "Pasteurizado"
                                        carga = 0
                                        print("Carga do tanque = ",carga)
                                        cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")
                                        if cor == '1':
                                            cor = "Azul"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '2':
                                            cor = "Vermelho"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '3':
                                            cor = "Verde"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '4':
                                            cor = "Roxo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '5':
                                            cor = "Amarelo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '6':
                                            cor = "Cinza"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '7':
                                            cor = "Preto"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '8':
                                            cor = "Laranja"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '9':
                                            cor = "Rosa"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '10':
                                            cor = "Violeta"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                            print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                            break

                                    if tipo == "2":
                                        tipo = "Cru"
                                        carga = 0
                                        #a = capacidade - (capacidade / 10)
                                        #capacidade = a
                                        print("Carga do tanque = ",carga)
                                        cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")
                                        #if (len(cor)) < 1:
                                            #print("Digite pelo menos uma cor válida")
                                            #break
                                        #else:
                                        if cor == '1':
                                            cor = "Azul"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '2':
                                            cor = "Vermelho"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '3':
                                            cor = "Verde"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '4':
                                            cor = "Roxo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '5':
                                            cor = "Amarelo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '6':
                                            cor = "Cinza"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '7':
                                            cor = "Preto"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '8':
                                            cor = "Laranja"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!")
                                            break

                                        elif cor == '9':
                                            cor = "Rosa"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '10':
                                            cor = "Violeta"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                            print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                            break



                                    if tipo != "1" or tipo != "2":
                                        print("Digite apenas '1' ou '2' para a escolha do tipo de leite !!!")
                                        break

                                if capacidade > 0:


                                    tipo = input("Digite 1 - Pasteurizado 2 - Cru")


                                    if tipo == "1":
                                        tipo = "Pasteurizado"
                                        carga = 0
                                        print("Carga do tanque = ",carga)
                                        cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")

                                        #if (len(cor)) < 1:
                                           # print("Digite pelo menos uma cor válida")
                                            #break
                                        #else:
                                        if cor == '1':
                                            cor = "Azul"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '2':
                                            cor = "Vermelho"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '3':
                                            cor = "Verde"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '4':
                                            cor = "Roxo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '5':
                                            cor = "Amarelo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '6':
                                            cor = "Cinza"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '7':
                                            cor = "Preto"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '8':
                                            cor = "Laranja"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '9':
                                            cor = "Rosa"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '10':
                                            cor = "Violeta"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break
                                        elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                            print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                            break


                                    if tipo == "2":
                                        tipo = "Cru"
                                        carga = 0


                                        print("Carga do tanque = ",carga)
                                        cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")
                                        #if (len(cor)) < 1:
                                            #print("Digite pelo menos uma cor válida")
                                            #break
                                        #else:
                                        if cor == '1':
                                            cor = "Azul"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso !!!")
                                            break


                                        elif cor == '2':
                                            cor = "Vermelho"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '3':
                                            cor = "Verde"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break


                                        elif cor == '4':
                                            cor = "Roxo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '5':
                                            cor = "Amarelo"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '6':
                                            cor = "Cinza"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '7':
                                            cor = "Preto"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '8':
                                            cor = "Laranja"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '9':
                                            cor = "Rosa"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor == '10':
                                            cor = "Violeta"
                                            tanque = Tanque(0,capacidade,tipo,carga,cor)
                                            tanqueDao.save(tanque)
                                            print("Tanque Salvo Com Sucesso!!!")
                                            break

                                        elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                            print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                            break


                                    if tipo != "1" or tipo != "2":
                                        print("Digite apenas '1' ou '2' para a escolha do tipo de leite !!!")
                                        break


                                else:
                                    print("Digite somente valores positivos para informar a capacidade do tanque")



                        elif opcao == '2':
                            while True:



                                login = input("Informe o seu login: ")
                                if (len(login)) == 0:
                                    print("Digite pelo menos um caracter para informar o login !!!")
                                else:
                                    if usuarioDao.LoginExistente(login):
                                        senha = input("Informe sua senha: ")
                                        usuario = Usuario(0,login,senha)
                                        usuarioDao.save(usuario)
                                        break

                                    else:
                                        print("Esse Login Já Existe... Digite outro !!!")



                        elif opcao == '3':
                            while True:


                                print("1 - Pesquisar Todos os Tanques: ")
                                print("2 - Pesquisar Todos os usuarios: ")
                                print("3 - Menu: ")
                                opcao = input()




                                if opcao == "1":

                                    listaTanques = tanqueDao.getLista()
                                    print("")
                                    print("TANQUE(S)")
                                    if(len(listaTanques)==0):
                                        print("TANQUES INEXISTENTES")
                                    for tanque in listaTanques:
                                        CARGA = float(tanque.carga)
                                        CAPACIDADE = float(tanque.capacidade)


                                        print(
                                            "COD: ",tanque.cod,"\nCAPACIDADE: ",tanque.capacidade,
                                            "\nTIPO: ",tanque.tipo,"\nCARGA: ",tanque.carga,"\nCOR: ",tanque.cor,"\nPERCENTUAL DE OCUPAÇÃO: ",CARGA / CAPACIDADE * 100,"%"
                                        )
                                        print("")



                                elif opcao == "2":
                                    listaUsuariro = usuarioDao.getLista()
                                    print("")
                                    print("USUARIO(S)")
                                    if(len(listaUsuariro)==0):
                                        print("USUARIOS INEXISTENTES")
                                    for usuario in listaUsuariro:
                                        print(
                                            "COD: ",usuario.cod,"\nLOGIN: ",usuario.login
                                            #"\nSENHA: ",usuario.senha
                                        )
                                        print("")

                                elif opcao == "3":
                                    print("Voltando ao Menu...")
                                    break

                                elif opcao != "1" or opcao != "2" or opcao != "3":
                                    print("Digite apenas '1,2,3' para escolha das opcoes !!!")


                                #AINDA FALTA A PARTE DO USUALY


                        elif opcao == '4':
                            while True:


                                print("--- Por qual opção deseja pesquisar ---")
                                print("--- (1) Capacidade: ")
                                print("--- (2) Tipo: ")
                                print("--- (3) Cor: ")
                                print("--- (4) Carga:")
                                print("--- (5) Menu: ")
                                opcaoCategoria = input()
                                if opcaoCategoria == '1':
                                    capacidades = input("Informe a capacidade do tanque: ")
                                    procurar = tanqueDao.getListaPesquisaCapacidade(capacidades)

                                    for Capacidade in procurar:
                                        #if (procurar!=None):

                                        print("**Dados do Tanque**")
                                        print("**** COD: ", Capacidade.cod)
                                        print("**** CAPACIDADE ", Capacidade.capacidade)
                                        print("**** TIPO: ", Capacidade.tipo)
                                        print("**** CARGA: ", Capacidade.carga)
                                        print("**** COR: ", Capacidade.cor)
                                        CARGA = float(Capacidade.carga)
                                        CAPACIDADE = float(Capacidade.capacidade)
                                        print("**** PERCENTUAL DE OCUPAÇÃO: ",CARGA / CAPACIDADE * 100)


                                        #else:
                                            #print("Capacidade Inexistente !!!")
                                            #break


                                elif opcaoCategoria == '2':
                                    tipos = input("Informe qual é o tipo do tanque: ")
                                    procurar = tanqueDao.getListaPesquisaTipo(tipos)

                                    for Tipo in procurar:
                                        #if (procurar!=None):
                                        print("**Dados do Tanque**")
                                        print("**** COD: ",Tipo .cod)
                                        print("**** CAPACIDADE ",Tipo.capacidade)
                                        print("**** TIPO: ",Tipo.tipo)
                                        print("**** CARGA: ",Tipo .carga)
                                        print("**** COR: ",Tipo.cor)
                                        CARGA = float(Tipo .carga)
                                        CAPACIDADE = float(Tipo.capacidade)
                                        print("**** PERCENTUAL DE OCUPAÇÃO: ",CARGA / CAPACIDADE * 100)

                                        #else:
                                            #print("Tipo Iexistente !!!")
                                            #break


                                elif opcaoCategoria == '3':
                                    cores = input("Informe a cor do Tanque: ")
                                    procurar = tanqueDao.getListaPesquisaCor(cores)

                                    for Cor in procurar:
                                        #if (procurar!=None):
                                        print("**Dados do Tanque**")
                                        print("**** COD: ",Cor.cod)
                                        print("**** CAPACIDADE ",Cor.capacidade)
                                        print("**** TIPO: ",Cor.tipo)
                                        print("**** CARGA: ",Cor.carga)
                                        print("**** COR: ",Cor.cor)
                                        CARGA = float(Cor.carga)
                                        CAPACIDADE = float(Cor.capacidade)
                                        print("**** PERCENTUAL DE OCUPAÇÃO: ",CARGA / CAPACIDADE * 100)

                                        #else:
                                            #print("Cor Inexistente !!!")
                                            #break


                                elif opcaoCategoria == '4':
                                    cargas = input("Informe a carga do Tanque: ")
                                    procurar = tanqueDao.getListaPesquisaCarga(cargas)

                                    for Carga in procurar:
                                        #if (procurar!=None):
                                        print("**Dados do Tanque**")
                                        print("**** COD: ",Carga.cod)
                                        print("**** CAPACIDADE ",Carga.capacidade)
                                        print("**** TIPO: ",Carga.tipo)
                                        print("**** CARGA: ",Carga.carga)
                                        print("**** COR: ",Carga.cor)
                                        CARGA = float(Carga.carga)
                                        CAPACIDADE = float(Carga.capacidade)
                                        print("**** PERCENTUAL DE OCUPAÇÃO: ",CARGA / CAPACIDADE * 100)

                                        #else:
                                            #print("Carga Inexistente !!!")
                                            #break



                                elif opcaoCategoria == '5':
                                    print("Voltando ao Menu...")
                                    break

                                elif opcao != "1" or opcao != "2" or opcao != "3":
                                    print("Digite apenas os valores '1,2,3,4,5!!!")

                        elif opcao == '5':
                            while True:


                                print("1 - Pesquisar Tanque: ")
                                print("2 - Pesquisar Usuario: ")
                                print("3 - Menu: ")
                                opcao = input()

                                if opcao == "1":
                                    while True:
                                        os.limpar()
                                        try:
                                            codes = int(input("Informe o cod do Tanque: "))
                                            break
                                        except:
                                            print("Digite apenas números !!!")
                                    tanque = tanqueDao.getTanque(codes)


                                    #for Cod in procurar:
                                    if (tanque!=None):
                                        print("**Dados do Tanque**")
                                        print("**** COD: ",tanque.cod)
                                        print("**** CAPACIDADE ",tanque.capacidade)
                                        print("**** TIPO: ",tanque.tipo)
                                        print("**** CARGA: ",tanque.carga)
                                        print("**** COR: ",tanque.cor)

                                    else:
                                        print("Tanque Inexistente !!!")


                                elif opcao == "2":
                                    while True:

                                        os.limpar()
                                        try:
                                            codes = int(input("Informe o cod do Usuario: "))
                                            break
                                        except:
                                            print("Digite apenas números !!!")

                                    usuario = usuarioDao.getListaPesquisa(codes)
                                    if (usuario!=None):
                                        print("COD: ",usuario.cod)
                                        print("LOGIN: ",usuario.login)
                                    else:
                                        print("Usuario Inexistente")


                                elif opcao == "3":
                                    print("Voltando ao menu...")
                                    break

                                elif opcao != "1" or opcao != "2" or opcao != "3":
                                    print("Digite apenas os valores '1,2,3'!!!")





                        elif opcao == '6':
                            while True:


                                print("1 - Excluir Tanque: ")
                                print("2 - Excluir Usuario: ")
                                print("3 - Menu: ")
                                opcao = input()

                                if opcao == "1":
                                    while True:
                                        os.limpar()
                                        try:
                                            cod = int(input("Informe o cod do tanque para excluir:"))
                                            break

                                        except:
                                            print("Digite apenas números !!!")
                                    tanque = tanqueDao.excluir(cod)
                                    print(tanque)

                                elif opcao == "2":
                                    while True:

                                        os.limpar()
                                        try:
                                            cod = int(input("Informe o cod do tanque para excluir:"))
                                            break
                                        except:
                                            print("Digite apenas números !!!")
                                    usuario = usuarioDao.excluir(cod)
                                    print(usuario)

                                elif opcao == "3":
                                    print("Voltando ao Menu...")
                                    break

                                elif opcao != "1" or opcao != "2" or opcao != "3":
                                    print("Digite apenas os valores '1,2,3' para a escolha das opcoes !!!")


                        elif opcao == '7':
                            while True:
                                print("1 - Deposito em um tanque: ")
                                print("2 - Retirar de um tanque: ")
                                print("3 - Menu: ")

                                opcao = input()

                                if opcao == '1':


                                    while True:


                                        try:
                                            cods = int(input("Digite o cod do tanque:"))
                                            break
                                        except:
                                            print("Digite apenas números !!!")

                                    while True:


                                        try:
                                            DEPOSITAR = float(input("Quanto deseja depositar:"))
                                            break
                                        except:
                                            print("Digite apenas números !!!")


                                    vai = tanqueDao.setCarga(cods,DEPOSITAR)
                                    print(vai)

                                elif opcao == '2':
                                    while True:


                                        try:
                                            cods = int(input("Digite o cod do tanque:"))
                                            break
                                        except:
                                            print("Digite apenas números !!!")

                                    while True:


                                        try:
                                            RETIRAR = float(input("Quanto deseja retirar:"))
                                            break
                                        except:
                                            print("Digite apenas números!!!")

                                    vai = tanqueDao.getCarga(cods,RETIRAR)
                                    print(vai)

                                elif opcao == "3":
                                    print("Voltando para o menu...")
                                    break

                                elif opcao != "1" or opcao != "2" or opcao != "3":
                                    print("Digite apenas o valores '1,2,3' !!!")




                        elif opcao == '8':
                            while True:


                                print("1 - Alterar Tanque: ")
                                print("2 - Alterar Usuario: ")
                                print("3 - Menu: ")
                                opcao = input()


                                if opcao == "1":
                                    while True:
                                        try:
                                            escreve = int(input("Digite o cod do tanque: "))
                                            altera = tanqueDao.alterar(escreve)
                                            break
                                        except:
                                            print("Digite apenas números !!!")
                                    if(altera !=None):
                                        print("COD: ",altera.cod)
                                        print("CAPACIDADE: ",altera.capacidade)
                                        print("TIPO: ",altera.tipo)
                                        print("CARGA: ",altera.carga)
                                        print("COR: ",altera.cor)
                                        while True:


                                            try:
                                                capacidade = float(input("Digite a capacidade do tanque: "))
                                                break
                                            except(ValueError):
                                                print("Digite apenas números !!!")




                                        if capacidade < 0:
                                            capacidade = capacidade * (-1)
                                            tipo = input("Digite 1 - Pasteurizado 2 - Cru")


                                            if tipo == "1":
                                                tipo = "Pasteurizado"
                                                carga = 0
                                                print("Carga do tanque = ",carga)
                                                cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")
                                                if cor == '1':
                                                    cor = "Azul"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '2':
                                                    cor = "Vermelho"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '3':
                                                    cor = "Verde"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '4':
                                                    cor = "Roxo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '5':
                                                    cor = "Amarelo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '6':
                                                    cor = "Cinza"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '7':
                                                    cor = "Preto"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '8':
                                                    cor = "Laranja"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '9':
                                                    cor = "Rosa"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '10':
                                                    cor = "Violeta"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                                    print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                                    break

                                            if tipo == "2":
                                                tipo = "Cru"
                                                carga = 0
                                                #a = capacidade - (capacidade / 10)
                                                #capacidade = a
                                                print("Carga do tanque = ",carga)
                                                cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")
                                                #if (len(cor)) < 1:
                                                    #print("Digite pelo menos uma cor válida")
                                                    #break
                                                #else:
                                                if cor == '1':
                                                    cor = "Azul"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '2':
                                                    cor = "Vermelho"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '3':
                                                    cor = "Verde"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '4':
                                                    cor = "Roxo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '5':
                                                    cor = "Amarelo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '6':
                                                    cor = "Cinza"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '7':
                                                    cor = "Preto"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '8':
                                                    cor = "Laranja"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '9':
                                                    cor = "Rosa"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '10':
                                                    cor = "Violeta"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break
                                                elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                                    print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                                    break



                                            if tipo != "1" or tipo != "2":
                                                print("Digite apenas '1' ou '2' para a escolha do tipo de leite !!!")


                                        if capacidade > 0:


                                            tipo = input("Digite 1 - Pasteurizado 2 - Cru")


                                            if tipo == "1":
                                                tipo = "Pasteurizado"
                                                carga = 0
                                                print("Carga do tanque = ",carga)
                                                cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")

                                                #if (len(cor)) < 1:
                                                   # print("Digite pelo menos uma cor válida")
                                                    #break
                                                #else:
                                                if cor == '1':
                                                    cor = "Azul"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '2':
                                                    cor = "Vermelho"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!")
                                                    break


                                                elif cor == '3':
                                                    cor = "Verde"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '4':
                                                    cor = "Roxo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '5':
                                                    cor = "Amarelo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '6':
                                                    cor = "Cinza"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '7':
                                                    cor = "Preto"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '8':
                                                    cor = "Laranja"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '9':
                                                    cor = "Rosa"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '10':
                                                    cor = "Violeta"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                                    print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                                    break


                                            if tipo == "2":
                                                tipo = "Cru"
                                                carga = 0


                                                print("Carga do tanque = ",carga)
                                                cor = input("Digite somente um único número para identificar a cor do seu tanque:\n1 - Azul\n2 - Vermelho\n3 - Verde\n4 - Roxo\n5 - Amarelo\n6 - Cinza\n7 - Preto\n8 - Laranja\n9 - Rosa\n10 - Violeta")
                                                #if (len(cor)) < 1:
                                                    #print("Digite pelo menos uma cor válida")
                                                    #break
                                                #else:
                                                if cor == '1':
                                                    cor = "Azul"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '2':
                                                    cor = "Vermelho"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '3':
                                                    cor = "Verde"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso !!!")
                                                    break

                                                elif cor == '4':
                                                    cor = "Roxo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '5':
                                                    cor = "Amarelo"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '6':
                                                    cor = "Cinza"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break


                                                elif cor == '7':
                                                    cor = "Preto"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '8':
                                                    cor = "Laranja"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor == '9':
                                                    cor = "Rosa"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!")
                                                    break

                                                elif cor == '10':
                                                    cor = "Violeta"
                                                    tanque = Tanque(escreve,capacidade,tipo,carga,cor)
                                                    tanqueDao.save(tanque)
                                                    print("Tanque Salvo Com Sucesso!!!")
                                                    break

                                                elif cor != '1' or cor != '2' or cor != '3' or cor != '4' or cor != '5' or cor != '6' or cor != '7' or cor != '8' or cor != '9' or cor != '10':
                                                    print("Digite apenas algum dos valores listados '1,2,3,4,5,6,7,8,9,10' para informar a cor do seu tanque !!!")
                                                    break




                                            if tipo != "1" or tipo != "2":
                                                print("Digite apenas '1' ou '2' para a escolha do tipo de leite !!!")


                                        else:
                                            print("Digite somente valores positivos para informar a capacidade do tanque")




                                    else:
                                        print("Tanque Inexistente")


                                elif opcao == '2':
                                    while True:
                                        try:
                                            alteraUsuario = int(input("Digite o cod do usuario: "))
                                            savecod = usuarioDao.alterar(alteraUsuario)
                                            break
                                        except:
                                            print("Digite Apenas Números !!!")




                                    if savecod !=None:
                                        print("COD: ",savecod.cod)
                                        print("LOGIN: ",savecod.login)
                                        print("Para Alterar, Confirme Seu Login e Senha !!!")

                                        while True:

                                            login = input("Informe o seu login:")
                                            if usuarioDao.LoginExistenteEntrar(login):
                                                senha = input("Informe sua senha: ")
                                                if usuarioDao.SenhaExistente(senha):
                                                    print("Verificado Com Sucesso")






                                                    print("Digite Seu Novo Login e Senha !!!")

                                                    login = input("Informe o seu login: ")


                                                    if(len(login)) == 0:
                                                        print("Digite pelo menos um caracter para informar o login !!!")
                                                    else:
                                                        if usuarioDao.LoginExistente(login):
                                                            senha = input("Informe sua senha: ")


                                                            usuario = Usuario(alteraUsuario,login,senha)
                                                            usuarioDao.save(usuario)



                                                            print("Dados Alterados Com Sucesso !!!")
                                                            break


                                                        else:
                                                            print("Esse Login Já Existe... Digite outro !!!")



                                                else:
                                                    print("Senha Inexistente!!!")


                                            else:
                                                print("Login Inexistente")



                                    else:
                                        print("Usuario Inexistente!!!")

                                elif opcao == '3':
                                    print("Voltando ao menu...")
                                    break

                                elif opcao != '1' or opcao != '2' or opcao != '3':
                                    print("Digite apenas os valores '1,2,3'")










                        elif opcao == '0':
                            print("Saindo do programa...")
                            sys.exit()


                else:
                    print("Senha incorreta... Digite novamente !!!")

            else:
                print("Login incorreto... Digite novamente!!!")
    else:
        print("Digite apenas '1,0' !!!")
