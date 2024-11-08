# Count the number of lines of text in a project directory if a flag is provided, the program
# will go through the directories recursively

import sys
import subprocess
import glob

flags = sys.argv[1:]

output = True

if not flags:
    output_str = 'Lines of text in current directory excluding hidden files:'
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
        non_binary = subprocess.run(['grep', '-lI', '.', file], capture_output=True, text=True)
        nb_files += non_binary.stdout
else:
    match flags:
        case ['-h'] | ['--hidden']:
            output_str = 'Lines of text in current directory including hidden files'
            dir_contents = subprocess.run(['ls', '-ap'], capture_output=True, text=True)
            only_files = subprocess.run(['grep', '-v', '/'], capture_output=True, text=True, input=dir_contents.stdout)
            file_list = only_files.stdout.split('\n')
            if file_list[-1] == '':
                del file_list[-1]
            nb_files = ''
            for file in file_list:
                non_binary = subprocess.run(['grep', '-lI', '.', file], capture_output=True, text=True)
                nb_files += non_binary.stdout
        case ['-r'] | ['--recursive']:
            output_str = 'Lines of text in current directory and all subdirectories excluding hidden ones:'
            # Search for the wildcard '.' pattern in all non-binary files recursively and return the filename if the pattern is found
            # Effectively returns a list of all the non-binary files within the directory and its subdirectories
            # The `ls` makes sure that only non-hidden directories and files are listed. FIXME: This only applies on the first directory level
            nb_files = ''
            cd_files = glob.glob('*')
            for file in cd_files:
                non_binary = subprocess.run(['grep', '-rlI', '.', file], capture_output=True, text=True)
                nb_files += non_binary.stdout
            print(nb_files)
        case ['-r', '-h'] | ['-h', '-r'] | ['--recursive', '--hidden'] | ['--hidden', '--recursive']:
            output_str = 'Lines of text in current directory and all subdirectories including hidden ones:'
            non_binaries = subprocess.run(['grep', '-rlI', '.'], capture_output=True, text=True)
            nb_files = non_binaries.stdout
            print(nb_files)
        case _:
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
    print('\nUSAGE:\n\nlinec [OPTIONAL FLAGS]\n\nFLAGS:\n\n -r, --recursive: list lines in subdirectories as well\n -h, --hidden: include hidden files and directories.\
\n\nNOTE: Hidden files and directories are currently only ignored in the starting directory')
