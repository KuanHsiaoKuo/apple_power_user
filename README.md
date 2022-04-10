# OSX迁移基础配置

## 系统重装

```
关机 >> 重启的同时按住cmd+R >> 磁盘工具 >> 抹除 >> 重装
```
> 重启MAC，按住cmd+R直到屏幕上出现苹果的标志和进度条，进入Recovery模式；

## 系统设置
- 触控板拖移：系统偏好设置 >> 辅助功能 >> 指针控制 >> 触控板选项：启动拖移 > 三指拖移


## 系统自带配置目录：

```
cd ~/.config
```
里面至少有下列配置文件夹：

- clash
- karabiner
- iTerm2


## 最优安装顺序
### 1. ClashX
### 2. iTerm2
### 3. github ssh key
### 4. vim config
[KuanHsiaoKuo/vim_config: my custom vim configurations](https://github.com/KuanHsiaoKuo/vim_config)
### 5. karabiner
- 首先GUI配置两个按键切换：caps_lock -> left_control; right_command -> escape
- 然后会自动生成配置文件：
```
~/.config/karabiner/karaginer.json
```
- 将karabiner.md里面的配置文件复制进去即可
### 6. manico/moom/popclip/Alfred
- manico: 配置快捷键
```
iTerm2: shift+space
Appstore: option+a
```
- moom：设置快捷建cmd+m
- alfred: 依次安装alfred_workflows中的workflow
### 7. zsh/tmux config + relate plugins
[KuanHsiaoKuo/zsh_config](https://github.com/KuanHsiaoKuo/zsh_config)
