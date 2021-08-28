'''
Exercício – Pólos Simples 
1.  Para o sistema representado pela seguinte equação diferencial: 

diff(y, t, 2) + 5*diff(y, t, 1) + 6*y = u

Determine: 
(a)  A função de transferência; 
(b)  A equação característica; 
(c)  Os pólos e os zeros; 
(d)  A estabilidade do sistema; 
(e)  A resposta no tempo para u(t) igual a um impulso unitário.

'''
#importação de módulos
from sympy import *
init_printing()
from sympy.abc import s, u, y, t

from control import *
from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt

#RESOLUÇÃO
print('Respostas')

print('Função no domínio da frequência')
func = s**2*y + 5*s*y + 6*y - u
pprint(func)

print('\nLetra A')
ft = solve(func, y)   #A função solve retorna uma lista de resoluções
ft = ft[0]/u
pprint(ft)

#---------------------------------
print('\nLetra B e C: Encontrando os polos')
ft_den = fraction(ft)
ft_den = ft_den[1]
pprint(ft_den)
print('Polos:')
pprint(solve(ft_den, s))

#---------------------------------
print('\nLetra D: Resposta do sistema para um impulso unitário')
# A função do impulso unitário no domínio da frequência é U(S) = 1
u_impulse = 1
resp = ft*u_impulse
print('\nResposta no domínio da frequência:')
pprint(ft)
print('\nResposta no domínio do tempo:')
resp_t = inverse_laplace_transform(resp, s, t)
pprint(resp_t)
print('\nExpandindo a função:')
resp_t = expand(resp_t)
pprint(resp_t)


#------------------------------------------------------
print('\nPlus, plotando o grafico de resposta no tempo')

#Criando o sistema pela função de transferência
#Os itens das listas representam os coeficientes do
#numerador e denominador da função de transferência.
num = [1]
den = [1, 5, 6]
sys = tf(num, den)
print('\nEncontrando os polos novamente')
print(pole(sys))

#Criando a base de tempo para resposta
ex = np.arange(0.0, 12.0, 0.1)
ex = list(ex)

#Plotando o gráfico de resposta ao impulso unitário
#baseado no objeto sys
T, Y = impulse_response(sys, ex)
plt.plot(T, Y)
plt.show()

#Plotando o gráfico de resposta ao impulso unitário
#baseado na equação da inversa de La Place
ey = [ resp_t.subs([(t, i)]) for i in ex]
plt.plot(ex, ey)
plt.show()









