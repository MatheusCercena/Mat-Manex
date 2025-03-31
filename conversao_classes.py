from datetime import date
from datetime import datetime

class cadastro:
    def __init__(self, id, tipo, data, valor, categoria, origem, obs):
        self.id = ''
        self.tipo = 'Receita ou despesa'
        self.data = validar_data(input(f'Data (tecle enter para data de hoje): '))
        self.valor = solicitar_float('Valor: ')
        self.categoria = input('Categoria: ')
        self.origem = input('Pagante: ')
        self.observaçoes = input('Observações: ')
        print('Receita cadastrada com sucesso.')
        transação = {}
        transação = {self.id: len(transação)+1, self.tipo: '...', self}
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        }

        return(transação.copy())

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



#...