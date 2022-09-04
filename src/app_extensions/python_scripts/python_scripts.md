# python处理脚本收集

<!--ts-->
* [python处理脚本收集](#python处理脚本收集)
   * [将字幕文件转为json](#将字幕文件转为json)
      * [spaCy自然语言处理](#spacy自然语言处理)
      * [源码](#源码)
   * [ffmpeg合并视频文件](#ffmpeg合并视频文件)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sun Sep  4 09:41:51 UTC 2022 -->

<!--te-->

## 将字幕文件转为json

### spaCy自然语言处理

> 上面那个脚本转化的文本并没有标点符号断句等内容，所以还需要用NLP来优化。 这里的核心还在于使用spaCy对文本进行自然语言处理。

- [自然语言处理就这么简单有趣 - 知乎](https://zhuanlan.zhihu.com/p/63110761)
- [spacy Can't find model 'en_core_web_sm' on windows 10 and Python 3.5.3 :: Anaconda custom (64-bit) - Stack Overflow](https://stackoverflow.com/questions/54334304/spacy-cant-find-model-en-core-web-sm-on-windows-10-and-python-3-5-3-anacon)
- [spaCy · Industrial-strength Natural Language Processing in Python](https://spacy.io/)
- [Prodigy · An annotation tool for AI, Machine Learning & NLP](https://prodi.gy/)

### 源码

```python
{{#include scripts/srt_to_json.py:1:145}}
```

## ffmpeg合并视频文件


```python
{{#include scripts/merge_videos.py:1:45}}
```
