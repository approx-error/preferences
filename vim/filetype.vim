if exists("did_load_filetypes")
    finish
endif
augroup filetypedetect
   au! BufRead,BufNewFile *.mini    setfiletype mini
   au! BufRead,BufNewFile *.prep    setfiletype mini
   au! BufRead,BufNewFile *.toke    setfiletype mini
   au! BufRead,BufNewFile *.pars    setfiletype mini
augroup END

