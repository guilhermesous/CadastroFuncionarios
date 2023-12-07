import os
import conex
import time
import cadastrar
conectar = conex.conectar
os.system('cls')
def main():
    print("Bem-Vindo ao Sistema de Cadastro de Funcionários 1.0v")
    print("--------------------------------------------------------")
    print()
    while True:
        try:
           escolha = int(input('[1]- Para cadastrar um novo funcinário\n[2]- Para listar os funcionários cadastrados\n[3]- Para pesquisar um funcionário\n[4]- Para deletar um funcionário\n[0]- Para encerrar o sistema\n-> ').strip())
           if escolha == 1:
               cadastrar.cadastrarFuncionario()
           elif escolha == 2:
               pass
           elif escolha == 3:
               pass
           elif escolha == 4:
               pass
           elif escolha == 0:
               print("Encerrando o programa...")
               time.sleep(1)
               os.system('cls')
               break
           elif escolha > 4 or escolha < 0:
               print("Oção inválida!\nTente novamente")
               time.sleep(0.7)
               os.system('cls')
        except ValueError:
            print('Nesse campo é válido apenas números!\nTente novamente')
            time.sleep(0.7)
            os.system('cls')
if __name__ == '__main__':
    main()