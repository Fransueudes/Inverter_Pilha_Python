import PilhaDinamica

p = PilhaDinamica.PilhaDinamica()

frase = "ESTE EXERCICIO E MUITO FACIL" 

lista = frase.split(" ")
print(lista)

inverso = ""

i = 0
while i < len(lista):
    for n in range(len(lista[i])):
        p.push(lista[i][n])
    for n in range(len(lista[i])):
        inverso += p.getTopo()
        p.pop()
    inverso += " "
    i += 1

print("Frase inicial: ", frase)
print("Frase inversa: ", inverso)
