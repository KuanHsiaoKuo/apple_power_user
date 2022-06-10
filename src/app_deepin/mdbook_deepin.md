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
   * [资源链接](#资源链接)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Fri Jun 10 06:46:00 UTC 2022 -->

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
# }
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


## 资源链接

- [rust-lang/mdBook: Create book from markdown files. Like Gitbook but implemented in Rust](https://github.com/rust-lang/mdBook)
- [Introduction - mdBook Documentation](https://rust-lang.github.io/mdBook/)

- [Git Large File Storage | Git Large File Storage (LFS) replaces large files such as audio samples, videos, datasets, and graphics with text pointers inside Git, while storing the file contents on a remote server like GitHub.com or GitHub Enterprise.](https://git-lfs.github.com/)

- [mdBook-specific features - mdBook Documentation](https://rust-lang.github.io/mdBook/format/mdbook.html)