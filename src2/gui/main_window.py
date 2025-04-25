import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QMenuBar, QPushButton, QHBoxLayout

# from src_terminal.utils import gerenciador

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        
        menu = QHBoxLayout()
        btn_inicio = QPushButton('Início')
        btn_inicio.clicked.connect(lambda: print("Configuração em desenvolvimento"))

        menu.addWidget(btn_inicio)
        

        tela_principal = QWidget()
        tela_principal.setLayout(menu)

        self.setCentralWidget(tela_principal)

        # btn_inicio.setGeometry(0, 0, 100, 100)
        # btn_inicio.clicked.connect(lambda: print("Configuração em desenvolvimento"))

        # btn_cad_rec = QPushButton('Cadastrar receita', main_window)
        # btn_cad_rec.setGeometry(100, 0, 150, 100)
        # btn_cad_rec.clicked.connect(lambda: abrir_modal('Recebimento'))

        # btn_cad_desp = QPushButton('Cadastrar despesa', main_window)
        # btn_cad_desp.setGeometry(250, 0, 150, 100)
        # btn_cad_desp.clicked.connect(lambda: gerenciador.cadastrar_transação('Pagamento'))

        # btn_categ = QPushButton('Categorias', main_window)
        # btn_categ.setGeometry(400, 0, 150, 100)
        # btn_categ.clicked.connect(lambda: gerenciador.ver_categorias())

        # btn_fav = QPushButton('Favorecidos/Pagantes', main_window)
        # btn_fav.setGeometry(550, 0, 150, 100)
        # btn_fav.clicked.connect(lambda: gerenciador.ver_origens())

        # btn_list = QPushButton('Lista de Transações', main_window)
        # btn_list.setGeometry(700, 0, 150, 100)
        # btn_list.clicked.connect(lambda: gerenciador.ver_lista())

        # btn_estat = QPushButton('Estatísticas', main_window)
        # btn_estat.setGeometry(850, 0, 150, 100)
        # btn_estat.clicked.connect(lambda: sub_menuEstatisticas())

        # btn_config = QPushButton('Configurações', main_window)
        # btn_config.setGeometry(1000, 0, 100, 100)
        # btn_config.clicked.connect(lambda: print("Configuração em desenvolvimento"))


        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

