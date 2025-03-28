lista = [3, 5, 1, 8, 2, 7, 4]
lista_filtrada = [x for x in lista if x % 2 == 0]
lista_ordenada = sorted(lista_filtrada)

print("Lista original:", lista)
print("Lista filtrada (pares):", lista_filtrada)
print("Lista ordenada:", lista_ordenada)
