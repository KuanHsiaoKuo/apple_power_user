# zsh_config使用

<!--ts-->
* [zsh_config使用](#zsh_config使用)
   * [首先安装zsh](#首先安装zsh)
   * [接着安装oh my zsh](#接着安装oh-my-zsh)
   * [zsh-config](#zsh-config)
      * [zsh-syntax-hightlighting插件安装](#zsh-syntax-hightlighting插件安装)
      * [zsh-autosuggestion](#zsh-autosuggestion)
      * [安装powerlevel10k主题](#安装powerlevel10k主题)
      * [nerd fonts使用](#nerd-fonts使用)
      * [一些终端小工具的安装，非zsh/oh-my-zsh](#一些终端小工具的安装非zshoh-my-zsh)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Mon Jul 18 03:06:43 UTC 2022 -->

<!--te-->

## 首先安装zsh

```
sudo apt-get install zsh
```

## 接着安装oh my zsh

```
wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh
```

或者安装：

```
chmod u+x oh_my_zsh_install.sh
./oh_my_zsh_install.sh
```

## zsh-config

我的zsh配置

> 在指定目录git clone之后，在~/.zshrc添加一行

```shell
source ~/Developer/spare_projects/apple_power_user/src/app_extensions/iterm2_around/zsh_config/custom_config¬
```

> 然后执行指令：

```
# 可能需要切换到zsh
source ~/.zshrc
```

### zsh-syntax-hightlighting插件安装

```
git clone git://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
# 然后在custom_config里面对plugins添加这个插件
```

### zsh-autosuggestion

```
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```

### 安装powerlevel10k主题

- 下载主题

```
git clone https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
```

- custom-config配置主题

```
ZSH_THEME="powerlevel10k/powerlevel10k"
POWERLEVEL9K_MODE="awesome-patched"
```

- 重新配置p10k

```
p10k configure
```

- 安装字体:默认情况下激活zshrc时会自动安装

> ubuntu

```
apt-get install fonts-powerline
```

- macos

```
https://github.com/powerline/fonts/blob/master/SourceCodePro/Source%20Code%20Pro%20for%20Powerline.otf
https://github.com/Falkor/dotfiles/blob/master/fonts/SourceCodePro%2BPowerline%2BAwesome%2BRegular.ttf
```

### nerd fonts使用

- 下载

```
git clone https://github.com/ryanoasis/nerd-fonts.git
```

- 安装

```
./install.sh
```

- iterm2设置喜欢的字体

### 一些终端小工具的安装，非zsh/oh-my-zsh

- lsd
  [Peltoche/lsd: The next gen ls command](https://github.com/Peltoche/lsd)

> ubuntu:

```
wget https://github.com/Peltoche/lsd/releases/download/0.17.0/lsd_0.17.0_amd64.deb
sudo dpkg -i lsd_0.17.0_amd64.deb
```

- tldr
  [tldr-pages/tldr: 📚 Collaborative cheatsheets for console commands](https://github.com/tldr-pages/tldr)
