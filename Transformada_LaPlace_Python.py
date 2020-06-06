#*****************************************************************
#                   TRANSFORMADA DE LA PLACE
# Python versão: 3.6.7
#*****************************************************************

from sympy.abc import s,t,x,y,z
from sympy import *

#Transformada de LaPlace com a variável do tempo em t e da
#freaquencia em s (t -> s)
print("Exemplo 1")
print(laplace_transform(5*t, t, s))

print("\nExemplo 2")
f = 5*t
F = laplace_transform(f, t, s)
print(F[0])
print(type(F))
print(type(F[0]))

print("\nExemplo 3")
f = 5*t+4*(t**2)-8
F = laplace_transform(f, t, s)
print(F[0])

print("\nExemplo 4")
f= 2*sin(t)
F = laplace_transform(f, t, s)
print(F[0])

print("\nExemplo 5")
f= t**2
df= diff(f, t)
F = laplace_transform(f, t, s)
print(F[0])
F = laplace_transform(df, t, s)
print(F[0])

print("\nExemplo 6")
f= t**2
df= diff(f, t, 2)   #Derivada segunda
F = laplace_transform(f, t, s)
print(F[0])
F = laplace_transform(df, t, s)
print(F[0])

print("\nExemplo 7")
f= t**2
itg_f= integrate(f, t)   #Integral
F = laplace_transform(f, t, s)
print(F[0])
F = laplace_transform(itg_f, t, s)
print(F[0])



#fim
