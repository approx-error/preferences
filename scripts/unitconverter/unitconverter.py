# Unit converter
# https://docs.scipy.org/doc/scipy/reference/constants.html#module-scipy.constants

# System module imports
import sys

# Custom module imports
import converter as conv

# Main function
def main(cmd_args) -> str:
    value_error = 'Value is not a valid number.'
    value_sig_fig_error = 'Value and/or significant figures are not valid numbers.'
    invalid_argument_count = '''
Invalid number of input arguments.

Usage: 

[dimension] [value] [cur prefix] [cur unit] to [opt:target prefix] [opt:target unit] [opt:significant figures]

Write "-" to leave prefix, unit, and/or significant figures blank if applicable.

If no target prefix or unit is provided but instead the number of significant figures is written after 'to',
the input value will be truncated to the specified precision


Example: Convert 2000 mJ to keV with default sig figs:
E 2000 m J to k eV 

Example: Convert 15000000000 Pa to GPa with 3 sig figs:
p 15000000000 - Pa to G Pa 3

Example: Convert 1543.234 to 2 sig figs:
U 1543.234 - - to 2
'''
    if len(cmd_args) == 8:
        try:
            category = cmd_args[0]
            value = float(cmd_args[1])
            prefix = cmd_args[2]
            unit = cmd_args[3]
            arrow = cmd_args[4]
            target_prefix = cmd_args[5]
            target_unit = cmd_args[6]
            sig_figs = int(cmd_args[7])
        except ValueError:
            return value_sig_fig_error
        
        result = conv.convert_unit(value, [category, prefix, unit], [category, target_prefix, target_unit], sig_figs)

    elif len(cmd_args) == 7:
        try:
            category = cmd_args[0]
            value = float(cmd_args[1])
            prefix = cmd_args[2]
            unit = cmd_args[3]
            arrow = cmd_args[4]
            target_prefix = cmd_args[5]
            target_unit = cmd_args[6]
        except ValueError:
            return value_error        

        result = conv.convert_unit(value, [category, prefix, unit], [category, target_prefix, target_unit])

    elif len(cmd_args) == 6:
        try:
            category = cmd_args[0]
            value = float(cmd_args[1])
            prefix = cmd_args[2]
            unit = cmd_args[3]
            arrow = cmd_args[4]
            sig_figs = int(cmd_args[5])
        except ValueError:
            return value_sig_fig_error

        result = conv.convert_unit(value, [category, prefix, unit], [], sig_figs)

    else:
        return invalid_argument_count 

    return result

# Main block:
if __name__ == '__main__':
    result = main(sys.argv[1:])
    print(result)
