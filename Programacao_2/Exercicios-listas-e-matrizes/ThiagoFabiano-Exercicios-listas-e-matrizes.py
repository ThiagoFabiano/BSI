#Exercicios Aula 1

def main():
   figurinhasCapturadas([
        ['.','.','.','.','*','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','*','.','.'],
        ['.','.','.','.','.','*','.','.','.','.'],
        ['.','.','*','.','#','.','.','.','.','.'],
        ['.','.','.','#','N','.','*','.','.','*'],
        ['.','.','.','*','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.','.'],
    ], ['F','D','F','F','F','F','F','F','E','E','F','F','F','F','F','F','E','F','D','F'])

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

#11. Média

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
    

#12. Temperaturas
def mediaTemperaturaEDiasAbaixo(dias: int, temperaturas: list):
    if dias == len(temperaturas):
        somaTemperaturas = 0
        diasAbaixoDaMedia = 0
        mediaTemperatura = 0
        for i in temperaturas:
            somaTemperaturas += i
        mediaTemperatura = somaTemperaturas / dias
        for i in temperaturas:
            if i < mediaTemperatura:
                diasAbaixoDaMedia += 1    
        
        return print(f'Temperatura Média:{mediaTemperatura}, dias abaixo da média: {diasAbaixoDaMedia}')
    else:
        print('O numero de dias e de temperaturas não são correspondentes')

#13.Iguais
def elementosIguaisENaMesmaPosicao(l1: list, l2: list):
    if len(l1) == len(l2):
        elemIguais = 0
        for i in range(len(l1)):
            if l1[i] == l2[i]:
                elemIguais += 1
        return print(elemIguais)
             
    else:
        print('l1 e l2 não possuem a mesma quantidade de itens')

#14. Salarios
def salariosAcimaDaMedia(n: int):
    i = 1
    listaFuncionarios = []
    listaSalarios = []
    somaSalarios = 0
    mediaDeSalarios = 0
    while i <= n:
        listaFuncionarios.append(str(input('Nome do Funcionário:')))
        listaSalarios.append((int(input('Salário:'))))
        i+=1
    
    for salario in listaSalarios:
        somaSalarios += salario
    
    mediaDeSalarios = somaSalarios / len(listaSalarios)
    for indice in range(len(listaSalarios)):
        if listaSalarios[indice] > mediaDeSalarios:
            print(listaFuncionarios[indice])

#15. Sublista
def elementosEntreXeY(listaOrdenada: list, x:int, y:int)->list:
    sublista = []
    for i in listaOrdenada:
        if i > x and i < y:
            sublista.append(i)
    return sublista

#16 Troca de Cartas:

def qntdDeCartasASeremTrocadas(deck1: list, deck2:list) -> int:
    naoRepeteNo2 = 0
    naoRepeteNo1 = 0

    for item1 in range(len(deck1) ):
        if deck2.count(deck1[item1]) == 0 and deck1[item1] != deck1[item1 - 1]:
            naoRepeteNo2+=1

    for item2 in range(len(deck2) ):
        if deck1.count(deck2[item2]) == 0 and deck2[item2] != deck2[item2 - 1]:
            naoRepeteNo1+=1
    
    if naoRepeteNo2 < naoRepeteNo1:
        print(f'O Máximo de cartas que podem ser trocadas é {naoRepeteNo2}')
    else:
        print(f'O Máximo de cartas que podem ser trocadas é {naoRepeteNo1}')

#Exercicios Aula 3 - Matrizes

#17. Criar Matriz

def criarMatriz(m: int, n:int):
    matriz=[]
    i = 1
    while i <= m:
        linha = [0] * n
        matriz.append(linha)
        i+=1
    return matriz

#18. Imprimir Matriz

def imprimirMatriz(matriz):
    for linha in matriz:
        linhaString = ''
        for i in linha:
            linhaString += str(i) + ' '
        print(linhaString)
        

#19. Somar Matrizes
def somarMatrizes(A: list, B:list)-> list:
    matrizSomada=[]
    for indiceLinha in range(len(A)):
        linha = []
        for indiceItem in range(len(A[indiceLinha])):
            linha.append( A[indiceLinha][indiceItem] + B[indiceLinha][indiceItem])
        matrizSomada.append(linha)
    return matrizSomada

#20. Notas

def mediaDeNotasAlunosETurma(m:int, n:int):
    alunoEMedia = []
    somaNotaTurma = 0
    for aluno in range(m):
        somaNota = 0
        aluno = str(input('Nome do aluno:'))
        for i in range(n):
            somaNota += int(input('Nota'))
        alunoEMedia.append([aluno,somaNota / n])
    
    for i in alunoEMedia:
        somaNotaTurma += i[1]
        print(f'{i[0]}: {i[1]}')
    print(f'Média da turma: {somaNotaTurma / len(alunoEMedia)}')
    

#21. Matriz identidade

def verificarSeEhMatrixIdentidade(matriz: list)-> bool:
    indice = 0
    while indice <= len(matriz) - 1:
        if len(matriz) != len(matriz[indice]):
            return False
        indice += 1

    if len(matriz) == len(matriz[0]):
        for i in range(len(matriz)):
            if matriz[i][i] != 1:
                return False
            for item in range(len(matriz[i])) :
                if matriz[i][item] != 0 and item != i:
                    return False 
        return True 
    
