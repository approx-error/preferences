# Information on making .desktop files for launching programs

Inspired by the hours I spent trying to make a custom launch script for an application work

## 1 - What are .desktop files?

In brief, .desktop files are configuration files, that describe how to launch a given program,
the name of the program's desktop shortcut, the icon of the program and so on. Every launchable
"program" on the desktop of your computer is actually a .desktop file describing how to actually
run the program. Your desktop is a directory just like any other and is usually located in your
home directory under the name 'Desktop'. If you place a .desktop file there, a graphical icon
representation of it will be shown on you computer's desktop. (Of course this applies to all
other files as well).

## 2 - How do .desktop files work?

.desktop files consist of a series of key-value pairs that describe what the file should do etc.
Here is an example of a desktop file:

[Desktop Entry]
Name=word editor
GenericName=writing application
Path=/stuff/things/directory
Exec=/stuff/bin/program
Comment=Launches program with default settings
Terminal=false
PrefersNonDefaultGPU=false
Icon=picture
Type=Application
Categories=Office

- The first line tells that the following key-value -pairs will be related to a desktop entry.
- Name is the text shown under the icon on the desktop
- GenericName is a more generic name for the program
- Path is the absolute path to the directory the program should be executed in. For example if
some important files needed by the program are in /stuff/things/directory, setting the Path
there means that the program doesn't have to be able to look for the files system-wide which
makes it easier to port to systems with arbitrary directory structures
- Exec is the absolute path to the actual program that should be executed when the icon is clicked.
You should make sure that the user is permitted to execute said program, or the icon won't be able
to execute it. If the program is in a directory the user can edit, you can make it executable
by running `chmod u+x <program_name>` in said directory. To make sure a file is executable, run
`ls -F` in the directory. An asterisk `*` will appear after the file's name if it is executable.
- Comment is used to describe birefly, what the icon does
- Terminal controls whether or not the icon should run the program through a terminal or not.
If the program you wan't to launch is a simple script that takes user input through the terminal,
and prints information to the terminal, this needs to be set to true, or you won't be able to use
the program. If the program doesn't require this kind of I/O, the terminal might not be needed.
For example a simple python script can still modify directories, read from and write to files etc.
even if terminal is sekt to false. If the application is a GUI-based application that runs in
its own window, the terminal is probably not needed, but sometimes it is useful to see the potential
error messages a program sends while running and to see those, you need to start the program from
a terminal window.
- Icon is the icon of the dekstop entry
- Type and Ctegories are the type of program the executable is and the categories it belongs to.
These help the desktop environment categorize the program and perhaps place it in a suitable menu
or make it show up when the general category is searched on the desktop environment's search function

There are many other keys whose values can be set but these are the most common and important keys.

A list of all keys can be found [here](https://specifications.freedesktop.org/desktop-entry-spec/latest/recognized-keys.html)

## 3 - Possible pitfalls

There are many things that may go wrong when trying to create a .desktop file that runs a program. Here is
a non-exhaustive list of possible problems and solutions to them

- A program cannot be executed:
    - Check that the path you have specified in Exec actually contains the program you want to execute
    - Check that the user has execution privileges on the program
    - If the program is a script in an interpreted language (like a shell script or python file), add a shebang
    to the beginning of the file to inform the computer that the file should be executed with an interpreter.
    For a python 3 script add the shebang #!/usr/bin/env python3 and for a shell script add the shebang #!/usr/bin/<shell>,
    where shell is a shell of your choice such as sh (which defaults to dash on debian-based distros), bash, zsh etc.
    If speed is important for the execution of a shell script, dash is a good choice since it is less focused on interactive
    use and more focused on speed and memory efficiency when compared with more feature-rich shells like bash.
    - Check that you have specified the executable's location with the Exec key, NOT the Path key

## 4 - Good Practices

Here are some good practices for using .desktop files

- If you want to make a desktop icon that executes a bunch of shell commands, don't try to specify the commands with the Exec key.
Insetad, put the commands in a file with a shell shebang at the top, make it executable and specify that file as the program
to execute when clicking the icon. The Exec field should be primarily used for specifying a single executable to run and the
actual executable should do all the things you actually want to do
