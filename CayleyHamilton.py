import numpy as np
import msvcrt
import sys
from os import system
from sympy import *
from sympy.solvers import solve
from fractions import Fraction as frac

programaSigue = True

t, lamb, a0, a1, a2 = symbols('t lamb a_0 a_1 a_2')

init_printing(use_unicode=True)

eq_lambda_1 = a1*lamb + a0 - exp(lamb*t)
eq_lambda_2 = a2*(lamb**2) + a1*lamb + a0 - exp(lamb*t)

def divide(list):
  return int(list[0])/int(list[1])

#construye la matriz
def armaMatriz(params):
  my_array = params.strip('[]').replace(" ","").split(';')
  for i, row in enumerate(my_array): 
    row = row.split(',')
    my_array[i]= [divide(number.split('/')) if '/' in number else float(number)  for number in row ]
  return np.array(my_array)

# se construye la lista de funciones
def sisEq(*args): 
  system_equations = []
  for eq in args:
    system_equations.append(eq)
  return system_equations

#MENU
def main():
  try:
    print("Ingrese la matriz A con el siguiente formato \n[x1 , y1; x2, y2] ó [x1 , y1, z1; x2, y2, z2; x3, y3, z3]\nIngrese un cero para salir del programa")
    params = input()
    system("cls")
    if (params == '0'):
      global programaSigue
      programaSigue = False
    else:

      arr = armaMatriz(params)
      
      if arr.shape == (2,2) or arr.shape == (3,3) :
        
        # Esta parte encuentra los eigen valores
        eig, v = np.linalg.eig(arr) 
        if(eig.size == 2):
          
          # Valida si los 2 eigen valores son iguales
          if(eig[0] == eig[1]):
            derivade_eq = diff(eq_lambda_1, lamb).subs(lamb,eig[0])     #Primera derivada
            # Lista de funciones      (Caso 1)
            system_equations = sisEq(derivade_eq, eq_lambda_1.subs(lamb,eig[1]))
          else :
            # Lista de funciones      (Caso 2)
            system_equations = sisEq(eq_lambda_1.subs(lamb,eig[0]), eq_lambda_1.subs(lamb,eig[1]))
          # Solucion del sistema de ecuaciones     (Caso 1 y 2)
          coef_sol = simplify(solve(system_equations, [a0, a1]))
          # Solución de e^at
          e_at = simplify(coef_sol.get(a1)*arr + coef_sol.get(a0)*eye(2))
        elif(eig.size == 3):

          # Valida si los 3 eigen valores son iguales
          if(eig[0] == eig[1] and eig[0] == eig[2]):
            derivade_eq_1 = diff(eq_lambda_2, lamb)          #Primera derivada
            derivade_eq_2 = diff(derivade_eq_1, lamb)        #Segunda derivada
            # Lista de funciones      (Caso 3)
            system_equations = sisEq(derivade_eq_1.subs(lamb,eig[0]), derivade_eq_2.subs(lamb,eig[1]), eq_lambda_2.subs(lamb,eig[2]))
          
          # 2 eigen valores son iguales
          elif(eig[0]==eig[1] or eig[0]== eig[2] or eig[1] == eig[2]):
            
            derivade_eq_1 = diff(eq_lambda_2, lamb).subs(lamb,eig[0])   #Primera derivada
            # Lista de funciones      (Caso 4)     
            system_equations = sisEq(derivade_eq_1, eq_lambda_2.subs(lamb,eig[1]), eq_lambda_2.subs(lamb,eig[2]))
          else:      
            # Lista de funciones      (Caso 5)
            system_equations = sisEq(eq_lambda_2.subs(lamb,eig[0]), eq_lambda_2.subs(lamb,eig[1]), eq_lambda_2.subs(lamb,eig[2]))
          
          # Solucion del sistema de ecuaciones     (Caso 3, 4 y 5)
          coef_sol = solve(system_equations, [a0, a1, a2])
          # Solución de e^at
          e_at = simplify(coef_sol.get(a2)*(arr**2) + coef_sol.get(a1)*arr + coef_sol.get(a1)*eye(3))
        
        #Impresión de entrada y salida
        print('A:\n')
        pprint(arr)
        print("\n\n e^At:") 
        pprint(expand(nsimplify(e_at)))

        print('\nPresione enter para calcular otra matriz')
        msvcrt.getch()
        system("cls")
      else:
        print('El tamaño de la matriz no es valido\n')  
  except:
    print("El formato de entrada no es válido\n")

#Bucle infinito hasta que ingrese 0 el usuario

print('Bienvenido a la mejor aplicación para el método de Cayley Hamilton\n')
while(programaSigue):
  main()
print('\nHasta luego, gracias por usar esta aplicación!!')
msvcrt.getch()
sys.exit(0)  