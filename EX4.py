"""4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora."""

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = (sp + rj + mg + es + outros)

estado = input('Digite o estado desejado (sp/rj/mg/es/outros):')

if estado == 'sp':
    print(f'A porcentagem total de SP é:{(sp/total)*100:2f}%')
elif estado =='rj':
    print(f'A porcentagem total do RJ é:{(rj/total)*100:2f}%')
elif estado =='mg':
    print(f'A porcentagem total de MG é:{(mg/total)*100:2f}%')
elif estado =='es':
    print(f'A porcentagem total do ES é:{(es/total)*100:2f}%')
elif estado =='outros':
    print(f'A porcentagem total dos outros estados é:{(outros/total)*100:2f}%')
