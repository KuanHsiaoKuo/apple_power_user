# OSX迁移基础配置

# 一、资料打包迁移

## 代码：github/gitee/gitlab

## app自存储（iCloud）：DT、Xmind、mindnode、Drafts、Marginnote
- DT: 本地数据库
- xmind/mindnode/drafts/marginnote：iCloud

## 分类打包：

- 图片、视频
- pdf等电子书
- 项目资料：按照项目整理
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

## 3. github ssh key

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