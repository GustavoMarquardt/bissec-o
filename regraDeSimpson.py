#Usando o método de simpson para calcular a integral de uma função
# integral de 0 a 7 de -x^2 + 3x^3 - 7x dx
import numpy as np

def f(x):
    return -x**2 + 3*x**3 - 7*x

def simpson(a, b, n):
    h = (b-a)/n
    x = np.linspace(a, b, n+1)
    y = f(x)
    s = y[0] + y[n]
    for i in range(1, n, 2):
        s += 4*y[i]
    for i in range(2, n-1, 2):
        s += 2*y[i]
    return (h/3)*s

# o meu esta dando 1514,91 (análise)

print(simpson(0, 7, 1000))
