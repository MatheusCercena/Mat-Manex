import json
import sys
from datetime import datetime, date
from time import localtime

class Transacao:
    def __init__(self, tipo, data, valor, categoria, origem, observacoes):
        self.id = None
        self.tipo = tipo  # 'Recebimento' ou 'Pagamento'
        self.data = self.validar_data(data)
        self.valor = self.solicitar_float(valor)
        self.categoria = categoria
        self.origem = origem
        self.observacoes = observacoes

    def to_dict(self):
        return {
            "id": self.id,
            "tipo": self.tipo,
            "data": self.data,
            "valor": self.valor,
            "categoria": self.categoria,
            "origem": self.origem,
            "observacoes": self.observacoes
        }

    @staticmethod
    def validar_data(data):
        data_padrao = date.today().strftime('%d/%m/%Y')
        if not data:
            return data_padrao
        formatos = ['%d/%m/%Y', '%d-%m-%Y', '%d.%m.%Y', '%d%m%Y']
        for formato in formatos:
            try:
                return datetime.strptime(data.strip(), formato).strftime('%d/%m/%Y')
            except ValueError:
                continue
        print('Data inválida. Usando data de hoje.')
        return data_padrao

    @staticmethod
    def solicitar_float(valor):
        while True:
            try:
                return float(valor.replace(",", "."))
            except ValueError:
                valor = input('Valor inválido. Digite novamente: ')


class GerenciadorFinancas:
    def __init__(self, arquivo_json='data.json'):
        self.arquivo_json = arquivo_json
        self.lista_de_transacoes = self.carregar_transacoes()

    def carregar_transacoes(self):
        try:
            with open(self.arquivo_json, "r") as file:
                transacoes = json.load(file)
                return [Transacao(**t) for t in transacoes]
        except  (FileNotFoundError, json.JSONDecodeError):
            return []

    def salvar_transacoes(self):
        with open(self.arquivo_json, "w") as file:
            json.dump([t.to_dict() for t in self.lista_de_transacoes], file, indent=4)

    def cadastrar_transacao(self, tipo):
        data = input('Data (Enter para hoje): ')
        valor = input('Valor: ')
        categoria = input('Categoria: ')
        origem = input('Pagante/Favorecido: ')
        observacoes = input('Observações: ')

        transacao = Transacao(tipo, data, valor, categoria, origem, observacoes)
        transacao.id = len(self.lista_de_transacoes) + 1
        self.lista_de_transacoes.append(transacao)
        self.salvar_transacoes()
        print(f'{tipo} cadastrado com sucesso!')

    def ver_lista(self):
        print('\nLista de transações:')
        for t in self.lista_de_transacoes:
            print(f'ID: {t.id} | {t.tipo} | {t.data} | R${t.valor:.2f} | {t.categoria} | {t.origem} | {t.observacoes}')
            print('-' * 50)

    def ver_saldo(self):
        saldo = sum(t.valor if t.tipo == 'Recebimento' else -t.valor for t in self.lista_de_transacoes)
        print(f"Saldo atual: R${saldo:.2f}")

    def ver_categorias(self):
        categorias = {t.categoria for t in self.lista_de_transacoes}
        print('Categorias cadastradas:')
        for categoria in categorias:
            print(f'- {categoria}')


class Menu:
    def __init__(self):
        self.gerenciador = GerenciadorFinancas()

    def saudacao(self):
        hora = localtime().tm_hour
        if hora < 5 or hora >= 18:
            print('Boa noite\n')
        elif 5 <= hora < 12:
            print('Bom dia\n')
        else:
            print('Boa tarde\n')

    def exibir_menu(self):
        while True:
            print("\nMenu:")
            print("[1] Cadastrar receita")
            print("[2] Cadastrar gasto")
            print("[3] Ver lista")
            print("[4] Ver estatísticas")
            print("[5] Sair")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.gerenciador.cadastrar_transacao('Recebimento')
            elif opcao == "2":
                self.gerenciador.cadastrar_transacao('Pagamento')
            elif opcao == "3":
                self.gerenciador.ver_lista()
            elif opcao == "4":
                self.submenu_estatisticas()
            elif opcao == "5":
                self.gerenciador.salvar_transacoes()
                print("Saindo...")
                sys.exit()
            else:
                print("Opção inválida, tente novamente.")

    def submenu_estatisticas(self):
        while True:
            print("\nEstatísticas:")
            print("[1] Ver saldo")
            print("[2] Ver categorias")
            print("[3] Voltar")

            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                self.gerenciador.ver_saldo()
            elif opcao == "2":
                self.gerenciador.ver_categorias()
            elif opcao == "3":
                break
            else:
                print("Opção inválida, tente novamente.")


if __name__ == "__main__":
    menu = Menu()
    menu.saudacao()
    menu.exibir_menu()
