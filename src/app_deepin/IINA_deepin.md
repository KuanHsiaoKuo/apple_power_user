# IINA深度使用

<!--ts-->


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sun Nov 27 15:02:30 UTC 2022 -->

<!--te-->

## 简介

Project IINA，是一个基于 mpv、契合 macOS 设计风格、力求做到最佳用户体验、轻便且功能强大的视频播放器项目。

## MPV指令定制与配置文件

### 截图格式自定义

- [mpv.io#screenshot](https://mpv.io/manual/stable/#screenshot)

```admonish info
screenshot-template: %{filename}-%p
1. 按照视频文件名先分段，方便统一存放
> 本来打算用screenshot-directory参数，但是要报错，就算了
2. %p: 截屏的时间，可以排序。这样方便后续按时间插入新章节。
```

![CleanShot 2022-09-06 at 21.52.28@2x](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/CleanShot%202022-09-06%20at%2021.52.28%402x.png)

### 设置播放速度

```admonish info
Meta+[ multiply speed 0.5
Meta+] add speed 0.25
Alt+Meta+[ multiply speed 0.9091
Alt+Meta+] multiply speed 1.1
Meta+\ set speed 1.0
```

1. 非关键内容快速过
2. 关键内容放慢速度

### 完整配置文件
