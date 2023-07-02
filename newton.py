# 1) Dados iniciais
# x0 = aproximação inicial
# erro1 e erro2 = precisões
# erro1 => f(x) < erro1
# erro2 => |xk+1 – xk| < erro2
# Mét odo de Newt on
# 2) Se |f(x0)| < erro1, x = x0, FIM
# 3) k = 1
# 4) x1 = x0 – f(x0)/f’(x0)
# 5) Se |f(x1)| < erro1 ou se |x1 – x0| < erro2
# x = x1
# , FIM
# 6) x0 = x1
# 7) k = K + 1
# Implementar o método de Newton para a função f(x) = x3 – 9x + 3

import numpy as np

def f(x):
    # não entendi o por que não precisei usar o np.cbrt, deu certo sem ele "análise"
    return x**3 - 9*x + 3

def df(x):
    #aqui a mesma coisa 
    return 3*x**2 - 9

def newton(x0, erro1, erro2, maxIter):

    if abs(f(x0)) < erro1:
        x = x0
        return x

    k = 1
    x1 = x0 - f(x0)/df(x0)

    while abs(f(x1)) > erro1 and abs(x1 - x0) > erro2 and k < maxIter:
        x0 = x1
        x1 = x0 - f(x0)/df(x0)
        k += 1
        print("Iteração: ", k, " | x: ", x1, " | Erro: ", abs(x1 - x0))
    x = x1
    return x

# tolerancia
erro1 = 0.0001

# chute inicial
x0 = -3.5

# numero maximo de iteracoes
maxIter = 100

# precisao
erro2 = 0.0001

raiz = newton(x0, erro1, erro2, maxIter)

print("A raiz é: ", raiz)
