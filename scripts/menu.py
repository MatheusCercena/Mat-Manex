from time import localtime
import sys
from menu_functions import cadastrar_transação, menu
from keyboard import is_pressed

hour = localtime().tm_hour 
if hour < 5 or hour >= 18:
    print('Boa noite \n')
if 5 <= hour < 12: 
    print('Bom dia \n')
if 12 <= hour < 18:
    print('Boa tarde \n')

menu_opt = menu()
lista_de_transações = []

if menu_opt == 1:
    while True:
        lista_de_transações.append(cadastrar_transação(0))
        lista_de_transações[-1]['id'] = len(lista_de_transações)
        res = input('Aperte enter para cadastrar outra receita ou qualquer outra tecla para parar.')
        if res != '':
            break
elif menu_opt == 2:
    while True:
        lista_de_transações.append(cadastrar_transação(1))
        lista_de_transações[-1]['id'] = len(lista_de_transações)
        res = input('Aperte enter para cadastrar outro gasto ou esc para parar.')
        if res != '':
            break
else:
    sys.exit   

menu_opt = menu()

print('Lista de transações \n', lista_de_transações)
