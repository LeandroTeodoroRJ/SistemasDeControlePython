#*****************************************************************
#                   OPERAÇÕES COM BLOCOS
# Python versão: 3.6
#*****************************************************************

from control import *
from control.matlab import *

num1 = [10]
den1 = [1, 2, 10]
num2 = [5]
den2 = [1, 5]

sys1 = tf(num1, den1)
sys2 = tf(num2, den2)

sys_serie = series(sys1, sys2)
print("\nBlocos em série: ", sys_serie)

sys_paralelo = parallel(sys1, sys2)
print("\nBlocos em paralelo: ", sys_paralelo)

sys_malha_fechada = feedback(sys1, sys2)
print("\nRealimentação em malha fechada: ", sys_malha_fechada)

