from random import randint

class Clients:
    def createClient(username, email, password, list:list):
        if len(list) > 0:
                cont = 0
                for index, value in enumerate(list):
                    if value[1] == email:
                        cont += 1
                if cont > 0:
                    return('Erro! Email ja cadastrado')
                else:
                    list.append([username, email, password])        
                    return f'Cliente `{username}` cadastrado com sucesso!'

        else:
            list.append([username, email, password])        
            return f'Cliente `{username}` cadastrado com sucesso!'

    def readAllClients(list:list):
        if len(list) > 0:
            result = ''
            for index, value in enumerate(list):
                result += (f'Username: {value[0]} || Email: {value[1]}\n')
            return result
        else:
            return ''

    def readOneClient(email, list:list):
        if len(list) > 0:
            cont = 0
            for index, value in enumerate(list):
                if value[1] == email:
                    cont += 1
                    item = {}
                    item['value'] = value 
                    item['index'] = index
                    return item
            if cont == 0:
                return('Cliente não existente.')
        else:
            return('Cliente não existente.')

    def updateClient(username, email, password, list:list, list_index):
        if len(list) > 0:
                cont = 0
                for index, value in enumerate(list):
                    if value[1] == email:
                        cont += 1
                if cont > 0 and list[list_index][1] : 
                    return('Erro! Email ja cadastrado')
                else:
                    list[list_index] = [username, email, password]      
                    return f'Cliente `{username}` atualizado com sucesso!'

        else:
            list[0] = [username, email, password]
            return f'Cliente `{username}` atualizado com sucesso!'

    def deleteClient(self, email, list:list):
        result = self.readOneClient(email=email, list=list)
        if result == 'Cliente não existente.':
            return result
        
        list.pop(result['index'])
        return 'Cliente deletado com sucesso.'

class Employees:
    def createEmployee(username, email, contact, password, list:list):
        if len(list) > 0:
                cont = 0
                for index, value in enumerate(list):
                    if value[1] == email:
                        cont += 1
                if cont > 0:
                    return('Erro! Email ja cadastrado')
                else:
                    list.append([username, email, contact, password])        
                    return f'Funcionário `{username}` cadastrado com sucesso!'

        else:
            list.append([username, email, contact, password])        
            return f'Funcionário `{username}` cadastrado com sucesso!'

    def readAllEmployees(list:list):
        if len(list) > 0:
            result = ''
            for index, value in enumerate(list):
                result += (f'Username: {value[0]} || Email: {value[1]} || Contact: {value[2]}\n')
            return result
        else:
            return ''

    def readOneEmployee(email, list:list):
        if len(list) > 0:
            cont = 0
            for index, value in enumerate(list):
                if value[1] == email:
                    cont += 1
                    item = {}
                    item['value'] = value 
                    item['index'] = index
                    return item
            if cont == 0:
                return('Funcionário não existente.')
        else:
            return('Funcionário não existente.')

    def updateEmployee(username, email, contact, password, list:list, list_index):
        if len(list) > 0:
                cont = 0
                for index, value in enumerate(list):
                    if value[1] == email:
                        cont += 1
                if cont > 0 and list[list_index][1] : 
                    return('Erro! Email ja cadastrado')
                else:
                    list[list_index] = [username, email, contact, password]      
                    return f'Funcionário `{username}` atualizado com sucesso!'

        else:
            list[0] = [username, email, password]
            return f'Funcionário `{username}` atualizado com sucesso!'

    def deleteEmployee(self, email, list:list):
        result = self.readOneEmployee(email=email, list=list)
        if result == 'Funcionário não existente.':
            return result
        
        list.pop(result['index'])
        return 'Funcionário deletado com sucesso.'

class Cellphones:
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
        length = len(list)        
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
    
    def updateCellphone(self, id, name, price, list:dict):
        id = int(id)
        list[id] = [name, price]

        return 'Celular atualizado com sucesso.'

    def deleteCellphone(self, id, list:dict):
        result = self.getKey(id=id, list=list)
        if result == 'Celular não existente.':
            return result
        
        list.pop(result)
        return 'Cliente deletado com sucesso.'
