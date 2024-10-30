# ODE solver and plotter 

import numpy as np
import matplotlib.pyplot as plt
import random
import sympy as sp

plt.rcParams.update({'text.usetex': True})

# FIXME: SUBSTITUTING VALUES DOES NOTHING AND THUS PLOTTING IS IMPOSSIBLE

def solve_and_plot(translated_input, debug=False):

    # Solve the ODE
    parameters = translated_input[0]
    variable = translated_input[1]
    function = translated_input[2]
    equation = translated_input[3]
    initial_conditions = translated_input[4]
    
    '''
    print('BEGIN DEBUG')
    print(sp.srepr(parameters))
    print(sp.srepr(variable))
    print(sp.srepr(function))
    print(sp.srepr(equation))
    print(sp.srepr(initial_conditions))
    print('END DEBUG')
    '''

    if initial_conditions:
        solution = sp.dsolve(equation, ics=initial_conditions)
    else:
        solution = sp.dsolve(equation)



    # Show solution to user

    print('Equation to solve:')
    sp.pprint(equation)
    print()
    print('Sympy\'s classification for the equation:')
    sp.pprint(sp.classify_ode(equation))
    print()
    if initial_conditions:
        print('Initial conditions:')
        sp.pprint(initial_conditions)
        print()
    print('Solution:')
    sp.pprint(solution)
    print()
    print('Latex:')
    sp.pprint(sp.latex(solution))
    print()

    return # NOTE: This is here to stop the plotting code from running since it doesn't work
    # Plot sample solutons

    solutions_substituted = []
    # Substitute in random sample values from [-1, 1] for all constants:
    
    sub_lists = [[], [], []]
    for i in range(3):
        for param in parameters:
            random_sample = round(random.choice([-1, 1]) * random.random(), 4)
            sp.pprint(solution.rhs.subs([(variable, 0)]))
            sub_lists[i].append((parameters[param], random_sample))
        solutions_substituted.append(solution.rhs.subs(sub_lists[i]))

    
    plot_title = f'${sp.latex(solution)}$   A sampling of three solution graphs'
    plot_xlabel = f'${sp.latex(variable)}$'
    plot_ylabel = f'${sp.latex(function(variable))}$'

    fig, ax = plt.subplots(figsize = (7, 7), tight_layout=True)
    x_var = np.linspace(-1, 1, 100)

    ax.set_title(plot_title, fontsize=15, pad=10.0)
    ax.set_xlabel(plot_xlabel, fontsize=15, loc='right')
    ax.set_ylabel(plot_ylabel, fontsize=15, labelpad=6.0, loc='top')
    #ax.set_aspect('equal')
    ax.grid(True, which='both')

    # set the x-spine
    ax.spines['left'].set_position('zero')
    # turn off the right spine/ticks
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    # set the y-spine
    ax.spines['bottom'].set_position('zero')
    # turn off the top spine/ticks
    ax.spines['top'].set_color('none')
    ax.xaxis.tick_bottom()

    # Add arrows to the axes
    ax.plot(1, 0, ">k", transform=ax.get_yaxis_transform(), clip_on=False)  
    ax.plot(0, 0, "<k", transform=ax.get_yaxis_transform(), clip_on=False)  
    ax.plot(0, 1, "^k", transform=ax.get_xaxis_transform(), clip_on=False)
    ax.plot(0, 0, "vk", transform=ax.get_xaxis_transform(), clip_on=False)

    # Evaluate substituted expressions and plot them
    if solutions_substituted:
        for i in range(3):
            substitutions = str()
            for sub in sub_lists[i]:
                substitutions += f'{sub[0]}: {sub[1]} '
                y_var = np.array([sp.N(sp.re(solutions_substituted[i].subs(variable, x))) for x in x_var])
                print(y_var)
                ax.plot(x_var, y_var, label=substitutions)
    else:
        name = f'{function}({variable})'
        sp.pprint(solution.rhs)
        temp_y = [sp.N(solution.rhs.subs(variable, num)) for num in range(10)]
        y_var = np.array(temp_y)
        ax.plot(x_var, y_var, label=name)

    ax.legend()
    plt.show()
