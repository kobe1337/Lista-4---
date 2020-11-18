#Disciplina: Probabilidade e Estatistica
#Aluno: Paulo Vinicius Mota - 2014290074
#Lista 4 - Exercicio 7

n = int(input("Digite apenas um numero de 1 a 4: "))#ler o valor digitado

if n > 4 or n < 1:#Verifica se o numero digitado é maior que 4 ou menor que 1
  print("Entrada invalida: ")#mensagem validando a verificação
  n = int(input("Digite apenas um numero de 1 a 4: "))#Solicita o numero novamente
else:
  print(n)# Caso o numero esteja entre 1 e 4 ele mostra o valor do numero
