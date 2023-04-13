import cryptographyFramework

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


def valida_user(user):
        if len(user) > 0 and len(user) <= 30 and user[0].isupper() and user.isalnum():
            return True
        else:
            print("Usuário inválido! O usuário deve ter a primeira letra maiúscula, sem caracteres especiais e sem espaços e no máximo 30 caracteres.")
            return False

def valida_senha(senha):
        if len(senha) >= 10 and any(char.isdigit() for char in senha) and any(char.isupper() for char in senha) and any(char.islower() for char in senha) and any(char in "!@#$%^&*()_+-=[]{}|;:,.<>?/" for char in senha):
            return True
        else:
            return False

def valida_mensagem(user, senha, mensagem):   
        if len(mensagem) <= 70:
            encryptedText = cryptographyFramework.encryptMessage(user, senha, mensagem)
            cryptographyFramework.saveNewLine(encryptedText)
            return True
        else:
            print("Mensagem inválida! A mensagem deve ter no máximo 70 caracteres.")
            return False
