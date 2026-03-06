
def salvar_doc(nome, idade, salario):
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{nome},{idade},{salario}\n")

def cadastrar():
    nome = input("qual seu nome?")
    idade = input("qual sua idade?")
    salario = input("quanto você ganha")
    salvar_doc(nome, idade, salario)


def listar():
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            nome, idade, salario = linha.strip().split(",")
            print(f"Nome: {nome}, Idade: {idade}, Salario: {salario}")