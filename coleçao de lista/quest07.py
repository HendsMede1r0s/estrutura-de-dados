p1 = {"nome": "A", "pontos": 10}
p2 = {"nome": "B", "pontos": 50}
p3 = {"nome": "C", "pontos": 30}

lista = [p1, p2, p3]
lista.sort(key=lambda x: x["pontos"], reverse = True)
print(lista)

