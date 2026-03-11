nome = input()
salario = float(input())
vendas = float(input())

totalSal = salario + (0.15 * vendas)

print(f'TOTAL = R$ {totalSal:.2f}')