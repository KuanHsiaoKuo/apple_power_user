# 自定义Anki模版

> 由于本人最为习惯md语法，再加上mermaid、语法高亮等需求，所以折腾一下，制作了一个anki卡片模版: showdown-hightlight-mermaid. 另外在[《marginnote使用自定义模版》](../workflows/marginnote_anki.md)一文中的折腾过程，添加了一个MNLink的字段。

<!--ts-->
* [自定义Anki模版](#自定义anki模版)
   * [正面模版](#正面模版)
   * [背面模版](#背面模版)
   * [说明](#说明)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Wed Jun 15 03:11:42 UTC 2022 -->

<!--te-->

## 正面模版

![image-20220606234758347](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220606234758347.png)

```javascript
<div class="section">
    <div class="Description md-content">{{Question}}</div>
</div>

<script>
    function addStylesheet(src, callback) {
    var s = document.createElement('link');
    s.rel = 'stylesheet';
    s.href = src;
    s.onload = callback;
    document.head.appendChild(s);
}
    function addScript(src, callback) {
    var s = document.createElement('script');
    s.src = src;
    s.type = "text/javascript";
    s.onload = callback;
    document.body.appendChild(s);
}

    function addMermaid() {
    // 开始mermaid配置
    addScript(mermaidUrl, function () {
        let config = {
            startOnLoad: true,
            theme: 'neutral',
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true,
                curve: 'Basis'
            },
            securityLevel: 'loose'
        }
        //mermaid.initialize(config)
        mermaid.init()
    });
}

    function replaceAllWhitespaceWithSpace(str) {
    return str.replace(/[\t\v\f \u00a0\u2000-\u200b\u2028-\u2029\u3000]/g, ' ');
}
    // anki本地存放多媒体文件路径： ~/Library/Application Support/Anki2/
    <account>/collection.media
        var highlightcssUrl = "_highlight.default.min.css";
        var showdownsCssUrl = "_showdowns.min.css"
        var showdownUrl = "_showdown.min.js";
        var showdownsUrl = "_showdowns.min.js";
        // https://cdn.bootcss.com/mermaid/8.0.0-rc.8/mermaid.min.js
        var mermaidUrl = "_mermaid.min.js";
        var highlightjsUrl = "_highlight.min.js";
        addStylesheet(highlightcssUrl, function () {});
        addStylesheet(showdownsCssUrl, function () {});
        addScript(showdownUrl, function () {
            addScript(highlightjsUrl, function () {
                function processShowdownDivs() {
                    var showdownConverter = new showdown.Converter({tables: true}); // 打开表格支持
                    showdownConverter.setFlavor('github');
                    document.querySelectorAll('div.md-content').forEach((div) => {
                        var rawText = div.innerText.replace(/<\/div>/g, ""); // div.innerHTML.replace(/<\/div>/g, ""); //innerText;
                        var classes = div.className.replace(/md-content/g, "");
                        var text = replaceAllWhitespaceWithSpace(rawText); //.replace(/<br>|<div>/g, "\n");
                        var html = showdownConverter.makeHtml(text);
                        var newDiv = document.createElement('div');
                        newDiv.innerHTML = html;
                        newDiv.className = classes;

                        newDiv.querySelectorAll('pre code').forEach((block) => {
                            hljs.highlightBlock(block);
                        });

                        div.parentNode.insertBefore(newDiv, div.nextSibling);
                        div.style.display = 'none';
                        addMermaid();
                    });
                };

                processShowdownDivs();
            });

        });

</script>
```

## 背面模版

![image-20220606234940109](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220606234940109.png)

```html
{{FrontSide}}

<hr id=answer>

<div class="section">
    <div id="back" class="Description md-content">感悟：</br>{{Tips}}</div>
</div>

<div class="section">
    <div id="back" class="Description md-content">回答： </br>{{Answer}}</div>
</div>

<div class="section">
    <div id="back" class="Description md-content">来源: </br>{{Origin}}</div>
</div>
{{MNLink}}
```

## 说明

1. anki本地存放多媒体文件路径：

```shell
~/Library/Application Support/Anki2/<account>/collection.media
```

2. 相关js文件可在github main分支的scripts/anki_md_js里面找到
