import json
from transação import Transação

class GerenciadorFinanças:
    def __init__(self, arquivo_json = 'data.json'):
        self.arquivo_json = arquivo_json
        self.lista_de_transações = self.carregar_transações()

    def carregar_transações(self):
        try:
            with open(self.arquivo_json, "r") as file:
                transações = json.load(file)
            return [Transação(**t) for t in transações]  # Retorna uma lista de objetos Transação por passar os elementos do dicionario t como parametros da funcao                   
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar_transações(self):
        with open(self.arquivo_json, "w") as file:
            json.dump([t.to_dict() for t in self.lista_de_transações], file)
    # def cadastrar_transação(self, tipo):
    #     data = input('Data (Enter para hoje): ')
    #     valor = input('Valor: ')
    #     categoria = input('Categoria: ')
    #     origem = input('Pagante/Favorecido: ')
    #     observacoes = input('Observações: ')

    #     transação = Transação(tipo, data, valor, categoria, origem, observacoes)
    #     transação.id = len(self.lista_de_transações) + 1
    #     self.lista_de_transações.append(transação)
    #     self.salvar_transações()
    #     print(f'{tipo} cadastrado com sucesso!')

    def ver_lista(self):
        print('\nLista de transações: \n')
        for transação in self.lista_de_transações:
            print(f'ID: {transação.id} | {transação.tipo} | {transação.data} | R${transação.valor:.2f} | {transação.categoria} | {transação.origem} | {transação.observaçoes}')

    def ver_saldo(self):
        saldo = 0
        for transação in self.lista_de_transações:
            saldo += float(transação.valor)
            GerenciadorFinanças.separador()
        print(f"Saldo atual: {saldo:.2f}")

    def ver_categorias(self):
        categorias = set()
        for transação in self.lista_de_transações:
            categorias.add(transação.categoria)
        print('\nCategorias: ')
        if not categorias:
            print('Você ainda não cadastrou nenhuma categoria')
        else:
            for index, categoria in enumerate(categorias, start=1):
                print(f'[{index}] - {categoria}')

    def ver_origens(self):
        origens = set()
        for transação in self.lista_de_transações:
                origens.add(transação.origem)
        print('\nFavorecidos/Pagantes: \n')
        if not origens:
            print('Você ainda não cadastrou nenhum favorecido/pagante.')
        else:
            for index, origem in enumerate(origens, start=1):
                print(f'[{index}] - {origem}')

    @staticmethod
    def separador():
        print('- '*20)  
