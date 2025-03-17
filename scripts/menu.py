from menu_functions import saudacao, menu, cadastrar_transação
import sys
import json
import os

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
            res = input('Aperte enter para cadastrar outro gasto ou esc para parar.')
            if res != '':
                break
    elif menu_opt == 3:
        def ver_lista():
            for transação in lista_de_transações:
                print(f'ID: {transação['id']:3} Tipo: {transação['tipo']:10} Data: {transação['data']:15} Valor: {transação['valor']:8} Categoria: {transação['categ']:20} Favorecido: {transação['orig']:20} \nObservações: {transação['obs']:20}')
        ver_lista()
    else:
        def salvar_transações():
            with open("data.json", "w") as file:
                json.dump(data, file)
        sys.exit   

saudacao()

menu_opt = menu()
data_json = 'data.json'
if os.path.exists(data_json, "r"):
    try:
        with open(data_json, "r") as file:
            lista_de_transações = json.load(file)
    except json.JSONDecodeError:
        lista_de_transações = []


while True:
    selecionar_acao(menu_opt)
    menu_opt = menu()

