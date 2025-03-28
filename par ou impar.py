def verificar_par_ou_impar(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

numero = 10
print(f"O número {numero} é {verificar_par_ou_impar(numero)}.")
