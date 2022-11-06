N = int(input("Digite o tamanho do array: "))
lista = []
i = 0
for i in range(0, N):
    lista.append(int(input(f"Digite o {i+1} elemento: ")))

print("Output: ", end='')

for i in range(0, len(lista)):
    if(i % 2 == 0):
        print(lista[i], end=" ")