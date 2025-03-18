from datetime import date
from datetime import datetime
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
    transação = {}
    if a == 0:
        transação['id'] = ''
        transação['tipo'] = 'Recebimento'
        transação['data'] = validar_data(input(f'Data (tecle enter para data de hoje): '))
        transação['valor'] = float(input('Valor: '))
        transação['categ'] = input('Categoria: ')
        transação['orig'] = input('Pagante: ')
        transação['obs'] = input('Observações: ')
        print('Receita cadastrada com sucesso.')
    if a == 1:
        transação['id'] = ''
        transação['tipo'] = 'Pagamento'
        transação['data'] = validar_data(input(f'Data (tecle enter para data de hoje): '))
        transação['valor'] = float(input('Valor: '))
        transação['categ'] = input('Categoria: ')
        transação['orig'] = input('Favorecido: ')
        transação['obs'] = input('Observações: ')
        print('Gasto cadastrado com sucesso.')
    return(transação.copy())

def validar_data(data):
    data_padrao = date.today().strftime('%d/%m/%Y')
    ano_atual = date.today().year
    if not data:
        return data_padrao
    formats = ['%d/%m/%Y', '%d %m %Y', '%d-%m-%Y', '%d.%m.%Y', '%d%m%Y', '%d/%m/%y', '%d %m %y', '%d-%m-%y', '%d.%m.%y', '%d%m%y', '%d/%m', '%d %m', '%d-%m', '%d.%m', '%d%m']
    for formato in formats:
        try:
            data_obj = datetime.strptime(data.strip(), formato)
            if formato in ['%d/%m', '%d %m', '%d-%m', '%d.%m', '%d%m']:
                data_obj = data_obj.replace(year=ano_atual)
            return data_obj.strftime('%d/%m/%Y')
        except ValueError:
            continue
    print('Data inválida.')
    return data_padrao

def validar_float():
    print('a ser feito')
def limite_de_caracteres(expressao, limite):
        print('a ser feito')

