def cadastrar_receita():
    valor = float(input('Valor: '))
    categ = input('Categoria: ')
    pag = input('Pagante: ')
    obs = input('Observações: ')

    ganho = {
        'Valor' : valor,
        'Categoria' : categ,
        'Pagante' : pag,
        'Observações' : obs
    }

    print('Receita cadastrada com sucesso. \n Valor: {valor}\n Categoria: {categ} \n Pagante: {pag} \n Observações: {obs}')
    return(ganho)
    
def cadastrar_gasto():
    valor = float(input('Valor: '))
    categ = input('Categoria: ')
    fav = input('Favorecido: ')
    obs = input('Observações: ')

    gasto = {
        'Valor' : valor,
        'Categoria' : categ,
        'Favorecido' : fav,
        'Observações' : obs
    }
    
    print(f'Gasto cadastrado com sucesso. \n Valor: {valor}\n Categoria: {categ} \n Favorecido: {fav} \n Observações: {obs}')

    return(gasto)



# def ver_lista():
    
# def ver_estatisticas():

