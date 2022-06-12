# Mdbook电子书发布工具使用说明

<!--ts-->
* [Mdbook电子书发布工具使用说明](#mdbook电子书发布工具使用说明)
   * [使用要点](#使用要点)
      * [基本结构](#基本结构)
      * [Summary](#summary)
      * [图片资源与git lfs](#图片资源与git-lfs)
         * [git lfs使用场景](#git-lfs使用场景)
         * [对mdbook的影响](#对mdbook的影响)
   * [Rust特供功能](#rust特供功能)
      * [隐藏代码行](#隐藏代码行)
      * [Rust Playground页面执行](#rust-playground页面执行)
      * [包含文件自动渲染为md](#包含文件自动渲染为md)
         * [全文件包含](#全文件包含)
         * [指定行数](#指定行数)
         * [指定锚点部分](#指定锚点部分)
      * [插入代码](#插入代码)
         * [插入可运行代码: 只支持rust](#插入可运行代码-只支持rust)
         * [页面直接编辑代码: *, editable](#页面直接编辑代码--editable)
   * [mdbook插件推荐](#mdbook插件推荐)
      * [自动检查](#自动检查)
         * [MDBook Link-Check](#mdbook-link-check)
      * [自动生成](#自动生成)
         * [global-search](#global-search)
         * [mdbook-toc](#mdbook-toc)
         * [mdbook-pagetoc: 添加页内侧边栏toc](#mdbook-pagetoc-添加页内侧边栏toc)
         * [mdbook-open-on-gh](#mdbook-open-on-gh)
         * [book-summary](#book-summary)
         * [mdbook-suto-gen-summary](#mdbook-suto-gen-summary)
         * [mdbook-transcheck](#mdbook-transcheck)
         * [mdbook-man](#mdbook-man)
         * [Gooseberry - a Knowledge Base for the Lazy](#gooseberry---a-knowledge-base-for-the-lazy)
         * [mdbook-bookimport](#mdbook-bookimport)
         * [md2tex](#md2tex)
         * [mdbook-checklist](#mdbook-checklist)
         * [mdBook Tag](#mdbook-tag)
         * [mdBook-template](#mdbook-template)
         * [trpl-zh-cn-pdf](#trpl-zh-cn-pdf)
         * [mdbook-cms](#mdbook-cms)
      * [自动渲染](#自动渲染)
         * [unevil rs](#unevil-rs)
         * [mdBook Graphviz](#mdbook-graphviz)
         * [svgbob plugin for mdbook](#svgbob-plugin-for-mdbook)
         * [mdbook-admonish](#mdbook-admonish)
         * [mdbook-curly-quotes](#mdbook-curly-quotes)
         * [mdbook-tera](#mdbook-tera)
         * [mdbook-template](#mdbook-template-1)
         * [mdbook-mark](#mdbook-mark)
         * [mdbook-all-the-markdowns](#mdbook-all-the-markdowns)
         * [mdbook-fluent](#mdbook-fluent)
         * [mdbook-kroki-preprocessor](#mdbook-kroki-preprocessor)
         * [mdBook Bibfile Referencing](#mdbook-bibfile-referencing)
         * [mdbook-wikilink](#mdbook-wikilink)
         * [mdbook-page-styles](#mdbook-page-styles)
         * [mdbook-note](#mdbook-note)
         * [mdbook-section-validator](#mdbook-section-validator)
   * [资源链接](#资源链接)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sun Jun 12 07:02:44 UTC 2022 -->

<!--te-->

## 使用要点

### 基本结构

```shell
tree -L 2                                                                                                                                                                                                                              ─╯
.
├── README.md # 项目基本说明
├── bin # mdbook可执行文件
│   └── mdbook
├── book.toml # 书籍基本信息配置
├── mermaid-init.js # mermaid用到的js文件
├── mermaid.min.js # mermaid用到的js文件
├── mytheme # 书籍用到的主题
│   ├── FontAwesome
│   ├── ayu-highlight.css
│   ├── book.js
│   ├── clipboard.min.js
│   ├── css
│   ├── favicon.png
│   ├── favicon.svg
│   ├── fonts
│   ├── head.hbs
│   ├── header.hbs
│   ├── highlight.css
│   ├── highlight.js
│   ├── index.hbs
│   ├── mod.rs
│   ├── playground_editor
│   ├── redirect.hbs
│   ├── searcher
│   └── tomorrow-night.css
├── scripts # 一些文章里面提及的脚本文件
│   ├── anki_md_js
│   ├── gh-md-toc
│   ├── toc_generator.sh
│   ├── update_toc
│   └── update_toc_raw
├── smart-anchor.js
└── src # 书籍内容主体
    ├── SUMMARY.md # 目录页，唯一可以添加跳转的地方
    ├── app_deepin
    ├── app_extensions
    ├── app_plugin_list.md
    ├── imgs
    ├── macos_essentials.md
    ├── macos_ios_tips.md
    ├── overview.md
    └── shortcuts_keymaps_config.md

13 directories, 29 files
```

### Summary

要注意，mdbook中所有文章跳转链接只能放在Summary中。

### 图片资源与git lfs

#### git lfs使用场景

![](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/graphic.gif)

Git LFS 是 Github 开发的一个 Git 的扩展，用于实现 Git 对大文件的支持. 比如在游戏开发过程中,设计资源占用了很大一部分空间. 像png,psd等文件是二进制(blob)
的,体积也很庞大.但git的diff/patch等是基于文件行的.对于二进制文件来说. git需要存储每次commit的改动.每次当二进制文件修改,发生变化的时候.
都会产生额外的提交量.导致clone和pull的数据量大增.在线仓库的体积也会迅速增长.

![](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/1200.png)
> LFS(Large File Storage) 就是为了解决这一问题而产生的工具.

- 它将你所标记的大文件保存至另外的仓库,而在主仓库仅保留其轻量级指针.
- 那么在你检出版本时,根据指针的变化情况下更新对应的大文件.而不是在本地保存所有版本的大文件

![](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/1200-20220608102711994.png)

#### 对mdbook的影响

因为mdbook默认是在src里面直接引用静态资源，所以如果用git lfs打开对应的资源存储就会导致发布后的github pages找不到静态资源。

## Rust特供功能

### 隐藏代码行

```rust
# fn main() {
    let x = 5;
    let y = 6;

    println!("{}", x + y);
    #
}
```

### Rust Playground页面执行

- 默认支持

```rust
#![allow(unused)]

fn main() {
    println!("Hello, World!");
}
```

- 指定不支持

```rust,noplayground
let mut name = String::new();
std::io::stdin().read_line(&mut name).expect("failed to read line");
println!("Hello {}!", name);
```

### 包含文件自动渲染为md

#### 全文件包含

````
```
\{{#include ../../scripts/update_toc_raw}}
```
````

> 渲染后：

```shell
{{#include ../../scripts/update_toc_raw}}
```

#### 指定行数

1. 指定一行

````
```
\{{#include ../../scripts/update_toc_raw:1}}
```
````

> 渲染后：

```shell
{{#include ../../scripts/update_toc_raw:1}}
```

2. 指定一行开始

````
```
\{{#include ../../scripts/update_toc_raw:1:}}
```
````

> 渲染后：

```shell
{{#include ../../scripts/update_toc_raw:1:}}
```

3. 指定范围

````
```
\{{#include ../../scripts/update_toc_raw:1:5}}
```
````

> 渲染后：

```shell
{{#include ../../scripts/update_toc_raw:1:5}}
```

4. 指定到某行

````
```
\{{#include ../../scripts/update_toc_raw::6}}
```
````

> 渲染后：

```shell
{{#include ../../scripts/update_toc_raw::6}}
```

#### 指定锚点部分

### 插入代码

#### 插入可运行代码: 只支持rust

#### 页面直接编辑代码: *, editable

## mdbook插件推荐

### 自动检查

#### MDBook Link-Check

[Michael-F-Bryan/mdbook-linkcheck: A backend for `mdbook` which will check your links for you.](https://github.com/Michael-F-Bryan/mdbook-linkcheck)

### 自动生成

#### global-search

[mattico/global-search: Global search for a collection of MDBooks](https://github.com/mattico/global-search)

#### mdbook-toc

[badboy/mdbook-toc: A preprocessor for mdbook to add inline Table of Contents support.](https://github.com/badboy/mdbook-toc)

#### mdbook-pagetoc: 添加页内侧边栏toc

[JorelAli/mdBook-pagetoc: A page table of contents for mdBook](https://github.com/JorelAli/mdBook-pagetoc)
![mdbook-toc-sample](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/mdbook-toc-sample.png)
[Chapter 1 - Sample](https://jorel.dev/mdBook-pagetoc/)

#### mdbook-open-on-gh

[badboy/mdbook-open-on-gh: mdbook preprocessor to add a open-on-github link on every page](

#### book-summary

> Automatically creates a SUMMARY.md file for your book (`mdbook/gitbook`)

[dvogt23/book-summary: 📔Book auto-summary 🦀🖤 (gitbook/mdBook)](https://github.com/dvogt23/book-summary)

#### mdbook-suto-gen-summary

[knightflower1989/mdbook-auto-gen-summary: mdbook auto-gen-summary](https://github.com/knightflower1989/mdbook-auto-gen-summary)

#### mdbook-transcheck

[dalance/mdbook-transcheck: Checker for translated mdbook](https://github.com/dalance/mdbook-transcheck)

#### mdbook-man

[vv9k/mdbook-man: Generate manual pages from mdBooks!](https://github.com/vv9k/mdbook-man)

#### Gooseberry - a Knowledge Base for the Lazy

> 一个很棒的工具，可以直接将mdbook转为知识库

[out-of-cheese-error/gooseberry: A command line utility to generate a knowledge base from Hypothesis annotations](https://github.com/out-of-cheese-error/gooseberry)

![obsidian_example-2](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/obsidian_example-2.png)

#### mdbook-bookimport

[tailwind/mdbook-bookimport: Import code/text from other files into your mdbook - without the link rot.](https://github.com/tailwind/mdbook-bookimport)

#### md2tex

> A small utility to convert markdown files to tex. Forked from md2pdf, with an added focus on mdbook conversions. Also with the goal of eventually contributing back upstream.

- Used by mdbook-latex to generate PDF's.

[lbeckman314/md2tex: A fork of tforgione's awesome md2pdf library, catered for mdbook.](https://github.com/lbeckman314/md2tex)

#### mdbook-checklist

[ANSSI-FR/mdbook-checklist: mdbook preprocessor for generating checklists and indexes](https://github.com/ANSSI-FR/mdbook-checklist)

#### mdBook Tag

[dylanowen/mdbook-tag](https://github.com/dylanowen/mdbook-tag)

#### mdBook-template

[sgoudham/mdbook-template: A mdbook preprocessor that allows the re-usability of template files with dynamic arguments](https://github.com/sgoudham/mdbook-template)

#### trpl-zh-cn-pdf

> [KaiserY/trpl-zh-cn: Rust 程序设计语言（2021 edition 施工中）](https://github.com/KaiserY/trpl-zh-cn/)

[me1ting/trpl-zh-cn-pdf: trpl-zh-cn的mdBook风格的pdf，带全书签](https://github.com/me1ting/trpl-zh-cn-pdf)

#### mdbook-cms

[AlongWY/mdbook-cms: A preprocessor bring cms to mdbook.](https://github.com/AlongWY/mdbook-cms)

### 自动渲染

#### unevil rs

[oknozor/unveil-rs: Unveil Rs is a tool to create presentations from markdown inspired by reveal.js, mdbook and zola.](https://github.com/oknozor/unveil-rs)

[在线示例](https://oknozor.github.io/unveil-rs/)

#### mdBook Graphviz

[dylanowen/mdbook-graphviz](https://github.com/dylanowen/mdbook-graphviz)

https://github.com/badboy/mdbook-open-on-gh)

#### svgbob plugin for mdbook

[boozook/mdbook-svgbob: SvgBob mdbook preprocessor which swaps code-blocks with neat SVG.](https://github.com/boozook/mdbook-svgbob)

#### mdbook-admonish

[tommilligan/mdbook-admonish: A preprocessor for mdbook to add Material Design admonishments.](https://github.com/tommilligan/mdbook-admonish)

#### mdbook-curly-quotes

> mdBook preprocessor that replaces straight quotes with curly quotes, except within code blocks or code spans.
> It does the same as the curly-quotes option of the mdBook HTML renderer. The only advantage is that it can be applied to any renderer.
[arminha/mdbook-curly-quotes: mdBook preprocessor that replaces straight quotes with curly quotes](https://github.com/arminha/mdbook-curly-quotes)

#### mdbook-tera

> 基于tera模版引擎渲染
[avitex/mdbook-tera: Tera preprocessor for mdBook](https://github.com/avitex/mdbook-tera)
[Keats/tera: A template engine for Rust based on Jinja2/Django](https://github.com/Keats/tera)

#### mdbook-template

> 可以自定义页脚的图像

[sgoudham/mdbook-template: A mdbook preprocessor that allows the re-usability of template files with dynamic arguments](https://github.com/sgoudham/mdbook-template)

#### mdbook-mark

[blazood/mdbook-mark: this is a mdbook preprocessor which can render ==== to <mark></mark>](https://github.com/blazood/mdbook-mark#readme)

#### mdbook-all-the-markdowns

![all-the-things](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/all-the-things.png)

[bombsimon/mdbook-all-the-markdowns: 🗃️ Preprocessor for mdbook to render all the markdowns!](https://github.com/bombsimon/mdbook-all-the-markdowns)

#### mdbook-fluent

[JakubKoralewski/mdbook-fluent: mdBook preprocessor for variable interpolation using the Fluent language](https://github.com/JakubKoralewski/mdbook-fluent)

#### mdbook-kroki-preprocessor

[JoelCourtney/mdbook-kroki-preprocessor: Render Kroki diagrams from files or code blocks in mdbook](https://github.com/JoelCourtney/mdbook-kroki-preprocessor)

[Kroki!](https://kroki.io/)

#### mdBook Bibfile Referencing

[jacob-pro/mdbook-bibfile-referencing: An mdBook preprocessor to add bibfile referencing to each page](https://github.com/jacob-pro/mdbook-bibfile-referencing)

#### mdbook-wikilink

[NOBLES5E/mdbook-wikilink: Support for wikilinks on mdBook.](https://github.com/NOBLES5E/mdbook-wikilink)

#### mdbook-page-styles

[ABCsOf/mdbook-page-styles: An mdbook preprocessor to apply styles to specific pages and elements.](https://github.com/ABCsOf/mdbook-page-styles)

#### mdbook-note

[Aedius/mdbook-note: preprocessor for mdbook to add organized chapter containing fragment from the rest of the book](https://github.com/Aedius/mdbook-note)

#### mdbook-section-validator

[younata/mdbook-section-validator: mdBook preprocessor for defining conditionally valid sections](https://github.com/younata/mdbook-section-validator)

## 资源链接

- [rust-lang/mdBook: Create book from markdown files. Like Gitbook but implemented in Rust](https://github.com/rust-lang/mdBook)
- [Introduction - mdBook Documentation](https://rust-lang.github.io/mdBook/)

- [Git Large File Storage | Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.](https://git-lfs.github.com/)

- [mdBook-specific features - mdBook Documentation](https://rust-lang.github.io/mdBook/format/mdbook.html)