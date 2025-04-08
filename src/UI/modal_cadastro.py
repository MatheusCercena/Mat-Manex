from PyQt6.QtWidgets import QDialog, QLineEdit, QVBoxLayout, QLabel, QPushButton
from utils.transação import Transação

class ModalCadastro(QDialog):
    def __init__(self, tipo, gerenciador):
        super().__init__()
        self.gerenciador = gerenciador
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
        btn_confirmar.clicked.connect(self.cadastrar_transação)

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

    def cadastrar_transação(self):
        tipo = self.tipo
        data = self.input_data.text()
        valor = self.input_valor.text()
        categoria = self.input_categoria.text()
        origem = self.input_origem.text()
        observacoes = self.input_observacoes.text()

        transação = Transação(tipo, data, valor, categoria, origem, observacoes)
        transação.id = len(self.gerenciador.lista_de_transações) + 1
        self.gerenciador.lista_de_transações.append(transação)
        self.gerenciador.salvar_transações()
        print(f'{tipo} cadastrado com sucesso!')
        self.accept()

def abrir_modal(tipo, gerenciador):
    try:
        modal = ModalCadastro(tipo, gerenciador)
        resultado = modal.exec()
        print("Resultado do modal:", resultado)
    except Exception as e:
        print("Erro ao abrir modal:", e)

    