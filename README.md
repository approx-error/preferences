# approx-error/preferences

A repository of preferences, templates, customization files, small scripts, example files and cheat sheets I have found useful. 
These mostly consist of [Vim](https://www.vim.org/) and bash configuration files, [ultisnips](https://github.com/SirVer/ultisnips) snippets and LaTeX commands.
There are also some example files and cheat sheets for correct syntax when using certain tools/languages (fortran and makefiles) that I keep coming back to for reference so might as well put them here.
Finally I've included some small useful scripts I've written that I keep using. I don't expect anyone else to find a use for these but in case someone does, they will be waiting here.

## Usage

I've decided to split this section on usage into sections. Each section is a self-contained tutorial on how to setup a certain aspect of the repository
on your system correctly. You don't need things from another section in order to setup a given section. The first section is dedicated to getting the Vim setup contained in this repository working. The
second section does the same as the first but for the bash and python setup. The third section is there to remind you that everyting elese in this repository is meant to be read or simply works out of the box.
IMPORTANT: Using this setup as is will require you to either move, delete or rename some of your existing files or merge them with the ones in this repository. Make sure that you don't lose your own precious
configuration files by copying them somewhere safe before doing anything else. Only if you like the configuration files in this repository and they function properly, should you consider deleting your old ones.

### Using the Vim setup

The Vim setup contained in this directory has a general philosophy of "don't fit Vim to your needs, fit your needs to Vim". The reasons for this philosophy are twofold. 1) I'm a relative Vim beginner
who isn't that comfortable with changing a bunch of settings in Vim that I don't fully understand. Vim is a very robust editor written by talented programmers so doing stuff the way Vim does them by default is 
probably a good idea. 2) I prefer setups that don't require you to change a bunch of settings in Vim for them to be functional. If I'm setting up Vim on a new computer, I want the setup to work without having to
configure a bunch of stuff (That's what the setup is made for).

This Vim setup uses (and actually contains) the [vim-plug](https://github.com/junegunn/vim-plug) plugin manager and the following tutorial assumes you do aswell.
To see a list of all the vim related files this repo contains, see the section entitled 'Currently included files'
If you use another plugin manager, you'll have to change this setup accordingly to fit your needs. If you follow the tutorial you might also
need to move around some of your existing configuration files but that shouldn't be too much of a hassle.

Without further ado here is how to use this setup:

1. Clone this repository to your home directory (ie. ~/) by running

```sh
git clone https://github.com/approx-error/preferences.git
```

2. If you're using a .vimrc file and it is located in your home directory, either delete it, merge it with the vimrc file in this repository or move it somewhere else if you want to preserve it

3. Create a symbolic link to the vimrc file in ~/preferences/vim/ under the name .vimrc in your home directory by running:

```sh
ln --symbolic ~/preferences/vim/vimrc ~/.vimrc
```

Alternatively you can create the symbolic link to a file called ~/.vim/vimrc since vim also knows to search for the vimrc file there:

```sh
ln --symbolic ~/preferences/vim/vimrc ~/.vim/vimrc
```

What this essentially does is create a "file" called .vimrc (or vimrc) which is actually a link to the vimrc file contained in this repository. This is done so that you don't have to change the
default location where Vim searches for the .vimrc (vimrc) file. Instead you can let Vim search for it in the default location and simply link the default location to somewhere else. This is especially convenient
if you, like me, have a github repository containing your preferences. Since the files being edited in the repo and the files being used by Vim are exactly the same there is no need for copying and
moving files around.

4. Make sure your ~/.vim directory does not contain the following directories: autoload, ftplugin and plugged. If any of these directories exist,
either delete them (if you don't need / don't want to use their contents), move their contents to the corresponding directories in ~/preferences/vim/ (if you want to keep using them)
or move them to some other directory (if you don't want to lose them but also don't want to use them).

5. Create symbolic links to the directories mentioned in step 4 in the ~/.vim/ directory by running:

```sh
ln --symbolic ~/preferences/vim/autoload ~/.vim
```

```sh
ln --symbolic ~/preferences/vim/ftplugin ~/.vim
```

```sh
ln --symbolic ~/preferences/vim/plugged ~/.vim
```

This has the same motivation as step 3 where we're letting Vim search for these directories in the default place and linking them so somewhere else.

6. Start Vim and run `:PlugInstall` to make vim-plug install the plugins

7. Create a directory for your .viminfo file according to the line 'set viminfo=...' in the vimrc file:

```sh
mkdir ~/.local/state/vim/
```

8. Rename and move your .viminfo file to the directory you just made:

```sh
mv ~/.viminfo ~/.local/state/vim/viminfo
```

Vim will now write all vim info there instead of to a file in your home directory making it less cluttered.

Now you're all set to begin using the setup! For specific tutorials on how the plugins and snippets actually work, I recommend [this fantastic tutorial](https://ejmastnak.com/tutorials/vim-latex/intro/) 
by Elijan Mastnak on supercharged mathematical typesetting. It covers the vim-plug plugin manager, the vimtex and ultisnips plugins and much, much more. Another great resource for awesome latex snippets is Gilles Castel's
[comprehensive article](https://castel.dev/post/lecture-notes-1/) on taking lecture notes with vim.

### Using the Bash setup and making the pythonrc file work

This repository contains rc-files for bash which so in order to use them you'll need to create symbolic links to each of them in your home directory. (Read the explanation and justification for this in the Vim setup section)
Note that the bashrc file contained in this repository defines a lot of different environment variables which will change where a lot of programs save certain files
so carefully look through the bashrc file to make sure there isn't anything defined that might break your system. The reason for a lot of these environment variables
is that I try to keep my home directory as decluttered as possible and so I have defined environment variables according to the [XDG Base Directory Specification](https://specifications.freedesktop.org/basedir-spec/latest/)
which has a goal of making programs not use the home directory as a dumping ground for their configuration files, cache files, and state files.
I really like this idea and so I have defined my environment variables according to the aforementioned specification. Currently the bashrc file redefines the path of the following files:

- ~/.bash\_history  -->  ~/.local/state/bash/bash-history
- ~/.lesshst --> ~/.local/state/less/less-history
- ~/.python\_history --> ~/.local/state/python/python-history
- ~/.gtkrc-2.0 --> ~/.config/gtk-2.0/gtkrc
- My custom pythonrc file, which doesn't exist by default: ~/.config/python/pythonrc.py

If any of these files currently exist on your system or you are already using some sort of python rc-file and you want to keep them, either move them somewhere else
or move them to the aforementioned new locations so that the programs will keep writing to them once you setup the bashrc in this repository. Speaking of which, here is how to do it:
 
1. If you alread cloned this repo when setting up Vim you can skip this but if not, run this in your home directory:

```sh
git clone https://github.com/approx-error/preferences.git
```

2. Make the state and config directories required:

```sh
mkdir ~/.local/state/bash ~/.local/state/less ~/.local/state/python ~/.config/gkt-2.0 ~/.config/python
```

3. Renane the files to match the filenames specified in the bashrc and move them to their new locations
(These commands are assuming the files are stored in the home directory):

```sh
mv .bash_history ~/.local/state/bash/bash-history
mv .lesshst ~/.local/state/less/less-history
mv .python_history ~/.local/state/python/python-history
mv .gtkrc-2.0 ~/.confic/gtk-2.0/gtkrc
```

4. Configure the actual bashrc (and bash\_profile and bash\_logout) and pythonrc files by making sure your own bash and python related
rc files are safe or merged with mine, and are NOT stored in your home directory. The configuration is done similarly to the vimrc file by making symbolic links:

```sh
ln --symbolic ~/preferences/bash/bashrc ~/.bashrc
ln --symbolic ~/preferences/bash/bash_profile ~/.bash_profile
ln --symbolic ~/preferences/bash/bash_logout ~/.bash_logout
ln --symbolic ~/preferences/python/pythonrc.py ~/.config/python/pythonrc.py
```

5. Source the new bashrc and thus update environment variables etc. by running:

```sh
source ~/.bashrc
```

6. Just for good measure exit and restart terminal to make sure everything is reset.

7. Test that the configuration works by running for example the python interpreter typing some commands and making sure that these commands
were no written to a file called ~/.python\_history but to the python-history file in ~/.local/state/python/

Now everything should work as intended. Finally a quick note on the pythonrc.py file. This file's function (currently) is to force python to write it's history
to ~/.local/state/python as defined in the bashrc. If this python file didn't exist and you were running a python version between 3.4 and 3.12 inclusive (I'm currently on python 3.12),
python would ignore the PYTHON\_HISTORY environment variable in the bashrc and keep writing history to ~/.python\_history.
(I don't know what python did before 3.4 but the PYTHON\_HISTORY feature wasn't implemented back then). Since python 3.13, the user can now define the environment PYTHON\_HISTORY to make
python save history in a specified location but since python 3.13 has yet to be packaged as a stable build which supports external modules (such as numpy and sympy which I use a lot),
I have to stay in python 3.12. Eventually I'll be able to switch and the pythonrc will only be there in case I need to run older python versions but for now it is a very important file indeed.

### All the other stuff

Everything else in this repository (ie. examples, scripts and tex files) is meant for reading and the scripts can
be executed provided you have the correct language interpreter/compiler. There is no need to configure any of these
for you to be able to use them.

## Currently included files

### Vim files

- My .vimrc file (vimrc)
	- Basic highlighting, colorscheme, numbering, indenting, pasting and pathing settings 
	- Plugin specific settings
- The [vim-plug](https://github.com/junegunn/vim-plug) plugin manager (autoload/plug.vim)
- The plugins I use (plugged/)
    - [nerdtree](https://github.com/preservim/nerdtree)
    - [numbers.vim](https://github.com/myusuf3/numbers.vim)
    - [vimtex](https://github.com/lervag/vimtex)
    - [ultisnips](https://github.com/SirVer/ultisnips)
- Filetype specific configuration files (ftplugin/)
	- Python (Set the tab width to 4 spaces since that is required by python)
	- Fortran (Set the tab width to 2 spaces. I prefer this look in fortran programs)
    - GNU Make (Make tabs expand as tabs, not spaces. Makefile requires this.)
- Lots of snippets for the ultisnips plugin (my-snippets/)
	- General snippets (all.snippets)
    - TeX snippets
    - Python snippets
    - Fortran snippets
    - GNU Make snippets
	- Snippets for making new snippets (snippets.snippets)
	- Vimscript snippets (TBA)
    - Shell script snippets (TBA)
    - HTML snippets (TBA)
    - CSS snippets (TBA)
    - Javascript snippets (TBA)

### Bash files

- My .bashrc file (bashrc)
    - The stuff that was already there once I started editing it
    - A rainbow-colored stegosaurus that says a fortune everytime you open bash (requires the following packages: fortune, figlet, cowsay and lolcat)
    - Some alias definitions (especially note the 'sympy' alias which calls one of the scripts included in this repository)
    - A lot of environment variables to make various programs save files to specified places and make tex be able to find packages

### Python files

- My python startup file (pythonrc.py)
    - Currently makes it so that python versions 3.4 - 3.12 inclusive can save python interpreter history to some non-default location
(Read the beginning of the section using the bash setup for my file location philosophy and the very end of that same section for what's going on with python 3.4 to 3.12 and why I'm not yet using
python 3.13 even though it fixes this problem)

### TeX files

- Custom Latex math commands I keep needing (These commands are also recognized by the TeX snippets for a smoother LaTeX experience)

### Scripts

- A simple python script to initiate a sympy session in terminal for symbolic calculations

### Examples

- Fortran
    - A fortran program that illustrates some correct fortran syntax
- GNU Make
    - An example of a makefile that compiles a fortran program from many sources
    - A makefile cheat sheet markdown file
- A markdown file containing some specific terminal/programming related problems I've run into and how I managed to fix them

## License

Distributed under the GPL-3.0 license which can be found in the file called 'LICENSE'

## Author

approx-error

2024

