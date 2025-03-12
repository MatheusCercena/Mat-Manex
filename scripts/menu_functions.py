# def cadastrar_receita():
#     receita = {}
#     receita['valor'] = float(input('Valor: '))
#     receita['categ'] = input('Categoria: ')
#     receita['pag'] = input('Pagante: ')
#     receita['obs'] = input('Observações: ')

#     print(f'Receita cadastrada com sucesso. \n Valor: {receita['valor']}\n Categoria: {receita['categ']} \n Pagante: {receita['pag']} \n Observações: {receita['obs']}')
#     return(receita.copy())
    
# def cadastrar_gasto():
#     gasto = {}
#     gasto['valor'] = float(input('Valor: '))
#     gasto['categ'] = input('Categoria: ')
#     gasto['fav'] = input('Favorecido: ')
#     gasto['obs'] = input('Observações: ')

#     print(f'Gasto cadastrado com sucesso. \n Valor: {gasto['valor']}\n Categoria: {gasto['categ']} \n Favorecido: {gasto['fav']} \n Observações: {gasto['obs']}')
#     return(gasto.copy())

from datetime import date

def cadastrar_transação(a):
    data_padrao = date.today().strftime('%d/%m/%Y')
    if a == 0:
        transações = {}
        transações['tipo'] = 'recebimento'
        transações['data'] = input(f'Data: tecle enter para {data_padrao}:')
        transações['valor'] = float(input('Valor: '))
        transações['categ'] = input('Categoria: ')
        transações['orig'] = input('Pagante: ')
        transações['obs'] = input('Observações: ')
        print(f'Receita cadastrada com sucesso. \nTipo: {transações['tipo']} \nData: {transações['data']} \nValor: {transações['valor']} \nCategoria: {transações['categ']} \nPagante: {transações['orig']} \nObservações: {transações['obs']}')

    if a == 1:
        transações = {}
        transações['tipo'] = 'pagamento'
        transações['data'] = input(f'Data: tecle enter para {data_padrao}:')
        transações['valor'] = float(input('Valor: '))
        transações['categ'] = input('Categoria: ')
        transações['orig'] = input('Favorecido: ')
        transações['obs'] = input('Observações: ')
        print(f'Gasto cadastrada com sucesso. \nTipo: {transações['tipo']} \nData: {transações['data']} \nValor: {transações['valor']} \nCategoria: {transações['categ']} \nFavorecido: {transações['orig']} \nObservações: {transações['obs']}')

    return(transações.copy())
    
def cadastrar_gasto():
    gasto = {}
    gasto['valor'] = float(input('Valor: '))
    gasto['categ'] = input('Categoria: ')
    gasto['pag'] = input('Pagante: ')
    gasto['obs'] = input('Observações: ')

    print(f'Gasto cadastrado com sucesso. \n Valor: {gasto['valor']}\n Categoria: {gasto['categ']} \n Favorecido: {gasto['fav']} \n Observações: {gasto['obs']}')
    return(gasto.copy())



# def ver_lista():
    
