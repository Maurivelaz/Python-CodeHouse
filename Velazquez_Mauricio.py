ruta = 'usuarios.txt'
users = {}
def register ():
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
            f = open(ruta, 'a')
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
                if password in users[name] and password == users[name]:
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
                    break
                else:
                    login()
    except:
        print('Error en el login vuelva a intentarlo')
        login()

def main():
    print('Bienvenido')
    while True:
        try:
            opcion = int(input('1. Loggear\n2. Registro\n3. Salir\n'))
            if opcion == 1:
                if(login()):
                    break
            elif opcion == 2:
                if(register()):
                    main()
            elif opcion >=3 or opcion == 0:
                print('Adios')
                break
        except:
            print('No es un valor aceptado porfavor vuelta a ingresar solo numero')
main()