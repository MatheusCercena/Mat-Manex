from time import localtime
import sys
from menu_functions import cadastrar_transação

hour = localtime().tm_hour 
if hour < 5 or hour >= 18:
    print('Boa noite \n')
if 5 <= hour < 12: 
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

if opt == 1:
    while True:
        lista_de_transações.append(cadastrar_transação(0))
        res = input('Aperte enter para cadastrar outra receita ou qualquer outra tecla para parar.')
        if res != '':
            break
elif opt == 2:
    while True:
        lista_de_transações.append(cadastrar_transação(1))
        res = input('Aperte enter para cadastrar outro gasto ou qualquer outra tecla para parar.')
        if res != '':
            break
# elif opt == 3:
#     # ver_lista()
    
# elif opt == 4:
#     ver_estatisticas()
else:
    sys.exit   

print('Lista de transações')

for transação in lista_de_transações:
    print(f'Tipo: {transação['tipo']} \nData: {transação['data']} \nValor: {transação['valor']} \nCategoria: {transação['categ']} \nFavorecido: {transação['orig']} \nObservações: {transação['obs']}')
