from datetime import datetime, date

class Transação:
    def __init__(self, tipo, data, valor, categoria, origem, observaçoes, id=None):
        self.id = id
        self.tipo = tipo
        self.data = self.validar_data(data)
        self.valor = self.validar_float(valor, self.tipo)
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
            'observaçoes' : self.observaçoes
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
    def validar_float(valor, tipo):
        try:
            if tipo == 'Pagamento':
                return -abs(float(str(valor).replace(",", ".")))
            else:
                return float(str(valor).replace(",", "."))
        except:
            return 0.0
