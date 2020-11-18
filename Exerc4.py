#Disciplina: Probabilidade e Estatistica
#Aluno: Paulo Vinicius Mota - 2014290074
#Lista 4 - Exercicio 4


l1 = int(input("Digite o valor do primeiro lado do triangulo: "))#ler o primeiro valor
l2 = int(input("Digite o valor do segundo lado do triangulo: "))#ler o segundo valor
l3 = int(input("Digite o valor do terceiro lado do triangulo: "))#ler o terceiro valor

if (l1 + l2 < l3) or (l1 + l3 < l2) or (l2 + l3 < l1): #Verifica se a soma de dois lados é menmor que a de um ultimo lado
   print('Nao é um triangulo')#imprimi o resultado do triangulo
elif (l1 == l2) and (l1 == l3):# Verifica se todos os lados sao iguais
  print("Triangulo Equilatero")#imprimi o resultado do triangulo
elif(l1 == l2) or (l1 == l3) or (l2 == l3): #Verifica se dois lados sao iguais
  print("Triagunlo Isoseles")#imprimi o resultado do triangulo
else:
  print("Triangulo Escaleno")#imprimi o resultado do triangulo
   