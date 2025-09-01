# Example makefile

# Which fortran compiler to use:
compiler = gfortran
# Which flags to user when compiling, current flags: Enable a whole host of warnings, free form fortran, no max line length in source code, no implicit typing, allow C-style escape characters in strings:
flags = -Wall -ffree-form -ffree-line-length-none -fimplicit-none  -fbackslash
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
