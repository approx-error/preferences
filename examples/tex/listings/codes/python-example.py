# Low-pass filter circuit

# Modules
import math

# Constants
FREQ_MEASUREMENT = 6e4 # Hertz
FREQ_NOISE = 2e6 # Hertz
VOLT_IN = 0.03 # Volts

# Requirements
MEASUREMENT_RATIO_MIN = 0.9
MEASUREMENT_RATIO_MAX = 1
NOISE_RATIO_MAX = 0.1

# Values to try for capacitance and resistance
CAP_VALUES = [1e-9, 1e-8, 1e-7, 1e-6, 1e-5, 1e-4, 1e-3, 1e-2, 1e-1] # Farads
RES_VALUES = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] # Ohms

# Amplitude of output voltage as function of frequency, capacitance and resistance
def volt_out(freq, cap, res):
    return VOLT_IN / math.sqrt(1 + (2 * math.pi * freq * cap * res) ** 2)

# Try all values of capacitance and resistance and print a notification if
# combination that satisfies all requirements is found
for c in CAP_VALUES:
    for r in RES_VALUES:
        volt_m_out = volt_out(FREQ_MEASUREMENT, c, r)
        m_ratio = volt_m_out / VOLT_IN
        volt_n_out = volt_out(FREQ_NOISE, c, r)
        n_ratio = volt_n_out / VOLT_IN
        if MEASUREMENT_RATIO_MIN <= m_ratio <= MEASUREMENT_RATIO_MAX and n_ratio <= NOISE_RATIO_MAX:
            print('Solution found!')
            print(f'C = {c} Farads and R = {r} Ohms')
            print(f'Measurement signal dampening ratio: {m_ratio:6.4f}')
            print(f'Noise signal dampening ratio: {n_ratio:6.4f}')
            print()
        


