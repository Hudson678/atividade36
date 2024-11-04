#Ler uma lista com 4 notas, em seguida o programa deve exibir as notas e a média.

notas = []

for n in range(4):
    nts = float(input("Adicione a nota: "))
    notas.append(nts)
    media = sum(notas) / len(notas)
print (media)
