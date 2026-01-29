# Makefile for GNU Make that can compile two different target programs 'transform' and 'calculate'
src_dir := src
transform_obj_dir := obj_transform
calculate_obj_dir := obj_calculate
mod_dir := mod
inc_dir := /usr/local/include
build_dir := build

transform_src := kinds.f90 parameters.f90 fftw3.f90 transform.f90
transform_exe := transform
calculate_src := kinds.f90 parameters.f90 convert_form.f90 calculate.f90
calculate_exe := calculate

compiler := gfortran
common_flags := -Wall -Wextra -O2
common_compilation_flags := -ffree-form -ffree-line-length-none -fimplicit-none -fbackslash -fmodule-private -std=f2018 -J "$(mod_dir)"
transform_compilation_flags := -I "$(inc_dir)" 
transform_libraries := -lfftw3 -lm  

transform_src_path := $(patsubst %.f90, $(src_dir)/%.f90, $(transform_src))
transform_obj_path := $(patsubst $(src_dir)/%.f90, $(transform_obj_dir)/%.o, $(transform_src_path))
transform_mod_path := $(patsubst $(src_dir)/%.f90, $(mod_dir)/%.mod, $(transform_src_path))
transform_exe_path := $(build_dir)/$(transform_exe)

calculate_src_path := $(patsubst %.f90, $(src_dir)/%.f90, $(calculate_src))
calculate_obj_path := $(patsubst $(src_dir)/%.f90, $(calculate_obj_dir)/%.o, $(calculate_src_path))
calculate_mod_path := $(patsubst $(src_dir)/%.f90, $(mod_dir)/%.mod, $(calculate_src_path))
calculate_exe_path := $(build_dir)/$(calculate_exe)


.PHONY: all, trans, calc
all: trans calc

trans: $(transform_mod_path) $(transform_exe_path)

$(transform_mod_path): | $(mod_dir)

# The executable is the target and the object files are the prerequisites
# If the executable doesn't exist, this block will be run
$(transform_exe_path): $(transform_obj_path) | $(build_dir)
	$(info Linking object files for executable '$(transform_exe)')
	$(compiler) $(common_flags) $^ -o $@ $(transform_libraries)

$(transform_obj_path): | $(transform_obj_dir)

$(transform_obj_dir):
	mkdir -p $(transform_obj_dir)


# The object files are the target and the source files are the prerequisites
# If the object files don't exist, this block will be run 
$(transform_obj_dir)/%.o: $(src_dir)/%.f90
	$(info Compiling source files for '$(transform_exe)')
	$(compiler) $(common_flags) $(common_compilation_flags) $(transform_compilation_flags) -c $< -o $@

calc: $(calculate_mod_path) $(calculate_exe_path)

$(calculate_mod_path): | $(mod_dir)

$(mod_dir):
	mkdir -p $(mod_dir)

$(calculate_exe_path): $(calculate_obj_path) | $(build_dir)
	$(info Linking object files for executable '$(calculate_exe)')
	$(compiler) $(common_flags) $^ -o $@
	
$(calculate_obj_path): | $(calculate_obj_dir)

$(calculate_obj_dir):
	mkdir -p $(calculate_obj_dir)

$(calculate_obj_dir)/%.o: $(src_dir)/%.f90
	$(info Compiling source files for '$(calculate_exe)')
	$(compiler) $(common_flags) $(common_compilation_flags) -c $< -o $@

$(build_dir):
	mkdir -p $(build_dir)


# Shorthand commands to delete the object files, modules and the final executable
.PHONY: clean deepclean
clean:
	-rm -f $(wildcard $(transform_obj_dir)/*.o) $(wildcard $(calculate_obj_dir)/*.o) $(wildcard $(mod_dir)/*.mod)
	-rm -f $(transform_exe_path) $(calculate_exe_path)

deepclean:
	-rm -rf $(transform_obj_dir) $(calculate_obj_dir) $(mod_dir) $(build_dir)
	
# Shorthand command to run the executable. Since the executable is a prerequisite,
# make will run the previous two block if it doesn't exist yet. thus running
# 'make run' is the same as running 'make' and then 'make run'
.PHONY: run runtrans runcalc
run: runtrans runcalc

runtrans: trans
	$(info Running the executable '$(transform_exe)')
	./$(transform_exe_path)

runcalc: calc
	$(info Running the executable '$(calculate_exe)')
	./$(calculate_exe_path)

