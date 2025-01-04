# Lê a primeira linha
linha1 = input().split()
cod1 = int(linha1[0])
num1 = int(linha1[1])
valor1 = float(linha1[2])

# Lê a segunda linha
linha2 = input().split()
cod2 = int(linha2[0])
num2 = int(linha2[1])
valor2 = float(linha2[2])

# Calcula o valor total
valorTotal = (num1 * valor1) + (num2 * valor2)

# Imprime o resultado com o formato correto
print(f"VALOR A PAGAR: R$ {valorTotal:.2f}")
