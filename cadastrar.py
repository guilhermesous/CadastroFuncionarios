import conex
conectar = conex.conectar
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
            escolha = int(input('Digite o setor do funcionário 1- [ADM] 2- [OPR] 3- [TI] 4- [LOG] 5- [RH]\n-> ').strip())
            if escolha == 1:
                setor == 'ADM'
                break
            elif escolha == 2:
                setor = 'OPR'
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
        except ValueError:
            print("Nesse campo é válido apenas números!\nTente novamente")
    while True:
        try:
            salario = float(input().strip())
        except ValueError:
            print()
    
    
