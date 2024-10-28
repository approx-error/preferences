# Conversion functions

import constants as cts

def significant_figures(value: float) -> int:
    '''
    Returns the number of significant figures in a given number
    '''
    string_value = str(value)
    number_count = len(string_value) - 1
    sig_figs = 0
    converted = False
    non_zero_found = False

    if '.' not in string_value:
        for i in range(number_count + 1):
            non_zero_found = False
            if string_value[i] != '0':
                sig_figs += 1
            else:
                for j in string_value[i+1:]:
                    if j != '0':
                        non_zero_found = True
                        break
                if non_zero_found:
                    sig_figs += 1
                else:
                    break
    else:
        for i in range(1, number_count):
            converted = False
            test = f'{value:.{i}g}'
            if 'e' in test:
                converted = True
                test = f'{value:.{i}f}'
            if test == string_value:
                if converted:
                    sig_figs = i + len(str(int(float(test))))
                else:
                    sig_figs = i
                break
    return sig_figs 

def parse_unit(unit_to_parse: list[str]) -> list[int]:
    category = unit_to_parse[0]
    prefix = unit_to_parse[1]
    unit = unit_to_parse[2]
    try:
        category_value = cts.CATEGORIES[category]
        prefix_value = cts.PREFIXES[prefix]
        unit_value = category_value[unit]

    except KeyError:
        return [0, 0]

    return [prefix_value, unit_value]
                
def convert_unit(value: float, unit: list[str], target_unit: list[str], sig_figs: int = 5) -> str:
    '''
    Convert a value expressed in one unit to some other unit.
    For example m/s -> km/h, eV -> kWh, W -> GW, Pa -> mmHg
    '''
    if target_unit == []:
        if unit[1] == '-':
            unit[1] = ''
        if unit[2] == '-':
            unit[2] = ''
        return f'{value:.{sig_figs}g} {unit[1]}{unit[2]}'

    parsed_unit = parse_unit(unit)
    prefix_value = parsed_unit[0]
    si_conversion_factor = parsed_unit[1]
    
    parsed_target_unit = parse_unit(target_unit)
    target_prefix_value = parsed_target_unit[0]
    target_conversion_factor = parsed_target_unit[1]

    new_value = value * prefix_value * si_conversion_factor / target_conversion_factor / target_prefix_value

    if target_unit[1] == '-':
        target_unit[1] = ''
    if target_unit[2] == '-':
        if unit[2] == '-':
            target_unit[2] = ''
        else:
            target_unit[2] = unit[2]
    return f'{new_value:.{sig_figs}g} {target_unit[1]}{target_unit[2]}'

