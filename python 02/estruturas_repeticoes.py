#ITERAR = REPETIR
# #exemplo utilizando um objeto iteravel
#ele percorre o nome e procura as vogais do nome

#estrutura basica do for
#  for item in sequência:
    # Bloco de código a ser executado para cada item





texto = input("digite um nome:")
vogais = "AEIOUaeiou"

for letra in texto:
    if letra in vogais:
        print(letra)


nome = "Python"

for letra in nome:
    print(letra)


numeros = [0, 1, 2, 3, 4]

for numero in numeros:
    print(numero)

#a variavel numero e letra ou seja, a variavel pos o FOR, pega a variavel nome e numeros e destrincha ela, fazendo uma repeticao dos caracteres.






#exemplo utilizando o range
#range pode ter ate 3 coisas ditos
#range (start, stop[, step])
#apenas o stop é obrigatorio, porem, é normal utilizar o start e stop. o step é apenas um "intervalo"

for numero in range(0, 51, 5):
    print(numero)

#o 0 é o start, o 51 o stop e o 5 step. ou seja, ele vai inicar o zero, parar no 50 e pular de 5 em 5. 
#ele para no 50 porque o 0 conta, ou seja, vai de 0 ate 50, 51 numeros.