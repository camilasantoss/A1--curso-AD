idade = int(input("Informe uma idade: "))
conta_idade = 0
soma_idade = 0

while (idade >= 0):
    conta_idade += 1
    soma_idade += idade
    idade = int(input("Informe uma idade: "))

print("Média das idades:", soma_idade / conta_idade)