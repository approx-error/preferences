# How to get assembly code out of your source code with gcc (gfortran)

Compiling with the `-S` flag will do the trick. Example:

```sh
gcc -S -o assembly-file source.c
```

Now you can check out the assembly code with your favorite text editor, for example:

```sh
vim assembly-file
```

That's it!
