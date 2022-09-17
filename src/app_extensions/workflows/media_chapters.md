# 多媒体资料章节化工作流

<!--ts-->
<!--te-->

## 缘起

一直以来我主要倾向于读文本资料来学习，其实人的接收讯息方式还有视觉和听觉，遂决定整理出一套将多媒体资料进行管理的想法。

这里的多媒体主要指视频、音频和图片，其中图片的管理主要是用github图床+eagle。而视频和音频一旦过长，在寻找知识点的时候就很麻烦，经过验证，发现可以用ffmpeg给多媒体文件的方式添加章节。

## Step1. 相关视频/音频合并-ffmpeg

- [ffmpeg合并视频文件](https://kuanhsiaokuo.github.io/apple_power_user/app_extensions/python_scripts/python_scripts.html#ffmpeg%E5%90%88%E5%B9%B6%E8%A7%86%E9%A2%91%E6%96%87%E4%BB%B6)

## Step2. 使用IINA结合MPV的指令自动化创建章节

- [iina与ffmpeg给视频添加章节](https://kuanhsiaokuo.github.io/apple_power_user/app_extensions/python_scripts/python_scripts.html#iina%E4%B8%8Effmpeg%E7%BB%99%E8%A7%86%E9%A2%91%E6%B7%BB%E5%8A%A0%E7%AB%A0%E8%8A%82)

## Step3. 将章节文本压入到多媒体文件-ffmpeg

## Step4. 播放工具选择

- 电脑端可以选择IINA，基于MPV
- 移动端选择VLC Player

这里再放一下二者的区别：

- [VLC vs mpv, Which one is the best? - LinuxForDevices](https://www.linuxfordevices.com/tutorials/linux/vlc-vs-mpv)
- [开源视频播放器介绍 - 掘金](https://juejin.cn/post/6844903662796406792)