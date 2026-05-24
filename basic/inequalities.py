from sympy import symbols
from sympy.solvers.inequalities import solve_univariate_inequality
from sympy import Lt,Le,Gt,Ge,Eq,Ne 
'''Lt=less than, Le=less than or equal to, Gt=Greater than, Ge=Greater than or equal to, Eq=Equals to, Ne= Not equals to'''
x=symbols('x')
ineq=solve_univariate_inequality(Ge((x-1)**2*(x+3)*(x+5),0),x) 
print(ineq)
