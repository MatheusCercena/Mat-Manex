import sys
from time import localtime
from gerenciador import GerenciadorFinanças


class Menu:
    def __init__(self):
        self.gerenciador = GerenciadorFinanças()

    def ver_menu_principal(self):
        while True:
            print('''\nMenu: 
                [1] Cadastrar receita 
                [2] Cadastrar despesa 
                [3] Ver lista 
                [4] Ver estatísticas 
                [5] Sair do programa
                ''')
            opt = ''
            options = (1, 2, 3, 4, 5)
            while opt not in options:
                opt = int(input('Digite o número da opção: '))
                if opt not in options:
                    print('Opção inválida! Digite um número de 1 a 5: ')
            if opt == 1:
                self.gerenciador.cadastrar_transação('Recebimento')
            elif opt == 2:
                self.gerenciador.cadastrar_transação('Pagamento')
            elif opt == 3:
                self.gerenciador.ver_lista()
            elif opt == 4:
                self.sub_menuEstatisticas()
            elif opt == 5:
                sys.exit()
    def sub_menuEstatisticas(self):
        while True:
            options2 = [1, 2, 3, 4]
            print('''\nMenu Estatísticas: 
            [1] Ver saldo: 
            [2] Categorias 
            [3] Favorecidos/Pagantes
            [4] Voltar ao menu principal
            ''')
            opt_estatisticas = int(input('\nDigite o número da opção: '))
            while opt_estatisticas not in options2:
                opt_estatisticas = int(input('\nNúmero inválido. \nDigite o número da opção: '))
            if opt_estatisticas == 1:
                self.gerenciador.ver_saldo()
            elif opt_estatisticas == 2:
                self.gerenciador.ver_categorias()
            elif opt_estatisticas == 3:
                self.gerenciador.ver_origens()
            elif opt_estatisticas == 4:
                self.ver_menu_principal()

    @staticmethod
    def saudacao():
        hour = localtime().tm_hour 
        if hour < 5 or hour >= 18:
            print('Boa noite')
        if 5 <= hour < 12: 
            print('Bom dia')
        if 12 <= hour < 18:
            print('Boa tarde')

