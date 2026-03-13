from UTIL import cadastrar
from UTIL import listar
import os

opcao = str


while opcao != "0":
    os.system('clear')
    print("|1 - cadastrar  |  2 - listar  |  0 - sair|")
    opcao = input("qual opcao vc deseja?")
    match opcao:
        case "1":
            os.system('clear')
            cadastrar()
            print("cadastro feito")
        case "2":
            listar()
