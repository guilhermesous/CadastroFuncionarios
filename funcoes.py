import os
os.system ('cls')
import conexao
conectar = conexao.conectar


def pesquisa_nome():
    print('-------PESQUISA DE FUNCIONÁRIOS-------\nDigite o Nome do Funcionário ')
    nome_digitado = input('->')
    while True:
        if nome_digitado.isalpha() == False:
            print('-------CARACTERES INVÁLIDOS-------')
            nome_digitado = input('Digite o Nome Novamente\n->')
        else:
            break
            

    pesquisa = """SELECT * FROM  funcionarios WHERE Nome like"""
    dado_nome = ""f"('{nome_digitado}%')"""
    sql = pesquisa + dado_nome

    cursor = conectar.cursor()
    cursor.execute(sql)
    retornoDeDados = cursor.fetchall()
    for x in retornoDeDados:
        print('-'*70)        
        print(f"ID: {x[0]}, Nome: {x[1]}, Cargo: {x[2]}, Setor: {x[3]}, Salário: {x[4]}")

def listar():
    print('-------FUNCIONÁRIOS CADASTRADOS-------')

    comando_visualizar = """SELECT * FROM funcionarios"""
    cursor = conectar.cursor()
    cursor.execute(comando_visualizar)
    retornoDeDados = cursor.fetchall()  
    for x in retornoDeDados:
        print('-'*70)
        print(f"ID: {x[0]}, Nome: {x[1]}, Cargo: {x[2]}, Setor: {x[3]}, Salário: {x[4]}")
            

def delet_cadastro():
    print('-------DELETAR CADASTROS-------\n')
    
    while True:

        try:
            id_digitado = float(input("Digite o Id Do Funcionário: "))
            while id_digitado < 0:
                os.system('cls')
                id_digitado = float(input("Digite um Id álido: "))
            break
        except ValueError:
            os.system('cls')
            print("Caracteres Inválids\n")           




    comando_delet = """DELETE FROM funcionarios WHERE ID="""
    dado_id_delet = ""f"('{id_digitado}')"""
    sql = comando_delet + dado_id_delet
    cursor = conectar.cursor()
    cursor.execute(sql) 
    conectar.commit()
    print('FUNCIONÁRIO DELETADO DO BANCO')