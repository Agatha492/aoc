# soma da sequencia de numeros até o numero informado
numero = int(input("Digite o número final da sequência: "))

soma = 0

for valor in range(1, numero + 1):
    soma = soma + valor

print(f"Sequência: 1 até {numero}")
print(f"Soma: {soma}")