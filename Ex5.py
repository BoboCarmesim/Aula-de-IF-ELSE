salario = float(input("Digite o salário:"))
num_filhos = int(input("Digite o número de filhos:"))

bonus = salario * 0.15 if salario < 2000 else 0
adc_filhos = num_filhos * 200
total = salario + bonus + adc_filhos

print(f"\nSalário base: R$ {salario:.2f}")
print(f"Bônus: R$ {bonus:.2f}")
print(f"Adicional por filhos: R$ {adc_filhos:.2f}")
print(f"Total a receber: R$ {total:.2f}")