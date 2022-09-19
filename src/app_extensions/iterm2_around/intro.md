# iTerm2配置

<!--ts-->
* [iTerm2配置](#iterm2配置)
   * [下载并设置环境变量](#下载并设置环境变量)
   * [iterm2同步配置方式](#iterm2同步配置方式)
   * [同步范围](#同步范围)
* [环境套件资料](#环境套件资料)
   * [A. Homebrew Around](#a-homebrew-around)
   * [B. tmux配置：tmux_config.md](#b-tmux配置tmux_configmd)
   * [C. zsh/Oh my zsh + plugins](#c-zshoh-my-zsh--plugins)
   * [D. vim配置](#d-vim配置)
      * [修改vimrc](#修改vimrc)
      * [进入vim，会自动激活~/.vimrc](#进入vim会自动激活vimrc)
      * [关于colorscheme设置为solarized(分支已经包含，可以不用下载)](#关于colorscheme设置为solarized分支已经包含可以不用下载)
      * [主要分为这几个部分：](#主要分为这几个部分)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Mon Sep 19 16:57:12 UTC 2022 -->

<!--te-->

## [Status Bar](https://iterm2.com/documentation-status-bar.html): 很多内容，值得管理

## 下载并设置环境变量

```shell
git clone git@github.com:KuanHsiaoKuo/apple_power_user.git
cd apple_power_user
pwd # 输出的值用于配置环境变量
```

```shell
# ~/.bashrc 或者 ～/.zshrc
export APU=<pwd value>
export VC=$APU/src/app_extensions/iterm2_around/vim_config
export ZC=$APU/src/app_extensions/iterm2_around/zsh_config
```

> 由于我用的是zsh，所以这里就修改~/.zshrc

```admonish tip title='三种设置环境变量的区别'

1. 单纯export：仅对当前登陆的终端有效
2. 在.bashrc文件中export: 对当前登陆用户有效
3. 在/etc/profile文件中export: 对所有用户都有效

```

## iterm2同步配置方式

> 设置同步方式
```none
iTerm2 >> Preferences >> General >> Preferences >> Load prefernces from a custom folder or URL
```

> 注意选择手动保存。

指向下载的文件夹

## 同步范围

1. 基础颜色配置
2. profiles自动登陆服务器配置

> 但是自动输入密码的文件在~/.ssh/logins，需要另外同步

# 环境套件资料

```kroki-svgbob
iTerm2 + config + plugins
+----------------------------------------------------+
|                                                    |
|                HomeBrew + Plugins                  |
|      +-----------------------------------+         |
|      |                                   |         |
|      |      Tmux + config + plugins      |         |
|      |       +---------------------+     |         |
|      |       |                     |     |         |
|      |       |    zsh/Oh my zsh    |     |         |
|      |       |    +----------+     |     |         |
|      |       |    |    vim   |     |     |         |
|      |       |    +----------+     |     |         |
|      |       |                     |     |         |
|      |       +---------------------+     |         |
|      |                                   |         |
|      |                                   |         |
|      +-----------------------------------+         |
|                                                    |
+----------------------------------------------------+
```

## A. Homebrew Around

1. [The Missing Package Manager for macOS (or Linux) — Homebrew](https://brew.sh/)

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

2. Around: brew install xxx

- [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)

> osx系统更新了clang++, 一些老版本的python无法安装，比如3.7.5。 pyenv install 3.10.3就没问题

## B. tmux配置：tmux_config.md

## C. zsh/Oh my zsh + plugins

- [tldr-pages/tldr: 📚 Collaborative cheatsheets for console commands](https://github.com/tldr-pages/tldr)
- [Peltoche/lsd: The next gen ls command(需配合nerd-fonts)](https://github.com/Peltoche/lsd)
- [ryanoasis/nerd-fonts: Iconic font aggregator, collection, & patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, & more](https://github.com/ryanoasis/nerd-fonts)
- [Oh My Zsh - a delightful & open source framework for Zsh](https://ohmyz.sh/)
- [zsh-syntax-highlighting/INSTALL.md at master · zsh-users/zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)
- [zsh-users/zsh-completions: Additional completion definitions for Zsh.](https://github.com/zsh-users/zsh-completions)
- [zsh-users/zsh-history-substring-search: 🐠 ZSH port of Fish history search (up arrow)](https://github.com/zsh-users/zsh-history-substring-search)
- [romkatv/powerlevel10k: A Zsh theme(需配合nerd-fonts)](https://github.com/romkatv/powerlevel10k#oh-my-zsh)
- zsh config

3. iterm_around.sh未完善，请一条条执行

```shell
python3 -m pip install --upgrade pip
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> /Users/kuanhsiaokuo/.zprofile
eval "$(/opt/homebrew/bin/brew shellenv)"
brew tap homebrew/cask-fonts
# 下方指令比较耗时，安装之后如果没有生效，就修改Iterm2的fonts为Meslo
# Profiles >> Open Profiles >> Edit Profiles... >> Text >> Fonts
brew install --cask font-hack-nerd-font
brew install tmux
brew install lsd
pip3 install tldr
brew install graphviz
cpan
sudo cpan Graph:Easy
sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-history-substring-search ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-history-substring-search
git clone https://github.com/zsh-users/zsh-completions ${ZSH_CUSTOM:-${ZSH:-~/.oh-my-zsh}/custom}/plugins/zsh-completions
git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
echo "source $ZC/custom_config" >> ~/.zshrc
source ~/.zshrc
p10k configure

```

## D. vim配置

### 修改vimrc

```shell
sh $VC/source_vimrc.sh
```

```shell
# $VC/source_vimrc.sh
# 在vimrc里面添加source
echo 'source $VC/basic' >> ~/.vimrc
echo 'source $VC/fold_break' >> ~/.vimrc
echo 'source $VC/leader_key' >> ~/.vimrc
echo 'source $VC/tab_key' >> ~/.vimrc
```

```admonish tip title='source filename 与 sh filename 及./filename执行脚本的区别在那里呢？'

1.当shell脚本具有可执行权限时，用sh filename与./filename执行脚本是没有区别得。./filename是因为当前目录没有在PATH中，所有"."是用来表示当前目录的。

2.sh filename 重新建立一个子shell，在子shell中执行脚本里面的语句，该子shell继承父shell的环境变量，但子shell新建的、改变的变量不会被带回父shell，除非使用export。

3.source filename：这个命令其实只是简单地读取脚本里面的语句依次在当前shell里面执行，没有建立新的子shell。那么脚本里面所有新建、改变变量的语句都会保存在当前shell里面。（当这个shell关闭后就失效了）
```

### 进入vim，会自动激活~/.vimrc

### 关于colorscheme设置为solarized(分支已经包含，可以不用下载)

- 下载vim主题

```
git clone git://github.com/altercation/vim-colors-solarized.git  
cp vim-colors-solarized/colors/solarized.vim ~/.vim/colors/ 
```

- 配置

```
colorscheme solarized 
```

### 主要分为这几个部分：

- basic
- fold_break
- leader_key
- tab_key
- cscope_conf