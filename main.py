#Disciplina: Probabilidade e Estatistica
#Aluno: Paulo Vinicius Mota - 2014290074
#Lista 4 - Exercicio 8

#obs: So estava conseguindo testar os meus codigos nesse arquivo main. portanto, se caso nao funcione rodando os arquivos diretos tente copiar o codigo e colar aqui que vai funcionar corretamente

l1 = [] #Lista para inserção de valores
while True:#Repetição sem parametro de encerramento
    x= int(input('Digite o número (0 para encerrar): '))#ler os valores
    l1.append(x)#Lista com o parametro da inserção de valores
    if x == 0:#Condição para encerramento da repetição
        break
print ('O maior número da lista é: ',max(l1))#imprimi o maior numero da lista
  