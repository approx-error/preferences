# Initiate a sympy session

import pythonrc

# NOTE: For a more convenient user experience I have the following alias defined in my .bashrc file:
# alias sympy='cd && python -i sympy_session.py'
# This alias navigates to home and runs this script interactively (that's the -i flag) so that
# once this script is finished you will be dropped in the python interpreter ready to do calculations

executed_commands ='''\
These commands were executed:
>>> from sympy import *
>>> x, y, z = symbols('x y z', real=True)
>>> p, q, r, s, t, u, v, w = symbols('p q r s t u v w')
>>> a, b, c = symbols('a b c')
>>> i, j, k, l, m, n = symbols('i j k l m n', integer=True)
>>> f, g, h = symbols('f g h', cls=Function)
>>> alp, bet, gam, delt, eps, zet, eta, the, iot, kap, lam, mu = symbols('alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu')
>>> nu, xi, omi, pie, rho, sig, tau, ups, phi, chi, psi, ome = symbols('nu xi omicron pi rho sigma tau upsilon phi chi psi omega')
>>> Gam, Delt, The, Lam, Xi, Pie, Sig, Phi, Psi, Ome = symbols('Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega')
>>> init_printing(pretty_print=True, order ='lex', use_unicode=True)
'''

from sympy import *

x, y, z = symbols('x y z', real=True)
p, q, r, s, t, u, v, w = symbols('p q r s t u v w')
a, b, c = symbols('a b c')
i, j, k, l, m, n = symbols('i j k l m n', integer=True)
f, g, h = symbols('f g h', cls=Function)

alp, bet, gam, delt, eps, zet, eta, the, iot, kap, lam, mu = symbols('alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu')
nu, xi, omi, pie, rho, sig, tau, ups, phi, chi, psi, ome = symbols('nu xi omicron pi rho sigma tau upsilon phi chi psi omega')

Gam, Delt, The, Lam, Xi, Pie, Sig, Phi, Psi, Ome = symbols('Gamma Delta Theta Lambda Xi Pi Sigma Phi Psi Omega')

init_printing(pretty_print=True, order='lex', use_unicode=True)

print(executed_commands)
