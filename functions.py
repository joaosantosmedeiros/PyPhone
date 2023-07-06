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
        cont = 0
        for key in list:
            if str(key) == id:
                cont += 1
                return key
        if cont == 0:
            return('Celular não existente.')
    else:
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
    else:
        return ''

def readOneCellphone(list:dict, id):
    if len(list) > 0:
        cont = 0
        for key in list:
            if str(key) == id:
                cont += 1
                return(f'Id: {key}\nNome:{list[key][0]}\nPreço: R${list[key][1]}')
        if cont == 0:
            return('Celular não existente.')
    else:
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
