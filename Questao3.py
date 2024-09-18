import json

with open('dados.json', 'r') as file:
    data = json.load(file)

faturamentos = [item['valor'] for item in data if item['valor'] > 0]

menor = min(faturamentos)
maior = max(faturamentos)
media = sum(faturamentos) / len(faturamentos)
dias_acima_media = sum(1 for f in faturamentos if f > media)

print(f"Menor faturamento: R${menor:.2f}")
print(f"Maior faturamento: R${maior:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
