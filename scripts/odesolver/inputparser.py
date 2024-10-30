# Input parser for ODE solver

import re
import copy
import constants as cts

def determine_symbols(object_to_search_for: str, search_from_this: list[str], ignore_these: list[str] = cts.DEFAULT_IGNORE, default_value: str = '') -> list[str]:
    '''
    Search for a given object type 'object_to_search_for' from a list of strings 'search_from_this' ignoring a string if it is contained in
    'ignore_these'. The object type should be a key in the global dictionary cts.PATTERNS. It contains regular expressions that match a given object type.
    If the regular expression is met, and the found object hasn't or already been found, the found object will be saved. If at least one object is
    found the found objects will be returned as a list. If no objects are found, an empty list will be returned unless a default value has been provided
    in the string 'default_value'. In that case a list containing said default value will be returned.
    '''
    category = cts.PATTERNS[object_to_search_for]
    found_objects = []
    for term in search_from_this:
        if term in ignore_these:
            continue
        occurences = re.findall(category, term)
        for occurence in occurences:
            if occurence not in found_objects: # additional filter
                found_objects.append(occurence)
    
    if not found_objects and default_value:
        found_objects = [default_value]

    return found_objects

def search_and_replace(objects_to_replace: list[str], object_type: str, search_from_this: list[str], ignore_these: list[str] = cts.DEFAULT_IGNORE) -> list[str]:
    '''
    Search for given objects in 'objects_to_replace' from a list of strings 'search_from_this' ignoring a string if it is contained in
    'ignore these'. If a given object is found, it will be replaced by the string appointed by 'object_type'. The string 'object_type' should be a key
    in the global dictionary cts.ENCODING_RULES. It contains special characters that certain object types should be mapped to when calling this function.
    Once all replacements have been made, a modifed version of the original 'search_from_this' list is returned leaving the original untouched.
    '''
    # Making a copy to do the operations on so as not to affect global state
    copied_search_from_this = copy.copy(search_from_this)
    encoding = cts.ENCODING_RULES[object_type]
    for i, term in enumerate(copied_search_from_this):
        if term in ignore_these:
            continue
        for j, obj in enumerate(objects_to_replace):
            if object_type in ['variable', 'function']:
                try_to_replace = term.replace(obj, encoding)
            else:
                try_to_replace = term.replace(obj, encoding + str(j))
            if try_to_replace != term:
                copied_search_from_this[i] = try_to_replace
            term = copied_search_from_this[i]

    return copied_search_from_this

def find_all_instances(search_this: str, find_this: str):
    '''
    Finds all instances of 'find_this' inside 'search_this' and records
    the index of the first character of 'find_this' in each instance found.
    a generator object containing the indices is returned.
    '''
    start_index = 0
    while True:
        start_index = search_this.find(find_this, start_index)
        if start_index == -1:
            return
        yield start_index
        start_index += len(find_this)

def insert_into_string(original: str, insert_this: str, position) -> str:
    '''
    Insert a given string 'insert_this' at index 'position' in 'original'.
    Since string are immmutable, a new string is created and returned
    '''
    if position > len(original) - 1:
        return 'Position is outside of string'
    else:
        inserted_string = original[:position] + insert_this + original[position:]
        return inserted_string



def add_multiplication_symbols(add_to_these: list[str], ignore_these: list[str] = cts.DEFAULT_IGNORE) -> list[str]:
    '''
    Adds multiplication symbols to the correct places in 'add_to_these' ignoring 'ignore_these' in order to make
    an expression python- and by extension sympy-friendly. A copy is created from the given terms and this copy
    is changed and eventually returned. A multiplication symbol * is added if all of these conditions are met:
        1. An object is not the last character of a term
        2. An object is not followed by any of * + - / ) ] ^
    What constitutes 'an object' will be explained next:
    A string is an object if it matches the OBJECT_PATTERN regular expression, ie:
        Any of ^, &, @ followed by a single number, # followed by a single number and parentheses containing one or more symbols, 
        % followed by zero or more primes ' and ($), % followed by zero or more primes ', or simply $, ) or ]
        A list of all possibilities where N is a single literal number: ^N, &N, @N, #N, %($), %'($), %''($), etc., %, %', %'', etc., $
    '''
    copied_add_to_these = copy.copy(add_to_these)
    for i, term in enumerate(copied_add_to_these):
        if term in ignore_these:
            continue
        object_list = re.findall(cts.OBJECT_PATTERN, term)
        for obj in object_list:
            new_indices = []
            indices = list(find_all_instances(term, obj))
            for j, ind in enumerate(indices):
                term_last_index = len(term) - 1
                if new_indices:
                    potential_multiplication_index = new_indices[j - 1] + len(obj)
                else:
                    potential_multiplication_index = ind + len(obj)
                if term_last_index >= potential_multiplication_index:
                    if term[potential_multiplication_index] not in cts.NO_MULTIPLICATION:
                        new_string = insert_into_string(term, '*', potential_multiplication_index)
                        copied_add_to_these[i] = new_string
                    term = copied_add_to_these[i]
                    new_indices = list(find_all_instances(term, obj))

    return copied_add_to_these

