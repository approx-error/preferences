" Syntax highlighting groups for *.mini files

if exists('b:current_syntax') | finish | endif

syntax keyword miniTodo contained NOTE TODO FIXME XXX
syntax match miniComment "//.*$" contains=miniTodo

syntax match miniType "<[#%"BS]\?\^*>"

syntax match miniCollection "\[\^\+\]\|\[[#%"BS]\^*\]\|\[[#%"]:\^\+\]\|\[[#%"]:[#%"BS]\^*\]"
syntax match miniStructlike "{[EU]}"

syntax match miniControl "!\|\.\.\?\|\$\|<-\|->"
syntax match miniImport "[MC]\?::"
syntax match miniCond "??\||?\||\.\|\~?\|##\|#=\|\~#"
syntax match miniLoop "@@\|\~@"
syntax match miniMain "!\~>\.\.<\~!"
syntax match miniBlock "}}}\|{{{\|>>>\|<<<"
syntax match miniSub "\$\$\|\~\$"
syntax match miniLiteralKwds "[TFN]\|\.\{3}\|\[\.\{2}\]\|_"
syntax match miniInts "[1-9]\d*\|0x\x\+\|0\o*"
syntax match miniFloats "-\?\d\+\.\d\+"
syntax match miniStrings "\"[^"]*\""
syntax match miniIdentifier "\<[a-z][a-z0-9]\{0,7}\>\|\<[A-Z][A-Z0-9]\{1,7}\>"
"syntax match miniOperators "[\^@+-\*/%]" 

hi def link miniTodo Todo
hi def link miniComment Comment

hi def link miniType GruvboxYellowBold
hi def link miniCollection GruvboxYellowBold
hi def link miniStructlike GruvboxYellowBold


hi def link miniControl GruvboxRedBold
hi def link miniImport GruvboxAquaBold
hi def link miniCond GruvboxRedBold
hi def link miniLoop GruvboxOrangeBold  
hi def link miniMain Added 
hi def link miniBlock GruvboxBlueBold
hi def link miniSub Function
hi def link miniLiteralKwds GruvboxPurpleBold
hi def link miniInts Number
hi def link miniFloats Float
hi def link miniStrings String
hi def link miniIdentifier GruvboxFg0
"hi def link miniOperators Identifier

let b:current_syntax = 'mini'
