from valida_login import *

def test_valida_user():
    assert valida_user("Usuario1") == True
    assert valida_user("usuario1") == False
    assert valida_user("Usuario1!") == False
    assert valida_user("") == False
    assert valida_user("UsuarioComMaisDeTrintaCaracteres1234567890") == False

def test_valida_senha():
    assert valida_senha("Senha1234#") == True
    assert valida_senha("senha123#") == False
    assert valida_senha("Senha#") == False
    assert valida_senha("Senha123") == False
    assert valida_senha("SenhaABC#") == False
    assert valida_senha("") == False
    assert valida_senha("Senhacommaisde10caracteressemcaracteresespeciais") == False

def test_valida_mensagem():
    assert valida_mensagem('usuario', 'senha', 'mensagem') == True

def test_valida_mensagem_invalida():
    assert valida_mensagem('usuario', 'senha', 'Uma mensagem com mais de 70 caracteres que deve ser inválida e não ser criptografada.') == False
