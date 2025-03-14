from datetime import date
from time import localtime

def saudacao():
    hour = localtime().tm_hour 
    if hour < 5 or hour >= 18:
        return print('Boa noite \n')
    if 5 <= hour < 12: 
        return print('Bom dia \n')
    if 12 <= hour < 18:
        return print('Boa tarde \n')

def menu():
    print('Menu: \n', '[1] Cadastrar receita \n', '[2] Cadastrar gasto \n', '[3] Ver lista  \n', '[4] Ver estatísticas \n', '[5] Sair do programa \n')
    global opt 
    opt = ''
    options = (1, 2, 3, 4, 5)
    while opt not in options:
        opt = int(input('Digite o número da opção: '))
        if opt not in options:
            print('Opção inválida! Digite um número de 1 a 5: ')
    return opt

def cadastrar_transação(a):
    data_padrao = date.today().strftime('%d/%m/%Y')
    transação = {}
    if a == 0:
        transação['id'] = ''
        transação['tipo'] = 'recebimento'
        transação['data'] = input(f'Data (tecle enter para data de hoje): ')
        if not transação['data']:
            transação['data'] == data_padrao
        transação['valor'] = float(input('Valor: '))
        transação['categ'] = input('Categoria: ')
        transação['orig'] = input('Pagante: ')
        transação['obs'] = input('Observações: ')
        print('Receita cadastrada com sucesso.')
    if a == 1:
        transação['id'] = ''
        transação['tipo'] = 'pagamento'
        transação['data'] = input(f'Data (tecle enter para data de hoje): ')
        if not transação['data']:
            transação['data'] = data_padrao
        transação['valor'] = float(input('Valor: '))
        transação['categ'] = input('Categoria: ')
        transação['orig'] = input('Favorecido: ')
        transação['obs'] = input('Observações: ')
        print('Gasto cadastrado com sucesso.')
    return(transação.copy())

