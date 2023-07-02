import numpy as np

#O método da Iteração Linear é muito simples
# Basta transformar uma função f(x) em uma g(x) equivalente
# Então o resultado de g(x0) é igual a x1 e a iteração continua

# definir a função equivalente, professor tentei fazer por matriz mas não consegui :(
def g(x):
    return np.cbrt(9*x - 3)


def iteracaoLinear(x0, tol, maxIter):
    x = x0
    numero_Iteracoes = 0
    err = tol + 1
    # circunstanceas para parar o loop como foi passado no slide da aula
    while err > tol and numero_Iteracoes < maxIter:
        x_prev = x
        x = g(x)
        err = abs(x - x_prev)
        numero_Iteracoes += 1
        print("Iteração: ", numero_Iteracoes, " | x: ", x, " | Erro: ", err)
    return x, numero_Iteracoes, err



# tolerancia
tol = 0.0001

# chute inicial
x0 = -3.5

# numero maximo de iteracoes
maxIter = 100

raiz,numero_Iteracoes, erro = iteracaoLinear(x0, tol, maxIter)

print("A raiz é: ", raiz)
print("Numero de Iterações: ", numero_Iteracoes)
print("Erro: ", erro)