from datetime import date
from datetime import datetime

class Transação:
    def __init__(self, id, tipo, data, valor, categoria, origem, observaçoes):
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

    def solicitar_float(mensagem):
        while True: 
            n = input(mensagem.strip())
            try:
                float(n.replace(",", "."))
                return float(n)
            except:
                print('Valor inválido')

class Cadastro:
    def __init__(self):
        pass


#...