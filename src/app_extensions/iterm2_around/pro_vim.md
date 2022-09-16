# vim专业使用

<!--ts-->
* [vim专业使用](#vim专业使用)
   * [VimScript](#vimscript)
      * [场景一：繁琐内容处理](#场景一繁琐内容处理)
         * [代码内容](#代码内容)
         * [使用说明](#使用说明)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Fri Sep 16 04:05:21 UTC 2022 -->

<!--te-->

## VimScript

> vim本身提供一种脚本语言，帮助进行个性化操作。

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