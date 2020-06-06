#*****************************************************************
#               TRANSFORMADA INVERSA DE LA PLACE
# Python versão: 3.6.7
#*****************************************************************


from sympy import *

#Transformada de LaPlace com a variável do tempo em t e da
#freaquencia em s (s -> t)

#OBS: A função Heaviside(t) é a função Degrau Unitário
print("OBS:")
print(Heaviside(-0.5))
print(Heaviside(0.5))

print("\nExemplo 1")
F = 5/s**2
f = inverse_laplace_transform(F,s,t)
print(f)

print("\nExemplo 2")
F = 2/(s**2 + 1)
f = inverse_laplace_transform(F,s,t)
print(f)

print("\nExemplo 3")
F = 2/s**2
f = inverse_laplace_transform(F,s,t)
print(f)
