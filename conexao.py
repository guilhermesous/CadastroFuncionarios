import mysql.connector
conectar = mysql.connector.connect(host = 'localhost',
                                   database = 'cadastrofuncionarios',
                                   user = '',
                                   password = '')
if conectar.is_connected():
    print('Conexão realizado com sucesso!')
else:
    print('falha na conexão')
