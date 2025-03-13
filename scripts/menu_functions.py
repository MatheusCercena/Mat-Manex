from datetime import date

def cadastrar_transação(a):
    data_padrao = date.today().strftime('%d/%m/%Y')
    transação = {}
    if a == 0:
        transação['tipo'] = 'recebimento'
        transação['data'] = input(f'Data: tecle enter para {data_padrao}: ')
        if not transação['data']:
            transação['data'] == data_padrao
        transação['valor'] = float(input('Valor: '))
        transação['categ'] = input('Categoria: ')
        transação['orig'] = input('Pagante: ')
        transação['obs'] = input('Observações: ')
        print('receita cadastrada com sucesso.')

    if a == 1:
        transação['tipo'] = 'pagamento'
        transação['data'] = input(f'Data: tecle enter para {data_padrao}:')
        if not transação['data']:
            transação['data'] = data_padrao
        transação['valor'] = float(input('Valor: '))
        transação['categ'] = input('Categoria: ')
        transação['orig'] = input('Favorecido: ')
        transação['obs'] = input('Observações: ')
        print('Gasto cadastrado com sucesso.')

    return(transação.copy())

# def ver_lista():
    
