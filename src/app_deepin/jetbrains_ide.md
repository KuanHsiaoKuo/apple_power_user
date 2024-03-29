# Jetbrains系列IDE共性与特性介绍

<!--ts-->


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sun Nov 27 15:02:32 UTC 2022 -->

<!--te-->

## 共性

### 快捷键整理

#### python配置虚拟环境

1. cmd+; -> 新增虚拟环境
2. add configuration -> 将虚拟环境配置给当前项目

> 可以配置远程虚拟环境/docker环境

![CleanShot 2022-10-19 at 16.37.06@2x](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/CleanShot%202022-10-19%20at%2016.37.06%402x.png)

### Tab方式打开项目

由于本人喜欢一个窗口打开多个项目，然后用tab方式来进行项目切换，所以专门找了一下设置方式：

1. macOS设置：系统偏好设置 > 通用 > 首选以标签页方式打开 > 始终

![CleanShot 2022-06-30 at 11.00.02@2x](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/CleanShot%202022-06-30%20at%2011.00.02%402x.png)

```admonish tip title='全局有效'
注意：这个设置对其他文档类app也有效
```

2. Jetbrains设置是否新窗口打开

- [Open, close, and move projects | IntelliJ IDEA](https://www.jetbrains.com/help/idea/open-close-and-move-projects.html#open-projects-new-same-window)

### 配置代理

![image-20220702163846633](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220702163846633.png)

### 指定项目root

> 由于idea等默认需要一个source root，所以有时候打开项目的路径不是它可用的，就可以自己右键指定文件目录设置为source root

![image-20220926110436737](https://raw.githubusercontent.com/KuanHsiaoKuo/writing_materials/main/imgs/image-20220926110436737.png)