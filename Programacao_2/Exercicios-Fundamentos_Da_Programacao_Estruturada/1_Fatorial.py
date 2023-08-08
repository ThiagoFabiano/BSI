
def main():
    print(verificarSeEhDivisor(5,10))
#Exercicio 1
def calcularFatorial(num: int):
    if (num >= 0):
        fatorial = num
        i = 1
        while (i < num):
            fatorial = fatorial * (num - i)
            i += 1
        
        return fatorial

#Exercicio 2
def calcularCombinacao(n: int, p: int):
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


if __name__ == "__main__":
    main()