from os import system
from functions import Clients, Employees, Cellphones

# O PyPhone é um sistema de gerenciamento de uma loja de celulares, onde é possível cadastrar
# funcionários, clientes e celulares.


def menu_principal():
    print("===================================================")
    print("\tM E N U   P R I N C I P A L")
    print("===================================================")
    print('     1 - Cadastro de Clientes')
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
    print(f"     2 - Listar {name.capitalize()}")
    print(f"     3 - Pesquisar {name.capitalize()}")
    print(f"     4 - Editar {name.capitalize()}")
    print(f"     5 - Apagar {name.capitalize()}")
    print(f"     0 - Voltar ao Menu Principal")
    print("====================================================")


while True:
    clients = []
    employees = []
    cellphones = {}

    menu_principal()

    opc = input('\nEscolha sua opção: ')
    if opc not in '1230':
        print('=== Opção Invalida ===')
    
    if opc == '0':
        break
    
    elif opc == '1':
        while True:
            menu_secundario('clientes')
            option = input('\nEscolha sua opção: ')

            if option == '0':
                break

            elif option == '1':
                username = input('\nDigite o nome do cliente: ')
                email = input('Digite o email do cliente: ')
                password = input('Digite a senha do cliente: ')
                print('\n', Clients.createClient(username=username, email=email, password=password, list=clients), '\n')

            elif option == '2':
                print(Clients.readAllClients(list=clients))

            elif option == '3':
                email = input('Digite o email: ')
                result = (Clients.readOneClient(email=email, list=clients))
                if result == 'Cliente não existente.':
                    print('\n', result, '\n')
                else:
                    print(f'\nUsername: {result["value"][0]}')
                    print(f'Email: {result["value"][1]}\n')
                    # Não é mostrado a senha por questões de segurança
            
            elif option == '4':
                email = input('Digite o email a ser buscado: ')
                result = Clients.readOneClient(email=email, list=clients)
                if result == 'Cliente não existente.':
                    print(result)
                else:
                    username = input('\nDigite seu nome: ')
                    email = input('Digite seu email: ')
                    password = input('Digite sua senha: ')

                    updated_result = Clients.updateClient(
                        username=username, email=email, password=password, list=clients, list_index=result['index'])
                    print('\n', updated_result, '\n')
            
            elif option == '5':
                email = input('Insira o email: ')
                print('\n', Clients.deleteClient(self=Clients, email=email, list=clients), '\n')
            input("Pressione qualquer tecla para continuar")
       
    elif opc == '2':
        while True:
            menu_secundario('funcionários')
            option = input('\nEscolha sua opção: ')

            if option == '0':
                break
            
            elif option == '1':
                username = input('\nDigite o nome do funcionário: ')
                email = input('Digite o email do funcionário: ')
                contact = input('Digite o contato do funcionário: ')
                password = input('Digite a senha do funcionário: ')
                print('\n', Employees.createEmployee(username=username, email=email, contact=contact, password=password, list=employees), '\n')
            
            elif option == '2':
                print(Employees.readAllEmployees(list=employees))
            
            elif option == '3':
                email = input('Digite o email: ')
                result = (Employees.readOneEmployee(email=email, list=employees))
                if result == 'Funcionário não existente.':
                    print('\n', result, '\n')
                else:
                    print(f'\nUsername: {result["value"][0]}')
                    print(f'Email: {result["value"][1]}')
                    print(f'Contato: {result["value"][2]}\n')
                    # Não é mostrado a senha por questões de segurança
            
            elif option == '4':
                email = input('Digite o email a ser buscado: ')
                result = Employees.readOneEmployee(email=email, list=employees)
                if result == 'Funcionário não existente.':
                    print(result)
                else:
                    username = input('\nDigite seu nome: ')
                    email = input('Digite seu email: ')
                    contact = input('Digite seu contato: ')
                    password = input('Digite sua senha: ')

                    updated_result = Employees.updateEmployee( username=username, email=email, contact=contact, password=password, list=employees, list_index=result['index'])
                    print('\n', updated_result, '\n')
            
            elif option == '5':
                email = input('Insira o email: ')
                print('\n', Employees.deleteEmployee(self=Employees, email=email, list=employees), '\n')
            input("Pressione qualquer tecla para continuar")
    
    elif opc == '3':
        while True:
            menu_secundario('celulares')
            option = input('\nEscolha sua opção: ')
            
            if option == '0':
                break
            
            elif option == '1':
                name = input('\nDigite o nome do celular:')
                price = input('Digite o preço do celular: ')
                print('\n', Cellphones.createCellphone(name=name, price=price, list=cellphones), '\n')
            
            elif option == '2':
                print(f'\n{Cellphones.readAllCellphones(cellphones)}\n')
            
            elif option == '3':
                id = input('Digite o id do celular: ')
                print(f'\n{Cellphones.readOneCellphone(id=id, list=cellphones)}\n')
            
            elif option == '4':
                id = input('Digite o id: ')
                result = Cellphones.getKey(list=cellphones, id=id)
                if result == 'Celular não existente.':
                    print(result)
                else:
                    name = input('Digite o nome: ')
                    price = input('Digite o preço: ')
                    print(f'\n{Cellphones.updateCellphone(self=Cellphones, id=id, name=name, price=price, list=cellphones)}\n')
            
            elif option == '5':
                id = input('Digite o id do celular: ')
                print(f'\n{Cellphones.deleteCellphone(self=Cellphones, id=id, list=cellphones)}\n')
            input("Tecle ENTER para continuar")

    input("Pressione qualquer tecla para continuar")
    system('cls || clear')
print('Fim.')
