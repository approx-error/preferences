# Input translator for ODE solver

import re
import copy
import constants as cts
import sympy as sp

#def clear_duplicates(list_to_clear: list, list_to_check_against: list[str]) -> list:
    #'''
    #Clear all items found in 'list_to_check_against' from 'list_to_clear'.
    #This function creates a copy of the list to clear and so the original list is retained.
    #'''
    #copied_list_to_clear = copy.copy(list_to_clear)
    #for item in copied_list_to_clear:
        #if item in list_to_check_against:
            #copied_list_to_clear.remove(item)

    #return copied_list_to_clear


def create_sympy_objects(list_of_labels: list, object_type: str = 'symbol') -> dict:
    '''
    Generates a dictionary of symyp objects of type 'object_type' with
    keys from 'list_of_labels'. Supported types are 'symbol' and 'function'.
    If 'function' is chosen the given label will be translated to sympy functions
    using cts.SYMPY_FUNCTION_MAP. 
    '''
    object_dict = dict()
    for label in list_of_labels:
        if object_type == 'symbol':
            if label in ['gamma', 'lambda', 'zeta']: 
                # NOTE: This check is here to prevent a bug where lambda is interpreted as the python keyword 'lambda'
                # and exp(zeta) and exp(gamma) evaluate to 1 when calling the function sp.sympify
                # By adding an underscore to the variable representation, sympy doesn't confuse lambda with the keyword
                # gamma with the gamma function or zeta with the zeta function when calling sp.sympify('...')
                object_dict[label] = sp.Symbol(f'{label}_', real=True)
            else:
                object_dict[label] = sp.Symbol(f'{label}', real=True)
        elif object_type == 'function':
            object_dict[label] = cts.SYMPY_FUNCTION_MAP[label]

    return object_dict



def translate(parsed_input, debug = False):
    # Translate user input to be recognizable by sympy
    
    encoded_eq = parsed_input[0]
    encoded_ics = parsed_input[1]
    var_symbol = parsed_input[2]
    func_symbol = parsed_input[3]
    elementary_symbols = parsed_input[4]
    latin_symbols = parsed_input[5]
    greek_symbols = parsed_input[6]
   
        
    # Generate required sympy objects
    var = sp.Symbol(f'{var_symbol}', real=True)
    func = sp.symbols(f'{func_symbol}', cls=sp.Function)
    
    elementary, latin, greek = dict(), dict(), dict()
    if elementary_symbols:
        elementary = create_sympy_objects(elementary_symbols, 'function')
    if latin_symbols:
        latin = create_sympy_objects(latin_symbols)
    if greek_symbols:
        greek = create_sympy_objects(greek_symbols)

    # Generate list containing the equation and ics if they have been provided
    equation_and_ics = [encoded_eq]
    for ic in encoded_ics:
        equation_and_ics.append(ic)

    # Generate sympy representations
    left_hand_side_terms = [[] for _ in range(len(equation_and_ics))]
    right_hand_side_terms = [[] for _ in range(len(equation_and_ics))]
    for i, relation in enumerate(equation_and_ics):
        sign = '+'
        lhs = True
        for j, term in enumerate(relation):
            if term in ['+', '-']:
                sign = term
                continue
            if term in ['=']:
                lhs = False
                sign = '+'
                continue
            object_list = re.findall(cts.OBJECT_TRANSLATE_PATTERN, term)
            object_list.sort(key=len, reverse=True) # Sorting from longest to shortest so that %'($) get replaced before $
            new_term = term
            for obj in object_list:
                match obj[0]:
                    case '@':
                        ind = int(obj[1])
                        symbol = latin_symbols[ind]
                        variable = str(latin[symbol])
                    case '&':
                        ind = int(obj[1])
                        symbol = greek_symbols[ind]
                        variable = str(greek[symbol])
                    case '#':
                        ind = int(obj[1])
                        symbol = elementary_symbols[ind]
                        variable = str(elementary[symbol])
                    case '%':
                        order = obj.count('\'')
                        if i == 0:
                            if order == 0:
                                variable = str(func(var))
                            else:
                                variable = str(sp.diff(func(var), var, order))
                        else:
                            begin_paren = obj.index('(')
                            end_paren = obj.index(')')
                            substitution = obj[begin_paren+1:end_paren]
                            if order == 0:
                                variable = str(func(substitution))
                            else:
                                variable = str(func(var).diff(var, order).subs(var, substitution))
                    case '$':
                        variable = str(var)
                    case _:
                        print('Not possible')
                new_term = term.replace(obj, variable)
                equation_and_ics[i][j] = new_term
                term = equation_and_ics[i][j]
            if lhs:
                left_hand_side_terms[i].extend(sign + new_term)
            else:
                right_hand_side_terms[i].extend(sign + new_term)
        
    left_hand_sides = [''.join(terms) for terms in left_hand_side_terms]
    right_hand_sides = [''.join(terms) for terms in right_hand_side_terms]

    sympy_lhs = [sp.sympify(lhs) for lhs in left_hand_sides]
    sympy_rhs = [sp.sympify(rhs) for rhs in right_hand_sides]

    equation = sp.Eq(sympy_lhs[0], sympy_rhs[0])

    if encoded_ics:
        initial_conditions = {sympy_lhs[i]: sympy_rhs[i] for i in range(1, len(equation_and_ics))}
    else:
        initial_conditions = 0

    if debug:
        print(30*'-', 'BEGIN TRANSLATOR DEBUG INFORMATION', 30*'-') 
        print()
        print('INPUT INFORMATION')
        print('PARSED INPUT:', parsed_input)
        print('EQ AND ICS COMBINED:', equation_and_ics)
        print()
        print('INFORMATION ON THE SIDES OF EQUATIONS')
        print('LEFT HAND SIDES:', *left_hand_sides, sep='  ')
        print('SYMPY LEFT HAND SIDES IN PYTHON NOTATION AND SYMPY NOTATION:')
        print(*sympy_lhs, sep='  ')
        print()
        sp.pprint(sympy_lhs)
        print('RIGHT HAND SIDES:', *right_hand_sides, sep='  ')
        print('SYMPY RIGHT HAND SIDES AS PYTHON NOTATION AND SYMPY NOTATION:')
        print(*sympy_rhs, sep='  ')
        print()
        sp.pprint(sympy_rhs)
        print()
        print('EQUATION AND INITIAL CONDITION INFORMATION')
        print('EQUATION AS PYTHON NOTATION AND SYMPY NOTATION:')
        print(equation)
        print()
        sp.pprint(equation)
        print('INITIAL CONDITIONS AS PYTHON NOTATION AND SYMPY NOTATION:')
        print(initial_conditions)
        print()
        sp.pprint(initial_conditions)
        print()
        print(32*'-', 'END TRANSLATOR DEBUG INFORMATION', 32*'-') 

    return (latin | greek, var, func, equation, initial_conditions)

