function! AddSpaceBeforeEqualInWholeBuffer()
    let l = 1
    let include_replace = {
      \ '{{ #': '{{#',
      \ '# include': '#include',
      \ 'include\.\.': 'include \.\.',
      \ '\/ ': '\/',
      \ ' \/': '\/'
    \ }
    for [substitute_key, substituted] in items(include_replace)
        echo substitute_key . substituted
        for line in getline(1,"$")
            call setline(l, substitute(line, substitute_key, substituted, "g"))
        let l = l + 1
        endfor
    endfor
endfunction
"将会在source的时候直接执行
"call AddSpaceBeforeEqualInWholeBuffer()
"source之后将会自定义一个指令
command Rp call AddSpaceBeforeEqualInWholeBuffer()