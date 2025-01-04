num1 = float(input(""))
num2 = float(input(""))
num3 = float(input(""))

a = num1 * 2
b = num2 * 3
c = num3 * 5

# media ponderada se divide pela soma dos pesos das notas
media = (a + b + c) / 10

print(f"MEDIA = {media:.1f}")