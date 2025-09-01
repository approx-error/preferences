COMPILER := gcc
CFLAGS := -Wall -MMD -c
LFLAGS := -Wall
LIBS := -lm
srcdir := src
objdir := obj
builddir := build

main_src := main.c
module_src := funcs.c test.c
exe_name := test_funcs

src_files := $(patsubst %.c, $(srcdir)/%.c, $(module_src)) $(srcdir)/$(main_src)
obj_files := $(patsubst $(srcdir)/%.c, $(objdir)/%.o, $(src_files))
dep_files := $(patsubst $(objdir)/%.o, $(objdir)/%.d, $(obj_files))
exe_file := $(builddir)/$(exe_name)

$(exe_file): $(obj_files)
	@echo Linking object files and libraries...
	-mkdir $(builddir)
	$(COMPILER) $(LFLAGS) $^ $(LIBS) -o $@

-include $(dep_files)

$(objdir)/%.o: $(srcdir)/%.c
	@echo Compiling source files...
	-mkdir $(objdir)
	$(COMPILER) $(CFLAGS) $< -o $@

run: $(exe_file)
	@echo Running the program...
	./$<

clean:
	@echo Cleaning up...
	-rm -f $(obj_files) $(dep_files) $(exe_file)
	-rmdir $(objdir) $(builddir)

