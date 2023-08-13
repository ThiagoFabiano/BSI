
def main():
    imprimirPrimosAteK(100)

#Exercicio 1
def calcularFatorial(num: int) -> int:
    if (num >= 0):
        fatorial = num
        i = 1
        while (i < num):
            fatorial = fatorial * (num - i)
            i += 1
        
        return fatorial

#Exercicio 2
def calcularCombinacao(n: int, p: int) -> int:
    if(n >=0 and p >= 0):
        return calcularFatorial(n) / (calcularFatorial(p) * calcularFatorial(n - p))

#Exercicio 3
def imprimirMultiplos(n: int, k:int):
    i = 1
    while i <= n:
        print(k*i)
        i += 1 

#Exercicio 4
def verificarSeEhDivisor(x:int, y:int) -> bool:
    return y % x == 0

#Exercicio 5
def imprimirDivisores(k:int):
    i = 1
    while i <= k:
        if k % i == 0:
            print(i)
        i+=1    

#Exercicio 6
def imprimirMDC(m: int, n: int):
    i = m
    while i>=0:
        if m % i == 0 and n % i == 0:
            return (print(i))
        i-=1

#Exercicio 7
def ehPrimo(x: int) -> bool:
    if x > 1 :
        i = 2
        while i < x:
            if(x % i == 0 ):
                return False
            i+=1
        
        return True
    return False

#Exercicio 8
def imprimirPrimosAteK(k: int):
    i = 0
    while i <= k:
        if ehPrimo(i):
            print(i)
        i+=1

#Exercicio 9
def imprimirMovimentosAteOTarget(x: int, y:int, m:int, n:int):
    if x<=8 and y<=8 and m<=8 and n<=8:  
        if(x == m and y == n):
            return print(0)
        elif x == m or y == n:
            return print(1)
        else:
            #Verificar se posicao esta na diagonal sentido inferior direito
            diagonalAnteriorM = m - 1 
            diagonalAnteriorN = n - 1 
            while diagonalAnteriorM >= 1 and diagonalAnteriorN >= 1:
                if diagonalAnteriorM == x and diagonalAnteriorN == y:
                    return print(1)
                diagonalAnteriorM -= 1
                diagonalAnteriorN -= 1
            else:
                #Verificar se posicao esta na diagonal sentido superior esquerdo
                diagonalAnteriorM = m + 1 
                diagonalAnteriorN = n + 1
                while (diagonalAnteriorM >= 1 and diagonalAnteriorM <= 8) and (diagonalAnteriorN >= 1 and diagonalAnteriorN <= 8):
                    if diagonalAnteriorM == x and diagonalAnteriorN == y:
                        return print(1)
                    diagonalAnteriorM += 1
                    diagonalAnteriorN += 1 
                else:
                     #Verificar se posicao esta na diagonal sentido superior direito
                    diagonalAnteriorM = m + 1 
                    diagonalAnteriorN = n - 1
                    while diagonalAnteriorM >= 1 and diagonalAnteriorN >= 1:
                        if diagonalAnteriorM == x and diagonalAnteriorN == y:
                            return print(1)
                        diagonalAnteriorM += 1
                        diagonalAnteriorN -= 1
                    else:
                        #Verificar se posicao esta na diagonal sentido superior direito
                        diagonalAnteriorM = m - 1 
                        diagonalAnteriorN = n + 1
                        while diagonalAnteriorM >= 1 and diagonalAnteriorN >= 1:
                            if diagonalAnteriorM == x and diagonalAnteriorN == y:
                                return print(1)
                            diagonalAnteriorM -= 1
                            diagonalAnteriorN += 1
                        else:
                            return print(2)

#Exercicio 10
def imprimirQuandidadeDeSucoPorPessoa(N:int, F: int):
    volumeDeSucoEmLitros =  (F * 50) / 1000
    print(f'{volumeDeSucoEmLitros / N:.2f}')

#Exercicio 11
def tempoDeSono(horaAtual: int, minutoAtual:int, horaAlarme: int, minutoAlarme: int) -> int:
    deuAHora = True
    minutosDeSono = 0
    hora = horaAtual
    minuto = minutoAtual
    while deuAHora:
        if minuto == 60:
            minuto = 0
            hora +=1 
        if hora == 24:
            
            hora = 0
        minuto +=1
        minutosDeSono+=1
        if (hora == horaAlarme and minuto == minutoAlarme):
            deuAHora = False
    return minutosDeSono
        


if __name__ == "__main__":
    main()