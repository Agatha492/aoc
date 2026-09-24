# verificador de numeros primos

numero_informado = int(input("informe um numero inteiro: "))

if numero_informado < 2 :
    print(f"{numero_informado} não é um número primo")
else:
    primo = True

    for divisor in range(2, numero_informado):
        if numero_informado % divisor == 0:
            primo = False
            break

    if primo:
        print(f"{numero_informado} é um número primo")
    else:
        print(f"{numero_informado} não é um número primo")
