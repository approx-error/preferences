# Example makefile

# Which fortran compiler to use:
compiler = gfortran
# Which flags to user when compiling, current flags: Enable a whole host of warnings, free form fortran, no max line length in source code, no implicit typing, allow C-style escape characters in strings:
flags = -Wall -Wextra -ffree-form -ffree-line-length-none -fimplicit-none -fbackslash
# Additional Fortran dialect flags that might be interesting:
# -fmodule-private (module variables are always private unless explicitly declared as public)
# -fmax-identifier-length=n (Specify the maximum allowed identifier length. Typical values are 31 (Fortran 95) and 63 (Fortran 2003 and later))
# -std=f2023 (Set the fortran standard the code should conform to. Default is 'gnu', other values of interest are 'f95', 'f2003', 'f2008', 'f2018', and 'legacy')
# -fdollar-ok (Allow '$' as a valid non-first character in a symbol name. Normally symbols with '$' are rejected since it is unclear which rules apply to implicit typing as
#  different vendors implement different rules. Using '$' in implicit statements is also rejected)
# Compilation flags:
# --include-directory=dir (or -I dir) (Add 'dir' to the list of directories that are searched when locating external libraries)
# -J dir (Spcifieds where to put .mod files for compiled modules and adds 'dir' to the list of directories searched by an use-statement)
# Grouping the source files and object files together so they can be referenced with a single variable:
src_files = sample_kinds.f90 sample_module.f90 sample_code.f90
obj_files = $(patsubst %.f90, %.o, $(src_files))
# Defining the name of the final executable:
exe_name = program

# The executable is the target and the object files are the prerequisites
# If the executable doesn't exist, this block will be run
$(exe_name): $(obj_files)
	@echo Linking object files
	$(compiler) $(flags) $^ -o $@

# The object files are the target and the source files are the prerequisites
# If the object files don't exist, this block will be run 
$(obj_files): $(src_files)
	@echo Compiling source files
	$(compiler) $(flags) -c $^

# Shorthand command to run the executable. Since the executable is a prerequisite,
# make will run the previous two block if it doesn't exist yet. thus running
# 'make run' is the same as running 'make' and then 'make run'
run: $(exe_name)
	@echo Running the program
	./$<

# Shorthand command to delete the object files, modules and the final executable
clean:
	@echo Cleaning up
	rm -f $(wildcard *.o) $(wildcard *.mod) $(exe_name)
