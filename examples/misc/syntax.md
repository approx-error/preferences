# Programming language syntax cheatsheet

Some miscellaneous programming language syntax snippets that I keep needing to remember

## Fortran assumed and deferred length

If a character's length is declared as `*`, it means that the
length will be determined by the program when the variable is assigned
a value. For example if you write:

```fortran
character (len=*), intent(in) :: name
```

inside a function definition, the length of "name" will be determined
when a string is passed into the function. This is called assumed length

If a character's length is declared as `:`, it means that the
length may vary during the execution of the program and must
be specified at a later time. For example if you write:

```fortran
character (len=:), allocatable :: name
```

in a program, you need to, before usgin the variable allocate its
length by writing:

```fortran
allocate(character (len=5) :: name)
```

or by specifying a name:

```fortran
name = 'Bob'
```

This is called deferred length and can only be used for variables
declared with the `allocatable` or `pointer` keywords.
