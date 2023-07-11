from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QTableWidget, QTableWidgetItem, QLineEdit, QPushButton

class ProductWindow(QWidget):
    def __init__(self, connection):
        super().__init__()
        self.setWindowTitle('Pesquisa de Produtos')
        self.connection = connection

        layout = QVBoxLayout()
        self.setLayout(layout)

        label_codprod = QLabel('Código do Produto:')
        self.input_codprod = QLineEdit()

        layout.addWidget(label_codprod)
        layout.addWidget(self.input_codprod)

        self.btn_search = QPushButton('Pesquisar')
        layout.addWidget(self.btn_search)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Código', 'Descrição', 'EAN'])
        layout.addWidget(self.table)

        self.btn_search.clicked.connect(self.search_product)

    def search_product(self):
        codprod = self.input_codprod.text()

        # Realizar a pesquisa dos produtos no banco de dados
        cursor = self.connection.cursor()
        query = "SELECT CODPROD, DESCRICAO, CODAUXILIAR AS EAN FROM PCPRODUT"

        if codprod:
            query += f" WHERE CODPROD = '{codprod}'"

        query += " ORDER BY CODPROD"  # Adicionar a cláusula de ordenação

        cursor.execute(query)
        data = cursor.fetchall()

        # Atualizar a tabela com os resultados
        self.table.setRowCount(len(data))
        for row, item in enumerate(data):
            for column, value in enumerate(item):
                self.table.setItem(row, column, QTableWidgetItem(str(value)))

    def closeEvent(self, event):
        self.connection.close()
