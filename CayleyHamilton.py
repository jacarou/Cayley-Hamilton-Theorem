import numpy as np
import sympy as sp

def getCoeffs(poly):
    coefficients = [poly[i][1] for i in range(len(poly))]
    return coefficients

def getExpons(poly):
    exponents = [poly[i][0][0] for i in range(len(poly))]
    return exponents

# EJEMPLOS DE MATRICES
M = sp.Matrix([[-3, 1], [0, -2]])
#M = Matrix([[1, 1,0], [0, 0,1], [0,2,-1]])
#M = Matrix([[0,0,0,1], [1,0,1,0], [0,0,1,0],[0,0,1,1]]) 
MATSIZE = M.rank()
I = sp.eye(MATSIZE)

# Impresion de matriz
print("Matriz A=") 
sp.pprint(M)
lamda = sp.symbols('lamda')
t = sp.symbols('t')

# Polinomio Caracteristico
poly = M.charpoly(lamda)      
print("Polinomio Caracteristico=")
print(poly)

# Tuplas exponente coeficiente
#print("Terms ", poly.terms()) 
poly_terms = poly.terms()          

# Coeficientes
coefficients = getCoeffs(poly_terms) 
print("Coeficientes: ", coefficients)

# Exponentes
exponents = getExpons(poly_terms) 
print("Exponentes: ", exponents)

# Polinomio factorizado
print("Polinomio Factorizado:")
sp.pprint(sp.factor(poly.as_expr()))   
print()

#Validar que termino no existe y remplazar por cero (0)


# Raices del polinomio 
print(np.roots(coefficients))
