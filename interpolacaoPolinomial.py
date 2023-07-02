# Implementem o método da interpolação polinomial que vai resultar em um sistem de equações lineares. Então, utiliza qualquer
# método para resolução de sistemas lineares já aprendidos na disciplina para encontrar as soluções.
# Crie um programa que calcule o sistema de equações
# Utilize um método para solução de sistemas para resolver a seguinte interpolação
# Faça então o programar ler um valor de x e utilizar a equação de interpolação para
# encontrar f(1.4)
# Para facilitar, o resultado é f(1.4) = 0.338

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def interpolacaoPolinomial(x, y):
    n = len(x)
    a = np.zeros((n, n))
    b = np.zeros(n)
    for i in range(n):
        for j in range(n):
            a[i, j] = x[i]**j
        b[i] = y[i]
    return np.linalg.solve(a, b)

x = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])
y = f(x)

a = interpolacaoPolinomial(x, y)

print("Coeficientes: ", a)
#print do coefiente f(1,4) tem que dar 0.338
print("f(1.4) = ", a[0] + a[1]*1.4 + a[2]*1.4**2 + a[3]*1.4**3 + a[4]*1.4**4)

x1 = np.linspace(0, np.pi/2, 100)
y1 = np.zeros(len(x1))

for i in range(len(a)):
    y1 += a[i]*x1**i
# achei essa biblioteca que plota gráficos, achei interessante
# pra ser bem honesto não entendi muito bem o que ela faz, mas
# ta ai kkkkkkkk
plt.plot(x, y, 'o')
plt.plot(x1, y1)
plt.show()