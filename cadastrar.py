import conexao
import time
import os
import sistema_cadastro
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


