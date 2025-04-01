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
                for t in transações:
                    return Transação(**t) 
                        
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
        print()
        for transação in self.lista_de_transações:
            print(f'ID: {transação.id:3} Tipo: {transação['tipo']:10} Data: {transação['data']:11} Valor: {transação['valor']:8} Categoria: {transação['categoria']:20} Favorecido: {transação['origem']:20} \nObservações: {transação['obs']:20}')
