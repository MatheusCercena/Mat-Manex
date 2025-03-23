from menu_functions import saudacao, menu, cadastrar_transação, ver_lista, separador
import sys
import json

def carregar_json():
    global arquivo_json
    arquivo_json = 'data.json'
    try:
        with open(arquivo_json, "r") as file:
            global lista_de_transações
            lista_de_transações = json.load(file)
    except:
        lista_de_transações = []

def menu_principal(opção):
    while True:
        selecionar_acao(opção)
        opção = menu()

def selecionar_acao(opção):
    if opção == 1:
        while True:
            lista_de_transações.append(cadastrar_transação(0))
            lista_de_transações[-1]['id'] = len(lista_de_transações)
            res = input('Aperte enter para cadastrar outra receita ou qualquer outra tecla para parar.')
            if res != '':
                break
    elif opção == 2:
        while True:
            lista_de_transações.append(cadastrar_transação(1))
            lista_de_transações[-1]['id'] = len(lista_de_transações)
            res = input('Aperte enter para cadastrar outro gasto ou qualquer outra tecla para parar.')
            if res != '':
                break
    elif opção == 3:
        if len(lista_de_transações) > 0:
            ver_lista(lista_de_transações)
        else:
            print('\nVocê não cadastrou nenhuma transação.')
    elif opção == 4:
        options2 = [1, 2, 3, 4]
        while True:
            while True:
                opt2 = int(input('\nMenu - Estatísticas: \n [1] Ver saldo: \n [2] Categorias \n [3] Favorecidos \n [4] Voltar ao menu principal \n Digite o número da opção: '))
                if opt2 not in options2:
                    print("Digite um número válido!")
                else: 
                    break
            if opt2 == 1:
                saldo = 0
                for c in lista_de_transações:
                    saldo += float(c['valor'])
                print(f"Saldo atual: {saldo:.2f}")
            elif opt2 == 2:
                categorias = []
                contador = 0
                print('\nCategorias: \n')
                for transação in lista_de_transações:
                    if transação['categoria'] not in categorias:
                        categorias.append(transação['categoria'])
                        contador += 1
                        print(f'[{contador}] {transação['categoria']}')
                separador()
            elif opt2 == 4:
                break
        menu_principal(menu())
    if opção == 5:
        salvar_transações()
        sys.exit()   
    salvar_transações()

def salvar_transações():
    with open(arquivo_json, "w") as file:
        json.dump(lista_de_transações, file)

carregar_json()
saudacao()
menu_principal(menu())

#Coisas para adicionar
#Alterar transações: Apagar uma transação específica, ou alterar algo nela.
#Fazer após mecher com PyQT


