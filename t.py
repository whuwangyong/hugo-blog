import os
import re


def walk_file(file):
    prefix = 'https://cdn.jsdelivr.net/gh/whuwangyong/whuwangyong.github.io/p/'

    for root, dirs, files in os.walk(file):

        # root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下的子目录名list
        # files 表示该文件夹下的文件list

        if str(root).find('图片加载网速测试') != -1:
            continue

        # 遍历文件
        for f in files:
            if str(f).endswith('.md'):
                mdf = os.path.join(root, f)
                with open(mdf, 'w+', encoding='utf-8') as md:
                    content = md.read()
                    # 查找md图片语法
                    img_list = re.findall(r'!\[.*?\]\(.*?\)', content)
                    new_img_list = []
                    if len(img_list) > 0:
                        # processing:  E:\blog\hugo-blog-stack\content\post\效率工具\vpn\V2Ray搭建指南\index.md
                        print('processing: ', mdf)

                        # 获取渲染为html之后文章的所在路径：md上级目录的小写
                        uplevel = str(mdf).split(os.sep)[-2].lower()

                        for img in img_list:
                            new_img = str(img).replace('](', '](' + prefix + uplevel + '/')
                            print("\treplacing " + img + " to " + new_img)
                            # new_img_list.append(new_img)

                            content = content.replace(img, new_img)
                    md.write(content)

if __name__ == '__main__':
    walk_file("E:\\blog\\hugo-blog-stack\\content\\post")
