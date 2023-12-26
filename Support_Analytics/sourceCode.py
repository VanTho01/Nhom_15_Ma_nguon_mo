from sympy import *

x = Symbol('x')
ans1 = diff(sin(x)*exp(x), x) 
print(f'ans1 = {ans1}')
ans2 = integrate(exp(x)*sin(x) + exp(x)*cos(x), x)
print(f'ans2 = {ans2}')
ans3 = integrate(sin(x**2), (x, -oo, oo))
print(f'ans3 = {ans3}')
ans4 = limit(sin(x)/x, x, 0)        
print(f'ans4 = {ans4}')             
ans5 = solve(x**2-2, x) 
print(f'ann5 = {ans5}')