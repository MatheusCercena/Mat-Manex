from PyQt6.QtWidgets import QWidget, QPushButton
from gerenciador import GerenciadorFinanças
from menu import Menu
from modal_cadastro import ModalCadastro

def f1():
    print("Função em desenvolvimento")

gerenciador = GerenciadorFinanças()
menu = Menu()




#Começo do menu
main_window = QWidget()
main_window.resize(640, 480)
main_window.setWindowTitle('Mat-Manex')

btn_inicio = QPushButton('Início', main_window)
btn_inicio.setGeometry(0, 0, 100, 100)
btn_inicio.clicked.connect(lambda: menu.ver_menu_principal())

btn_cad_rec = QPushButton('Cadastrar receita', main_window)
btn_cad_rec.setGeometry(100, 0, 150, 100)
btn_cad_rec.clicked.connect(lambda: ModalCadastro('Recebimento', gerenciador).exec())

btn_cad_desp = QPushButton('Cadastrar despesa', main_window)
btn_cad_desp.setGeometry(250, 0, 150, 100)
btn_cad_desp.clicked.connect(lambda: ModalCadastro('Pagamento', gerenciador).exec())

btn_categ = QPushButton('Categorias', main_window)
btn_categ.setGeometry(400, 0, 150, 100)
btn_categ.clicked.connect(lambda: gerenciador.ver_categorias())

btn_fav = QPushButton('Favorecidos/Pagantes', main_window)
btn_fav.setGeometry(550, 0, 150, 100)
btn_fav.clicked.connect(lambda: gerenciador.ver_origens())

btn_list = QPushButton('Lista de Transações', main_window)
btn_list.setGeometry(700, 0, 150, 100)
btn_list.clicked.connect(lambda: gerenciador.ver_lista())

btn_estat = QPushButton('Estatísticas', main_window)
btn_estat.setGeometry(850, 0, 150, 100)
btn_estat.clicked.connect(lambda: menu.sub_menuEstatisticas())

btn_config = QPushButton('Configurações', main_window)
btn_config.setGeometry(1000, 0, 100, 100)
btn_config.clicked.connect(lambda: f1)
#Fim do menu








#25/03 manha min 5:00 https://youtu.be/SelawmXHtPg?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB&t=299
#25/03 meio-dia: video 3 https://www.youtube.com/watch?v=tJQk57qcliA&list=PLwsAoT89dh3qnjwQ1lJYzauTsFj9e8Qho&index=3
#27/03 manha - vendo a começando a aplicar video 3, continuar design da home antes de ir para 4.









