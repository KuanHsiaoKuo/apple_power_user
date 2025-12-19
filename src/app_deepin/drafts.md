# drafts深度使用技巧

<!--ts-->


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Fri Dec 19 17:17:52 UTC 2025 -->

<!--te-->

## 使用技巧

### 双向链接

- [Wiki-Style Cross-Linking Drafts](https://docs.getdrafts.com/docs/drafts/cross-linking#wiki-style-cross-linking-drafts)

![](https://docs.getdrafts.com/images/docs/drafts/linking-drafts.png)

官方的叫法是 Wiki-Style Cross-Linking，这是一个很不错的功能，方便同一个主题的草稿下跳转，既可以链接文章，也可以进行关键词搜索。先在草稿中输入 [[，然后 Drafts
就会自动跳出待选的草稿标题，点击即可创建跳转链接。

#### 相关actions

- [New Linked Draft | Drafts Directory](https://actions.getdrafts.com/a/2AO)
- [run shortcuts from wikilink | Drafts Directory](https://actions.getdrafts.com/a/1xD)
- [Add Backlinks | Drafts Directory](https://actions.getdrafts.com/a/1rv)
- [Check Wikilinks | Drafts Directory](https://actions.getdrafts.com/a/1ru)
- [Insert Wikilink | Drafts Directory](https://actions.getdrafts.com/a/1qj)
- [New draft from selection/line with back-link | Drafts Directory](https://actions.getdrafts.com/a/1mh)
- [Search for Back Links | Drafts Directory](https://actions.getdrafts.com/a/1fY)

### 模版写作

### 草稿引用

在版本 29 更新中，更新了一个名为「Insert Full Text of Other Drafts」的功能，翻译过来就是草稿全文的引用。它的语法和标准 Markdown 有些类似，在 Markdown 中引用是一个 >，而 Drafts
中如果需要对某个草稿进行全文引用，可以输入 << 进行选择引用。输入两个 < 之后，Drafts 弹出了草稿选择列表，选择需要引用插入的草稿，Drafts
就会直接将这段文本复制进来，而不用手动切会草稿列表，复制之后再粘贴过来。如果在 Drafts 中之前有很多零碎的想法，在需要将这些想法汇总，写成具有条理性的文章，那么这个功能就可以帮用户快速引用其他草稿。

## 动作收集

### md格式化

> 只支持macOS

- [Is there anyway to format the markdown? - General Discussion - Drafts Community](https://forums.getdrafts.com/t/is-there-anyway-to-format-the-markdown/7850/5)
- [Format Markdown | Drafts Directory](https://actions.getdrafts.com/a/1bP)

```shell
npm install -g prettier 
```

### preview

- [Preview - Adjustable | Drafts Directory](https://actions.getdrafts.com/a/2Bz)

## 自定义: 需要pro版本

### 打开开发者模式

- [什么是开发者模式](https://docs.getdrafts.com/extending/development#what-is-developer-mode-pro)

### 自定义语法高亮

- [Creating Syntaxes - Drafts User Guide](https://docs.getdrafts.com/docs/extending/development/syntax-format)

### 自定义主题

- [Creating Themes - Drafts User Guide](https://docs.getdrafts.com/docs/extending/development/theme-format)