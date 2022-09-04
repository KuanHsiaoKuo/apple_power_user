# python处理脚本收集

<!--ts-->
* [python处理脚本收集](#python处理脚本收集)
   * [将字幕文件转为json](#将字幕文件转为json)
      * [spaCy自然语言处理](#spacy自然语言处理)
      * [源码](#源码)
   * [ffmpeg合并视频文件](#ffmpeg合并视频文件)
   * [IINA与ffmpeg给视频添加章节](#iina与ffmpeg给视频添加章节)
      * [ffmpeg](#ffmpeg)
      * [mpv screenshot template](#mpv-screenshot-template)
      * [思路](#思路)
      * [源码](#源码-1)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sun Sep  4 14:29:04 UTC 2022 -->

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
{{#include scripts/srt_to_json.py:1:}}
```

## ffmpeg合并视频文件

```python
{{#include scripts/merge_videos.py:1:}}
```

## IINA与ffmpeg给视频添加章节

### ffmpeg

- [How to Add Chapters to MP4s with FFmpeg - Kyle Howells](https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg)

```shell
ffmpeg -i part1.mp4 -f ffmetadata part1.txt
ffmpeg -i part1.mp4 -i part1.txt -map_metadata 1 -codec copy part1_insert.mp4
```

### mpv screenshot template

- [mpv.io#screenshot](https://mpv.io/manual/stable/#screenshot)

```admonish info
screenshot-template: %p.%{filename}
1. %p: 截屏的时间，可以排序。这样方便后续按时间插入新章节。

```


### 思路

```plantuml
{{#include ../../../materials/plantumls/video_bookmarks.puml:1:}}
```

### 源码

```python
{{#include scripts/chapter_videos.py:1:}}
```
