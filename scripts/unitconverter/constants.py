# Constants for the unit conversions

import scipy.constants as cts


# Basic constants in SI-units:
CONSTANTS = {'mu0': cts.mu_0, 'eps0': cts.epsilon_0, 'h': cts.Planck, 'hbar': cts.hbar, 
             'G': cts.gravitational_constant, 'R': cts.gas_constant, 'alpha': cts.fine_structure,
             'k': cts.Boltzmann, 'stefboltz': cts.Stefan_Boltzmann, 'wien': cts.Wien, 'rydbg': cts.Rydberg}
# Unitless
UNITLESS = {'-': 1}

# Amount units
AMOUNT = {'-': 1, 'mol': cts.Avogadro}

# Mass units
MASS = {'-': 1, 'kg': 1, 'g': cts.gram, 't': cts.metric_ton, 'u': cts.atomic_mass, 
        'ME': 5.9722e24, 'MS': 1.988416e30, 'MM': 7.346e22,
        'me': cts.electron_mass, 'mp': cts.proton_mass, 'mn': cts.neutron_mass}

# Length units
LENGTH = {'-': 1, 'm': 1, 'au': cts.astronomical_unit, 'ly': cts.light_year, 'pc': cts.parsec, 
        'RE': 6.371e6, 'RS': 6.957e8, 'RM': 1.7374e6}

# Angle units
ANGLE = {'-': 1, 'rad': 1, 'deg': cts.degree, 'arcmin': cts.arcminute, 'arcsec': cts.arcsecond}

# Time units
TIME = {'-': 1, 's': 1, 'min': cts.minute, 'h': cts.hour, 'd': cts.day, 'w': cts.week, 'a': cts.year, 'Ja': cts.Julian_year}

# Area units
AREA = {'-': 1, 'm^2': 1, 'ha': 10000}

# Volume units
VOLUME = {'-': 1, 'm^3': 1, 'l': cts.liter}

# Density
DENSITY = {'-': 1, 'kg/m^3': 1, 'g/cm^3': 1000}

# Temperature units
TEMPERATURE = {'-': 1, 'K': 1}

# velocity units
VELOCITY = {'-': 1, 'm/s': 1, 'km/h': cts.kmh, 'c': cts.speed_of_light, 'mach': cts.speed_of_sound, 'knot': cts.knot}

# Acceleration unit
ACCELERATION = {'-': 1, 'm/s^2': 1, 'g': cts.g}

# Force units
FORCE = {'-': 1, 'N': 1}

# Pressure units
PRESSURE = {'-': 1, 'Pa': 1, 'atm': cts.atmosphere, 'bar': cts.bar, 'mmHg': cts.mmHg}

# Energy units
ENERGY = {'-': 1, 'J': 1, 'eV': cts.electron_volt, 'cal': cts.calorie, 'kWh': 3.6e6}

# Power units
POWER = {'-': 1, 'W': 1, 'hp': cts.horsepower}

# Electric charge
CHARGE = {'-': 1, 'C': 1, 'e': cts.elementary_charge}

# Prefixes
PREFIXES = {'f': cts.femto, 'p': cts.pico, 'n': cts.nano, 'µ': cts.micro, 'm': cts.milli, 'c': cts.centi, 'd': cts.deci, '-': 1,
            'da': cts.deka, 'h': cts.hecto, 'k': cts.kilo, 'M': cts.mega, 'G': cts.giga, 'T': cts.tera, 'P': cts.peta}

# Categories:

CATEGORIES = {'C': CONSTANTS, '-': UNITLESS, 'n': AMOUNT, 'm': MASS, 'l': LENGTH, '<': ANGLE, 't': TIME, 'A': AREA, 'V': VOLUME, 'D': DENSITY, 'T': TEMPERATURE,
        'v': VELOCITY, 'a': ACCELERATION, 'F': FORCE, 'p': PRESSURE, 'E': ENERGY, 'P': POWER, 'Q': CHARGE, 'pref': PREFIXES}

