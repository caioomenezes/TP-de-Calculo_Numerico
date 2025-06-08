import math

def trapezio(f, a, b, n):
    h = (b - a) / n
    print(f"\nPasso h = {h:.6f}")
    print("i\tx_i\t\tf(x_i)\t\tCoef\tContribuição")
    print("-" * 60)
    
    soma = 0
    for i in range(n + 1):
        x = a + i * h
        fx = f(x)
        coef = 1 if i == 0 or i == n else 2
        contrib = coef * fx
        soma += contrib
        print(f"{i}\t{x:.6f}\t{fx:.6f}\t{coef}\t{contrib:.6f}")
    
    resultado = (h / 2) * soma
    print(f"\nResultado = (h/2) × {soma:.6f} = {resultado:.10f}")
    return resultado

def simpson_1_3(f, a, b, n):
    if n % 2 != 0: n += 1
    h = (b - a) / n
    print(f"\nPasso h = {h:.6f}")
    print("i\tx_i\t\tf(x_i)\t\tCoef\tContribuição")
    print("-" * 60)
    
    soma = 0
    for i in range(n + 1):
        x = a + i * h
        fx = f(x)
        if i == 0 or i == n: coef = 1
        elif i % 2 == 1: coef = 4
        else: coef = 2
        contrib = coef * fx
        soma += contrib
        print(f"{i}\t{x:.6f}\t{fx:.6f}\t{coef}\t{contrib:.6f}")
    
    resultado = (h / 3) * soma
    print(f"\nResultado = (h/3) × {soma:.6f} = {resultado:.10f}")
    return resultado

def simpson_3_8(f, a, b, n):
    while n % 3 != 0: n += 1
    h = (b - a) / n
    print(f"\nPasso h = {h:.6f}")
    print("i\tx_i\t\tf(x_i)\t\tCoef\tContribuição")
    print("-" * 60)
    
    soma = 0
    for i in range(n + 1):
        x = a + i * h
        fx = f(x)
        if i == 0 or i == n: coef = 1
        elif i % 3 == 0: coef = 2
        else: coef = 3
        contrib = coef * fx
        soma += contrib
        print(f"{i}\t{x:.6f}\t{fx:.6f}\t{coef}\t{contrib:.6f}")
    
    resultado = (3 * h / 8) * soma
    print(f"\nResultado = (3h/8) × {soma:.6f} = {resultado:.10f}")
    return resultado

def gaussiana(f, a, b, pontos=3):
    dados = {
        2: ([-0.5773502692, 0.5773502692], [1.0, 1.0]),
        3: ([-0.7745966692, 0.0, 0.7745966692], [0.5555555556, 0.8888888889, 0.5555555556]),
        4: ([-0.8611363116, -0.3399810436, 0.3399810436, 0.8611363116], 
            [0.3478548451, 0.6521451549, 0.6521451549, 0.3478548451]),
        5: ([-0.9061798459, -0.5384693101, 0.0, 0.5384693101, 0.9061798459], 
            [0.2369268851, 0.4786286705, 0.5688888889, 0.4786286705, 0.2369268851])
    }
    
    if pontos not in dados: pontos = 3
    pts, pesos = dados[pontos]
    
    print(f"\nPontos e pesos gaussianos para n={pontos}:")
    print("i\tξ_i\t\tW_i\t\tx_i\t\tf(x_i)\t\tContribuição")
    print("-" * 80)
    
    soma = 0
    for i in range(len(pts)):
        x = ((b - a) * pts[i] + (b + a)) / 2
        fx = f(x)
        contrib = pesos[i] * fx
        soma += contrib
        print(f"{i}\t{pts[i]:.6f}\t{pesos[i]:.6f}\t{x:.6f}\t{fx:.6f}\t{contrib:.6f}")
    
    resultado = ((b - a) / 2) * soma
    print(f"\nResultado = ((b-a)/2) × {soma:.6f} = {resultado:.10f}")
    return resultado

def integral_dupla(f, x_min, x_max, y_min, y_max, nx, ny):
    print(f"Domínio: [{x_min}, {x_max}] × [{y_min}, {y_max}]")
    print(f"Divisões: nx = {nx}, ny = {ny}")
    print("=" * 50)
    
    def integral_em_y(x_fixo):
        print(f"\n--- Integrando em y para x = {x_fixo:.6f} ---")
        def g(y):
            return f(x_fixo, y)
        return trapezio(g, y_min, y_max, ny)
    
    print(f"\n--- Integrando em x ---")
    resultado = trapezio(integral_em_y, x_min, x_max, nx)
    
    print(f"Integral dupla = {resultado:.10f}")
    return resultado

def obter_funcao_1d():
    print("Digite sua função (ex: x**2, math.sin(x), math.exp(x)):")
    expr = input("f(x) = ")
    return lambda x: eval(expr)

def obter_funcao_2d():
    print("Digite sua função de duas variáveis (ex: x**2 + y**2, x*y):")
    expr = input("f(x,y) = ")
    return lambda x, y: eval(expr)

def main():
    print("CALCULADORA DE INTEGRAIS NUMÉRICAS")
    print("1 - Regra do Trapézio")
    print("2 - Regra de Simpson 1/3")
    print("3 - Regra de Simpson 3/8") 
    print("4 - Quadratura Gaussiana")
    print("5 - Integral Dupla")
    
    metodo = int(input("Escolha o método (1-5): "))
    
    if metodo == 5:
        f = obter_funcao_2d()
        print("Digite os limites e subdivisões:")
        x_min = float(input("x mínimo: "))
        x_max = float(input("x máximo: "))
        y_min = float(input("y mínimo: "))
        y_max = float(input("y máximo: "))
        nx = int(input("Subdivisões em x: "))
        ny = int(input("Subdivisões em y: "))
        
        resultado = integral_dupla(f, x_min, x_max, y_min, y_max, nx, ny)
        print(f"\nResultado da integral dupla: {resultado}")
        
    else:
        f = obter_funcao_1d()
        a = float(input("Limite inferior (a): "))
        b = float(input("Limite superior (b): "))
        n = int(input("Número de subdivisões (n): "))
        
        if metodo == 1:
            resultado = trapezio(f, a, b, n)
            print(f"\nResultado (Trapézio): {resultado}")
        elif metodo == 2:
            resultado = simpson_1_3(f, a, b, n)
            print(f"\nResultado (Simpson 1/3): {resultado}")
        elif metodo == 3:
            resultado = simpson_3_8(f, a, b, n)
            print(f"\nResultado (Simpson 3/8): {resultado}")
        elif metodo == 4:
            pontos = int(input("Número de pontos gaussianos (2-5): "))
            resultado = gaussiana(f, a, b, pontos)
            print(f"\nResultado (Gaussiana): {resultado}")

if __name__ == "__main__":
    main()