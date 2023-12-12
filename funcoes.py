import os
os.system ('cls')
import time
import conexao
conectar = conexao.conectar

def cadastrarFuncionario():
    print("Cadastrar Funcionário")
    print("------------------------")
    print()
    setor = ''
    while True:
        nome = input('Digite nome completo do funcionário: ').strip()
        if not nome:
            print("É necessário digitar algum caractere para continuar!")
        elif all(part.isalpha() or part.isspace() for part in nome.split()):
            break
        else:
            print("Nesse campo é válido apenas letras!\nTente novamente")
    while True:
        funcao = input('Digite a função do funcionário: ').strip()
        if not funcao:
            print("É necessário digitar algum caractere para continuar!")
        elif all(part.isalpha() or part.isspace() for part in funcao.split()):
            break
        else:
            print("Nesse campo é válido apenas letras!\nTente novamente")
    while True:
        try:
            escolha = int(input(
                'Digite o setor do funcionário 1- [ADM] 2- [OP] 3- [TI] 4- [LOG] 5- [RH]\n-> ').strip())
            if escolha == 1:
                setor = 'ADM'
                break
            elif escolha == 2:
                setor = 'OP'
                break
            elif escolha == 3:
                setor = 'TI'
                break
            elif escolha == 4:
                setor = 'LOG'
                break
            elif escolha == 5:
                setor = 'RH'
                break
            else:
                print("Número inválido!\nTente novamente")
        except ValueError:
            print("Nesse campo é válido apenas números!\nTente novamente")
    while True:
        try:
            salario = float(input('Digite o sálario do funcionário: ').strip())
            if salario < 660.50:
                print("Sálario inválido!\nPor favor, digite um sálario válido")
            elif salario > 500000:
                print("Sálario inválido!\nPor favor, digite um sálario válido")
            else:
                break
        except ValueError:
            print("Nesse campo é válido apenas números!\nTente novamente")
    time.sleep(0.3)
    os.system('cls')
    print("Cadastrando usuário...")
    dados = ""f"('{nome}', '{funcao}', '{setor}', '{salario}')"""
    comando_Insert = "INSERT INTO funcionarios(Nome, Funcao, setor, salario)values"
    sql = comando_Insert + dados
    cursor = conectar.cursor()
    cursor.execute(sql)
    conectar.commit()
    time.sleep(0.6)
    print("Usuário cadastrado com sucesso!")
    time.sleep(1)
    os.system('cls')

def pesquisa_nome():
    print('-------PESQUISA DE FUNCIONÁRIOS-------\nDigite o Nome do Funcionário ')
    nome_digitado = input('->')
    while True:
        if all(part.isalpha() or part.isspace() for part in nome_digitado.split()):
            break
        else:
            print('-------CARACTERES INVÁLIDOS-------')
            nome_digitado = input('Digite o Nome Novamente\n->')            

    pesquisa = """SELECT * FROM  funcionarios WHERE Nome like"""
    dado_nome = ""f"('{nome_digitado}%')"""
    sql = pesquisa + dado_nome

    cursor = conectar.cursor()
    cursor.execute(sql)
    retornoDeDados = cursor.fetchall()
    for x in retornoDeDados:
        print('-'*70)        
        print(f"ID: {x[0]}, Nome: {x[1]}, Cargo: {x[2]}, Setor: {x[3]}, Salário: {x[4]}")
    print('-'*70)

def listar():
    print('-------FUNCIONÁRIOS CADASTRADOS-------')

    comando_visualizar = """SELECT * FROM funcionarios"""
    cursor = conectar.cursor()
    cursor.execute(comando_visualizar)
    retornoDeDados = cursor.fetchall()  
    for x in retornoDeDados:
        print('-'*70)
        print(f"ID: {x[0]} Nome: {x[1]}, Cargo: {x[2]}, Setor: {x[3]}, Salário: {x[4]}")
    print('-'*70)     

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
    print('\nFUNCIONÁRIO DELETADO DO BANCO\n')