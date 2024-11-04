# ODE solver using sympy as a backend

import sys

import inputparser as ip
import translator as tr
import solverplotter as sp


def main(cmd_arguments):

    usage_str ='''\
This ODE solver will try to solve a given ODE using sympy's dsolve()-function as a backend.
Once executed correctly, the requested equation will be shown along with its classification and
the initial conditions given (if they were given). Next the equation will be solved and a solution
will be printed in an easy-to-read format as well as in a LaTeX format. Finally a plot will be drawn
with three sample solutions that solve the given equation.

USAGE:

ode [flags] "[equation], [initial_cond1], [initial_cond2]"

FLAGS:

-h or --help to print this helpsheet

-v or --version to print the version

-np or --no-plot to disable plotting the solution 

-e=EQUATION or --equation=EQUATION to make ode solve a sample equation thats already stored in memory.
Current list of sample equations:

    - basic: f'(x) = f(x)
    - harmonic: f''(x) = -{ome}^2f(x)
    - cauchy_euler: x^2f''(x) + axf'(x) + by = 0
    - bessel: x^2f''(x) + xf'(x) + (x^2 - {alp}^2)f(x) = 0
    - legendre: (1 - x^2)f''(x) - 2xf'(x) + n(n + 1)f(x) = 0

-d or --debug to display debugging information when solving equations



NOTATION:
- Derivatives are denoted by single quotes: '. This means that if one uses single
  quotes as string delimiters, the derivatives have to be escaped: \\'. A better
  solution is to use double quotes " as string delimiters. That way derivatives
  don't need to be escaped.
- A function's variable must be explicitly included if one wishes to choose one. 
  If it is not included, the symbol x will be used as the variable unless x is the
  function in which case u will be used instead
- A single term (ie. ay''(x), sin(x), b^2tan(z), etc.) CANNOT contain spaces
- Arithmetic symbols that separate terms (-, +, =) MUST be padded on both sides 
  by a SINGLE space. Examples: CORRECT: ay' + by = 0, INCORRECT: ay'(x)+by(x)=0, INCORRECT: ay'(x)+   by(x)  = 0
- Terms can be grouped using normal parentheses or square brackets. Curly braces are reserved for greek letters.
  Examples: CORRECT: (ax+b)^2y''(x), CORRECT: [ax+b]^2y''(x), INCORRECT: {ax+b}^2y''(x)
- Greek letters can be used as variables, functions and parameters and are denoted by the first three letters in their english names unless
  they only contain two letters. The letters must be placed inside curly braces.
  Examples: {alp} = alpha, {xi} = xi, {Sig} = capital sigma, {Nu} = capital nu
- Subscripts are denoted with an underscore and can only contain one number. Examples: y_0, {ome}_1
- Builtin functions that are supported include: normal and hyperbolic trig and their inverses, exp(), ln() = log(), sqrt(), cbrt()

EXAMPLES:

Providing initial conditions:
ode "ay''(x) = -{ome}_0y(x), y(0) = 0, y'(0) = 1"

Not providing initial conditions:
ode "ay''(x) - bxy'(x) + sin(x) = 4"

Not providing a variable:
ode "ay' + y = 0"

Not plotting:
ode --no-plot "ay' + y = 0"

Solving the cauchy euler equation

ode --equation=cauchy_euler

KNOWN BUGS:

Numbers that are inside parentheses might not get appended with multiplication signs.
'''

    EQUATIONS = {'basic': "f'(x) = f(x)", 'harmonic': "f''(x) = -{ome}^2f(x)", 'cauchy_euler': "x^2f''(x) + axf'(x) + by = 0", 
                 'bessel': "x^2f''(x) + xf'(x) + (x^2 - {alp}^2)f(x) = 0", 'legendre': "(1 - x^2)f''(x) - 2xf'(x) + n(n + 1)f(x) = 0"}
    DEBUG = False
    PLOT = True
    input_to_parse = ''
    if len(cmd_arguments) == 0: 
        print(usage_str)
        return
    flags = [arg for arg in cmd_arguments if arg[0] == '-']
    if flags:
        if '-h' in flags or '--help' in flags:
            print(usage_str)
            return
        if '-v' in flags or '--version' in flags:
            print('ode version 0.1.0')
            return
        if '-d' in flags or '--debug' in flags:
            DEBUG = True
        if '-np' in flags or '--no-plot' in flags: 
            PLOT = False
        for flag in flags:
            if '-e' in flag or '--equation' in flag:
                equality = flag.find('=')
                equation = flag[equality+1:]
                if equation in EQUATIONS:
                    input_to_parse = EQUATIONS[equation]
                    break
                else:
                    print('Equation name not recognized! Please try again.')
                    return

    if not input_to_parse:
        input_to_parse = cmd_arguments[-1]

    parsed_input = ip.inputparse(input_to_parse, debug=DEBUG)
    translated_input = tr.translate(parsed_input, debug=DEBUG)
    sp.solve_and_plot(translated_input, debug=DEBUG, plot=PLOT)
    return


if __name__ == '__main__':
    # Get the command line arguments
    cmd_arguments = sys.argv[1:] # The first item in argv is the path to the current script which isn't needed
    main(cmd_arguments)
    # Call main with different examples
    #main(['--debug', "2xsin(a)y''(x) + cos(b)y'(x) + c = {ome}{lam}y(x), y(0) = exp(p), y'(0) = q{mu}"])
    #main(['--debug', "2xsin(a)y''(x) + cos(b)y'(x) + c = {ome}{lam}y(x)"])
    # Basic
    #main(['--debug', "f'(x) = a*f(x), f(0) = 1"])
    # Harmonic oscilator
    #main(['--debug', "f''(x) = -{ome}^2f(x), f(0) = 1, f'(0) = 0"])
    # Bessel equation
    #main(['--debug', "x^2f''(x) + xf'(x) + (x^2 - {alp}^2)f(x) = 0"])
    #main("2ay''(x) + by'(x) = 0, y(0) = a, y(b) = 1")
    #main("2ay''(x) + by'(x) = sin(x), y(0) = 0, y'(0) = 1")
    #main("y'' = {ome}_0^2y")
    #main("a*sin(x) + {Gam}y'' - (x+b)^2y' = y - exp({gam}) + exp({zet})")
    #main("[abc*F''(z)+ln(z)]F'(z) + 2*{ome}_0F = [ag*h]^2 + 5, sin(2*a^2) = 0, cos(2*b) = 5, F'(0) = {ome}_0")
    #main("a_1b_3y_5'(x_0) + {gam}_4{lam}_5a_2y_5''(x_0) = sin({pi})")
    #main("(a_1/b_3)y_5'(x_0) + {gam}_4{lam}_5a_2y_5''(x_0) = 0, y_5(5) = sin({pi}/2), y_5''(0) = a_2")
