from PyQt6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QLabel, QPushButton
from utils.transação import Transação
from utils.gerenciador import GerenciadorFinanças

class ModalCadastro(QDialog):
    def __init__(self, tipo):
        super().__init__()
        self.gerenciador = GerenciadorFinanças()
        self.tipo = tipo

        self.setWindowTitle(f'Cadastrar {tipo}')
        self.setModal(True)
        self.setGeometry(0, 0, 1000, 800)

        self.input_data = QLineEdit(self)
        self.input_valor = QLineEdit(self)
        self.input_categoria = QLineEdit(self)
        self.input_origem = QLineEdit(self)
        self.input_observacoes = QLineEdit(self)

        btn_confirmar = QPushButton("Cadastrar", self)
        btn_confirmar.clicked.connect(GerenciadorFinanças.cadastrar_transação('Recebimento'))

        layout = QVBoxLayout()
        layout.addWidget(QLabel('Data (Enter para hoje): '))
        layout.addWidget(self.input_data)
        layout.addWidget(QLabel("Valor:"))
        layout.addWidget(self.input_valor)
        layout.addWidget(QLabel("Categoria:"))
        layout.addWidget(self.input_categoria)
        layout.addWidget(QLabel("Pagante/Favorecido:"))
        layout.addWidget(self.input_origem)
        layout.addWidget(QLabel("Observações:"))
        layout.addWidget(self.input_observacoes)
        layout.addWidget(btn_confirmar)

        self.setLayout(layout)



    