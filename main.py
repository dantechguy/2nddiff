from sympy import *
x,u,A,B=symbols('x u A B')

equation = 3*x**2 + 6*x + 1 + sin(x) - 16*cos(2*x)
x_sub = exp(u)
co = {
    2: 1,
    1: 2,
    0: 1
}

# answer
x_eq = sympify(equation)
u_eq = x_eq.subs(x, x_sub)
complimentary = None

aux = solve(co[2]*x**2 + co[1]*x + co[0], x)
det = co[1]**2 - 4*co[2]*co[0]
if det > 0:
    complimentary = A*exp(aux[0]*x) + B*exp(aux[1]*x)
elif det == 0:
    complimentary = (A + B*x) * exp(aux[0]*x)
else:
    complimentary = exp(re(aux[0])*x) * (A*sin(im(aux[0])*x) + B*sin(im(aux[1])*x))

# rhs
x_first_diff = diff(x_eq, x)
x_second_diff = diff(x_eq, x, x)
x_rhs = co[0]*x_eq + co[1]*x_first_diff + co[2]*x_second_diff
u_rhs = x_rhs.subs(x, x_sub)

# lhs
u_sub = solve(Eq(x, x_sub), u)[0]
du_dx = diff(u_sub, x).subs(x, x_sub) # in terms of u
d2u_dx2 = diff(u_sub, x, x).subs(x, x_sub) # in terms of u
dx_du = diff(x_sub, u)
d2x_du2 = diff(x_sub, u, u)

x_lhs = f'{co[2]}d2y/dx2 + {co[1]}dy/dx + {co[0]}y'
y_co = co[0]
dy_du_co = co[2]*d2u_dx2 + co[1]*du_dx
d2y_du2_co = co[2] * du_dx**2
u_lhs = f'({d2y_du2_co})d2y/du2 + ({dy_du_co})dy/du + ({y_co})y'

print(f'''QUESTION
With substitution x={x_sub}, and differential equation
{u_lhs} = {u_rhs}
Find y in terms of x

ANSWER
y = {x_eq + complimentary}''')