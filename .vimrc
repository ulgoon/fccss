set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'gmarik/Vundle.vim'

" The following are examples of different formats supported.
" Keep Plugin commands between vundle#begin/end.
" plugin on GitHub repo
Plugin 'tpope/vim-fugitive'
" plugin from http://vim-scripts.org/vim/scripts.html
Plugin 'L9'
" Git plugin not hosted on GitHub
Plugin 'git://git.wincent.com/command-t.git'
" git repos on your local machine (i.e. when working on your own plugin)
Plugin 'file:///home/gmarik/path/to/plugin'
" The sparkup vim script is in a subdirectory of this repo called vim.
" Pass the path to set the runtimepath properly.
Plugin 'rstacruz/sparkup', {'rtp': 'vim/'}
" Avoid a name conflict with L9
Plugin 'user/L9', {'name': 'newL9'}

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

"NERDTreeToggle Plugin
Plugin 'The-NERD-Tree'
"NERDTree AutoStart
autocmd VimEnter * NERDTree
autocmd VimEnter * if argc() | wincmd p | endif

"Syntaxhighlight
if has("syntax")
	syntax on
endif

"set tabspace
set ts=4
set shiftwidth=4
set softtabstop=4
set expandtab
set enc=utf8
set et ts=4
ret 4

"set linenumber
set nu

"solarized theme
"set rtp+=~/.vim/bundle/vim-colors-solarized/
syntax enable
set bg=dark
set t_Co=256
"colorscheme solarized

"color lucius
colorscheme lucius 

"color distinguished
"colorscheme distinguished

"vim-go
Plugin 'fatih/vim-go'

"julia-vim
Plugin 'Julialang/julia-vim'

"vim-snipmate
Plugin 'MarcWeber/vim-addon-mw-utils'
Plugin 'tomtom/tlib_vim'
Plugin 'garbas/vim-snipmate'
"Optional
Plugin 'honza/vim-snippets'

"Autocomplete
Plugin 'othree/vim-autocomplpop'

"autocomplpop settings
function! InsertTabWrapper()
    let col = col('.') - 1
    if !col || getline('.')[col-1]!~'\k'
        return "\<TAB>"
    else
        if pumvisible()
            return "\<C-N>"
        else
            return "\<C-N>\<C-P>"
        end
    endif
endfunction

inoremap <tab> <c-r>=InsertTabWrapper()<cr>

"autocomplpop color settings
"hi Pmenu ctermbg=blue
hi PmenuSel ctermbg=yellow ctermfg=black
hi PmenuSbar ctermbg=blue

"vim-pug - Syntaxhighlighter for pug engine
Plugin 'digitaltoad/vim-jade'

"vim-powerline
Plugin 'https://github.com/Lokaltog/vim-powerline.git'

language en_US.UTF-8
let g:Powerline_symbols = 'unicode'
set laststatus=2
