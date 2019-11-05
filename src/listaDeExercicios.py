# -*- coding: utf-8 -*-
# 1-Faca um programa que receba a idade de um usuario e digaseeleeh maior ou menor de idade.

# idade = input("Informe sua idade")

# if idade > 18 :
#     print("Usuario maior de idade")
# else:
#     print("Menor de idade")

# 2- faca um programa que receba 5 notas de um usuario e se a media das notas for maiorque 6 imprima aprovado,
# senao reprovado

#notas = []

'''qtd = input("Quantas notas deseja receber: ")
soma = 0

for count in range(0, qtd) :
    nota = input("Informe a nota numero " + str(count + 1) + ":  ")
    #notas.insert(count, nota)
    soma = soma + nota

media = (soma / qtd)

if media >= 6:
    print("Voce esta aprovado \n")
else:
    print("Voce foi reprovado \n")

print("Sua nota foi: " + str(media))'''

# 3 - Faca umprograma que resolva uma equacao do segundo grau: formula: a² + bx + c
# (-b +- sqtr(b2-4ac))/2

'''from math import sqrt
a = input("Informe o valor de a : ")
b = input("Informe o valor de b : ")  
c = input("Informe o valor de c : ") 

delta = b**2 - 4*a*c
raiz_delta = sqrt(delta)

x1 = (-b + raiz_delta)/2*a
x2 = (-b - raiz_delta)/2*a

print("x1 = %d" %x1)
print("x2 = %d" %x2)'''

# 4 - Crie um programa queorden umalista com 3 elementos:
lista =[2,6,12]
lista.sort()
print(lista)