#22. Determinante
def calcularDeterminanteMatriz3x3(matriz:list)->int:
    diagonalPrimaria = 0
    diagonalSecundaria = 0


    for linha in matriz:
        linha.append(linha[0])
        linha.append(linha[1])

    for item in range(3):
        diagonal1 = 1
        for i in range(3):
            diagonal1 *= matriz[i][i+item]
        diagonalPrimaria += diagonal1

    for item in range(2,5):
        diagonal2 = 1
        for i in range(3):
            diagonal2 *=  matriz[i][item-i]
        diagonalSecundaria += diagonal2
        
    return diagonalPrimaria - diagonalSecundaria


#23. Triangular inferior da transposta de uma matriz:

def triangularInferiorDaTranspostaDeUmaMatriz(matriz: list):
    matrizTransposta = []
    matrizTriangularInferior = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz)):
            linha.append(matriz[j][i])
        matrizTransposta.append(linha)
    
    for linha in range(len(matrizTransposta)):
        linhaDaMatrizTI = []
        for item in range(len(matrizTransposta[linha])):
            if item <= linha:
                linhaDaMatrizTI.append(matrizTransposta[linha][item])
            else:
                linhaDaMatrizTI.append(0)
        matrizTriangularInferior.append(linhaDaMatrizTI)
                
    return imprimirMatriz(matrizTriangularInferior)

#24. Cavalo
def movimentosPossiveisDoCavalo(matriz: list):
    posicaoDoCavalo = []
    movimentosDoCavalo  = 8
    for linha in range(len(matriz)):
        for item in range(len(matriz[linha])):
            if matriz[linha][item] == 1:
                posicaoDoCavalo = [linha,item]
  
    if posicaoDoCavalo == [0,0] or posicaoDoCavalo == [0,7] or posicaoDoCavalo == [7,0] or posicaoDoCavalo == [7,7]:
        movimentosDoCavalo -=6
    elif (posicaoDoCavalo[0] <= 1 or posicaoDoCavalo[0] >= 6) or ( posicaoDoCavalo[1] <=1 or posicaoDoCavalo[1] >= 6):
        movimentosDoCavalo-=2
        if ((posicaoDoCavalo[0]==0 or posicaoDoCavalo[0] ==7) and ( posicaoDoCavalo[1] <=1 or posicaoDoCavalo[1] >= 6)) or ((posicaoDoCavalo[1]==0 or posicaoDoCavalo[1] ==7) and ( posicaoDoCavalo[0] <=1 or posicaoDoCavalo[0] >= 6)):
            movimentosDoCavalo-=3
        else:
            movimentosDoCavalo -=2
        
        
            
    print(posicaoDoCavalo,movimentosDoCavalo)

#25. Robo Colecionador
def figurinhasCapturadas(arena:list, instrucoes:list):
    qntdFigurinhas = 0
    posicaoAtual = []
    orientacaoAtual = ''
    orientacoes = ['N','L','S','O']

    for i in range(len(arena)):
        for j in range(len(arena[i])):
            if arena[i][j] != '.' and arena[i][j] != '*' and arena[i][j] != '#':
                posicaoAtual = [i,j]
                orientacaoAtual =orientacoes[orientacoes.index(arena[i][j]) ]

    for comando in instrucoes:
        if comando == 'F':
            if orientacaoAtual == 'N':
                if posicaoAtual[0] >= 1 and arena[posicaoAtual[0]-1][posicaoAtual[1]] != '#':
                    posicaoAtual[0] = posicaoAtual[0] - 1
                    if arena[posicaoAtual[0]][posicaoAtual[1]] == '*':
                        qntdFigurinhas +=1
                        arena[posicaoAtual[0]][posicaoAtual[1]] = '.'

            elif orientacaoAtual == 'S':
                if posicaoAtual[0] <= (len(arena)-2) and arena[posicaoAtual[0]+1][posicaoAtual[1]] != '#':
                    posicaoAtual[0] = posicaoAtual[0] - 1
                    if arena[posicaoAtual[0]][posicaoAtual[1]] == '*':
                        qntdFigurinhas +=1
                        arena[posicaoAtual[0]][posicaoAtual[1]] = '.'

            if orientacaoAtual == 'L':
                if posicaoAtual[1] <= (len(arena[0])-2) and arena[posicaoAtual[0]][posicaoAtual[1]+1] != '#':
                    posicaoAtual[1] = posicaoAtual[1] + 1
                    if arena[posicaoAtual[0]][posicaoAtual[1]] == '*':
                        qntdFigurinhas +=1
                        arena[posicaoAtual[0]][posicaoAtual[1]] = '.'

            if orientacaoAtual == 'O':
                if posicaoAtual[1] >= 1 and arena[posicaoAtual[0]][posicaoAtual[1]-1] != '#':
                    posicaoAtual[1] = posicaoAtual[1] - 1
                    if arena[posicaoAtual[0]][posicaoAtual[1]] == '*':
                        qntdFigurinhas +=1
                        arena[posicaoAtual[0]][posicaoAtual[1]] = '.'

        elif comando == 'D':
            if orientacoes.index(orientacaoAtual) == 3:
                orientacaoAtual = 'N'
            else:
                orientacaoAtual = orientacoes[orientacoes.index(orientacaoAtual) + 1]
        elif comando == 'E': 
            if orientacoes.index(orientacaoAtual) == 0:
                orientacaoAtual = 'O'
            else: 
                orientacaoAtual = orientacoes[orientacoes.index(orientacaoAtual) -1]
    
    print(qntdFigurinhas)

if __name__ == '__main__':
    main()