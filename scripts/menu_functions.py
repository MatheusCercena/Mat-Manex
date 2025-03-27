from datetime import date
from datetime import datetime
from time import localtime

def saudacao():
    hour = localtime().tm_hour 
    if hour < 5 or hour >= 18:
        print('Boa noite')
    if 5 <= hour < 12: 
        print('Bom dia')
    if 12 <= hour < 18:
        print('Boa tarde')

def cadastrar_transação(a):
    transação = {}
    if a == 0:
        transação['id'] = ''
        transação['tipo'] = 'Receita'
        transação['data'] = validar_data(input(f'Data (tecle enter para data de hoje): '))
        transação['valor'] = solicitar_float('Valor: ')
        transação['categoria'] = input('Categoria: ')
        transação['origem'] = input('Pagante: ')
        transação['obs'] = input('Observações: ')
        print('Receita cadastrada com sucesso.')
    if a == 1:
        transação['id'] = ''
        transação['tipo'] = 'Despesa'
        transação['data'] = validar_data(input(f'Data (tecle enter para data de hoje): '))
        transação['valor'] = -abs(solicitar_float('Valor: '))
        transação['categoria'] = input('Categoria: ')
        transação['origem'] = input('Favorecido: ')
        transação['obs'] = input('Observações: ')
        print('Despesa cadastrada com sucesso.')
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

def solicitar_float(mensagem):
    while True: 
        n = input(mensagem.strip())
        try:
            float(n.replace(",", "."))
            return float(n)
        except:
            print('Valor inválido')

def ver_lista(lista):
    print()
    print('Lista de transações: ')
    print()
    for transação in lista:
        print(f'ID: {transação['id']:3} Tipo: {transação['tipo']:10} Data: {transação['data']:11} Valor: {transação['valor']:8} Categoria: {transação['categoria']:20} Favorecido: {transação['origem']:20} \nObservações: {transação['obs']:20}')
        separador()
        
def separador():
    print('- '*20)
