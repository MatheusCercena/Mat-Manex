import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QLabel

app = QApplication(sys.argv)#cria um app com a classe QApplication acessando o sistema

main_window = QWidget()
main_window.resize(640, 480)
main_window.setWindowTitle('Mat-Manex')

btn_inicio = QPushButton('Início', main_window)
btn_cad_rec = QPushButton('Cadastrar receita', main_window)
btn_cad_desp = QPushButton('Cadastrar despesa', main_window)
btn_categ = QPushButton('Categorias', main_window)
btn_fav = QPushButton('Favorecidos', main_window)
btn_list = QPushButton('Lista de Transações', main_window)
btn_estat = QPushButton('Estatísticas', main_window)
btn_config = QPushButton('Configurações', main_window)


btn_inicio.setGeometry()


main_window.show()

app.exec()






#25/03 manha min 5:00 https://youtu.be/SelawmXHtPg?list=PL3JVwFmb_BnSOj_OtnKlsc2c7Jcs6boyB&t=299
#25/03 meio-dia: video 3 https://www.youtube.com/watch?v=tJQk57qcliA&list=PLwsAoT89dh3qnjwQ1lJYzauTsFj9e8Qho&index=3
#27/03 manha - vendo a começando a aplicar video 3, continuar design da home antes de ir para 4.









