from math import log10

def fibo(num):
    if(num == 0) or (num == 1):
        return num
    else:
        return fibo(num - 1) + fibo(num - 2)

n = int(input("Digite um número: "))

resulfibo = fibo(n)

resdiv100 = resulfibo % 100


print(f"o {n}º número de Fibonacci é: {resulfibo} \nAssim, os dois últimos digitos são {(resdiv100 // 10)} e {resdiv100 % 10}")




