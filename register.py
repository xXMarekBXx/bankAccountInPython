import io, os, sys, time, xml.etree.ElementTree as ET
try:
    sys.stdout = io.TextIOWrapper(open(sys.stdout.fileno(), 'wb', 0), write_through=True)
except TypeError:
    sys.stdout = os.fdopen(sys.stdout.fileno(), 'w', 0)

class Register():

    def __init__(self):
        self.FILE_NAME = 'accounts.xml'
        self.tree = ET.parse(self.FILE_NAME)
        self.root = self.tree.getroot()

    def setNewLastIdFromOldLastIdOrEmptyFileFromXMLFile(self):
        isUserExist = self.root.findall('user')
        if isUserExist == []:
            return 0
        else:
            lastId = self.root.findall('user')[-1].get('id')
            newLastId = int(lastId) + 1
            return newLastId

    def prettify(self, element, indent='  '):
        queue = [(0, element)]  # (level, element)
        while queue:
            level, element = queue.pop(0)
            children = [(level + 1, child) for child in list(element)]
            if children:
                element.text = '\n' + indent * (level + 1)  # for child open
            if queue:
                element.tail = '\n' + indent * queue[0][0]  # for sibling open
            else:
                element.tail = '\n' + indent * (level - 1)  # for parent close
            queue[0:0] = children  # prepend so children come before siblings

    def makeEntireXMLFilePreety(self):
        register.prettify(self.root)
        self.tree.write(self.FILE_NAME, encoding = 'UTF-8', xml_declaration = True)

    def addNewUserToXMLFile(self, id, login, password, email, saldo):
        user = ET.fromstring(f"<user><login>{login}</login>"
                             f"<password>{password}</password><email>{email}</email>"
                             f"<saldo>{saldo}</saldo></user>")
        user.set('id', str(id))
        self.root.append(user)
        self.tree.write(self.FILE_NAME, encoding = 'UTF-8', xml_declaration = True)

    def showRegisterMenu(self):
        print('______________')
        print(' REGISTRATION ')
        print('--------------')

    def setNewUserlogin(self):
        newUserlogin = input('Enter login: ')
        for index in self.root.findall('user'):
            takenLogin = index.find('login').text
            while newUserlogin == takenLogin:
                print('This login is taken. Please try again with a different login.')
                newUserlogin = input('Enter login: ')
                newUserlogin = str(newUserlogin)
        return newUserlogin

    def setNewUserpassword(self):
        newUserpassword = input('Enter password: ')
        newUserpassword = str(newUserpassword)
        return newUserpassword

    def setNewUseremail(self):
        newUseremail = input('Enter email: ')
        newUseremail = str(newUseremail)
        return newUseremail

    def registerNewUser(self):
        register.showRegisterMenu()
        newUserId = register.setNewLastIdFromOldLastIdOrEmptyFileFromXMLFile()
        newUserlogin = register.setNewUserlogin()
        newUserpassword = register.setNewUserpassword()
        newUseremail = register.setNewUseremail()
        newUsersaldo = 0
        register.addNewUserToXMLFile(newUserId, newUserlogin, newUserpassword, newUseremail, newUsersaldo)
        register.makeEntireXMLFilePreety()
        print('Your bank account has been created.')
        time.sleep(3)

register = Register()