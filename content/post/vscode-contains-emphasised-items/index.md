---
title: "VSCode Contains Emphasised Items"
description: VSCode workspace 文件夹提示包含强调内容
date: 2022-02-23T12:19:19+08:00
draft: false
categories:
    - VSCode
---

## 问题
在VSCode中开发项目时，有些文件夹右边有个小绿点，鼠标放上去，提示“Contains emphasised items”。但是，文件夹下面的所有修改都已经commit并push了，`git status`显示`nothing to commit, working tree clean`。
## 解决
`Shift Ctrl P`打开`Command Palette`，输入`Developer: Reload Window`。


