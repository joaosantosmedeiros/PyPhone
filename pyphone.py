def create(name, number, address, list:list):
    if len(list) > 0:
            cont = 0
            for index, value in enumerate(list):
                if value[1] == number:
                    cont += 1
            if cont > 0:
                return('Erro! Número ja cadastrado')
            else:
                list.append([name, number, address])        
                return f'Contato `{name}` cadastrado com sucesso!'

    else:
        list.append([name, number, address])
        return f'Contato `{name}` cadastrado com sucesso!'

def readAll(list:list):
    if len(list) > 0:
        result = ''
        for index, value in enumerate(list):
            result += (f'Nome: {value[0]} || Número: {value[1]} || Endereço: {value[2]} \n')
        return result
    else:
        return 'Agenda vazia.'

def readOne(number, list:list):
    if len(list) > 0:
        cont = 0
        for index, value in enumerate(list):
            if value[1] == number:
                cont += 1
                item = {}
                item['value'] = value 
                item['index'] = index
                return item
        if cont == 0:
            return('Contato não existente.')
    else:
        return('Contato não existente.')

def update(name, number, address, list:list, list_index):
    if len(list) > 0:
            cont = 0
            for index, value in enumerate(list):
                if value[1] == number:
                    cont += 1
            if cont > 0 and list[list_index][1] : #MExer aqui!
                return('Erro! Número ja cadastrado')
            else:
                list[list_index] = [name, number, address]      
                return f'Contato `{name}` atualizado com sucesso!'

    else:
        list[0] = [name, number, address]
        return f'Contato `{name}` atualizado com sucesso!'

def delete(number, list:list):
    result = readOne(number=number, list=list)
    if result == 'Contato não existente.':
        return result
    
    list.pop(result['index'])
    return 'Usuário deletado com sucesso.'

def menu():
    print('______PyPhone Agenda Telefônica______')
    print('1........Cadastrar contato..........1')
    print('2........Listar contatos............2')
    print('3........Buscar contato.............3')
    print('4........Editar contato.............4')
    print('5........Deletar contato............5')
    print('6........Sair.......................6')


menu()

agenda = []
while True:
    option = input('Digite sua opção: ')
    while option not in '123456':
        option = input('Erro! Digite sua opção: ')
    if option == '1':
        name = input('\nDigite seu nome: ')
        number = input('Digite seu número: ')
        address = input('Digite seu endereço: ')

        print(create(name=name, number=number, address=address, list=agenda), '\n')

    if option == '2':
        print(readAll(list=agenda))

    if option == '3':
        number = input('Digite o número a ser buscado: ')
        result = readOne(number=number, list=agenda)
        if result == 'Contato não existente.':
            print(result)
        else:
            result = result['value']
            print(f'Nome: {result[0]}  ||  Número: {result[1]}  ||  Endereço: {result[2]}')
        print()

    if option == '4':
        number = input('Digite o número a ser buscado: ')
        result = readOne(number=number, list=agenda)
        if result == 'Contato não existente.':
            print(result)
        else:
            name = input('\nDigite seu nome: ')
            number = input('Digite seu número: ')
            address = input('Digite seu endereço: ')
            
            updated_result = update(name=name, number=number, address=address, list=agenda, list_index=result['index'])
            print(updated_result, '\n')
        
    if option == '5':
        number = input('Digite o número: ')

        print(delete(number=number, list=agenda), '\n')

    if option == '6':
        break

print('Programa encerrado!')