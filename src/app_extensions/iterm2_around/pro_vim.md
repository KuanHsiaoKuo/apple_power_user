# vim专业使用

<!--ts-->
* [vim专业使用](#vim专业使用)
   * [Macros](#macros)
      * [相关资料](#相关资料)
   * [VimScript](#vimscript)
      * [相关资料](#相关资料-1)
      * [场景一：繁琐内容处理](#场景一繁琐内容处理)
         * [代码内容](#代码内容)
         * [使用说明](#使用说明)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Mon Sep 19 16:57:13 UTC 2022 -->

<!--te-->

## Macros

> 对于临时的复杂操作，可以使用宏。这里举例一下

1. 浏览模式下按 q
2. 选择一个 mark， 比如 e
3. 开始记录批量操作
4. 按 q 退出宏记录
5. :echo @e 或者:reg @e 可以查看宏记录
6. 编辑修改：打开新的 vim，"ep, 编辑修改，复制，"eyy
7. 列出所有的宏：:reg
8. 清除指定宏：:let @e=''

### 相关资料

- [recording macros](marginnote3app://note/91233E56-7CF4-48CD-9FD9-CA75C4DF930B)
- [vim 编辑器宏的使用 – 初果编程](https://chuguo.pro/share/473)

## VimScript

> vim本身提供一种脚本语言，帮助进行个性化操作。

### 相关资料

- [Tutorial: vimscript](https://mmmnnnmmm.com/#tutorial_vimscript)
- [Vimscript functions cheatsheet](https://devhints.io/vimscript-functions)
- [VimScript 五分钟入门（翻译） - 知乎](https://zhuanlan.zhihu.com/p/37352209)
- [Five Minute Vimscript](http://andrewscala.com/vimscript/)
- [Vim documentation: usr_41](http://vimdoc.sourceforge.net/htmldoc/usr_41.html)

### 场景一：繁琐内容处理

> 我比较喜欢在idea里面写markdown文档，但是idea格式化mdbook的include语法时会出现问题, 自动添加空格导致语法失效。

这里自己写了一个vimscript解决这个问题，正好举例如何使用。

#### 代码内容

```vim-script
{{#include vim_config/scripts/replace_collections.vim:1:}}
```

#### 使用说明

1. vim内：命令模式输入`Ir`
2. 终端内：`vim -c 'Ir' <target_file>`