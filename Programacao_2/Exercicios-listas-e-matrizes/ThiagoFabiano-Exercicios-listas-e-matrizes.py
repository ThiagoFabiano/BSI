#Exercicios Aula 1

def main():
    mediaEAlunosAcima(10, [40,80,65,22,36,80,99,10,70,55])

#1. Regressiva
def numerosParesDe100a1() -> list:
    i = 100
    listaDePares= []
    while i >= 1:
        if i % 2 == 0:
            listaDePares.append(i)
        i-=1
    return listaDePares


#2. Metade
def metadeDosNumeros() -> list:
    listaDeMetades = []
    for i in range(10):
        listaDeMetades.append(int(input()) / 2) 
    return listaDeMetades

#3. Leitura
def lerNNumeros(n:int)-> list:
    numeros = []
    for i in range (n):
        numeros.append(int(input()))
    return numeros

#4. Ocorrencias
def ocorrenciasNaLista(lista, elemento)-> int:
    numeroDeOcorrencias =0 
    for i in lista:
        if i == elemento:
            numeroDeOcorrencias += 1
    return numeroDeOcorrencias

#5. Máximo
def encontrarMaiorNumero(numeros: list) -> int:
    maiorNumero = 0
    for i in numeros:
        if i > maiorNumero:
            maiorNumero = i
    return maiorNumero

#6. Posição do Máximo
def encontrarIndiceMaiorNumero(numeros: list) -> int:
    indiceMaiorNumero = 0
    maiorNumero = 0 
    i = 0
    while i <= (len(numeros) - 1):
        if numeros[i] > maiorNumero:
            maiorNumero = numeros[i]
            indiceMaiorNumero = i
        i += 1
    return indiceMaiorNumero
    
#7. Inverter

def inverterLista(lista: list)-> list:
    qntdItemsLista = len(lista) - 1
    listaInvertida = []
    while qntdItemsLista >= 0:
        listaInvertida.append(lista[qntdItemsLista])
        qntdItemsLista -= 1
    return listaInvertida


#Exercicios Aula 2

#8. Fibonacci
def fibonacci(n:int)-> list:
    i = 3
    lista = [1,1]
    if n == 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1,1]
    else:
        while i <= n:
            lista.append(lista[len(lista)-1] + lista[len(lista)-2])
            i+=1
    return lista

#9. Ordenadas e abscissas:
def somaDeAbcissasOuProdutoDeOrdenadas(abcissas:list, ordernadas: list)-> int:
    if len(abcissas) == len(ordernadas):
        qntdAbcissasPares = 0
        qntdOrdenadasImpares = 0
        i = 0
        while i <= len(abcissas) - 1:
            if abcissas[i] % 2 == 0:
                qntdAbcissasPares +=1
            if ordernadas[i] % 2 != 0:
                qntdOrdenadasImpares +=1
            i+=1
        if qntdAbcissasPares >= qntdOrdenadasImpares:
            somaAbcisssas = 0
            for i in abcissas:
                somaAbcisssas += i
            return print(somaAbcisssas)
        else:
            produtoOrdenadas = 1
            for i in ordernadas:
                produtoOrdenadas *= i
            return print(produtoOrdenadas)
     
    else:
        print('As listas não possuem a mesma quantidade de items')

#10. k Múltiplos:
def kMultiplosDeN(k:int, n:int) -> list:
    multiplosDeN = []
    for i in range(k+ 1):
        if i % n ==0 and i > n:
            multiplosDeN.append(i) 
    return multiplosDeN

#Exercicios Aula 3

#Média

def mediaEAlunosAcima(numeroDeAlunos: int, notas: list):
    if numeroDeAlunos == len(notas):
        somaNotas = 0
        alunosAcimaDaMedia = 0
        for i in notas:
            somaNotas += i
            if i > 60:
                alunosAcimaDaMedia+=1
        return print(f'Nota Média:{somaNotas / numeroDeAlunos}, Alunos acima de 60 pontos: {alunosAcimaDaMedia}')
    else:
        print('O numero de alunos e notas não são correspondentes')
    

if __name__ == '__main__':
    main()