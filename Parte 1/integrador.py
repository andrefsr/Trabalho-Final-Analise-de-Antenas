import numpy as np

### Integrador Simpson

def SimpsonInt(a,b,num,f):
    
    if num % 2 == 0: num += 1

    pontos = np.linspace(a,b,num)

    h = (b-a)/(num-1)

    I = f(a,0) + f(b,0)

    for i in range(1,num-1):

        if i % 2 == 0: I += 2*f(pontos[i],0)
        else: I += 4*f(pontos[i],0)

    I = (h/3) * I
    return I

### Intervalo de análise
x2 = 1
x1 = 0

n = 102  ### Número de pontos

print(SimpsonInt(x1,x2,n, f = lambda x,y: x**2))

