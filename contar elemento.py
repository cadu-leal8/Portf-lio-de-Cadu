def contar_elemento(lista, elemento):
    return lista.count(elemento)

numeros = [1, 2, 3, 4, 5, 2, 2]
elemento = 2
print(f"O número {elemento} aparece {contar_elemento(numeros, elemento)} vezes na lista.")
