#!/usr/bin/python3
# -*- coding: UTF-8 -*-

"""
this script use to:
1. delete old files(resources, public) built by hugo
2. run hugo to generate new files
3. delete old files in github.io
4. mv files from hugo/public/ to github.io/
"""

import os
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
def raplece_img_url(hugo_dir):
    postdir = hugo_dir + os.sep + "content" + os.sep + "post"


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


if __name__ == "__main__":
    print("+++++++++++++++++++")
    print("++ publish start...")
    print("++ current dir is:", os.getcwd())
    hugo_dir = os.path.abspath(sys.path[0])
    print("++ python script dir is:", hugo_dir)

    delete_last_hugo_files(hugo_dir)

    start_hugo()

    # parent dir
    pardir = os.path.join(hugo_dir, os.pardir)
    githubio_dir = os.path.join(pardir, GITHUB_IO_SITE)

    # delete older files
    del_files_in_site(githubio_dir)

    move_new_files_to_site(hugo_dir, githubio_dir)

    print("+++++++++++++++++++")
    print("done!")
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
