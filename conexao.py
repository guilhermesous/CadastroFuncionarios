import os
os.system ('cls')
import mysql.connector
conectar = mysql.connector.connect(host = 'localhost',
                                   database = 'cadastrofuncionarios',
                                   user = '',
                                   password = '')