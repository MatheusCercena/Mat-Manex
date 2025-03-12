def cadastrar_receita():
    receita = {}
    receita['valor'] = float(input('Valor: '))
    receita['categ'] = input('Categoria: ')
    receita['pag'] = input('Pagante: ')
    receita['obs'] = input('Observações: ')

    print(f'Receita cadastrada com sucesso. \n Valor: {receita['valor']}\n Categoria: {receita['categ']} \n Pagante: {receita['pag']} \n Observações: {receita['obs']}')
    return(receita.copy())
    
def cadastrar_gasto():
    gasto = {}
    gasto['valor'] = float(input('Valor: '))
    gasto['categ'] = input('Categoria: ')
    gasto['pag'] = input('Pagante: ')
    gasto['obs'] = input('Observações: ')

    print(f'Gasto cadastrado com sucesso. \n Valor: {gasto['valor']}\n Categoria: {gasto['categ']} \n Favorecido: {gasto['fav']} \n Observações: {gasto['obs']}')
    return(gasto.copy())

# def ver_lista():
    
