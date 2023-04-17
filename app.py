import valida_login
import cryptographyFramework
from valida_login import *
def valida_login():
    while True:
        user = input('Digite o user: ')
        if valida_user(user) ==  True:
            break
    while True:
        senha = input('Digite a senha: ')
        if valida_senha(senha) == True:
            break
    while True:
        mensagem = input('Digite a mensagem: ') 
        if valida_mensagem(user, senha, mensagem) == True:
            mensagemV = mensagem
            break
    return mensagemV

valida_login()