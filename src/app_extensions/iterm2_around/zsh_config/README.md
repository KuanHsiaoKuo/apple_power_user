# zsh_config使用

<!--ts-->


<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Sun Nov 27 15:02:37 UTC 2022 -->

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

我的zsh配置，采用两层配置结构：

- `~/.zshrc`：本地文件（不纳入 Git），只配置路径环境变量
- `custom_config` + `alias_collections`：通用配置（Git 管理）

### 配置步骤

1. 在指定目录 git clone 本仓库

2. 创建 `~/.zshrc` 文件，内容如下（根据实际路径修改 `ZSH_CONFIG`）：

```shell
# ============================================
# 本地环境变量配置（根据实际路径修改）
# ============================================
export ZSH="$HOME/.oh-my-zsh"

# 指向 Git 仓库中 zsh_config 的路径
export ZSH_CONFIG="$HOME/Projects/apple_power_user/src/app_extensions/iterm2_around/zsh_config"

# ============================================
# 加载 Git 管理的通用配置
# ============================================
source "$ZSH_CONFIG/custom_config"
```

3. 执行指令生效：

```shell
# 可能需要切换到zsh
source ~/.zshrc
```

### 文件说明

| 文件 | 管理方式 | 职责 |
|------|----------|------|
| `~/.zshrc` | 本地（不入 Git） | 定义 `ZSH`、`ZSH_CONFIG` 路径，然后 source 通用配置 |
| `custom_config` | Git | 主题、插件、通用设置 |
| `alias_collections` | Git | 所有 alias 定义 |

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
