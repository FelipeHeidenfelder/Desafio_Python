#Exercício 1

x = 5000000 #5 milhões
i = 1
n = 0

while i <= x:
    if i % 2 == 0 and i % 49 == 0 and i % 37 ==0:
        n +=1
    i+=1

print(f"\nQuestão 1\nTemos {n} números que são pares, múltiplos de 49 e de 37\n\n")






#Exercício 2
import numpy as np
import math 

vet = []
#criando o vetor
for i in range(10):
    if i % 2 == 0:     
        vet.append((3**i)+7*(math.factorial(i)))
    else:
        vet.append((2**i)+4*(np.log(i)))
      
#Capturar a posição do máximo                  
i=0 
while i < len(vet):
    if vet[i] == max(vet):
        position = i
    i+=1
    
#Exibir o resultado
print(f"Questão 2\nMaior número: {max(vet)}\nPosição: {position}\nMédia: {round(sum(vet)/len(vet),2)} \n\n")








#Exercício 3
nomes = []
notas = []

print("Questão 3\n")
for i in range(5):
    nome = input("Digite seu nome: ")
    nota = float(input("Digite sua nota: "))
    nomes.append(nome)
    notas.append(nota)

dic = {"Nomes": nomes, "Notas": notas}

maxi = max(dic["Notas"])

cont = 0
for i in dic["Notas"]:
    if i == maxi:
        index = cont
    cont +=1
    
print(f"\n{dic['Nomes'][index]} possui a maior nota: {maxi}\n\n")


while 1:
    x = input("Digite 'q' para finalizar do programa")
    if x == 'q':break
