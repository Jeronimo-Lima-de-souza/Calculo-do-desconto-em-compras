# O código abaixo calcula o desconto aplicado a uma compra com base no valor informado pelo usuário.
# Verifica se o valor da compra é menor que R$ 200,00, entre R$ 200,00 e R$ 300,00, ou maior que R$ 300,00, aplicando o desconto correspondente. 
# Exibe o valor do desconto calculado com 2 casa decimais. 

# solicita do usuário que informe o valor da compra.
valor_compra = float(input("Digite o valor de compra: "))
if valor_compra < 200.00:
    # calcula o desconto de 5% para compras menores que R$ 200,00
    desconto = valor_compra * 0.05
    # exibe o valor do desconto calculado com 2 casas decimais
    print(f"Desconto de 5%: R$ {desconto:.2f}")

    # Caso o valor da compra seja maior ou igual a R$ 200,00 e menor que R$ 300,00, aplica um desconto de 10%
elif valor_compra >= 200.00 and valor_compra < 300.00:
    # aplica o desconto de 10% para compras entre R$ 200,00 e R$ 300,00
    desconto = valor_compra * 0.10
    # exibe o valor do desconto calculado com 2 casas decimais
    print(f"Desconto de 10%: R$ {desconto:.2f}")

    # para qualquer valor a partir de R$ 300.00, aplica um desconto de 15%
else:
    desconto = valor_compra * 0.15
    # exibe o valor do desconto calculado com 2 casas decimais
    print(f"Desconto de 15%: R$ {desconto:.2f}")