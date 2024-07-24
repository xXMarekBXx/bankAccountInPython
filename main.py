import register
import login

register = register.Register()
login = login.Login()

while True:
    print('__________')
    print(' M E N U  ')
    print('----------')
    print('1. Log in')
    print('2. Register')
    print('3. Close project')
    option = input('Choose option: ')
    option = str(option)
    match(option):
        case '1':
            login.logInUser()
        case '2':
            register.registerNewUser()
        case '3':
            print()
            print('Project closed.')
            exit()