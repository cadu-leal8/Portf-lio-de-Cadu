import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, label='y = 2x', color='blue', marker='o')
plt.title("Gráfico de Linha Simples")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()
