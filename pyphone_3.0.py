from os import system
# O PyPhone é um sistema de gerenciamento de uma loja de celulares, onde é possível cadastrar
# funcionários, usuários e celulares.


def menu_principal():
    print("===================================================")
    print("\tM E N U   P R I N C I P A L")
    print("===================================================")
    print('     1 - Cadastro de Usuários')
    print('     2 - Cadastro de Funcionários')
    print('     3 - Cadastro de Celulares')
    print('     0 - Finalizar')
    print("===================================================")

def menu_secundario(name):
    system('cls || clear')
    print("===================================================")
    print("\t M E N U   ", end='')
    for char in name:
        print(char.upper(), end=' ')
    print("\n==================================================")
    print(f"     1 - Cadastrar {name.capitalize()}")
    print(f"     2 - Pesquisar {name.capitalize()}")
    print(f"     3 - Editar {name.capitalize()}")
    print(f"     4 - Apagar {name.capitalize()}")
    print("     0 - Voltar ao Menu Principal")
    print("====================================================")


while True:
    menu_principal()

    opc = input('\nEscolha sua opção: ')
    if opc not in '1230':
        print('=== Opção Invalida ===')
    if opc == '0':
        break
    elif opc == '1':
        while True:
            menu_secundario('usuários')
            option = input('\nEscolha sua opção: ')
            if option == '0':
                break
            elif option == '1':
                print("=== Menu Cadastrar Usuário  ==")
                print("==== Em Desenvolvimento ======")
            elif option == '2':
                print("=== Menu Pesquisar Usuário ===")
                print("===== Em Desenvolvimento =====")
            elif option == '3':
                print("===  Menu Editar Usuário ===")
                print("==== Em Desenvolvimento ====")
            elif option == '4':
                print("===  Menu Apagar Usuário ===")
                print("==== Em Desenvolvimento ====")
            input("Tecle ENTER para continuar")
    elif opc == '2':
        while True:
            menu_secundario('funcionários')
            option = input('\nEscolha sua opção: ')
            if option == '0':
                break
            elif option == '1':
                print("=== Menu Cadastrar Funcionários ===")
                print("=======  Em Desenvolvimento =======")
            elif option == '2':
                print("=== Menu Pesquisar Funcionários ===")
                print("=======  Em Desenvolvimento =======")
            elif option == '3':
                print("=== Menu Editar Funcionários ===")
                print("====== Em Desenvolvimento ======")
            elif option == '4':
                print("=== Menu Apagar Funcionários ===")
                print("====== Em Desenvolvimento ======")
            input("Tecle ENTER para continuar")
    elif opc == '3':
        while True:
            menu_secundario('celulares')
            option = input('\nEscolha sua opção: ')
            if option == '0':
                break
            elif option == '1':
                print("=== Menu Cadastrar Celulares ===")
                print("======  Em Desenvolvimento =====")
            elif option == '2':
                print("=== Menu Pesquisar Celulares ===")
                print("=====  Em Desenvolvimento ======")
            elif option == '3':
                print("===  Menu Editar Celulares ===")
                print("===== Em Desenvolvimento =====")
            elif option == '4':
                print("===  Menu Apagar Celulares ===")
                print("=== ==Em Desenvolvimento =====")
            input("Tecle ENTER para continuar")

    input("Pressione qualquer tecla para continuar")
    system('cls || clear')
print('Fim.')
