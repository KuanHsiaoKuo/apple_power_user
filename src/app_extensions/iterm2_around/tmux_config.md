# tmux配置
<!--ts-->
* [tmux配置](#tmux配置)
   * [OSX](#osx)
   * [Linux(Simplified)](#linuxsimplified)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Mon Jul 18 02:05:14 UTC 2022 -->

<!--te-->
## OSX
```
# 解绑前缀，改为和screen一样的
unbind C-b
set -g prefix C-a
# bind a reload key
bind r source-file ~/.tmux.conf ; display-message "Config reloaded.."
# 切换分窗格方式
bind | split-window -h
bind - split-window -v
# 重新按照vi习惯定义方向键
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
# 交换窗格
bind ^u swapp -U
bind ^d swapp -D
# 将window的起始设置为1
set -g base-index 1
# 将pane的起始下标设为1
set -g pane-base-index 1
# 设置pane编号显示时间
set -g display-panes-time 2000 #2s
# UI 样式调整
setw -g window-status-current-fg white
setw -g window-status-current-bg red
setw -g window-status-current-attr bright
set -g status-justify left
setw -g monitor-activity on
# 开始美化状态栏

# tmux插件管理器
# List of plugins
#  要装的插件直接在这里写就可以了
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-prefix-highlight'
# 这两个插件是备份tmux会话与自动备份
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
# 打开会话自动保存
set -g @continuum-restore 'on'
# 默认每隔15分钟备份一次,这里改成半个小时
set -g @continuum-save-interval '30'
set -g @plugin 'tmux-plugins/tmux-online-status'
# 添加状态栏电池显示插件
set -g @plugin 'tmux-plugins/tmux-battery'
# 添加tmux侧边栏, prefix-tab
set -g @plugin 'tmux-plugins/tmux-sidebar'
# tmux窗格管理
set -g @plugin 'tmux-plugins/tmux-pain-control'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'git@github.com/user/plugin'
# set -g @plugin 'git@bitbucket.com/user/plugin'



# 关于复制方式
#set-window-option -g mode-keys vi
#bind-key -t vi-copy 'v' begin-selection
#bind-key -t vi-copy 'y' copy-selection

# 状态栏统一设置
# Update the status line every sixty seconds
set -g status-interval 60
# Center the window list in the status line
set -g status-justify centre
# enable activity alerts
setw -g monitor-activity on
# Displays a message in the message area when there is activity in another window
set -g visual-activity on
set -g status-left-length 200
set -g status-right-length 200
##H
#Hostname of local host
##h
#Hostname of local host without the domain name
##F
#Current window flag
##I
#Current window index
##P
#Current pane index
##S
#Current session name
##T
#Current window title
##W
#Current window name
###
#A literal #
##(shell-command)
#First line of the shell command’s output
##[attributes]
#Color or attribute change
set -g status-left "session:#S window:#W pane:#P"
# 设置电量状态所用的图标
set -g @batt_charged_icon "😎"
set -g @batt_charging_icon "👍"
set -g @batt_discharging_icon "👎"
set -g @batt_attached_icon "😐"
set -g @batt_full_charge_icon "🌕 "
set -g @batt_high_charge_icon "🌖 "
set -g @batt_medium_charge_icon "🌗 "
set -g @batt_low_charge_icon "🌘 "
set -g status-right '#{battery_status_bg} Batt: #{battery_icon} #{battery_percentage} #{battery_remain} | Continuum status: #{continuum_status} | Online: #{online_status} | %a %h-%d %H:%M '
# 添加powerline支持
source "/usr/local/bin/powerline/powerline/bindings/tmux/powerline.conf"
# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
# bind a reload key
bind r source-file ~/.tmux.conf ; display-message "Config reloaded.."
# 切换分窗格方式
bind | split-window -h
bind - split-window -v
# 重新按照vi习惯定义方向键
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
# 将window的起始设置为1
set -g base-index 1
# 将pane的起始下标设为1
set -g pane-base-index 1
# UI 样式调整
setw -g window-status-current-fg white
setw -g window-status-current-bg red
setw -g window-status-current-attr bright
set -g status-justify left
setw -g monitor-activity on
# 开始美化状态栏

# tmux插件管理器
# List of plugins
#  要装的插件直接在这里写就可以了
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
set -g @plugin 'tmux-plugins/tmux-prefix-highlight'
# 这两个插件是备份tmux会话与自动备份
set -g @plugin 'tmux-plugins/tmux-resurrect'
set -g @plugin 'tmux-plugins/tmux-continuum'
# 打开会话自动保存
set -g @continuum-restore 'on'
# 默认每隔15分钟备份一次,这里改成半个小时
set -g @continuum-save-interval '30'
set -g @plugin 'tmux-plugins/tmux-online-status'
# 添加状态栏电池显示插件
set -g @plugin 'tmux-plugins/tmux-battery'
# 添加tmux侧边栏, prefix-tab
set -g @plugin 'tmux-plugins/tmux-sidebar'
# tmux窗格管理
set -g @plugin 'tmux-plugins/tmux-pain-control'

# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'git@github.com/user/plugin'
# set -g @plugin 'git@bitbucket.com/user/plugin'



# 关于复制方式
#set-window-option -g mode-keys vi
#bind-key -t vi-copy 'v' begin-selection
#bind-key -t vi-copy 'y' copy-selection

# 状态栏统一设置
# Update the status line every sixty seconds
set -g status-interval 60
# Center the window list in the status line
set -g status-justify centre
# enable activity alerts
setw -g monitor-activity on
# 设置窗口名字不再自动变化
set-option -g allow-rename off
# 设置窗格名字
set-option -g pane-border-format " #P: #{pane_current_command} "
# Enable names for panes
set -g pane-border-status top
# Displays a message in the message area when there is activity in another window
set -g visual-activity on
set -g status-left-length 100
set -g status-right-length 200
set -g status-left "session:#S window:#I pane:#P"
# 设置电量状态所用的图标
set -g @batt_charged_icon "😎"
set -g @batt_charging_icon "👍"
set -g @batt_discharging_icon "👎"
set -g @batt_attached_icon "😐"
set -g @batt_full_charge_icon "🌕 "
set -g @batt_high_charge_icon "🌖 "
set -g @batt_medium_charge_icon "🌗 "
set -g @batt_low_charge_icon "🌘 "
set -g status-right '#{battery_status_bg} Batt: #{battery_icon} #{battery_percentage} #{battery_remain} | Continuum status: #{continuum_status} | Online: #{online_status} | %a %h-%d %H:%M '
# 添加powerline支持
#source "/usr/local/lib/python3.6/site-packages/powerline/bindings/tmux/powerline.conf"
# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'

# 设置resurrect保存窗格的内容page
set -g @resurrect-capture-pane-contents 'on'
# for vim
set -g @resurrect-strategy-vim 'session'

# ----------------------------tricks-------------
# displays "prefix" (in red) in statusline when prefix is pressed
set -g status-left "#[bg=red]#{s/root//:client_key_table}"
# view current pane history (including colors) with "less" in new window
bind-key u capture-pane -S - -E - -e -b lesshist \; new-window -n "history" 'tmux show-buffer -b lesshist| less -R +G'

```

## Linux(Simplified)

```
# 解绑前缀，改为和screen一样的
unbind C-b
set -g prefix C-a
# 切换分窗格方式
bind | split-window -h
bind - split-window -v
# 重新按照vi习惯定义方向键
bind h select-pane -L
bind j select-pane -D
bind k select-pane -U
bind l select-pane -R
# 交换窗格
bind ^u swapp -U
bind ^d swapp -D
# 将window的起始设置为1
set -g base-index 1
# 将pane的起始下标设为1
set -g pane-base-index 1
# 设置pane编号显示时间
set display-panes-time 2000 #2s
# UI 样式调整
setw -g window-status-current-fg white
setw -g window-status-current-bg red
setw -g window-status-current-attr bright
set -g status-justify left
setw -g monitor-activity on

```