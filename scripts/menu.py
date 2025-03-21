from menu_functions import saudacao, menu, cadastrar_transação
import sys
import json

def selecionar_acao(menu_opt):
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
            res = input('Aperte enter para cadastrar outro gasto ou qualquer outra tecla para parar.')
            if res != '':
                break
    elif menu_opt == 3:
        def ver_lista():
            print()
            print('Lista de transações: ')
            print()
            for transação in lista_de_transações:
                print(f'ID: {transação['id']:3} Tipo: {transação['tipo']:10} Data: {transação['data']:11} Valor: {transação['valor']:8} Categoria: {transação['categ']:20} Favorecido: {transação['orig']:20} \nObservações: {transação['obs']:20}')
                print('- '*20)
        ver_lista()
    elif menu_opt == 4:
        options2 = [1, 2, 3]
        while True:
            opt2 = input('1 - Ver saldo: \n2 - Categorias \n3 - Favorecidos \n Digite o número da opção: ')
            if opt2 in options2:
                continue
            else:
                break
        if opt2 == 1:
            for i, v in enumerate(lista_de_transações):
                print(lista_de_transações[i]['id'][v])
        #def ver_estatisticas():

def salvar_transações():
    with open(arquivo_json, "w") as file:
        json.dump(lista_de_transações, file)

saudacao()

menu_opt = menu()
arquivo_json = 'data.json'
try:
    with open(arquivo_json, "r") as file:
        lista_de_transações = json.load(file)
except:
    lista_de_transações = []

while True:
    selecionar_acao(menu_opt)
    menu_opt = menu()
    if menu_opt == 5:
        salvar_transações()
        sys.exit()   


#cadastrar função para mostrar saldo atual


