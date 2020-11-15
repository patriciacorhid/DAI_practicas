from pickleshare import *

# Usuarios de Cactus Web (P3) 
db = PickleShareDB('miBD')

# Para eliminar usuarios creados anteriormente en la base de datos
db.clear()

# Creo un par de usuarios de prueba
db['Pepe'] = dict()
db['Pepe']['pass'] = '1234'
db['Pepe'] = db['Pepe']

db['Maria'] = dict()
db['Maria']['pass'] = '1111'
db['Maria'] = db['Maria']

# Comprueba si el usuario está registrado
def user_registrado(user):
    if user in db:
        return True
    return False

# Comprueba si la contraseña es la suya
def pwd_correcta(user, pwd):
    if db[user]['pass'] == pwd:
        return True
    return False

# Crea un nuevo usuario
def crea_user(username, password):
    db[username] = dict()
    db[username]['pass'] = password
    db[username] = db[username]

# Borra un usuario
def borra_user(username):
    del db[username]

# Devuelve la contraseña del usuario
def get_pwd(user):
    return db[user]['pass']

