import sys
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QToolBar, QPushButton, QHBoxLayout, QStatusBar
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('media/icons/logo.ico'))
        self.setWindowTitle('Mat-Manex')

        self.toolbar = QToolBar()
        self.addToolBar(self.toolbar)
        self.toolbar.setIconSize(QSize(16, 16))

        self.criar_botoes_toolbar()
        self.definir_estilo_da_toolbar()

    def criar_botoes_toolbar(self):
        self.botoes = [
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Inicio', 'Funcao' : "Configuração em desenvolvimento"},
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Cadastrar receita', 'Funcao' : "Recebimento"},
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Cadastrar despesa', 'Funcao' : "Pagamento"},
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Categorias', 'Funcao' : "gerenciador.ver_categorias()"},
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Favorecidos/Pagantes', 'Funcao' : "gerenciador.ver_origens()"},
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Lista de Transações', 'Funcao' : "gerenciador.ver_lista()"},
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Estatísticas', 'Funcao' : "sub_menuEstatisticas"},
                {'Path' : 'media/icons/logo.ico', 'Nome' : 'Configurações', 'Funcao' : 'Configuração em desenvolvimento'}
             ]
        
        for botao in self.botoes:
            acao = QAction(QIcon(botao['Path']), botao['Nome'], self)
            acao.triggered.connect(lambda _, comando = botao['Funcao']: print(comando))
            self.toolbar.addAction(acao)

        
    def definir_estilo_da_toolbar(self):
        tamanho_toolbar = 850
        tamanho_tela  = self.size()#continuar, tá errado
        print(tamanho_tela)
        if tamanho_tela > tamanho_toolbar:
            self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextOnly)
        else:
            self.toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())

