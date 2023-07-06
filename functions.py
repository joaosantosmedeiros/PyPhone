from random import randint

# Clientes
def createClient(username, email, password, list:dict):
    for key in list:
        if(key == email):
            return('Erro! Email ja cadastrado')
    
    list[email] = [ username, password]
    return f'Cliente `{username}` cadastrado com sucesso!'

def readAllClients(list:dict):
    result = ''
    if list:
        for email in list:
            result += f'Username: {list[email][0]} | Email: {email}\n'
    return result

def readOneClient(email, list:dict):
    if list:
        for key in (list):
            if key == email:
                return {
                    'value': list[key],
                    'email': key
                }
        
    return('Cliente não existente.')

def updateClient(searchEmail, list:dict):
    result = readOneClient(email=searchEmail, list=list)
    if result == 'Cliente não existente.':
        return result

    del list[searchEmail]

    newEmail = input('Novo email: ')
    newUsername = input('Novo nome de usuário: ')
    newPassword = input('Nova senha: ')

    return createClient(username=newUsername, email=newEmail, password=newPassword, list=list)
    
def deleteClient( email, list:dict):
    result = readOneClient(email=email, list=list)
    if result == 'Cliente não existente.':
        return result
    
    del list[email]
    return 'Cliente deletado com sucesso.'


# Celulares
def getKey(list:dict, id):
    if len(list) > 0:
        for key in list:
            if str(key) == id:
                return key
    return('Celular não existente.')

def createCellphone(name, price, list:dict):
    list[randint(0, 999999)] = [name, price]
    return f'Celular `{name}` cadastrado com sucesso!'

def readAllCellphones(list:dict):
    if len(list) > 0:
        result = ''
        for key in list:
            result += (f'Id: {key} || Nome: {list[key][0]} || Preço: R${list[key][1]}\n')
        return result
    return ''

def readOneCellphone(list:dict, id):
    if len(list) > 0:
        for key in list:
            if str(key) == id:
                return(f'Id: {key}\nNome:{list[key][0]}\nPreço: R${list[key][1]}')
    return('Celular não existente.')

def updateCellphone(id, name, price, list:dict):
    id = int(id)
    list[id] = [name, price]

    return 'Celular atualizado com sucesso.'

def deleteCellphone(id, list:dict):
    result = getKey(id=id, list=list)
    if result == 'Celular não existente.':
        return result
    
    list.pop(result)
    return 'Celular deletado com sucesso.'


# Vendas
def getOrderKey(list:dict, id):
    if len(list) > 0:
        for key in list:
            if str(key) == id:
                return key
    return('Venda não existente.')

def createOrder(clientEmail, productId, list:dict):
    cont = 0
    clientsFile = open('clients.txt')
    for linha in clientsFile:
        email = linha.split("Email: ")[1]
        email = email.replace('\n', '')
        if email == clientEmail:
            cont = 1
            break

    if cont != 1:
        return 'Cliente nao encontrado.'
    clientsFile.close()


    cellphonesFile = open('cellphones.txt')
    cont = 0
    for linha in cellphonesFile:
        id = linha.split("Id: ")[1].split(" ||")[0].replace('\n', '')
        if id == productId:
            cont = 1
            break

    if cont != 1:
        return 'Produto nao encontrado.'
    cellphonesFile.close()

    
    randomId = randint(0, 99999999)
    list[randomId] = [clientEmail, productId]
    return f'Venda de Id: {randomId} criada!'

def readAllOrders(list:dict):
    if len(list) > 0:
        result = ''
        for key in list:
            result += (f'Id: {key} || Cliente: {list[key][0]} || Produto: {list[key][1]}\n')
        return result
    else:
        return ''

def readOneOrder(list:dict, id):
    if len(list) > 0:
        for key in list:
            if str(key) == id:
                return(f'Id: {key}\nEmail: {list[key][0]}\nProduto: {list[key][1]}')
    return('Venda não existente.')

def updateOrder(id, email, productId, list:dict):
    id = int(id)

    cont = 0
    clientsFile = open('clients.txt')
    for linha in clientsFile:
        fileEmail = linha.split("Email: ")[1].replace('\n', '')
        if fileEmail == email:
            cont = 1
            break

    if cont != 1:
        return 'Cliente nao encontrado.'
    clientsFile.close()


    cellphonesFile = open('cellphones.txt')
    cont = 0
    for linha in cellphonesFile:
        fileId = linha.split("Id: ")[1].split(" ||")[0].replace('\n', '')
        if fileId == productId:
            cont = 1
            break

    if cont != 1:
        return 'Produto nao encontrado.'
    cellphonesFile.close()

    list[id] = [email, productId]
    return 'Venda atualizado com sucesso.'

def deleteOrder(id, list:dict):
    result = getOrderKey(id=id, list=list)
    if result == 'Venda não existente.':
        return result
    
    list.pop(result)
    return 'Venda deletado com sucesso.'
