"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""


N = int(input("Digite o número para verificar se "
              "ele faz parte da sequencia de fibonacci: "))

f3 = 0
f1 = 1
f2 = 1

if (N == 0 or N == 1):
    print("Faz parte da sequência de Fibonacci")

else:
    while f3 < N:
        f3 = f1 + f2
        f2 = f1
        f1 = f3
    if f3 == N:
        print("Faz parte da sequência de Fibonacci")
    else:
        print("NÃO faz parte da sequência de Fibonacci")
        