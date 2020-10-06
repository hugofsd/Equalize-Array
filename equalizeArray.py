
print("----------------------------------------------------------------------")
print("                             INTRUÇÕES!                               ")
print("1) Digite 20 numeros(pixels), com um traço entre os numeros para")
print("contruir o vetor.")
print("2)Exemplo, copie (Ctrl+C) e cole (Ctrl + botão diteirto do mouse)")
print("para visualizar um exemplo de equalização:")
print("0-0-4-6-8-8-4-7-8-9-9-4-3-2-3-8-2-2-1-0")
print("----------------------------------------------------------------------")

lista = []

lista = (input("Digite o niveis de luminosidade que deseja equalizar: ").split("-"))

array = []
for val in lista:
    array.append(int(val))


hK = [] #repetição de x
Kak = []
pk = [] #Ha(k)/N
kLine = [] #k'(k_)=9*pk

equalizadoMeuPatrao = []

n = len(array)
l = 10
soma = 0


for x in range(l):
    hK.append(0)
    for y in array:
        if x == y:
            hK[x] = hK[x] + 1


for a in range(len(hK)):
    soma += hK[a]
    if a == 0:
        Kak.append(hK[a])
        pk.append(hK[a] / n)
        kLine.append(round((l - 1) * pk[a]))
    else:
        Kak.append(soma)
        pk.append(soma / n)
        kLine.append(round((l - 1) * pk[a]))


for b in array:
    equalizadoMeuPatrao.append(kLine[b])

resultado = ' '.join(str(e) for e in equalizadoMeuPatrao)

print("----------------------------------------------------------------------")
print('Niveis de luminosidade equalizados com sucesso: ', resultado)
print('\U0001F601')
print("----------------------------------------------------------------------")
