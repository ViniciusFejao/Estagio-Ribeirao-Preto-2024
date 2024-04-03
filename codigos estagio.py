import os

#Estágio Ribeirão Preto - 2024

#1) Observe o trecho de código abaixo:

INDICE = int(13)
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K
    #print(SOMA)

print(SOMA)

#R: valor da SOMA é 91.

'''2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma
 dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem
 que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma 
 mensagem avisando se o número informado pertence ou não a sequência.'''

Num1 = 0
Num2 = 1
Num3 = 0

X = int(input("Informe um número: "))
while Num3 < X:
    Num3 = Num2 + Num1
    Num1 = Num2
    Num2 = Num3

if X == 0 or X == 1 or X == Num3:
    print("O número informado pertence a sequência de Fibonacci")
else:
    print("O número informado não pertence a sequência de Fibonacci")

#5)  Escreva um programa que inverta os caracteres de um string.

string = str(input("Insira uma string: "))
invertida = string[::-1]
print(invertida)