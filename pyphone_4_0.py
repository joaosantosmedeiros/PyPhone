from os import system
from functions import createClient, readAllClients, readOneClient, updateClient, deleteClient
from functions import createCellphone, readOneCellphone, readAllCellphones, getKey, updateCellphone, deleteCellphone
from functions import createOrder, readOneOrder, readAllOrders, updateOrder, getOrderKey, deleteOrder

def menu_principal():
    print("===================================================")
    print("\tM E N U   P R I N C I P A L")
    print("===================================================")
    print('     1 - Cadastro de Clientes')
    print('     2 - Cadastro de Celulares')
    print('     3 - Cadastro de Vendas')
    print('     4 - Informações')
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
    print(f"     6 - Salvar em arquivo")
    print(f"     0 - Voltar ao Menu Principal")
    print("====================================================")

while True:
    clients = {}
    cellphones = {}
    orders = {}

    menu_principal()

    opc = input('\nEscolha sua opção: ')
    if opc not in '123450':
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
                print(f'\n{createClient(username=username, email=email, password=password, list=clients)}\n')

            elif option == '2':
                print(f'\n{readAllClients(list=clients)}')

            elif option == '3':
                email = input('Digite o email: ')
                result = (readOneClient(email=email, list=clients))
                if result == 'Cliente não existente.':
                    print('\n', result, '\n')
                else:
                    print(f'\nUsername: {result["value"][0]}')
                    print(f'Email: {result["value"][1]}\n')
                    # Não é mostrado a senha por questões de segurança
            
            elif option == '4':
                searchEmail = input('Digite o email do usuário que deseja alterar: ')

                result = updateClient(searchEmail=searchEmail, list=clients)
                print(f'\n{result}\n')

            elif option == '5':
                email = input('Insira o email: ')
                print('\n', deleteClient(email=email, list=clients), '\n')
            
            elif option == '6':
                with open('clients.txt','w') as f:
                    f.write(readAllClients(list=clients))

            input("Pressione qualquer tecla para continuar")
       
    elif opc == '2':
        while True:
            menu_secundario('celulares')
            option = input('\nEscolha sua opção: ')

            if option == '0':
                break
            
            elif option == '1':
                name = input('\nDigite o nome do celular:')
                price = input('Digite o preço do celular: ')
                print('\n', createCellphone(name=name, price=price, list=cellphones), '\n')
            
            elif option == '2':
                print(f'\n{readAllCellphones(cellphones)}\n')
            
            elif option == '3':
                id = input('Digite o id do celular: ')
                print(f'\n{readOneCellphone(id=id, list=cellphones)}\n')
            
            elif option == '4':
                id = input('Digite o id: ')
                result = getKey(list=cellphones, id=id)
                if result == 'Celular não existente.':
                    print(f'\n{result}\n')
                else:
                    name = input('Digite o nome: ')
                    price = input('Digite o preço: ')
                    print(f'\n{updateCellphone( id=id, name=name, price=price, list=cellphones)}\n')
            
            elif option == '5':
                id = input('Digite o id do celular: ')
                print(f'\n{deleteCellphone(id=id, list=cellphones)}\n')

            elif option == '6':
                with open('cellphones.txt','w') as f:
                    f.write(readAllCellphones(list=cellphones))

            input("Tecle ENTER para continuar")

    elif opc == '3':
        while True:
            menu_secundario('vendas')
            option = input('\nEscolha sua opção: ')

            if option == '0':
                break
            
            elif option == '1':
                clientEmail = input('\nDigite o email do cliente: ')
                id = input('Digite o id do produto: ')
                
                print('\n', createOrder(clientEmail=clientEmail, productId=id, list=orders))

            elif option == '2':
                print(f'\n{readAllOrders(orders)}')

            elif option == '3':
                id = input('Digite o id do pedido: ')
                print(f'\n{readOneOrder(id=id, list=orders)}\n')
            
            elif option == '4':
                id = input('Digite o id: ')
                result = getOrderKey(list=orders    , id=id)
                if result == 'Venda não existente.':
                    print(f'\n{result}\n')
                else:
                    email = input('Digite o email: ')
                    productId = input('Digite o id do produto: ')
                    print(f'\n{updateOrder( id=id, email=email, productId=productId, list=orders)}\n')

            elif option == '5':
                id = input('Digite o id do pedido: ')
                print(f'\n{deleteOrder(id=id, list=orders)}\n')
      
            input("Tecle ENTER para continuar")

    elif opc == '4':
        print('\n\nPyPhone')
        print('\nPrograma desenvolvido para a terceira unidade da disciplina')
        print('Algoritmos e Lógica de Programação. O software simula um ge-')
        print('renciamento de loja de celulares')
        print('\nDesenvolvido por João Pedro\n')

    input("Pressione qualquer tecla para continuar")
    system('cls || clear')
print('Fim.')
