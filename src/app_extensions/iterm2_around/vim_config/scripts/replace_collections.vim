function! MdbookIncludeSyntaxFormatInWholeBuffer()
    let include_replace = {
      \ '{{ #': '{{#',
      \ '# include': '#include',
      \ 'include\.\.': 'include\ \.\.',
      \ '\/ ': '\/',
      \ ' \/': '\/',
      \ ': ': ':',
      \ ' }}': '}}'
    \ }
    let l = 1
    for line in getline(1,"$")
        if stridx(line,  'include') > -1
            let replaced_line = line
            for [substitute_key, substituted] in items(include_replace)
                "echo l.replaced_line
                "echo l.substitute_key.substituted
                "call setline(l, substitute(line, substitute_key, substituted, "g"))
                let replaced_line = substitute(replaced_line, substitute_key, substituted, "g")
            endfor
            call setline(l, replaced_line)
        endif
        let l = l + 1
    endfor
    "保存文件
    write
    "退出vim
    exit
endfunction
"将会在source的时候直接执行
"call AddSpaceBeforeEqualInWholeBuffer()
"source之后将会自定义一个指令
command Ir call MdbookIncludeSyntaxFormatInWholeBuffer()
