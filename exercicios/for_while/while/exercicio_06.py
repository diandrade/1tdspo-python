'''
O dono de uma mercearia da zona rural do interior de SP necessita automatizar
o processo de totalização das compras de seus clientes,
porém ele não tem condições financeiras para adquirir os
equipamentos necessários para leitura de códigos de barras e afins.
Dessa forma, o funcionário do caixa terá que digitar os preços dos produtos e as quantidades
para que as compras dos clientes sejam totalizadas. Escreva um programa que calcule o total da compra do cliente,
sendo que o usuário deverá digitar os preços e as quantidades dos produtos e, quando a compra terminar,
digitar 0 (zero) no valor do preço para finalizar e informar o valor a pagar ao cliente.
'''

preco = float(input("Insira o preço do produto: "))
soma_produtos = 0

while preco != 0:
    qtd = int(input("Insira a quantidade do produto: "))
    valor = qtd * preco
    soma_produtos += valor

    preco = float(input("Insira o preço do produto: "))

print(f"A soma total dos produtos é de: R${soma_produtos:.2f}")
