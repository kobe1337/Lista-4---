#Disciplina: Probabilidade e Estatistica
#Aluno: Paulo Vinicius Mota - 2014290074
#Lista 4 - Exercicio 1

l = int(input("Digite a quantidade de lados: "))
m = float(input("Digite a medidade do lado: "))

if l == 3:  #Condicional Verificando se foi digitado 3 lados
    a = l**2 * 3**(1 / 2) / 4  #Calculo da Area do Triangulo
    print("A figura é um triangulo: ")
    print(a)
elif l == 4:  #Condicional Verificando se foi digitado 4 lados
    a = l**2  #Calculo da Area do Quadrado
    print("A figura é um quadrado: ")  #Imprindo o valor da area do quadrado
    print(a)
elif l == 5:  #Condicional Verificando se foi digitado 5 lados
    print("A figura é um poligono")  #Imprindo o valor da area do quadrado
    print(a)
