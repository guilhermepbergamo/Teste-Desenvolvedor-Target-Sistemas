"""3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;"""


import json
import sys


with open('dados.json') as f:
    data = json.load(f)
    print(data)

maiorvalor = numerodias = media = diasmedia = contador = 1
menorvalor = sys.maxsize
 
for i in data:
    if i['valor'] != 0:
        if menorvalor > i['valor']:
            menorvalor = i['valor']
        if maiorvalor < i['valor']:
            maiorvalor = i['valor'] 
       
print(f'O maior valor foi de: {maiorvalor}')
print(f'O menor valor foi de: {menorvalor}')


if i['valor'] > media:  
    contador += 1
for i in data:
    media = (i['valor'] + media) / contador
    if i['valor'] > media:
        diasmedia += 1 
print(f'A média foi de: {media}')
print(f'A quantidade de dias com valor acima da média foi: {diasmedia}')
