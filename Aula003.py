#Operadores aritiméticos
numeroA = 2 
numeroB = 3
#Soma
respostaSoma = numeroA + numeroB
print("Resposta da soma:",respostaSoma)
print("Resposta da soma:", (numeroA + numeroB)) 
 
#Subtração
respostaSubtracao = numeroA - numeroB
print("Resposta da subtração:",respostaSubtracao)
print("Resposta da subtração:", (numeroA - numeroB))

#Multiplicação
repostaMultriplicacao = numeroA * numeroB
print("Respota da multiplicação:",repostaMultriplicacao)
print("Resposta da multiplicação:", (numeroA * numeroB))

#Divisão
respostaDivisao = numeroA / numeroB
print("Resposta da divisão:",respostaDivisao)
print("Resposta da divisão:", (numeroA / numeroB)) 

#Expoente
respostaExpoente = numeroA ** numeroB
print("Resposta do expoente",respostaExpoente)
print("Resposta do expoente", (numeroA ** numeroB))

#Operadores Logicos e relacionais
print("Operador logico AND(e):",(numeroA < 5 and numeroB < 10))
print("Operador logico OR(ou):",(numeroA < 5 or numeroB < 20))
print("Operados logico NOT(não):",(not(numeroA < 5 and numeroB < 10)))
print("Operados relacional !=(diferente) :",(numeroA != numeroB))

#Usando input parar armazenar dados
armazenaValorTeclado = input("Digite um valor: ") #int ou float na frente para converter
print("O valor digitado foi:", type(armazenaValorTeclado))#Type para saber o tipo da variavel

exemplo = armazenaValorTeclado * 5 
