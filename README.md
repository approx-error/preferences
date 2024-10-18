# approx-error/preferences

A repository of preferences, templates, customization files and small scripts I have found useful. 
These mostly consist of [Vim](https://www.vim.org/) configuration files, [ultisnips](https://github.com/SirVer/ultisnips) snippets and LaTeX commands.
There are also some example files for correct syntax when using certain tools/languages that I keep coming back to for reference so might as well put them here.
I don't expect anyone else to find a use for these but in case someone does, they will be waiting here.

## Usage

Here is the quickest way to be able to use these preferences out of the box on your own system (assuming a unix-based system where symbolic links can be created):

1. Clone this repository to your home directory (ie. ~/)
2. Create symlinks (TBA)
3. (TBA)

## Currently included files

### Vim

- My .vimrc file
	- Basic highlighting, indentation and colorscheme settings 
	- Plugin specific settings (I use the [vim-plug](https://github.com/junegunn/vim-plug) plugin manager)
	- Current plugins in use: [nerdtree](https://github.com/preservim/nerdtree), [vimtex](https://github.com/lervag/vimtex), [ultisnips](https://github.com/SirVer/ultisnips)
- Filetype specific configuration fles
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

### TeX

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
