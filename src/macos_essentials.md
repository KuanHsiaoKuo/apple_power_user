# OSX迁移基础配置

<!--ts-->
* [OSX迁移基础配置](#osx迁移基础配置)
* [一、资料打包迁移:](#一资料打包迁移)
   * [代码：github/gitee/gitlab](#代码githubgiteegitlab)
   * [app自存储：](#app自存储)
      * [wechat: 备份数据之后再恢复](#wechat-备份数据之后再恢复)
      * [DT:](#dt)
         * [本地数据库配置](#本地数据库配置)
         * [PDF Expert: 作为dt中pdf的外置阅读器](#pdf-expert-作为dt中pdf的外置阅读器)
         * [typora：作为dt中md的外置阅读器](#typora作为dt中md的外置阅读器)
         * [自动化脚本](#自动化脚本)
         * [SingleFile: 可以将网页保存为单独文件后存入dt](#singlefile-可以将网页保存为单独文件后存入dt)
      * [Eagle: 本地数据库配置](#eagle-本地数据库配置)
      * [xmind/mindnode/drafts/marginnote：iCloud](#xmindmindnodedraftsmarginnoteicloud)
   * [分类打包：](#分类打包)
* [二、系统重装](#二系统重装)
* [三、系统设置](#三系统设置)
* [四、最优安装顺序](#四最优安装顺序)
   * [1. ClashX](#1-clashx)
   * [2. iTerm2](#2-iterm2)
   * [3. github/gitlab ssh key](#3-githubgitlab-ssh-key)
   * [4. vim config](#4-vim-config)
   * [5. karabiner](#5-karabiner)
   * [6. manico/moom/popclip/Alfred](#6-manicomoompopclipalfred)
   * [7. iTerm2 Around:](#7-iterm2-around)
   * [8. DT/Marginnote3/xmind](#8-dtmarginnote3xmind)
   * [9. Jetbrains Sync](#9-jetbrains-sync)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Mon Aug  8 03:45:23 UTC 2022 -->

<!--te-->

# 一、资料打包迁移: 
> 定期整理到~/Migrations, 备份到外接硬盘。

> 主要为了避免存档大文件自动保存到iCloud

> 后期未整理的内容可以放在文档里面，同步在iCloud上

> 在Finder左侧添加Migrations快捷路径 
## 代码：github/gitee/gitlab

## app自存储：
### wechat: 备份数据之后再恢复
### DT:
#### 本地数据库配置
1. 安装后登陆[网站](https://www.devontechnologies.com)激活
2. 配置css显示：Preferences >> Web >> Style Sheet >> 选择dt_extras里面的样式表
3. Menu >> File >> Open Database...
4. 打开～/Migrations/DEVONThink_Databases
5. 打开iCloud同步：Preferences >> Sync >> check iCloud(CloudKit)
> 这将会合并在线数据库与步骤3导入的数据库，耗时较长
#### PDF Expert: 作为dt中pdf的外置阅读器
#### typora：作为dt中md的外置阅读器
1. picGo上传配置: [Upload Images - Typora Support](https://support.typora.io/Upload-Image/)
2. [PicGo](https://molunerfinn.com/PicGo/)
3. 快捷键配置及配置文件同步: [Shortcut Keys - Typora Support](https://support.typora.io/Shortcut-Keys/#change-shortcut-keys)
#### 自动化脚本
1. dt_md_export: dt_extras/scripts
```applescript
tell application id "DNtp"
	set theSelection to the selection
	if theSelection is {} then error "Please select some documents."
	set md_result to ""
	repeat with this_record in theSelection
		set md_link to (("[" & name of this_record as string) & "]" & "(" & reference URL of this_record as string) & ")"
		set md_result to md_result & "- " & md_link & return & return
	end repeat
	--display dialog md_result
	set the clipboard to md_result
end tell
```
#### SingleFile: 可以将网页保存为单独文件后存入dt
- [gildas-lormeau/SingleFile: Web Extension for Firefox/Chrome/MS Edge and CLI tool to save a faithful copy of an entire web page in a single HTML file](https://github.com/gildas-lormeau/SingleFile#command-line-interface)
- 这个方式可以完美保存网页，将所有图片、代码都放在一个文件中
### Eagle: 本地数据库配置
1. 保存路径：～/Migrations/Eagle_Libraries
### xmind/mindnode/drafts/marginnote：iCloud

## 分类打包：

- 图片、视频: ~/Documents/media
- pdf等电子书: 有用的放dt，没用的删除
- 项目资料：按照项目整理，～/Documents/Projects
- logins: 放在~/.ssh/logins里面的登陆用脚本

---

# 二、系统重装

```
关机 >> 重启的同时按住cmd+R >> 磁盘工具 >> 抹除 >> 重装
```

> 重启MAC，按住cmd+R直到屏幕上出现苹果的标志和进度条，进入Recovery模式；

---
# 三、系统设置

- 触控板拖移：系统偏好设置 >> 辅助功能 >> 指针控制 >> 触控板选项：启动拖移 > 三指拖移

- 系统自带配置目录：

```
cd ~/.config
```

里面至少有下列配置文件夹：

- clash
- karabiner
- iTerm2

---

# 四、最优安装顺序

## 1. ClashX

## 2. iTerm2

> 详见iterm2

## 3. github/gitlab ssh key

```
ssh-keygen -t rsa -C "your_email@example.com"
```

## 4. vim config

[KuanHsiaoKuo/vim_config: my custom vim configurations](https://github.com/KuanHsiaoKuo/vim_config)

## 5. karabiner

- 首先GUI配置两个按键切换：caps_lock -> left_control; right_command -> escape
- 然后会自动生成配置文件：

```
~/.config/karabiner/karaginer.json
```

- 将karabiner.md里面的配置文件复制进去即可

## 6. manico/moom/popclip/Alfred

- manico: 配置快捷键

```
iTerm2: shift+space
Appstore: option+a
```

- moom：设置快捷建cmd+m
- alfred: 依次安装alfred_workflows中的workflow

## 7. iTerm2 Around:
- iterm2/iterm2_around.sh

## 8. DT/Marginnote3/xmind

## 9. Jetbrains Sync

包含：IDEA、Pycharm、Webstorm、Goland等 Jetbrains有两种同步配置方式, 都是插件，首次安装时自带：

- IDE settings sync: 使用jetbrains账号同步，可以直接同步插件
- settings repository: 使用git同步配置，不包含插件。

> 注意，二者只能激活其一，其中第二种激活后会自动覆盖第一种方式。

> 推荐第一种方式，同步更全面无痕。

> 第二种是idea默认开启，需要主动去关闭：
```
Preferences >> Plugins >> search "Settings Repository" >> unabled
```