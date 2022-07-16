# 关于marginnote使用自定义模版
> 由于marginnote自带的模版太简单，所以找了一下如何使用自定义模版导出
<!--ts-->
* [关于marginnote使用自定义模版](#关于marginnote使用自定义模版)
   * [一、自定义模版导出：不可行](#一自定义模版导出不可行)
   * [二、自动在anki中修改模版](#二自动在anki中修改模版)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sat Jul 16 09:36:05 UTC 2022 -->

<!--te-->
## 一、自定义模版导出：不可行
- [Anki 導出自定義模板後，在 MN 中 Fields 丢失 - 方法、技巧、工作流 / Anki专区——记忆宫殿 - MarginNote 中文社区](https://bbs.marginnote.cn/t/topic/17640)
- [功能点快速参考手册](https://manual.marginnote.cn/review/#anki%E5%8D%A1%E7%89%87%E7%BB%84%E5%AD%97%E6%AE%B5%E5%90%AB%E4%B9%89)
## 二、自动在anki中修改模版
- 对照字段更换模版可行
- 需要解决MNLink的超链接问题
- [HTML Window source - AnkiWeb](https://ankiweb.net/shared/info/1214415810)
- showdown卡片模版添加MNLink字段
- 只要卡片标题不修改，就不会覆盖更新
- 正面备注都会出现在标题
- 背面备注都在back里面

最终结果放在[《自定义anki模版》](../Anki_around/custom_md_template.md)