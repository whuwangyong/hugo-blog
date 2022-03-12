#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
这个脚本执行以下操作：
1. 删除hugo上次渲染的文件(resources, public)
2. 修改md，将图片从相对路径替换为在线url
3. 运行hugo，渲染md为html
4. 删除github.io里面的全部文件
5. 将hugo/public/下的所有文件移动到 github.io/
"""

import os
import re
import shutil
import sys
import time

GITHUB_IO_SITE = "whuwangyong.github.io"


# 将上次编译出来的hugo文件删除
def delete_last_hugo_files(hugo_dir):
    print("++")
    print("++ delete resources and public in hugo...")
    os.chdir(hugo_dir)
    if os.path.exists("resources"):
        shutil.rmtree("resources")
    if os.path.exists("public"):
        shutil.rmtree("public")


# 处理post目录下的md文档，将相对路径的图片替换为在线url。这样做的目的是，便于md文档复制到其他平台进行发表
def replace_img_url(hugo_dir):
    print("++")
    print("++ replace_img_url...")
    post_dir = hugo_dir + os.sep + "content" + os.sep + "post"
    prefix = 'https://cdn.jsdelivr.net/gh/whuwangyong/whuwangyong.github.io/p/'

    for root, dirs, files in os.walk(post_dir):
        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        if str(root).find('图片加载网速测试') != -1:
            continue

        # 遍历文件
        for f in files:
            if str(f).endswith('.md'):
                mdf = os.path.join(root, f)
                with open(mdf, 'r+', encoding='utf-8') as md:
                    content = md.read()
                    # 查找md图片语法
                    img_list = re.findall(r'!\[.*?\]\(.*?\)', content)
                    for i in img_list:
                        if str(i).find('https') != -1:
                            img_list.remove(i)

                    if len(img_list) > 0:
                        # processing:  E:\blog\hugo-blog-stack\content\post\效率工具\vpn\V2Ray搭建指南\index.md
                        print('processing: ', mdf)

                        # 获取渲染为html之后文章的所在路径：md上级目录的小写
                        uplevel = str(mdf).split(os.sep)[-2].lower()

                        for img in img_list:
                            new_img = str(img).replace('](', '](' + prefix + uplevel + '/')
                            print("\treplacing " + img + " to " + new_img)
                            content = content.replace(img, new_img)
                    # 将指针移到文件头，然后写入替换后的内容
                    md.seek(0)
                    md.write(content)


# 开始渲染md为html
def start_hugo():
    print("++")
    print("++ start hugo...")
    result = os.system("hugo")
    print("++ hugo completed! result=", result)


# 删除目标网站上的旧文件
def del_files_in_site(site_dir):
    print("++")
    print("++ delete older files...")
    print("++ site_dir:", site_dir)

    for f_name in os.listdir(site_dir):
        f_path = site_dir + os.sep + f_name
        if os.path.isfile(f_path):
            os.remove(f_path)
            print("++ remove file:", f_path)
        elif f_name == ".git":
            print("++ reserve .git")
            continue
        else:
            shutil.rmtree(f_path)
            print("++ remove dir:", f_path)


# 将刚渲染出来的html复制到目标站点
def move_new_files_to_site(hugo_dir, githubio_dir):
    print("++")
    print("++ move files from hugo/public/ to github.io/")
    for f_name in os.listdir(hugo_dir + os.sep + 'public'):
        f_path = hugo_dir + os.sep + "public" + os.sep + f_name
        print("++ move:", f_name)
        shutil.move(f_path, githubio_dir)


def main():
    print("+++++++++++++++++++")
    print("++ publish start...")
    print("++ current dir is:", os.getcwd())
    hugo_dir = os.path.abspath(sys.path[0])
    print("++ python script dir is:", hugo_dir)

    delete_last_hugo_files(hugo_dir)

    replace_img_url(hugo_dir)

    start_hugo()

    # parent dir
    pardir = os.path.join(hugo_dir, os.pardir)
    github_io_dir = os.path.join(pardir, GITHUB_IO_SITE)

    # delete older files
    del_files_in_site(github_io_dir)

    move_new_files_to_site(hugo_dir, github_io_dir)

    print("+++++++++++++++++++")
    print("done!")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == "__main__":
    main()
