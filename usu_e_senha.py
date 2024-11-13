"""Exercício 02.

Cadastro de Usuário e Senha
Desenvolva um programa que receba um nome de usuário e sua senha.
O sistema deve validar se a senha é diferente do nome do usuário.
Caso seja igual, uma mensagem de erro deve ser exibida e as informações solicitadas
novamente até que sejam válidas.
"""

nome = input(f"Entre com o nome do usuario: ")
senha = input(f"Entre com a senha: ")

while True:
    if nome == senha:
        print("nome e senha iguais, tente novamente!")
        nome = input(f"Entre com o nome do usuario: ")
        senha = input(f"Entre com a senha: ")
    else:
        break
print(f"nome {nome} e senha {senha} agora esta ok")
