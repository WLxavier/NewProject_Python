import sys
from PyQt5.QtWidgets import QApplication
from database_connection import establish_connection
from product_search import ProductWindow

if __name__ == '__main__':
    # Estabelecer conexão com o banco de dados
    connection = establish_connection()

    if connection:
        app = QApplication(sys.argv)
        # Abrir a janela de pesquisa de produtos
        product_window = ProductWindow(connection)
        product_window.show()
        sys.exit(app.exec_())
    else:
        print('Falha na conexão com o banco de dados.')
