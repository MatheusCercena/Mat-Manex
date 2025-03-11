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
while opt not in options :
    try:
        opt = int(input('Digite o número da opção: '))
        if opt not in options:
            print('Por favor, digite um número de 1 a 5: ')
    except ValueError:
        print('Por favor, digite um número de 1 a 5: ')

if opt == 1:
    cadastrar_receita()
elif opt == 2:
    
    lista_de_gastos = []
    lista_de_gastos.append(cadastrar_gasto())
    print(*lista_de_gastos[1])

# elif opt == 3:
#     ver_lista()
# elif opt == 4:
#     ver_estatisticas()
elif opt == 5:
    sys.exit   
else:
    print('Por favor, digite um número de 1 a 5.')
