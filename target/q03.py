import json

with open('faturamentos.json', 'r') as f:
    data = json.load(f)

valores = data['faturamentos']

filtrados = [v for v in valores if v > 0]

menor = min(filtrados)
maior = max(filtrados)
media = sum(filtrados) / len(filtrados)

dias_acima = sum(1 for v in filtrados if v > media)

print(f"Menor: R${menor:.2f}")
print(f"Maior: R${maior:.2f}")
print(f"Dias acima da média: {dias_acima}")