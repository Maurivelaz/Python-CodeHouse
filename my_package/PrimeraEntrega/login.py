ruta = 'usuarios.txt'
users = {}
def register ():
    """
    Register a new user
    Returns:
        True: if was register successful
    """
    try:
        readTxt()
    except:
        print('Error en ruta de txt')
        return
    print('Bienvenido \nVa a registrar un usuario porfavor')
    name = input('Ingrese un usuario \n')
    password = input('Ingrese una contraseña \n')
    while True:
        if name not in users:
            users[name] = password
            f = open(ruta,'a')
            f.write(f'{name}:{password}:')
            f.close()
            print('Usuario registrado correctamente')
            return True
            break
        else:
            print('El usuario es repetido ingrese otro')
            name = input('Ingrese nuevamente otro usuario\n')
            password = input('ingrese la contraseña\n')

def readTxt():
    """
    Read Database in txt
    """
    f = open(ruta,'r')
    datos = list(f.read().split(':'))
    f.close()
    datos.pop()
    usuarios=[]
    contraseñas=[]
    
    for clave,valor in enumerate(datos):
        if(clave%2==0):
            usuarios.append(valor)
    for clave,valor in enumerate(datos):
        if(not clave%2==0):
            contraseñas.append(valor)
    
    newdiccionario = dict(zip(usuarios,contraseñas))
    for clave, valor in newdiccionario.items():
        users[clave]= valor

def login():
    """
    Login user
    Returns:
        True: if user is inside database
    """
    try:
        readTxt()
    except:
        print('Error en ruta de txt')
        return
    name = input('Ingrese su usuario \n')
    password = input('ingrese la contraseña \n')
    try:
        while True:
            if name in users:
                if name == 'Admin' and password == users[name]:
                    print(f'Bienvenido {name}')
                    case1= int(input('Desea ver la lista de usuarios? aprete 1 , de lo contrario aprete cualquier otro numero \n'))
                    if case1 == 1:
                        show_users()
                        return True
                    else:
                        return True
                elif password in users[name] and password == users[name]:
                    print(f'Bienvenido {name}')
                    return True
                else:
                    print('Contraseña incorrecta')
                    login()
            else:
                print('El usuario ingresado no existe')
                opcion = int(input('Si desea registrarlo presione 1 \nSi desea intentarlo nuevamente presione cualquier tecla\n'))
                if(opcion ==1):
                    register()
                    main()
                    break
                else:
                    login()
    except:
        print('Error en el login vuelva a intentarlo')
        login()

def show_users():
    """
    Method for show user in dictionary
    """
    readTxt()
    print(f'La lista de usuarios es \nUsuario:     Contraseña:')
    for clave,valor in users.items():
        print(f'{clave}      {valor}')

def main():
    """
    Method Main
    """
    print('Bienvenido')
    while True:
        try:
            opcion = int(input('1. Loggear\n2. Registro\n3. Salir\n'))
            if opcion == 1:
                if(login()):
                    return True
                else:
                    break
            elif opcion == 2:
                if(register()):
                    main()
                else:
                    break
            elif opcion >=3 or opcion == 0:
                print('Adios')
                break
        except:
            print('No es un valor aceptado porfavor vuelta a ingresar solo numero')

