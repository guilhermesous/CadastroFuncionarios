import os
os.system ('cls')
import mysql.connector 

conectar = mysql.connector.connect(host='localhost',
                                   database = 'cadastrofuncionarios',
                                   user='henrygab', 
                                   password='897612')


def pesquisa_nome():
    print('-------PESQUISA DE FUNCIONÁRIOS-------\nDigite o Nome do Funcionário ')
    nome_digitado = input('->')
    while True:
        if nome_digitado.isalpha() == False:
            print('-------CARACTERES INVÁLIDOS-------')
            nome_digitado = input('Digite o Nome Novamente\n->')
        else:
            break
            

    pesquisa = """SELECT * FROM  cadastrofuncionarios WHERE Nome="""
    dado_nome = ""f"('{nome_digitado}')"""
    sql = pesquisa + dado_nome

    cursor = conectar.cursor()
    cursor.execute(sql)
    retornoDeDados = cursor.fetchall()
    for linha in retornoDeDados:
        print('-'*20)
        for x in linha: 
            print(x)

def listar():
    print('-------FUNCIONÁRIOS CADASTRADOS-------')

    comando_visualizar = """SELECTE * FROM cadastrofuncionarios"""
    cursor = conectar.cursor()
    cursor.execute(comando_visualizar)
    retornoDeDados = cursor.fetchall()  
    for linha in retornoDeDados:
        print('____')
    for x in linha:
        print(x)

def delet_cadastro():
    print('-------DELETAR CADASTROS-------\nDigite o ID do Funcionário ')
    print('Digite o ID que deseja excluir')
    
    while True:

        try:
            id_digitado = float(input("Digite o Id Do Funcionário"))
            while id_digitado < 0:
                os.system('cls')
                id_digitado = float(input("Digite um Id válido"))
            break
        except ValueError:
            os.system('cls')
            print("Caracteres Inválids\n")           




    comando_delet = """DELET * FROM cadastrofuncionarios WHERE ID="""
    dado_id_delet = ""f"('{id_digitado}')"""
    sql = comando_delet + dado_id_delet
    cursor = conectar.cursor()
    cursor.execute(sql)
    retornoDeDados = cursor.fetchall()


    for linha in retornoDeDados:
        print('-'*20)
        for x in linha: 
            print(x)