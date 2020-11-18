#Disciplina: Probabilidade e Estatistica
#Aluno: Paulo Vinicius Mota - 2014290074
#Lista 4 - Exercicio 9

x= int(input('Digite o número: '))#ler os valor a ser calculado

mil = x // 1000 % 10 #Faz o operação de retirada do numero de milhar
cen = x // 100 % 10 #Faz o operação de retirada do numero de centena
dez = x // 10 % 10 #Faz o operação de retirada do numero de dezena
uni = x // 1 % 10 #Faz o operação de retirada do numero de unidade


print("Numero inteiro {}".format(x)) #Imprimi o numero inteiro
print("Milhar {}".format(mil)) #Imprimi o numero correspondente ao milhar
print("Centena {}".format(cen)) #Imprimi o numero correspondente a centena
print("Dezena {}".format(dez)) #Imprimi o numero correspondente a dezena
print("Unidade {}".format(uni)) #Imprimi o numero correspodente a unidade