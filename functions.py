from random import randint

class Clients:
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

    def updateClient(self, searchEmail, list:dict):
        result = self.readOneClient(email=searchEmail, list=list)
        if result == 'Cliente não existente.':
            return result

        del list[searchEmail]

        newEmail = input('Novo email: ')
        newUsername = input('Novo nome de usuário: ')
        newPassword = input('Nova senha: ')

        return self.createClient(username=newUsername, email=newEmail, password=newPassword, list=list)
        
    def deleteClient(self, email, list:dict):
        result = self.readOneClient(email=email, list=list)
        if result == 'Cliente não existente.':
            return result
        
        del list[email]
        return 'Cliente deletado com sucesso.'


class Employees:
    def createEmployee(username, email, contact, password, list:dict):
        for key in list:
            if(key == email):
                return('Erro! Email ja cadastrado')
        
        list[email] = [ username, contact, password]
        return f'Funcionário `{username}` cadastrado com sucesso!'

    def readAllEmployees(list:dict):
        result = ''
        if list:
            for email in list:
                result += f'Username: {list[email][0]} | Email: {email} | Contato: {list[email][1]}\n'
        return result

    def readOneEmployee(email, list:dict):
        if list:
            for key in (list):
                if key == email:
                    return {
                        'value': list[key],
                        'email': key
                    }

            return('Funcionário não existente.')

    def updateEmployee(self, searchEmail, list:dict):
        result = self.readOneEmployee(email=searchEmail, list=list)
        if result == 'Funcionário não existente.':
            return result

        del list[searchEmail]

        newEmail = input('Novo email: ')
        newUsername = input('Novo nome de usuário: ')
        newContact = input('Novo contato:')
        newPassword = input('Nova senha: ')

        return self.createEmployee(username=newUsername, email=newEmail, contact=newContact,  password=newPassword, list=list)
        
    def deleteEmployee(self, email, list:dict):
        result = self.readOneEmployee(email=email, list=list)
        if result == 'Funcionário não existente.':
            return result
        
        del list[email]
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
        return 'Celular deletado com sucesso.'
