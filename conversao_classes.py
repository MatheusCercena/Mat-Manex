from datetime import date
from datetime import datetime
import json

class Transação:
    def __init__(self, tipo, data, valor, categoria, origem, observaçoes):
        self.id = None
        self.tipo = tipo
        self.data = self.validar_data(data)
        self.valor = self.solicitar_float(valor)
        self.categoria = categoria
        self.origem = origem
        self.observaçoes = observaçoes
    
    def to_dict(self):
        return {
            'id': self.id,
            'tipo' : self.tipo,
            'data' : self.data,
            'valor' : self.valor,
            'categoria' : self.categoria,
            'origem' : self.origem,
            'obs' : self.observaçoes
        }  
    
    @staticmethod
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

    @staticmethod
    def solicitar_float(mensagem):
        while True: 
            n = input(mensagem.strip())
            try:
                float(n.replace(",", "."))
                return float(n)
            except:
                print('Valor inválido')

class Cadastro:
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

    def cadastrar_transação(self, tipo):
        data = input('Data (Enter para hoje): ')
        valor = input('Valor: ')
        categoria = input('Categoria: ')
        origem = input('Pagante/Favorecido: ')
        observacoes = input('Observações: ')

        transação = Transação(self, tipo, data, valor, categoria, origem, observacoes)#cria um objeto da classe Transação, em que seus atributos podem ser acessados pela notação: objeto.atributo
        transação.id = len(self.lista_de_transações) + 1
        self.lista_de_transações.append(transação)
        self.salvar_transações()
        print(f'{tipo} cadastrado com sucesso!')

    def ver_lista(self):
        print('\nLista de transações: \n')
        for transação in self.lista_de_transações:
            print(f'ID: {transação.id} | {transação.tipo} | {transação.data} | R${transação.valor:.2f} | {transação.categoria} | {transação.origem} | {transação.observaçoes}')

    def ver_saldo(self):
        saldo = 0
        for transação in self.lista_de_transações:
            saldo += float(transação.valor)
            Cadastro.separador()
        print(f"Saldo atual: {saldo:.2f}")

    def ver_categorias(self):
        categorias = []
        contador = 0
        print('\nCategorias: \n')
        for transação in self.lista_de_transações:
            if transação.categoria not in categorias:
                categorias.append(transação.categoria)
                contador += 1
                print(f'[{contador}] {transação.categoria}')

    @staticmethod
    def separador():
        print('- '*20)  
