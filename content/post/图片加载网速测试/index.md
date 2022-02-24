---
title: "图片加载网速测试"
date: 2022-02-25T00:25:31+08:00
draft: false
---


图片与网页在同一文件夹下，都采用懒加载方式，测试下面三种方式的加载速度。


**加载方式1: 相对路径**
```
![qq-img](qq.png)
```
![qq-img](qq.png)

---

**加载方式2：在线路径**
```
![qq-img](https://whuwangyong.github.io/p/图片加载网速测试/qq.png)
```
![qq-img](https://whuwangyong.github.io/p/图片加载网速测试/qq.png)


---


**加载方式3：在线路径 + cdn加速**
```
![qq-img](https://cdn.jsdelivr.net/gh/whuwangyong/whuwangyong.github.io/p/图片加载网速测试/qq.png)
```
![qq-img](https://cdn.jsdelivr.net/gh/whuwangyong/whuwangyong.github.io/p/图片加载网速测试/qq.png)

