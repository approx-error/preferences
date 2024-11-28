# Example of using the warnings module to catch
# np.loadtxt():ts file empty warning


import numpy as np
import warnings

def load_data_file(path):
    '''
    Loads data from file into a numpy array
    '''
    file_data = np.array([])
    error_msg = ''
    with warnings.catch_warnings():
        warnings.filterwarnings('error')
        try:
            try:
                file_data = np.loadtxt(path, dtype = str, comments = '#', delimiter = '\t', skiprows = 1)
            except FileNotFoundError:
                error_msg = 'file not found'
        except Warning as e:
            # print('WARNING OCCURED:', e)
            error_msg = 'file empty'

    # If the data only contains 1 row, reshape it to force it to be 2d
    if file_data.ndim == 1:
        file_data = file_data.reshape(1, len(file_data))

    return file_data, error_msg
