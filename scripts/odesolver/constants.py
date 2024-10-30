# Constants module for ODE solver

import sympy as sp


PATTERNS = {
            'variable': '\\([a-zA-Z]_*[0-9]*\\)|\\(\\{[a-zA-Z]+\\}_*[0-9]*\\)', 'function': '[a-zA-Z]_*[0-9]*\'+|\\{[a-zA-Z]+\\}_*[0-9]*\'+', 'greek': '\\{[a-zA-Z]+\\}_*[0-9]*', 'latin': '[a-zA-Z]_*[0-9]*', \
            'elementary function': 'sin|cos|tan|sec|csc|cot|asin|acos|atan|asec|acsc|acot|sinh|cosh|tanh|sech|csch|coth|asinh|acosh|atanh|asech|asech|acsc|sqrt|cbrt|exp|ln|log'
           }

ENCODING_RULES = {'variable': '$', 'function': '%', 'greek': '&', 'latin': '@', 'elementary function': '#'}

DEFAULT_IGNORE = ['+', '-', '=']

ENCODING_SYMBOLS = ['$', '%', '&', '@', '#']

OBJECT_SYMBOLS = ['^'] + ENCODING_SYMBOLS

OBJECT_PATTERN = '\\^[0-9]|&[0-9]|@[0-9]|#[0-9]\\([0-9]*[\\@]*[\\&]*[\\#]*[0-9]*[\\$]*\\)|#[0-9]\\([0-9]*[a-z]*[A-Z]*[\\$]*[\\*]*[\\+]*[\\^]*[\\-]*[/]*[0-9]*[a-z]*[A-Z]*[\\$]*]+\\)|\
                #[0-9]\\([0-9]*\\{[a-zA-Z]+\\}[\\$]*[\\*]*[\\+]*[\\^]*[\\-]*[/]*[0-9]*\\)|%\'*\\([0-9]*\\$*\\)|%\'*|\\$|\\)|\\]|^[0-9]+'#|[0-9]+|[^&][0-9]+|[^@][0-9]+|[^#][0-9]+|[^\\(][0-9]+|[^\\]][0-9]+|^[0-9]+'

OBJECT_TRANSLATE_PATTERN = '&[0-9]|@[0-9]|#[0-9]|%\'*\\([0-9]*\\$\\)|%\'*\\([0-9]*\\)|%\'*|\\$'

NO_MULTIPLICATION = ['*', '+', '-', '/', ')', ']', '^']

SYMPY_FUNCTION_MAP = {
        'sin': sp.sin, 'cos': sp.cos, 'tan': sp.tan, 'sec': sp.sec, 'csc': sp.csc, 'cot': sp.cot,\
        'asin': sp.asin, 'acos': sp.acos, 'atan': sp.atan, 'asec': sp.asec, 'acsc': sp.acsc, 'acot': sp.acot,\
        'sinh': sp.sinh, 'cosh': sp.cosh, 'tanh': sp.tanh, 'sech': sp.sech, 'csch': sp.csch, 'coth': sp.coth,\
        'asinh': sp.asinh, 'acosh': sp.acosh, 'atanh': sp.atanh, 'asech': sp.asech, 'acsch': sp.acsch, 'acoth': sp.acoth,\
        'sqrt': sp.sqrt, 'cbrt': sp.sqrt, 'exp': sp.exp, 'ln': sp.log, 'log': sp.log
        }

GREEK_LETTER_MAP = {
        '{alp}': 'alpha', '{bet}': 'beta', '{gam}': 'gamma', '{del}': 'delta', '{eps}': 'epsilon', '{zet}': 'zeta',\
        '{eta}': 'eta', '{the}': 'theta', '{iot}': 'iota', '{kap}': 'kappa', '{lam}': 'lambda', '{mu}': 'mu',\
        '{nu}': 'nu', '{xi}': 'xi', '{omi}': 'omi', '{pi}': 'pi', '{rho}': 'rho', '{sig}': 'sigma', '{tau}': 'tau',\
        '{ups}': 'upsilon', '{phi}': 'phi', '{chi}': 'chi', '{psi}': 'psi', '{ome}': 'omega',\
        '{Alp}': 'Alpha', '{Bet}': 'Beta', '{Gam}': 'Gamma', '{Del}': 'Delta', '{Eps}': 'Epsilon', '{Zet}': 'Zeta',\
        '{Eta}': 'Eta', '{The}': 'Theta', '{Iot}': 'Iota', '{Kap}': 'Kappa', '{Lam}': 'Lambda', '{Mu}': 'Mu',\
        '{Nu}': 'Nu', '{Xi}': 'Xi', '{Omi}': 'Omi', '{Pi}': 'Pi', '{Rho}': 'Rho', '{Sig}': 'Sigma', '{Tau}': 'Tau',\
        '{Ups}': 'Upsilon', '{Phi}': 'Phi', '{Chi}': 'Chi', '{Psi}': 'Psi', '{Ome}': 'Omega',\
        }