def replace_symbols(change_in_this: list[str], change_these: list[str], to_these: list[str]) -> list[str]:
    '''
    Changes all 'change_these' into 'to_these' in list 'change_in_this'. Creates a
    copy of the original lsit an operates on the copy leaving the original unchanged
    '''
    copied_change = copy.copy(change_in_this)
    for i, term in enumerate(copied_change):
        for j, change in enumerate(change_these):
            new_term = term.replace(change, to_these[j])
            copied_change[i] = new_term
            term = copied_change[i]

    return copied_change

def translate_greek_symbols(list_of_symbols: list[str]) -> list[str]:
    '''
    Translates a given list of greek symbols 'list_of_symbols' to their actual sympy recognized names
    using cts.GREEK_LETTER_MAP.
    '''
    translated = []
    
    for symbol in list_of_symbols:
        if '_' in symbol:
            translated.append(cts.GREEK_LETTER_MAP[symbol[:-2]] + symbol[-2:])
        else:
            translated.append(cts.GREEK_LETTER_MAP[symbol])

    return translated

def inputparse(input_to_parse, debug = False):

    # Want to know: variable, function to solve for, parameters, the actual equation and intial/boundary conditions
    # Syntax should be as easy as possible. For example from this input: "ay''(x) + bxy'(x) + sin(x) = 4, y(0) = 1, y'(0) = 0"
    # The program should be able to deduce that x is the variable, y is the function to solve for, a and b are the parameters,
    # a*sp.diff(y(x), x, 2) + b*x*sp.diff(y(x),x) + sp.sin(x) = 4 is the actual equation and ics = {y(0): 1, diff(y(x),x).subs(x.0): 0}
    # are the initial conditions

    # Split the arguments up

    initial_conds_provided = 0
    equation_and_init_conds = input_to_parse.split(',')

    initial_conds_provided += len(equation_and_init_conds) - 1 # No initial conds if len() is 1 since that means only an equation was provided

    all_terms = []
    for item in equation_and_init_conds:
        terms = item.split(' ')
        for i, term in enumerate(terms):
            terms[i] = term.strip()
        all_terms.append(terms)
    
    equation_terms = all_terms[0]
    if initial_conds_provided > 0:
        initial_condition_terms = all_terms[1:]
    else:
        initial_condition_terms = []

    # Removing trailing whitespaces
    for i, terms in enumerate(initial_condition_terms):
        for j, term in enumerate(terms):
            if term == '':
                initial_condition_terms[i].pop(j)


    # Finding the elementary functions, the variable, the unknown function and the parameters
    # And replacing them with their respective encodings
    
    replaced = copy.copy(equation_terms)
            
    # The elementary functions        
    eq_elementary_symbols = determine_symbols('elementary function', replaced)
    if eq_elementary_symbols:
        replaced = search_and_replace(eq_elementary_symbols, 'elementary function', replaced)

    # The independent variable
    variable_symbols = determine_symbols('variable', replaced, default_value = '(x)')
    
    unique_symbols = list(dict.fromkeys(variable_symbols))
    unique_symbols = [symb[1:-1] for symb in unique_symbols] # Remove parentheses
    if len(unique_symbols) > 1:
        print('Found multiple variable candidates. Please choose the intended variable:')
        print(*unique_symbols, sep='  ')
        validated = False
        while not validated:
            candidate = input('>>> ')
            if candidate in unique_symbols:
                print(f'Proceeding with variable \'{candidate}\'.')
                validated = True
            else:
                print('Not a valid variable! Please try again.')
        
        variable_symbol = [candidate]
    else:
        variable_symbol = unique_symbols

    replaced = search_and_replace(variable_symbol, 'variable', replaced)

    # The unknown function
    function_symbols = determine_symbols('function', replaced, default_value = 'f')
    first_prime = function_symbols[0].find('\'')
    function_symbol = [function_symbols[0][:first_prime]] # function_symbols = ["y_0''", "y_0'", ...] the slice [:first_prime] is simply 'y_0'
    replaced = search_and_replace(function_symbol, 'function', replaced)

    # The greek letter parameters
    eq_greek_symbols = determine_symbols('greek', replaced)
    if eq_greek_symbols:
        replaced = search_and_replace(eq_greek_symbols, 'greek', replaced)

    # The latin letter parameters
    eq_latin_symbols = determine_symbols('latin', replaced)
    if eq_latin_symbols:
        replaced = search_and_replace(eq_latin_symbols, 'latin', replaced)

    # Adding multiplication signs

    multiplied = add_multiplication_symbols(replaced)

    # Changing symbols:

    changed = replace_symbols(multiplied, ['[', ']', '^'], ['(', ')', '**'])


    # Processing initial conditions
    replaced_ic = copy.copy(initial_condition_terms)
    ic_elementary_symbols, ic_greek_symbols, ic_latin_symbols = [], [], []
    multiplied_ic = []
    changed_ic = []
    if initial_conds_provided:
        for i, term_list in enumerate(replaced_ic):
            # The elementary functions
            ic_elementary_symbols.extend(determine_symbols('elementary function', term_list))
            replaced_ic[i] = search_and_replace(eq_elementary_symbols + ic_elementary_symbols, 'elementary function', term_list)
            term_list = replaced_ic[i]
            
            # The independent variable
            replaced_ic[i] = search_and_replace(variable_symbol, 'variable', term_list)
            term_list = replaced_ic[i]

            # The unknown function
            replaced_ic[i] = search_and_replace(function_symbol, 'function', term_list)
            term_list = replaced_ic[i]

            # The greek letter paramters
            ic_greek_symbols.extend(determine_symbols('greek', term_list))
            replaced_ic[i] = search_and_replace(eq_greek_symbols + ic_greek_symbols, 'greek', term_list)
            term_list = replaced_ic[i]

            # The latin letter parameters
            ic_latin_symbols.extend(determine_symbols('latin', term_list))
            replaced_ic[i] = search_and_replace(eq_latin_symbols + ic_latin_symbols, 'latin', term_list)
            term_list = replaced_ic[i]
            
            # Adding multiplication symbols, changing brackets to parentheses and changing ^:s to **:s
            multiplied_ic.append(add_multiplication_symbols(term_list))
            changed_ic.append(replace_symbols(multiplied_ic[i], ['[', ']', '^'], ['(', ')', '**']))

    # Merging the elementary functions, greek and latin parameters from the equation and initial conditions making sure to not include duplicates
    elementary_function_symbols = list(dict.fromkeys(eq_elementary_symbols + ic_elementary_symbols))
    latin_parameter_symbols = list(dict.fromkeys(eq_latin_symbols + ic_latin_symbols))
    greek_parameter_symbols = list(dict.fromkeys(eq_greek_symbols + ic_greek_symbols))
    # Translating the greek paramters to sympy recognized names:
    translated_greek = translate_greek_symbols(greek_parameter_symbols)

    # Debugging information
    if debug:
        print(30*'-' + ' BEGIN INPUTPARSER DEBUG INFORMATION ' + 30*'-')
        print()
        print('EQUATION INFORMATION:')
        print('EQ:    ', ' '.join(equation_terms))
        print('ENC EQ:', ' '.join(replaced))
        print('MUL EQ:', ' '.join(multiplied))
        print('CHA EQ:', ' '.join(changed))
        print() 
        print('INITIAL CONDITION INFORMATION:')
        print(f'ICS:    ', *[' '.join(ic) for ic in initial_condition_terms], sep='    ')
        print(f'ENC ICS:', *[' '.join(ic) for ic in replaced_ic] , sep='    ')
        print(f'MUL ICS:', *[' '.join(ic) for ic in multiplied_ic], sep='    ')
        print(f'CHA ICS:', *[' '.join(ic) for ic in changed_ic], sep='    ')
        print()
        print('VARIABLE INFORMATION')
        print('VAR:  ', variable_symbol[0])
        print('FUNC: ', function_symbol[0])
        print('EQ ELEMS:', *eq_elementary_symbols, sep='  ')
        print('EQ LATIN:', *eq_latin_symbols, sep='  ')
        print('EQ GREEK:', *eq_greek_symbols, sep='  ')
        print('IC ELEMS:', *ic_elementary_symbols, sep='  ')
        print('IC LATIN:', *ic_latin_symbols, sep='  ')
        print('IC GREEK:', *ic_greek_symbols, sep='  ')
        print('ALL TRANSLATED GREEK:', *translated_greek, sep='  ')
        print()
        print(32*'-' + ' END INPUTPARSER DEBUG INFORMATION ' + 32*'-')
    
    return (changed, changed_ic, variable_symbol[0], function_symbol[0], elementary_function_symbols, latin_parameter_symbols, translated_greek)

