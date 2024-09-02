texto = input("Digite algo a ser invertido: ")

invertida = ""
for i in range(len(texto) - 1, -1, -1):
    invertida += texto[i]

print(invertida)