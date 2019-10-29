a = "Anildo"
b = "Caldas"

nome = a + " " + b

print(nome)

tamanho = len(nome)

print(tamanho)

#print(nome[10])
print(nome[0:])
print(nome[1:])

print(nome.lower())
print(nome.upper())

nomecomespaco = "  Anildo  calds   "
print(nomecomespaco.strip())

alfabeto = "A B C D E F G H I"
lista_Alfabeto = alfabeto.split()

print(lista_Alfabeto)

for lis in lista_Alfabeto:
    print(lis + " teste")

buscaC = alfabeto.find("C")
print(buscaC)

alfabeto = alfabeto.replace("F", "f")

print(alfabeto)




