import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QLineEdit, QPushButton, QComboBox, QListWidget, QInputDialog

class CadastroColaboradores(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Cadastro de Colaboradores')
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        self.label_nome = QLabel('Nome do Colaborador:')
        self.input_nome = QLineEdit()
        
        self.label_chefe = QLabel('Chefe:')
        self.combo_chefe = QComboBox()
        self.combo_chefe.addItem('Nenhum')

        self.button_adicionar_chefe = QPushButton('Adicionar Chefe')
        self.button_adicionar_chefe.clicked.connect(self.adicionar_chefe)

        self.button_cadastrar = QPushButton('Cadastrar')
        self.button_cadastrar.clicked.connect(self.cadastrar_colaborador)

        self.lista_colaboradores = QListWidget()

        layout.addWidget(self.label_nome)
        layout.addWidget(self.input_nome)
        layout.addWidget(self.label_chefe)
        layout.addWidget(self.combo_chefe)
        layout.addWidget(self.button_adicionar_chefe)
        layout.addWidget(self.button_cadastrar)
        layout.addWidget(self.lista_colaboradores)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def adicionar_chefe(self):
        chefe, ok = QInputDialog.getText(self, 'Adicionar Chefe', 'Nome do Chefe:')
        if ok and chefe:
            self.combo_chefe.addItem(chefe)

    def cadastrar_colaborador(self):
        nome = self.input_nome.text()
        chefe = self.combo_chefe.currentText()

        if nome:
            self.lista_colaboradores.addItem(f"Nome: {nome}, Chefe: {chefe}")
            self.input_nome.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CadastroColaboradores()
    window.show()
    sys.exit(app.exec_())
