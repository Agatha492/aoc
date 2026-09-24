# calculadora de mmc e mdc
numero_a = int(input("digite o primeiro numero: ")) # Entrada dos números
numero_b = int(input("digite o segundo numero: "))
original_a = numero_a #Guarda os valores originais
original_b = numero_b

while numero_b != 0: # Calcula o MDC
    resto = numero_a % numero_b # Calcula o resto da divisão
    numero_a = numero_b  # Atualiza os números
    numero_b = resto

mdc = abs(numero_a) # Define o MDC

if mdc == 0: # Calcula o MMC
    mmc = 0
else:
    mmc = abs(original_a * original_b) // mdc

    print("\n===== RESULTADOS =====") # Calcula o MMC
    print(f"MDC de {original_a} e {original_b}: {mdc}")
    print(f"MMC de {original_a} e {original_b}: {mmc}")