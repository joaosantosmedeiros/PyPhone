from os import system

while True:
    print("=====================================")
    print("==== M E N U   P R I N C I P A L ====")
    print("=====================================")
    print('     1 - Cadastro de usuários')
    print('     2 - Cadastro de funcionários')
    print('     3 - Cadastro de Celulares')
    print('     0 - Finalizar')
    print("=====================================")

    opc = input('\nEscolha sua opção: ')
    if opc not in '1230':
        print('=== Opção Invalida ===')
    if opc == '0':
        break
    elif opc == '1':
        print('====      Usuários      ====')
        print('==== Em desenvolvimento ====')
    elif opc == '2':
        print('====    Funcionários    ====')
        print('==== Em desenvolvimento ====')
    elif opc == '3':
        print('====     Celulares      ====')
        print('==== Em desenvolvimento ====')

    input("Pressione qualquer tecla para continuar")
    system('cls || clear')
print('Fim.')
