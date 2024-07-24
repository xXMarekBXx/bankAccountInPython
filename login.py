import io, os, sys, time, xml.etree.ElementTree as ET

class Login():
    def __init__(self):
        self.FILE_NAME = 'accounts.xml'
        self.LOGIN = 0
        self.PASSWORD = 1
        self.EMAIL = 2
        self.SALDO = 3
        self.isUserLoggedIn = False
        self.userNumber = 0
        self.tree = ET.parse(self.FILE_NAME)
        self.root = self.tree.getroot()
        self.isSetingsShown = False

    def setUserNumber(self, id):
        self.userNumber = id
        return self.userNumber

    def getUserNumber(self):
        return self.userNumber

    def setTheLoginFlagToTrue(self):
        self.isUserLoggedIn = True
        return self.isUserLoggedIn

    def setTheLoginFlagToFalse(self):
        self.isUserLoggedIn = False
        return self.isUserLoggedIn

    def showPrintAndConstantValue(self, text, numberOfSteps, constantValue):
        print(f'{text}{self.root[numberOfSteps - 1][constantValue].text}')

    def showAccountMenu(self):
        while self.isUserLoggedIn == True:
            print('__________')
            print(' ACCOUNT  ')
            print('----------')
            print('1.Show actual saldo')
            print('2.Deposit money')
            print('3.Withdraw money')
            print('4.Settings')
            print('5.Log out')
            option = input('Choose option: ')
            option = str(option)
            match (option):
                case '1':
                    login.showLoggedInUserSaldo()
                case '2':
                    login.depositMoneyToLoggedInUser()
                case '3':
                    login.withdrawMoneyFromLoggedInUser()
                case '4':
                    self.isSetingsShown = True
                    login.showSettingsMenu()
                case '5':
                    print()
                    print('Logged out.')
                    time.sleep(3)
                    login.setTheLoginFlagToFalse()

    def logInUser(self):
        enterLogin = input('Enter login: ')
        numberOfSteps = 0
        for index in self.root.findall('user'):
            xmlLogin = index.find('login').text
            numberOfSteps += 1
            self.userNumber = login.setUserNumber(numberOfSteps)
            if enterLogin == xmlLogin:
                numberOfSteps -= 1
                xmlPassword = self.root[numberOfSteps][self.PASSWORD].text
                enterPassword = input('Enter password: ')
                if enterPassword == xmlPassword:
                    print('You are logged in.')
                    time.sleep(3)
                    login.setTheLoginFlagToTrue()
                    login.showAccountMenu()
                    return self.userNumber
                else:
                    print('Incorrect password.')
                    time.sleep(3)

    def depositMoneyToLoggedInUser(self):
        depositingMoney = input('How much money You want to deposit: ')
        depositingMoney = float(depositingMoney)
        numberOfSteps = 0
        for saldo in self.root.iter('saldo'):
            numberOfSteps += 1
            if numberOfSteps == login.getUserNumber():
                newSaldo = float(saldo.text) + depositingMoney
                saldo.text = str(newSaldo)
                self.tree.write(self.FILE_NAME)
                print('Account is updated.')
                time.sleep(1)
                print(f'Actual saldo: {self.root[numberOfSteps - 1][self.SALDO].text}')

    def withdrawMoneyFromLoggedInUser(self):
        withdrawMoney = input('How much money You want to withdraw: ')
        withdrawMoney = float(withdrawMoney)
        numberOfSteps = 0
        for saldo in self.root.iter('saldo'):
            numberOfSteps += 1
            if numberOfSteps == login.getUserNumber():
                newSaldo = float(saldo.text) - withdrawMoney
                saldo.text = str(newSaldo)
                self.tree.write(self.FILE_NAME)
                print('Account is updated.')
                time.sleep(1)
                print(f'Actual saldo: {self.root[numberOfSteps - 1][self.SALDO].text}')

    def showLoggedInUserSaldo(self):
        numberOfSteps = 0
        for saldo in self.root.iter('saldo'):
            numberOfSteps += 1
            if numberOfSteps == login.getUserNumber():
                login.showPrintAndConstantValue("Actual saldo: ", numberOfSteps, self.SALDO)

    def checkIfLoginIsTaken(self, loginToCheck):
        counter = 0
        for index in self.root.findall('user'):
            takenLogin = index.find('login').text
            if loginToCheck == takenLogin:
                counter += 1
        return counter

    def setNewLogin(self):
        newLogin = input('Enter your new login: ')
        login = Login()
        counterIfLoginIsTaken = login.checkIfLoginIsTaken(newLogin)
        while counterIfLoginIsTaken != 0:
            print('This login is taken. Please try again with a different login.')
            newLogin = input('Enter your new login: ')
            counterIfLoginIsTaken = login.checkIfLoginIsTaken(newLogin)
        numberOfSteps = 0
        for login in self.root.iter('login'):
            numberOfSteps += 1
            if numberOfSteps == self.userNumber:
                login.text = str(newLogin)
                self.tree.write(self.FILE_NAME)
                print('Account is updated.')
                time.sleep(1)
                print(f'Actual login: {self.root[numberOfSteps - 1][self.LOGIN].text}')

    def setNewPassword(self):
        newPassword = input('Enter your new password: ')
        newPassword = str(newPassword)
        numberOfSteps = 0
        for password in self.root.iter('password'):
            numberOfSteps += 1
            if numberOfSteps == login.getUserNumber():
                password.text = str(newPassword)
                self.tree.write(self.FILE_NAME)
                print('Account is updated.')
                time.sleep(1)
                login.showPrintAndConstantValue("Actual password: ", numberOfSteps, self.PASSWORD)

    def setNewEmail(self):
        newEmail = input('Enter your new email: ')
        newEmail = str(newEmail)
        numberOfSteps = 0
        for email in self.root.iter('email'):
            numberOfSteps += 1
            if numberOfSteps == login.getUserNumber():
                email.text = str(newEmail)
                self.tree.write(self.FILE_NAME)
                print('Account is updated.')
                time.sleep(1)
                login.showPrintAndConstantValue("Actual email: ", numberOfSteps, self.EMAIL)

    def showSettingsMenu(self):
        while self.isSetingsShown == True:
            print('__________')
            print(' Settings ')
            print('----------')
            print('1. Change login')
            print('2. Change password')
            print('3. Change email')
            print('4. Back to account')
            option = input('Choose option: ')
            option = str(option)
            match (option):
                case '1':
                    login.setNewLogin()
                case '2':
                    login.setNewPassword()
                case '3':
                    login.setNewEmail()
                case '4':
                    self.isSetingsShown = False
                    print()

login = Login()