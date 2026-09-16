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

### Trapézios repetidos

# x = np.linspace(0, 1, 1000000)

# y = f(x)

# area = np.trapezoid(y, x)

# gabarito = 1/3

# erro_relativo_trapezio = np.abs(gabarito-trapezio)/gabarito
# erro_relativo_simpson = np.abs(gabarito-simpson)/gabarito
# erro_relativo_numpy = np.abs(gabarito-area)/gabarito

#print(f'Erro relativo trapézio = {erro_relativo_trapezio}\n')
#print(f'Erro relativo simpson = {erro_relativo_simpson}\n')
#print(f'Erro relativo numpy = {erro_relativo_numpy}')

#def intnumtr(a,b,num):
#    pontos = np.linspace(a,b,num)

#    h = (b-a)/(num-1)

#    I = f(a) + f(b)
#    for i in range(1,num-1):
#        I += 2*f(pontos[i])

#    I = (h/2)*I
#    return I

#trapezio = intnumtr(x1,x2,n)