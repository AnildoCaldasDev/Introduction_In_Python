# -*- coding: utf-8 -*-

arquivo = open(r'C:\Programacao\Lab-Python\LabUdemy\Introduction_In_Python\src\arquivo.txt')

#lista = arquivo.readlines()
lista = arquivo.read()

#print(lista)

w = open("C:\Programacao\Lab-Python\LabUdemy\Introduction_In_Python\src\\arquivo2.txt", "w")

count = 0
for linha in lista:
    w.writelines(linha)
    count = count + 1

w.close()
print(count)

w = open("C:\Programacao\Lab-Python\LabUdemy\Introduction_In_Python\src\\arquivo2.txt", "a")

w.write("Teste de ultima inserção")

w.close()
