import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from menu import realizar_acao

def f1():
    print("Função em desenvolvimento")

app = QApplication(sys.argv)

main_window = QWidget()
main_window.resize(640, 480)
main_window.setWindowTitle('Mat-Manex')


btn_inicio = QPushButton('Início', main_window)
btn_inicio.setGeometry(0, 0, 100, 100)
btn_inicio.clicked.connect(f1)

btn_cad_rec = QPushButton('Cadastrar receita', main_window)
btn_cad_rec.setGeometry(100, 0, 150, 100)
btn_cad_rec.clicked.connect(lambda: realizar_acao(1))

btn_cad_desp = QPushButton('Cadastrar despesa', main_window)
btn_cad_desp.setGeometry(250, 0, 150, 100)
btn_cad_desp.clicked.connect(lambda: realizar_acao(2))

btn_categ = QPushButton('Categorias', main_window)
btn_categ.setGeometry(400, 0, 150, 100)
btn_categ.clicked.connect(f1)

btn_fav = QPushButton('Favorecidos', main_window)
btn_fav.setGeometry(550, 0, 150, 100)
btn_fav.clicked.connect(f1)

btn_list = QPushButton('Lista de Transações', main_window)
btn_list.setGeometry(700, 0, 150, 100)
btn_list.clicked.connect(lambda: realizar_acao(3))

btn_estat = QPushButton('Estatísticas', main_window)
btn_estat.setGeometry(850, 0, 150, 100)
btn_estat.clicked.connect(lambda: realizar_acao(4))

btn_config = QPushButton('Configurações', main_window)
btn_config.setGeometry(1000, 0, 100, 100)
btn_config.clicked.connect(f1)




#25/03 manha min 5:00 https://youtu.be/SelawmXHtPg?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB&t=299
#25/03 meio-dia: video 3 https://www.youtube.com/watch?v=tJQk57qcliA&list=PLwsAoT89dh3qnjwQ1lJYzauTsFj9e8Qho&index=3
#27/03 manha - vendo a começando a aplicar video 3, continuar design da home antes de ir para 4.









