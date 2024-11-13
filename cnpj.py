from cnpj import CNPJClient
from pprint import pprint

cnpj_client = CNPJClient()
cnpj = input("Entre com um cnpj para consulta: ")

resultado = cnpj_client.cnpj(cnpj)
# ender = []
print(resultado)
ender = resultado["endereco"]
print(ender["logradouro"])
