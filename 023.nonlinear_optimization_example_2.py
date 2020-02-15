import numpy as np
from scipy.optimize import minimize

# define the cost function
def objective(x):
    return (x[0] - 1)**2 + (x[1] - 2.5)**2

# define the constraints
def constraint1(x):
    return x[0] - 2 * x[1] + 2 

def constraint2(x):
    return -x[0] - 2 * x[1] + 6

def constraint3(x):
    return -x[0] + 2 * x[1] + 2

# initial guesses
n = 2
x0 = np.zeros(n)
x0[0] = 0
x0[1] = 0

# show initial objective
print('Initial SSE Objective: ' + str(objective(x0)))

# optimize
b = (0.0, None)
bnds = (b, b) 
con1 = {'type': 'ineq', 'fun': constraint1} 
con2 = {'type': 'ineq', 'fun': constraint2}
con3 = {'type': 'ineq', 'fun': constraint3} 
cons = ([con1,con2,con3])

# solution
solution = minimize(objective, x0, method = 'SLSQP',
           bounds = bnds, constraints = cons, options = {'disp': True}, tol = 10e-10)
x = solution.x

# show final objective
print('Final SSE Objective: ' + str(objective(x)))

# print solution
print('Solution')
print('x1 = ' + str(x[0]))
print('x2 = ' + str(x[1]))
