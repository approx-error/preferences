# approx-error/preferences

A repository of preferences, templates, customization files and small scripts I have found useful. 
These mostly consist of [Vim](https://www.vim.org/) configuration files, [ultisnips](https://github.com/SirVer/ultisnips) snippets and LaTeX commands.
There are also some example files for correct syntax when using certain tools/languages that I keep coming back to for reference so might as well put them here.
I don't expect anyone else to find a use for these but in case someone does, they will be waiting here.

## Usage

I've decided to split this section on usage into two sections. The first section is dedicated to getting the Vim setup cotained in this repository working. 
The second section is dedicated to the usage of all the other stuff in this repository

### Using the Vim setup

The Vim setup contained in this directory has a general philosophy of "don't fit Vim to your needs, fit your needs to Vim". The reasons for this philosophy are twofold. 1) I'm a relative Vim beginner
who isn't that comfortable with changing a bunch of settings in Vim that I don't fully understand. Vim is a very robust editor written by talented programmers so doing stuff the way Vim does them by default is 
probably a good idea. 2) I prefer setups that don't require you to change a bunch of settings in Vim for them to be functional. If I'm setting up Vim on a new computer, I want the setup to work without having to
configure a bunch of stuff (That's what the setup is made for).

This Vim setup uses (and actually contains) the [vim-plug](https://github.com/junegunn/vim-plug) plugin manager and the following tutorial assumes you do aswell.
To see a list of the files this repo contains, see the section entitled 'Currently include files'
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

What this essentially does is create a "file" called .vimrc in your home directory which is actually a link to the vimrc file contained in this repository. This is done so that you don't have to change the
default location where Vim searches for the .vimrc file. Instead you can let Vim search for it in the default location and simply link the default location to somewhere else. This is especially convenient
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
ln --symbolic ~/preferences/vim/ftplugin ~/.vim
```

This has the same motivation as step 3 where we're letting Vim search for these directories in the default place and linking them so somewhere else.

6. Start Vim and run `:PlugInstall` to make vim-plug install the plugins

Now you're all set to begin using the setup! For specific tutorials on how the plugins and snippets actually work, I recommend [this fantastic tutorial](https://ejmastnak.com/tutorials/vim-latex/intro/) 
by Elijan Mastnak on supercharged mathematical typesetting. It covers the vim-plug plugin manager, the vimtex and ultisnips plugins and much, much more.

### All the other stuff

Everything else currently included in this repo can be used straight away without any configuration.

## Currently included files

### Vim files

- My .vimrc file
	- Basic highlighting, indentation and colorscheme settings 
	- Plugin specific settings
- The [vim-plug](https://github.com/junegunn/vim-plug) plugin manager
- The plugins I use
    - [nerdtree](https://github.com/preservim/nerdtree)
    - [numbers.vim](https://github.com/myusuf3/numbers.vim)
    - [vimtex](https://github.com/lervag/vimtex)
    - [ultisnips](https://github.com/SirVer/ultisnips)
- Filetype specific configuration files (ftplugin)
	- Python
	- Fortran
- Lots of snippets for the ultisnips plugin
	- General snippets (all.snippets) (TBA)
    - TeX snippets
    - Python snippets (TBA)
    - Fortran snippets
    - GNU Make snippets (TBA)
	- Snippets for making new snippets (snippets.snippets)
	- Vimscript snippets (TBA)
    - Shell script snippets (TBA)
    - HTML snippets (TBA)
    - CSS snippets (TBA)
    - Javascript snippets (TBA)

### TeX files

- Custom Latex math commands I keep needing (These commands are also recognized by the TeX snippets for a smoother LaTeX experience)

### Scripts

- A simple python script to initiate a sympy session in terminal for symbolic calculations

### Examples

- An example of a makefile that compiles a fortran program from many sources
- A fortran program that illustrates some correct fortran syntax
- A markdown file containing some specific terminal/programming related problems I've run into and how I managed to fix them

## License

Distributed under the GPL-3.0 license which can be found in the file called 'LICENSE'

## Author

approx-error

2024

