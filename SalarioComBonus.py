nome = input("")
salarioFixo = float(input(""))
totalVendas = float(input(""))

salarioTotal = salarioFixo + (totalVendas * 0.15)

print(f"TOTAL = R$ {salarioTotal:.2f}")