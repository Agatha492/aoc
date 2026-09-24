# demonstrador da tabela da verdade

print("===== TABELA-VERDADE =====")
print("A      B      A AND B    A OR B    NOT A")

valores = [True, False] # Mostra os valores possíveis

for a in valores: #valores de A e B
    for b in valores:
        and_resultado = a and b
        or_resultado = a or b
        not_resultado = not a

        a_texto = "V" if a else "F" #Converte True e False para V e F
        b_texto = "V" if b else "F"
        and_texto = "V" if and_resultado else "F"
        or_texto = "V" if or_resultado else "F"
        not_texto = "V" if not_resultado else "F"

        print( #mostra os resultados da tabela da verdade
            f"{a_texto}      {b_texto}         "
            f"{and_texto}          {or_texto}        {not_texto}"
        )