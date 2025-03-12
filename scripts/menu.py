from time import localtime
import sys
from menu_functions import cadastrar_gasto, cadastrar_receita

hour = localtime().tm_hour 
if hour < 8 or hour >= 18:
    print('Boa noite \n')
if 8 <= hour < 12: 
    print('Bom dia \n')
if 12 <= hour < 18:
    print('Boa tarde \n')

print('Menu: \n', 
'[1] Cadastrar receita \n',
'[2] Cadastrar gasto \n',
'[3] Ver lista  \n',
'[4] Ver estatísticas \n',
'[5] Sair do programa \n',
)
opt = ''
options = (1, 2, 3, 4, 5)
while opt not in options:
    opt = int(input('Digite o número da opção: '))
    if opt not in options:
        print('Opção inválida! Digite um número de 1 a 5: ')


lista_de_transações = []
# lista_de_receitas = []
# lista_de_gastos = []

# if opt == 1:
#     while True:
#         lista_de_receitas.append(cadastrar_receita())
#         res = input('Aperte enter para cadastrar outra receita ou qualquer outra tecla para parar.')
#         if res != '':
#             break
#     cadastrar_receita()
# elif opt == 2:
#     while True:
#         lista_de_gastos.append(cadastrar_gasto())
#         res = input('Aperte enter para cadastrar outro gasto ou qualquer outra tecla para parar.')
#         if res != '':
#             break
# elif opt == 3:
#     # ver_lista()
    
#     for receita in lista_de_receitas:
#         print(f'Valor: {receita['valor']} - Categoria: {receita['categ']} - Pagante: {receita['pag']} - Observações: {receita['obs']}')
#     for gasto in lista_de_gastos:
#         print(f'Valor: {gasto['valor']}\n Categoria: {gasto['categ']} \n Favorecido: {gasto['fav']} \n Observações: {gasto['obs']}')

# # elif opt == 4:
# #     ver_estatisticas()
# else:
#     sys.exit   
