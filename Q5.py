def calcula_salario(salario_bruto):
    salario_bruto = salario_bruto - (salario_bruto * 0.11)
    salario_bruto = salario_bruto - (salario_bruto * 0.15)
    return salario_bruto


salario = float(input("informe o salário: "))
print("Salário líquido: %.2f" % calcula_salario(salario))