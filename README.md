# 使用Python爬取百度搜索图像

用来训练神经网络，现场采集的数据集不够，从网上爬一些数据。
之前没有写过爬虫，当前大部分是参考了其他人的代码。

当前主要参考Python3 爬取百度图片。
4,5,6是爬取meizitu网站的图片，这个网站很不利于青少年成长，但是网页组织很好，所以爬取分析网页和爬取都很容易，但不适用于爬取百度搜索特定类型的图片，仅供学习使用。

## 运行环境

我使用的是Anaconda，创建虚拟环境，避免安装的库与caffe和tensorflow的库有冲突。

```
conda create -n crawler python=3.6
```

激活后安装爬虫需要的库
```
source activate crawler
conda install requests
conda install beautifulsoup4
conda install lxml
```

## 测试

1. 测试用来下载meizitu的脚本
```
python crawler.py
```
这个脚本比较简单，用来测试用，但是可以下载真实的图像，代码中有文件存储路径，自行修改，另外，注意图像不要随意打开，特别是在人多的时候，很尴尬。

2. 测试百度搜索图像爬取

```
python scratch.py
```
这个也是硬编码路径。

## 参考
1. [正则表达式30分钟入门教程](http://deerchao.net/tutorials/regex/regex.htm)
2. [Requests: 让 HTTP 服务人类](http://docs.python-requests.org/zh_CN/latest/)
3. [Beautiful Soup 4.2.0 文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

4. [下载meizitu网站图片的源代码](https://github.com/thsheep/mzitu)
5. [小白爬虫第一弹之抓取妹子图](https://cuiqingcai.com/3179.html)
6. [Python爬虫之——爬取妹子图片](https://blog.csdn.net/baidu_35085676/article/details/68958267)

7. [爬取百度图片各种狗狗的图片，使用caffe训练模型分类](https://github.com/bbfamily/DogJudge)
8. [python3 爬取百度图片](https://blog.csdn.net/hust_bochu_xuchao/article/details/79431145)
