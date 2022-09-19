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
         * [默认支持](#默认支持)
         * [指定不支持](#指定不支持)
      * [包含文件自动渲染为md](#包含文件自动渲染为md)
         * [全文件包含](#全文件包含)
         * [指定行数](#指定行数)
         * [指定锚点部分](#指定锚点部分)
         * [打开行数](#打开行数)
      * [插入代码](#插入代码)
         * [插入可运行代码: 只支持rust](#插入可运行代码-只支持rust)
         * [页面直接编辑代码: *, editable](#页面直接编辑代码--editable)
   * [mdbook主题修改](#mdbook主题修改)
      * [基本页面介绍](#基本页面介绍)
* [mdbook高级用法](#mdbook高级用法)
   * [关于book](#关于book)
   * [关于mdbook serve panit-失败](#关于mdbook-serve-panit-失败)
   * [关于主题修改(theme)](#关于主题修改theme)
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
      * [md2tex](#md2tex)
      * [mdbook-checklist](#mdbook-checklist)
      * [mdbook-chapter-path: 可以用来生成面包屑导航](#mdbook-chapter-path-可以用来生成面包屑导航)
      * [mdBook Tag](#mdbook-tag)
      * [mdbook toc: 自动生成toc](#mdbook-toc-自动生成toc)
      * [mdbook-footnote: 可以用于生成引用内容](#mdbook-footnote-可以用于生成引用内容)
      * [trpl-zh-cn-pdf](#trpl-zh-cn-pdf)
      * [mdbook-cms: 自动生成Summary](#mdbook-cms-自动生成summary)
      * [mdbook-open-on-gh: 添加打开github分支的功能](#mdbook-open-on-gh-添加打开github分支的功能)
      * [mdbook-readme: 解决readme与index不一致的问题](#mdbook-readme-解决readme与index不一致的问题)
      * [mdbook-cmdrun: 提供强悍的终端执行功能](#mdbook-cmdrun-提供强悍的终端执行功能)
   * [配置与替换](#配置与替换)
      * [mdbook-fluent: 可以用配置文件进行整理](#mdbook-fluent-可以用配置文件进行整理)
      * [mdbook-variables: 在book.toml配置全局变量](#mdbook-variables-在booktoml配置全局变量)
      * [mdbook-regex: 对内容进行正则替换](#mdbook-regex-对内容进行正则替换)
   * [绘图](#绘图)
      * [mdBook Graphviz: 支持graphviz的dot语言](#mdbook-graphviz-支持graphviz的dot语言)
      * [svgbob plugin for mdbook](#svgbob-plugin-for-mdbook)
      * [mdbook-skill-tree: 添加技能树渲染](#mdbook-skill-tree-添加技能树渲染)
      * [mdbook-chart: 添加c3.js图表渲染功能](#mdbook-chart-添加c3js图表渲染功能)
      * [mdbook-puml: plantuml渲染](#mdbook-puml-plantuml渲染)
   * [绘图合集：kroki](#绘图合集kroki)
      * [IntelliPikchr: IDEA内置插件](#intellipikchr-idea内置插件)
      * [mdbook-kroki-preprocessor: 支持kroki渲染](#mdbook-kroki-preprocessor-支持kroki渲染)
   * [自动渲染](#自动渲染)
      * [mdbook-admonish](#mdbook-admonish)
      * [mdbook-curly-quotes](#mdbook-curly-quotes)
      * [mdbook-tera](#mdbook-tera)
      * [sgoudham/mdbook-template](#sgoudhammdbook-template)
      * [zjp-CN/mdbook-theme](#zjp-cnmdbook-theme)
      * [mdbook-mark: 渲染高亮标签](#mdbook-mark-渲染高亮标签)
      * [mdbook-all-the-markdowns](#mdbook-all-the-markdowns)
      * [mdbook-wikilink](#mdbook-wikilink)
      * [mdbook-page-styles](#mdbook-page-styles)
      * [mdbook-note](#mdbook-note)
      * [mdbook-section-validator](#mdbook-section-validator)
      * [mdbook-quiz: 添加在线测验功能](#mdbook-quiz-添加在线测验功能)
         * [配置方式](#配置方式)
         * [注意<g-emoji class="g-emoji" alias="warning" fallback-src="https://github.githubassets.com/images/icons/emoji/unicode/26a0.png">⚠️</g-emoji>](#注意️)
         * [题型说明](#题型说明)
   * [其他格式](#其他格式)
      * [playscript: 戏剧脚本格式](#playscript-戏剧脚本格式)
      * [unevil-rs: 与mdbook无关，只是单独用来写ppt](#unevil-rs-与mdbook无关只是单独用来写ppt)
      * [Gooseberry - a Knowledge Base for the Lazy](#gooseberry---a-knowledge-base-for-the-lazy)
      * [ppt: 可以切换ppt还是markdown](#ppt-可以切换ppt还是markdown)
         * [举例(windows-alt+p|osx-option+p切换)](#举例windows-altposx-optionp切换)
         * [本地示例](#本地示例)
   * [这里是slides-only: 待完成内容](#这里是slides-only-待完成内容)
   * [资源链接](#资源链接)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Mon Sep 19 16:57:09 UTC 2022 -->

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

#### 默认支持

```rust
#![allow(unused)]

fn main() {
    println!("Hello, World!");
}
```

#### 指定不支持

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

#### 打开行数

- [output.html.playground](https://rust-lang.github.io/mdBook/format/configuration/renderers.html?highlight=book.toml#outputhtmlplayground)

```toml
[output.html.playground]
editable = false         # allows editing the source code
copyable = true          # include the copy button for copying code snippets
copy-js = true           # includes the JavaScript for the code editor
line-numbers = false     # displays line numbers for editable code
runnable = true          # displays a run button for rust code
```

> line-numbers Display line numbers on editable sections of code. Requires both editable and copy-js to be true. Defaults to false.

### 插入代码

#### 插入可运行代码: 只支持rust

#### 页面直接编辑代码: *, editable

## mdbook主题修改

[Theme - mdBook Documentation](https://rust-lang.github.io/mdBook/format/theme/index.html)

### 基本页面介绍

```shell
 tree mytheme -L 1                                                                                                                                ─╯
mytheme
├── FontAwesome
├── ayu-highlight.css
├── book.js
├── clipboard.min.js
├── css
├── favicon.png
├── favicon.svg
├── fonts
├── head.hbs
├── header.hbs
├── highlight.css
├── highlight.js
├── index.hbs
├── mod.rs
├── playground_editor
├── redirect.hbs
├── searcher
└── tomorrow-night.css

5 directories, 13 files
```

- index.hbs is the handlebars template.
- head.hbs is appended to the HTML <head> section.
- header.hbs content is appended on top of every book page.
- css/ contains the CSS files for styling the book.
- css/chrome.css is for UI elements.
- css/general.css is the base styles.
- css/print.css is the style for printer output.
- css/variables.css contains variables used in other CSS files.
- book.js is mostly used to add client side functionality, like hiding / un-hiding the sidebar, changing the theme, ...
- highlight.js is the JavaScript that is used to highlight code snippets, you should not need to modify this.
- highlight.css is the theme used for the code highlighting.
- favicon.svg and favicon.png the favicon that will be used. The SVG version is used by newer browsers.

# mdbook高级用法

## 关于book

1. 首先，这是mdbook serve/build之后生成的静态网站目录
2. src，和Summary同级的目录，就是网站根目录
3. src之外的内容不会被自动加入到book，所以无法访问。
4. 这里有三个办法解决静态文件访问的问题：
    - 生成book之后再复制进去，不过每次都需要重新复制
    - 把静态文件放在src里面，将会自动复制进去
    - 只对于js和css文件，可以用book的additional-css/js参数配置进去

## 关于mdbook serve panit-失败

> 这可能是由于本地电脑开了太多程序占用资源，mdbook serve资源不足，重启电脑可解决

## 关于主题修改(theme)
1. 在book.toml指定主题路径
2. 只有指定文件名才会被用来渲染网页

[Theme - mdBook Documentation](https://rust-lang.github.io/mdBook/format/theme/index.html?highlight=theme#theme)

# mdbook插件推荐

## 自动检查

### MDBook Link-Check

[Michael-F-Bryan/mdbook-linkcheck: A backend for `mdbook` which will check your links for you.](https://github.com/Michael-F-Bryan/mdbook-linkcheck)

## 自动生成

### global-search

[mattico/global-search: Global search for a collection of MDBooks](https://github.com/mattico/global-search)

### mdbook-toc

[badboy/mdbook-toc: A preprocessor for mdbook to add inline Table of Contents support.](https://github.com/badboy/mdbook-toc)

### mdbook-pagetoc: 添加页内侧边栏toc

[JorelAli/mdBook-pagetoc: A page table of contents for mdBook](https://github.com/JorelAli/mdBook-pagetoc)
![mdbook-toc-sample](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/mdbook-toc-sample.png)
[Chapter 1 - Sample](https://jorel.dev/mdBook-pagetoc/)

### mdbook-open-on-gh

[badboy/mdbook-open-on-gh: mdbook preprocessor to add a open-on-github link on every page](https://github.com/badboy/mdbook-open-on-gh)

### book-summary

> Automatically creates a SUMMARY.md file for your book (`mdbook/gitbook`)

[dvogt23/book-summary: 📔Book auto-summary 🦀🖤 (gitbook/mdBook)](https://github.com/dvogt23/book-summary)

### mdbook-suto-gen-summary

[knightflower1989/mdbook-auto-gen-summary: mdbook auto-gen-summary](https://github.com/knightflower1989/mdbook-auto-gen-summary)

### mdbook-transcheck

[dalance/mdbook-transcheck: Checker for translated mdbook](https://github.com/dalance/mdbook-transcheck)

### mdbook-man

[vv9k/mdbook-man: Generate manual pages from mdBooks!](https://github.com/vv9k/mdbook-man)

### ~~mdbook-bookimport~~: 使用标记块引入其他文件内容

> mdbook自带的include语法同时支持行数和标记来引入文件内容

[tailwind/mdbook-bookimport: Import code/text from other files into your mdbook - without the link rot.](https://github.com/tailwind/mdbook-bookimport)

### md2tex

> A small utility to convert markdown files to tex. Forked from md2pdf, with an added focus on mdbook conversions. Also
> with the goal of eventually contributing back upstream.

- Used by mdbook-latex to generate PDF's.

[lbeckman314/md2tex: A fork of tforgione's awesome md2pdf library, catered for mdbook.](https://github.com/lbeckman314/md2tex)

### mdbook-checklist

[ANSSI-FR/mdbook-checklist: mdbook preprocessor for generating checklists and indexes](https://github.com/ANSSI-FR/mdbook-checklist)

### mdbook-chapter-path: 可以用来生成面包屑导航

- [mdbook-chapter-path - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-chapter-path)

### mdBook Tag

[dylanowen/mdbook-tag](https://github.com/dylanowen/mdbook-tag)

### mdbook toc: 自动生成toc

- [mdbook-toc - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-toc)
- [badboy/mdbook-toc: A preprocessor for mdbook to add inline Table of Contents support.](https://github.com/badboy/mdbook-toc)

```shell
cargo install mdbook-toc
```

```admonish quote title='说两句'
不过我主要用github action自动解析后插入生成，这样用起来感觉更方便本地修改
```

### mdbook-footnote: 可以用于生成引用内容

- [mdbook-footnote - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-footnote)

### ~~mdBook-template~~: 不需要，直接修改主题

[sgoudham/mdbook-template: A mdbook preprocessor that allows the re-usability of template files with dynamic arguments](https://github.com/sgoudham/mdbook-template)

### trpl-zh-cn-pdf

> [KaiserY/trpl-zh-cn: Rust 程序设计语言（2021 edition 施工中）](https://github.com/KaiserY/trpl-zh-cn/)

[me1ting/trpl-zh-cn-pdf: trpl-zh-cn的mdBook风格的pdf，带全书签](https://github.com/me1ting/trpl-zh-cn-pdf)

### mdbook-cms: 自动生成Summary

> this will also walk your mdbook src dir and generate the book summary in /path/to/your/mdbook/src/SUMMARY.md

[AlongWY/mdbook-cms: A preprocessor bring cms to mdbook.](https://github.com/AlongWY/mdbook-cms)

### mdbook-open-on-gh: 添加打开github分支的功能

> 可以在页面底部添加对应源文件的超链接

- [mdbook-open-on-gh - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-open-on-gh)

### mdbook-readme: 解决readme与index不一致的问题

```admonish tip title='为什么需要转化'
mdbook生成的目录菜单，最上方的链接是指向index.html. 但是网址根目录又指向README.md。这里需要统一
```

[mdbook-readme - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-readme)

### mdbook-cmdrun: 提供强悍的终端执行功能

- [mdbook-cmdrun - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-cmdrun)

> 该插件内置了下列编译器，可以直接执行代码

1. Shell

```console
<!-- cmdrun ls -alh . -->
```

2. Bash Script

```console
<!-- cmdrun ../../materials/cmdrun/script.sh>
```

3. Python3

<!-- cmdrun python3 ../../materials/cmdrun/script.py -->

4. Rust

```rust
/ < / ! / - / - / cmdrun cmdrun/script.rs - ->
```

## 配置与替换

### mdbook-fluent: 可以用配置文件进行整理

[JakubKoralewski/mdbook-fluent: mdBook preprocessor for variable interpolation using the Fluent language](https://github.com/JakubKoralewski/mdbook-fluent)

```admonish tip title='关于fluent'
fluent主要是用来本地化配置
- [Project Fluent](https://projectfluent.org/)
- [Home · projectfluent/fluent Wiki](https://github.com/projectfluent/fluent/wiki/)
- 语法说明：[Introduction · GitBook](https://projectfluent.org/fluent/guide/)
1. book.toml可以用dir参数配置查找fluent文件的目录路径
2. **目前暂未试验成功**
```

```none
\{\{\#\fluent ../../../materials/global.motto}}
```

```
\{\{\#\fluent global.hello}}
```

### mdbook-variables: 在book.toml配置全局变量

- [mdbook-variables - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-variables)
- [tglman / mdbook-variables · GitLab](https://gitlab.com/tglman/mdbook-variables)

```shell
# book.toml
[preprocessor.variables.variables]
motto = "保持批判，有所取舍，知行合一，方见真我"
```

```shell
# here
\{\{motto}}
```

> {{motto}}

### mdbook-regex: 对内容进行正则替换

> 可以看作是mdbook-variables的升级版

- [mdbook-regex - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-regex)

## 绘图

### mdBook Graphviz: 支持graphviz的dot语言

[dylanowen/mdbook-graphviz](https://github.com/dylanowen/mdbook-graphviz)

https://github.com/badboy/mdbook-open-on-gh)

### svgbob plugin for mdbook

[boozook/mdbook-svgbob: SvgBob mdbook preprocessor which swaps code-blocks with neat SVG.](https://github.com/boozook/mdbook-svgbob)

### mdbook-skill-tree: 添加技能树渲染

- [skill-tree/skill_tree.md at master · nikomatsakis/skill-tree](https://github.com/nikomatsakis/skill-tree/blob/master/book/src/skill_tree.md)
- 在线示例: [Skill Tree - Skill-tree Book](https://nikomatsakis.github.io/skill-tree/)

### mdbook-chart: 添加c3.js图表渲染功能

> 主要是通过添加额外js、css文件

- what is c3js: [C3.js | D3-based reusable chart library](https://c3js.org/)
- [knightflower1989/mdbook-chart: mdbook chart](https://github.com/knightflower1989/mdbook-chart)

### mdbook-puml: plantuml渲染

> 比mdbook-plantuml更好用
[mdbook-puml - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-puml)

## 绘图合集：kroki

![image-20220715114804075](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220715114804075.png)

- [Kroki!](https://kroki.io/#examples)
- [Kroki! Examples](https://kroki.io/examples.html)

### IntelliPikchr: IDEA内置插件

- [IntelliPikchr - IntelliJ IDEs Plugin | Marketplace](https://plugins.jetbrains.com/plugin/17624-intellipikchr)

> Split editor with preview pane for **.pikchr** files, using kroki.io or self-hosted server for rendering

### mdbook-kroki-preprocessor: 支持kroki渲染

> kroki可以看作多种图表语言的统一接口

- [mdbook-kroki-preprocessor - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-kroki-preprocessor)

```admonish info title='md语法'
The code block's language has to be kroki-<diagram type>.
- kroki-mermaid
- kroki-plantuml
```

```shell
cargo install mdbook-kroki-preprocessor
```

## 自动渲染

### mdbook-admonish

[tommilligan/mdbook-admonish: A preprocessor for mdbook to add Material Design admonishments.](https://github.com/tommilligan/mdbook-admonish)

### mdbook-curly-quotes

> mdBook preprocessor that replaces straight quotes with curly quotes, except within code blocks or code spans.
> It does the same as the curly-quotes option of the mdBook HTML renderer. The only advantage is that it can be applied
> to any renderer.
[arminha/mdbook-curly-quotes: mdBook preprocessor that replaces straight quotes with curly quotes](https://github.com/arminha/mdbook-curly-quotes)

### mdbook-tera

> 基于tera模版引擎渲染
[avitex/mdbook-tera: Tera preprocessor for mdBook](https://github.com/avitex/mdbook-tera)
[Keats/tera: A template engine for Rust based on Jinja2/Django](https://github.com/Keats/tera)

### sgoudham/mdbook-template

> 可以自定义页脚的图像

[sgoudham/mdbook-template: A mdbook preprocessor that allows the re-usability of template files with dynamic arguments](https://github.com/sgoudham/mdbook-template)

### zjp-CN/mdbook-theme

> 提供更多主题自定义选项

- [zjp-CN/mdbook-template: Yield a mdbook demo with mdbook-theme and a yml file for github action automation and page publication.](https://github.com/zjp-CN/mdbook-template)
- [mdbook-theme - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-theme)

### mdbook-mark: 渲染高亮标签<mark></mark>

[blazood/mdbook-mark: this is a mdbook preprocessor which can render ==== to <mark></mark>](https://github.com/blazood/mdbook-mark#readme)

### mdbook-all-the-markdowns

![all-the-things](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/all-the-things.png)

[bombsimon/mdbook-all-the-markdowns: 🗃️ Preprocessor for mdbook to render all the markdowns!](https://github.com/bombsimon/mdbook-all-the-markdowns)

### mdbook-wikilink

[NOBLES5E/mdbook-wikilink: Support for wikilinks on mdBook.](https://github.com/NOBLES5E/mdbook-wikilink)

### mdbook-page-styles

[ABCsOf/mdbook-page-styles: An mdbook preprocessor to apply styles to specific pages and elements.](https://github.com/ABCsOf/mdbook-page-styles)

### mdbook-note

[Aedius/mdbook-note: preprocessor for mdbook to add organized chapter containing fragment from the rest of the book](https://github.com/Aedius/mdbook-note)

### mdbook-section-validator

[younata/mdbook-section-validator: mdBook preprocessor for defining conditionally valid sections](https://github.com/younata/mdbook-section-validator)

### mdbook-quiz: 添加在线测验功能

- [mdbook-quiz - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-quiz)

```admonish warn title='自动生成'
该插件会在src自动创建生成mdbook-quiz目录，里面包含embed.css和embed.js
```

```shell
cargo install mdbook-quiz
```

```shell
git clone https://github.com/willcrichton/mdbook-quiz
cd mdbook-quiz
cargo install --path .
```

- [live demo](https://willcrichton.net/mdbook-quiz/)
- [willcrichton/mdbook-quiz: Interactive quizzes for Markdown](https://github.com/willcrichton/mdbook-quiz)

#### 配置方式

> You can configure mdbook-quiz by adding options to the [preprocessor.quiz] section of book.toml. The options are:

1. validate (boolean):
   If true, then mdbook-quiz will validate your quiz TOML files using the validator.js script installed with
   mdbook-quiz. You must have NodeJS installed on your machine and PATH for this to work.
2. fullscreen (boolean):
   If true, then a quiz will take up the web page's full screen during use.
3. cache-answers (boolean):
   If true, then the user's answers will be saved in their browser's localStorage. Then the quiz will show the user's
   answers even after they reload the page.

#### 注意⚠️

~~~admonish warn title='使用说明'

1. 该插件默认只是在src里面自动生成mdbook-quiz, 里面包含必须但js和css文件
2. 默认情况下只能在src目录下生效，与mdbook-quiz同级。
3. 目前改成直接从book.toml引入，就可以全局使用
4. 注意引入测试文件的代码行上下需要为空行

```none

\{\{\#\quiz ../../materials/quizzes/rust-variables.toml}}

\{\{\#\quiz ../../materials/quizzes/quiz.toml}}

```
~~~

#### 题型说明

~~~admonish info title='测试题类型'
```toml
[[questions]]
type = "MultipleChoice"
prompt.prompt = "What does it mean if a variable `x` is immutable?"
prompt.choices = [
  "`x` is stored in the immutable region of memory.",
  "After being defined, `x` can be changed at most once.",
  "`x` cannot be changed after being assigned to a value.",
  "You cannot create a reference to `x`."
]
answer.answer = 2
context = """
Immutable means "not mutable", or not changeable.
"""

[[questions]]
type = "ShortAnswer"
prompt.prompt = "What is the keyword used after `let` to indicate that a variable can be mutated?"
answer.answer = "mut"
context = """
For example, you can make a mutable variable `x` by writing: `let mut x = 1`.
"""

[[questions]]
type = "Tracing"
prompt.program = """
fn main() {
  let x = 1;
  println!("{x}");
  x += 1;
  println!("{x}");
}
"""
answer.doesCompile = false
answer.lineNumber = 4
context = """
This is a compiler error because line 4 tries to mutate `x` when `x` is not marked as `mut`.
"""
```
~~~

{{#quiz ../../materials/quizzes/rust-variables.toml}}

{{#quiz ../../materials/quizzes/quiz.toml}}

## 其他格式

### playscript: 戏剧脚本格式

- [ShotaroTsuji/mdplayscript](https://github.com/ShotaroTsuji/mdplayscript)

### unevil-rs: 与mdbook无关，只是单独用来写ppt

[oknozor/unveil-rs: Unveil Rs is a tool to create presentations from markdown inspired by reveal.js, mdbook and zola.](https://github.com/oknozor/unveil-rs)

[在线示例](https://oknozor.github.io/unveil-rs/)

### Gooseberry - a Knowledge Base for the Lazy

> 一个很棒的工具，可以直接将mdbook转为知识库

[out-of-cheese-error/gooseberry: A command line utility to generate a knowledge base from Hypothesis annotations](https://github.com/out-of-cheese-error/gooseberry)

![obsidian_example-2](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/obsidian_example-2.png)

### ppt: 可以切换ppt还是markdown

> 这个插件将html算是玩的比较深入

- [mdbook-presentation-preprocessor - crates.io: Rust Package Registry](https://crates.io/crates/mdbook-presentation-preprocessor)

- [FreeMasen/mdbook-presentation-preprocessor: A preprocessor for utilizing an MDBook as slides for a presentation.](https://github.com/FreeMasen/mdbook-presentation-preprocessor)

#### 举例(windows-alt+p|osx-option+p切换)

~~~admonish info title='举例'
# An Interesting Thing
> Press `alt+p` to toggle which version is displayed.
> Open the console to see the notes printed there

$web-only$
Here is a much longer explanation about what this
interesting thing is and how interesting you might find it.

To elaborate, it is extremely interesting.
$web-only-end$

$slides-only$
## A list of things
- Fact one is intriguing
- Fact two is piquing my interest
- Fact three has me down right flabbergasted
- Fact four is almost obscene
$slides-only-end$

$notes$
- Don't for get to mention this
- And This
- And This
$notes-end$
~~~

- web-only

![image-20220716181352654](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220716181352654.png)

- Slides-only

  ![image-20220716181430206](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220716181430206.png)

- notes

  ![image-20220716181503831](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220716181503831.png)

#### 本地示例

$web-only$
这里是默认内容，web-only
$web-only-end$

$slides-only$

## 这里是slides-only: 待完成内容

- Fact one is intriguing
- Fact two is piquing my interest
- Fact three has me down right flabbergasted
- Fact four is almost obscene
  $slides-only-end$

$notes$

- 未完待续！
  $notes-end$

## 资源链接

- [rust-lang/mdBook: Create book from markdown files. Like Gitbook but implemented in Rust](https://github.com/rust-lang/mdBook)
- [Introduction - mdBook Documentation](https://rust-lang.github.io/mdBook/)

- [Git Large File Storage | Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.](https://git-lfs.github.com/)

- [mdBook-specific features - mdBook Documentation](https://rust-lang.github.io/mdBook/format/mdbook.html)
- [mdbook - Keywords - crates.io: Rust Package Registry](https://crates.io/keywords/mdbook)
