#calculamos la serie de Maclaurin para la función
# 1/sqrt(x^3 + 1)
# la serie de Maclaurin es la serie de Taylor con a = 0
#importamos la librería
from sympy.abc import x 
from sympy import sqrt, diff, factorial, expand, pprint
#Definimos la función que calcula la serie
def PolTaylor(a,n):
    f = 1/sqrt(x**3 + 1) #función a utilizar
    F = f
    T = f.subs(x,a)
    for k in range(1,n+1):
        dfk=diff(f,x)
        T = T + dfk.subs(x,a)*(x**k/factorial(k))
        f = dfk
    #Para mostrar el resultado de forma más estética
    pprint(expand(T))

n = 10 #orden máximo de la serie
a = 0 # punto donde se busca la aproximación
PolTaylor(a,n)