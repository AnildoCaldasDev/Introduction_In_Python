
def pares(i):
    if i % 2 == 0:
        return i

lista = [2,4,1,5,8,7,9,12,23,15]

lista_pares = filter(pares, lista)
print(list(lista_pares))