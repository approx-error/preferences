# Basic usage of the GNU Debugger (gdb)

## What?

gdb is a debugging tool that allows you to look at the code you've written in more detail by adding breakpoints, looking at the assembly code, and much more.

## How?

Normally when compiling something with gcc (gfortran), you so something like this:

```sh
gcc -o output source.c
```

Or:

```sh
gfortran -o output source.f90
```

If you now look at the file information of the compiled file "output", you'll see something like this:

```sh
> file output
output: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked,
interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f05a350bdb4f0d3bd6944a8da4fcbc70f73cdd36,
for GNU/Linux 3.2.0, not stripped
```

If you instead compile with the `-g` flag, like so:

```sh
gcc -o output source.c -g
```

You'll see something like this:
```sh
> file output
output: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked,
interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=0ac5381373e24a2ed8fbfeee6e635317d413534f,
for GNU/Linux 3.2.0, with debug_info, not stripped
```
Notice how at the end it says "with debug\_info"? This is how you know you can use gdb to analyze the executable. Now do:

```sh
gdb output
```

You are now in gdb. By running:

```sh
lay next
```

and pressing enter you'll see the original source code as well as the assembly code in a terminal UI.
Now you can add breakpoints with the break-command followed by where you want to break, for example
at the main function:

```sh
break main
```

You'll see that reflected in the UI with a little b+ symbol appearing where main is in both the source and the assembly codes. Now type run

```sh
run
```

to start executing the program. It will stop at the specified breakpoints allowing you to check out what's happening before continuing the execution.
To go forward by one line of source code, type

```sh
next
```

To go forwar by one line of assembly code, type

```sh
nexti
```

for "next instruction". To refresh the view type

```sh
ref
```

To quit the debugging process type

```sh
quit
```

If/when the program crashes, you can get information about the moment the crash happened
by typing

```sh
x/i $pc
```

And by typing

```sh
info registers
```

To see what values were stored in the registers at the time of the crash

