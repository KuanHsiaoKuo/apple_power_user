# MacOS X 专用命令行梳理

<!--ts-->
* [MacOS X 专用命令行梳理](#macos-x-专用命令行梳理)
   * [open](#open)
   * [pbcopy and pbpaste](#pbcopy-and-pbpaste)
   * [mdfind](#mdfind)
   * [screencapture](#screencapture)
   * [launchctl](#launchctl)
   * [say](#say)
   * [diskutil](#diskutil)
   * [brew](#brew)
   * [列表清单](#列表清单)
      * [快捷操作](#快捷操作)
      * [基础操作](#基础操作)
      * [list](#list)
      * [文件磁盘](#文件磁盘)
   * [参考资源](#参考资源)

<!-- Created by https://github.com/ekalinin/github-markdown-toc -->
<!-- Added by: runner, at: Thu Sep  1 14:58:09 UTC 2022 -->

<!--te-->

## open

## pbcopy and pbpaste

```shell
tree -L 1 | pbcopy
```

## mdfind

## screencapture

## launchctl

## say

## diskutil

## brew

## 列表清单

### 快捷操作

| Tab                      | Auto-complete file and folder names                          |
| ------------------------ | ------------------------------------------------------------ |
| Ctrl + A                 | Go to the beginning of the line you're currently typing on   |
| Ctrl + E                 | Go to the end of the line you're currently typing on         |
| Ctrl + U                 | Clear the line before the cursor                             |
| Ctrl + K                 | Clear the line after the cursor                              |
| Ctrl + W                 | Delete the word before the cursor                            |
| Ctrl + T                 | Swap the last two characters before the cursor               |
| Esc + T                  | Swap the last two words before the cursor                    |
| Ctrl + L                 | Clear the screen                                             |
| Ctrl + C                 | Kill whatever you're running                                 |
| Ctrl + D                 | Exit the current shell                                       |
| Option + →               | Move cursor one word forward                                 |
| Option + ←               | Move cursor one word backward                                |
| Ctrl + F                 | Move cursor one character forward                            |
| Ctrl + B                 | Move cursor one character backward                           |
| Ctrl + Y                 | Paste whatever was cut by the last command                   |
| Ctrl + Z                 | Puts whatever you're running into a suspended background process |
| Ctrl + _                 | Undo the last command                                        |
| Option + Shift + Cmd + C | Copy plain text                                              |
| Shift + Cmd + V          | Paste the selection                                          |
| exit                     | End a shell sessio                                           |

### 基础操作

| / (Forward Slash)    | Top level directory                                        |
| -------------------- | ---------------------------------------------------------- |
| . (Single Period)    | Current directory                                          |
| .. (Double Period)   | Parent directory                                           |
| ~ (Tilde)            | Home directory                                             |
| sudo [command]       | Run command with the security privileges of the super user |
| nano [file]          | Opens the Terminal editor                                  |
| open [file]          | Opens a file                                               |
| [command] -h         | Get help about a command                                   |
| man [command]        | Show the help manual of the command                        |
| **Change Directory** |                                                            |
| cd                   | Home directory                                             |
| cd [folder]          | Change directory, e.g. cd Documents                        |
| cd ~                 | Home directory                                             |
| cd/                  | Root of the drive                                          |
| cd -                 | Previous directory or folder you last browsed              |
| pwd                  | Show your working directory                                |
| cd..                 | Move up to the parent directory                            |
| cd../..              | Move up two levels                                         |

### list

| ls      | Display the name of files and subdirectories in the directory |
| ------- | :----------------------------------------------------------: |
| ls -C   |           Force multi-column output of the listing           |
| ls -a   | List all entries including those with .(period) and ..(double period) |
| ls -1   |    Output the list of files in one entry per line format     |
| ls -F   | Display a / (slash) immediately after each path that is a directory, * (asterisk) after executable programs or scripts, and @ after a symbolic link |
| ls -S   |                Sort files or entries by size                 |
| ls -l   | List in a long format. Includes file mode, owner and group name, date and time file was modified, pathname, and more |
| ls -l / |    List of the file system from root with symbolic links     |
| ls -lt  |  List the files sorted by time modified (most recent first)  |
| ls -lh  | Long listing with human readable file sizes in KB, MB, or GB |
| ls -lo  |       List the file names with size, owner, and flags        |
| ls -la  |   List detailed directory contents, including hidden files   |

### 文件磁盘

| du                  | List usage for each subdirectory and its contents            |
| ------------------- | ------------------------------------------------------------ |
| du -sh [folder]     | Human readable output of all files in a directory            |
| du -s               | Display an entry for each specified file                     |
| du -sk* \| sort -nr | List files and folders, totaling the size including the subfolders. Replace sk* with sm* to list directories in MB |
| df -h               | Calculate your system's free disk space                      |
| df -H               | Calculate free disk space in powers of 1,000 (as opposed to 1,024) |

## 参考资源

- [Eight Terminal Utilities Every OS X Command Line User Should Know · mitchchn.me](http://www.mitchchn.me/2014/os-x-terminal/)
- [The Mac Terminal Commands Cheat Sheet](https://www.makeuseof.com/tag/mac-terminal-commands-cheat-sheet/)
- [An A-Z Index of the Apple macOS command line - SS64 Command line reference](https://web.archive.org/web/20220620084651/https://ss64.com/osx/)