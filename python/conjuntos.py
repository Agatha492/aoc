# operação básica dos conjuntos
## Pede para o usuário digitar os elementos do conjunto A,
## separados por vírgula
entrada_a = input ("digite os elementos do conjunto A separados por virgula: ")
entrada_b = input ("digite os elementos do conjunto B separados por virgula: ") ## Pede para o usuário digitar os elementos do conjunto B,tambem separados por vírgula
conjunto_a = set (map(int, entrada_a.split(","))) ## Separa os elementos digitados pela vírgula, converte cada elemento para inteiro e cria um conjunto A
conjunto_b = set (map(int, entrada_b.split(","))) ## Separa os elementos digitados pela vírgula, converte cada elemento para inteiro e cria um conjunto B

print("\n===== RESULTADOS =====")
print("Conjunto A:", conjunto_a) # mostra o conjunto A
print("Conjunto B:", conjunto_b) # mostra o conjunto B
print("União (A ∪ B):", conjunto_a | conjunto_b) # mostra a união dos conjuntos A e B
print("Interseção (A ∩ B):", conjunto_a & conjunto_b) # mostra a interseção dos conjuntos A e B
print("Diferença (A - B):", conjunto_a - conjunto_b) # mostra a diferença entre os conjuntos A e B
print("Diferença (B - A):", conjunto_b - conjunto_a) # mostra a diferença entre os conjuntos B e A