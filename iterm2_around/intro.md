## iTerm2配置
### [Status Bar](https://iterm2.com/documentation-status-bar.html): 很多内容，值得管理
## 同步配置方式
1. 下载此文件夹
2. 设置同步方式
iTerm2 >> Preferences >> General >> Preferences >> Load prefernces from a custom folder or URL
> 注意选择手动保存。
3. 指向下载的文件夹

## 同步范围
1. 基础颜色配置
2. profiles自动登陆服务器配置
> 但是自动输入密码的文件在~/.ssh/logins，需要另外同步

## 环境套件资料
```text
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
### A. Homebrew Around
1. [The Missing Package Manager for macOS (or Linux) — Homebrew](https://brew.sh/)
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
2. Around: brew install xxx
- [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv)
> osx系统需要打补丁
```
CFLAGS="-I$(brew --prefix openssl)/include -I$(brew --prefix bzip2)/include -I$(brew --prefix readline)/include -I$(xcrun --show-sdk-path)/usr/include" LDFLAGS="-L$(brew --prefix openssl)/lib -L$(brew --prefix readline)/lib -L$(brew --prefix zlib)/lib -L$(brew --prefix bzip2)/lib" pyenv install --patch 3.7.5 < <(curl -sSL https://github.com/python/cpython/commit/8ea6353.patch\?full_index\=1)
```
### tmux配置：tmux_config.md
### zsh/Oh my zsh + plugins
- [tldr-pages/tldr: 📚 Collaborative cheatsheets for console commands](https://github.com/tldr-pages/tldr)
- [Peltoche/lsd: The next gen ls command(需配合nerd-fonts)](https://github.com/Peltoche/lsd)
- [ryanoasis/nerd-fonts: Iconic font aggregator, collection, & patcher. 3,600+ icons, 50+ patched fonts: Hack, Source Code Pro, more. Glyph collections: Font Awesome, Material Design Icons, Octicons, & more](https://github.com/ryanoasis/nerd-fonts)
- [Oh My Zsh - a delightful & open source framework for Zsh](https://ohmyz.sh/)
- [zsh-syntax-highlighting/INSTALL.md at master · zsh-users/zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md)
- [zsh-users/zsh-completions: Additional completion definitions for Zsh.](https://github.com/zsh-users/zsh-completions)
- [zsh-users/zsh-history-substring-search: 🐠 ZSH port of Fish history search (up arrow)](https://github.com/zsh-users/zsh-history-substring-search)
- [romkatv/powerlevel10k: A Zsh theme(需配合nerd-fonts)](https://github.com/romkatv/powerlevel10k#oh-my-zsh)
- zsh config
