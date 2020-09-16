minhaLista = ["Eduardo", "Julia", "Ana", 10]
print(minhaLista)

#Acesso ao item por posição 
print(minhaLista[0])

#Acesso indexado negativo por posição, -1 é a ultima posição da lista
print(minhaLista[-1])
 
#Intervalo de itens
print(minhaLista[1:3])
print(minhaLista[:3]) #Sem o item de inicio
print(minhaLista[1:]) #Sem o item de final

#Intervalo de itens indexação negativo
print(minhaLista[-2:-1])

#Alterando valor do item
minhaLista[3] = "Francine"
print("Lista com valor do item alterado: ",minhaLista)

#Percorrer lista
for i in minhaLista:
 print("Item da lista: ",i)

if "Julia" in minhaLista:
 print("Sim,está na lista!")
else:
 print("Não está!")

 #Retorna a quantidade de itens da lista
print(len(minhaLista))

minhaLista.append("Henrique")
print("Minha lista com novo item no final: ",minhaLista)

#Adiciona item na lista
minhaLista.insert(2,"Madu")
print("Minha lista com item em posição específica: ",minhaLista)

#Remove o indice epecificado
minhaLista.pop(4)
print("Minha lista com indeice removido: ",minhaLista)

#Se usar o pop sem passar o parametro, vai remover o ultimo da lista
minhaLista.pop()
print("Minha lista com indice removido: ",minhaLista)

del minhaLista[1]
print("Minha lista com item removido com del: ",minhaLista)

#delta a lista toda
#del minhaLista

minhaLista.clear()
print("Minha lista vazia com metodo clear: ",minhaLista)

minhaLista.insert(0,"Hello")
minhaLista.insert(1,"Opa")
print("Minha lista com novos itens: ",minhaLista)

#Copia dados de uma lista para outra lista 
minhaSegundaLista = minhaLista.copy()
print("Lista cópia: ",minhaSegundaLista)

minhaTerceiraLista = list(minhaSegundaLista)
print(minhaTerceiraLista)

#Juntando listas
minhaQuartaLista = minhaSegundaLista + minhaTerceiraLista
print("Juntando listas: ", minhaQuartaLista)

#Encontrando a posição de um item na lista
print("Encontrando a posição de um item na lista: ",minhaQuartaLista.index("hello"))