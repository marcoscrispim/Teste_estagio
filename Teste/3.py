import json

# Suponha que o JSON seja carregado da seguinte forma:
faturamento_json = '''
{
    "faturamento": [
        {"dia": 1, "valor": 100.0},
        {"dia": 2, "valor": 200.0},
        {"dia": 3, "valor": 150.0},
        {"dia": 4, "valor": 0.0},
        {"dia": 5, "valor": 300.0}
        # Mais dados aqui...
    ]
}
'''

# Carregar os dados JSON
dados = json.loads(faturamento_json)
valores = [item['valor'] for item in dados['faturamento'] if item['valor'] > 0]

menor_valor = min(valores)
maior_valor = max(valores)
media_mensal = sum(valores) / len(valores)

dias_acima_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor valor: R${menor_valor:.2f}")
print(f"Maior valor: R${maior_valor:.2f}")
print(f"Número de dias acima da média: {dias_acima_media}")
