def bissection_method(func, a, b, tolerance=1e-6, max_iterations=100):
    if func(a) * func(b) >= 0:
        raise ValueError("A função deve ter sinais opostos nos pontos a e b.")
    
    for iteration in range(max_iterations):
        c = (a + b) / 2
        if func(c) == 0 or abs(b - a) / 2 < tolerance:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    
    raise ValueError("O método da bissecção atingiu o número máximo de iterações.")

# Exemplo de uso
def f(x):
    return x**3 - 2*x - 5

root = bissection_method(f, 1, 3)
print("Aproximação da raiz:", root)
print("Valor da função na raiz aproximada:", f(root))
