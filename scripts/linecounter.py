# Count the number of lines of text in a project directory if a flag is provided, the program
# will go through the directories recursively

import sys
import subprocess

flags = sys.argv[1:]

output = True

if not flags:
    output_str = 'Lines of text in current directory:'
    # List directory contents with slashes denoting directories and filter
    # out anything containign a slash thus leaving just the files
    # After that filter the files so that only non-binary files remain
    dir_contents = subprocess.run(['ls', '-p'], capture_output=True, text=True)
    only_files = subprocess.run(['grep', '-v', '/'], capture_output=True, text=True, input=dir_contents.stdout)
    file_list = only_files.stdout.split('\n')
    if file_list[-1] == '':
        del file_list[-1]
    nb_files = ''
    for file in file_list:
        non_binary = subprocess.run(['grep', '-lI', '.', f'{file}'], capture_output=True, text=True)
        nb_files += non_binary.stdout
elif flags and flags[0] in ['-r', '--recursive']:
    output_str = 'Lines of text in current directory and all subdirectories:'
    # Search for the wildcard '.' pattern in all non-binary files recursively and return the filename if the pattern is found
    # Effectively returns a list of all the non-binary files within the directory and its subdirectories
    non_binaries = subprocess.run(['grep', '-rlI', '.'], capture_output=True, text=True)
    nb_files = non_binaries.stdout
else:
    output = False

if output:
    nb_list = nb_files.split('\n')
    if nb_list[-1] == '':
        del nb_list[-1]

    all_file_contents = ''
    for file in nb_list:
        single_file_contents = subprocess.run(['cat', f'{file}'], capture_output=True, text=True)
        all_file_contents += single_file_contents.stdout

    lines_counted = subprocess.run(['wc', '-l'], capture_output=True, text=True, input=all_file_contents)
    line_count = lines_counted.stdout.strip('\n')
    print(output_str, line_count)
else:
    print('\nUSAGE:\n\nList lines of text in current directory:\nlinec\n\nList lines of text in current directory and all subdirectories:\nlinec [-r | --recursive]\n')
