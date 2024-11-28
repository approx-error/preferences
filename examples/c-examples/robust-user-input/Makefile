COMPILER := gcc
FLAGS := -Wall
main_src := main.c
dyn_array_src := dyn-array/dyn-char-array.c dyn-array/dyn-int-array.c
input_funcs_src := input-functions/input-functions.c
src_files := $(dyn_array_src) $(input_funcs_src) $(main_src)
exe_name := rui

$(exe_name): $(src_files)
	@echo Compiling the files...
	$(COMPILER) $(FLAGS) $^ -o $@

run: $(exe_name)
	@echo Running the program...
	./$<

clean:
	@echo Cleaning up...
	rm -f $(exe_name)
