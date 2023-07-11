import cx_Oracle


def establish_connection():
    server = ''
    database = ''
    username = ''
    password = ''

    try:
        # Estabelecer conexão com o banco de dados Oracle
        connection = cx_Oracle.connect(username, password, f'{server}/{database}')
        print('Conexão estabelecida com sucesso!')
        return connection
    except cx_Oracle.Error as error:
        print(f'Erro ao conectar ao banco de dados: {error}')
        return None
