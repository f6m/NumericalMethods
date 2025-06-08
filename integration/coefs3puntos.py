from sympy import *
x,a,b=symbols('x,a,b')
print(simplify(integrate(((x-((a+b)/2))*(x-b))/((a-((a+b)/2))*(a-b)),(x, a, b))))
#"-a/6 + b/6"
print(simplify(integrate(((x-a)*(x-b))/((((a+b)/2)-a)*(((a+b)/2)-b)),(x, a, b))))
#"-2*a/3 + 2*b/3"
print(simplify(integrate(((x-a)*(x-((a+b)/2)))/((b-a)*(b-((a+b)/2))),(x, a, b))))
#"-a/6 + b/6"
