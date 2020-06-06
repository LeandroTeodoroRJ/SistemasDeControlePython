#********************************************************************************
#       RESPOSTA TRANSITÓRIA NO TEMPO USANDO ESPAÇO DE ESTADOS
#                    RESPOSTA AO DEGRAU UNITÁRIO
#********************************************************************************
'''
Exemplo no MatLab - Ogata - Pág 183

Programa 5.13 em MATLAB
t = 0:0.1:12;
A = [-1 0.5;-1 0];
B = [0;1];
C = [1 0];
D = [0];
% Para a entrada em degrau unitário u = 1(t),
% utilize o comando 'y = step(A,B,C,D,1,t)'.
y = step(A,B,C,D,1,t);
plot(t,y)
grid
title('Resposta ao Degrau Unitário')
xlabel('t (s)')
ylabel('Saída')
% Para a resposta à ebtrada exponencial
% u = exp(-t), utilize o comando
% 'z = lsim(A,B,C,D,u,t)' .
u = exp(-t);
z = lsim(A,B,C,D,u,t);
plot(t,u,'-',t,z,'o')
grid
title('Resposta à Entrada Exponencial u = exp(-t)')
xlabel('t (s)')
ylabel('Entrada Exponencial e Saída do sistema')
text(2.3,0.49,'Entrada Exponencial')
text(6.4,0.28,'Saída')

'''

from control import *
from control.matlab import *
import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0, 12.0, 0.1)
#print(t)
t = list(t)
#print(t)
#print(type(t))
A = [[-1, 0.5], [-1, 0]]
#print(type(A))
B = [[0], [1]]
C = [1, 0]
D = [0]

sys = ss(A, B, C, D)

u = list(range(len(t)))  #Cria uma lista de valores de entrada no tamanho dos elementos de tempo
for i in range(len(t)):
    u[i] = 1             #Função da entrada u(t) = 1

T, Y, X = forced_response(sys, t, u)
plt.plot(T, Y)
plt.show()