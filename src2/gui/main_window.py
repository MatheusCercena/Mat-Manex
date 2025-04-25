import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QToolBar, QPushButton, QHBoxLayout, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize

# from src_terminal.utils import gerenciador

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.setIconSize(QSize(16, 16))

        btn_inicio = QAction('Início')
        btn_inicio.triggered.connect(lambda: print("Configuração em desenvolvimento"))

        btn_cad_rec = QAction(QIcon('..media/images/logo_mat-manex.png'), 'Cadastrar receita')
        btn_cad_rec.triggered.connect(lambda: print('Recebimento'))

        btn_cad_desp = QAction(QIcon('..media/images/logo_mat-manex.png'), 'Cadastrar despesa')
        btn_cad_desp.triggered.connect(lambda: print('Pagamento'))
                                     
        btn_categ = QAction(QIcon('..media/images/logo_mat-manex.png'), 'Categorias')
        btn_categ.triggered.connect(lambda: print('gerenciador.ver_categorias()'))

        btn_fav = QAction(QIcon('..media/images/logo_mat-manex.png'), 'Favorecidos/Pagantes')
        btn_fav.triggered.connect(lambda: print('gerenciador.ver_origens()'))

        btn_list = QAction(QIcon('..media/images/logo_mat-manex.png'), 'Lista de Transações')
        btn_list.triggered.connect(lambda: print('gerenciador.ver_lista()'))

        btn_estat = QAction(QIcon('..media/images/logo_mat-manex.png'), 'Estatísticas')
        btn_estat.triggered.connect(lambda: print('sub_menuEstatisticas()'))
                                  
        btn_config = QAction(QIcon('..media/images/logo_mat-manex.png'), 'Configurações')
        btn_config.triggered.connect(lambda: print("Configuração em desenvolvimento"))

        toolbar.addAction(btn_inicio)
        toolbar.addAction(btn_cad_rec)
        toolbar.addAction(btn_cad_desp)
        toolbar.addAction(btn_categ)
        toolbar.addAction(btn_fav)
        toolbar.addAction(btn_list)
        toolbar.addAction(btn_estat)
        toolbar.addAction(btn_config)


        self.setStatusBar(QStatusBar(self))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

