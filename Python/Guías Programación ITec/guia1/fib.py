#La sucesión de Fibonacci {f_n} se define como el resultado de la suma de los dos números anteriores, partiendo de 0, 1
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end= ' ')
        a, b = b, a+b
    #print()
fib(1000000000)

#El primer método funciona, el segundo NO FUNCIONA. ¿Por qué?
"""
def fib2(m):
    a, b = 0, 1
    while a < m:
        print(a, end= ' ')
        
        b= a + b
        a = b
    #print()

print("\n ||----------|| Segundo método ||----------||\n")

fib2(100000)
"""