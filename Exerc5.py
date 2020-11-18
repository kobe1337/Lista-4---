#Disciplina: Probabilidade e Estatistica
#Aluno: Paulo Vinicius Mota - 2014290074
#Lista 4 - Exercicio 5


l1 = int(input("Digite o valor do primeiro Angulo: "))#ler o primeiro angulo
l2 = int(input("Digite o valor do segundo Angulo: "))#ler o segundo angulo
l3 = int(input("Digite o valor do terceiro Angulo: "))#ler o terceiro angulo

if l1 == 90 or l2 == 90 or l3 == 90:#Verifica se todas os numeros digitados sao iguais a 90
  print("É um triângulo retangulo")#imprimi o valor do triangulo
elif l1 < 90 and l2 < 90 and l3 < 90:#Verifica se todos os numeros digitados sao menores que 90
  print("É um triâgunlo Acutângulo")#imprimi o valor do triangulo
else:#Verifica se os valores foram maior que 90
  print("É um triagunlo Obtusângulo")#imprimi o valor do triangulo
