def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

notas = [8, 7, 9, 6, 10]
media = calcular_media(notas)
print(f"A média das notas é: {media:.2f}")
