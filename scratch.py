# coding=utf-8
"""根据搜索词下载百度图片"""
import re
import urllib
import requests


def getPage(keyWord, page, n):
    page = page * n
    keyWord = urllib.parse.quote(keyWord, safe='/')
    url_begin = "http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word="
    url = url_begin + keyWord + "&pn=" + str(page) + "&gsm=" + str(hex(page)) + "&ct=&ic=0&lm=-1&width=0&height=0"
    return url


def get_onepage_urls(OnePageURL):
    try:
        html = requests.get(OnePageURL).text
    except Exception as e:
        print(e)
        pic_urls = []
        return pic_urls
    pic_urls = re.findall('"objURL":"(.*?)",', html, re.S)
    return pic_urls


def down_pic(pic_urls):
    savePath = '/home/runisys/Desktop/UAV2/'
    """给出图片链接列表, 下载所有图片"""
    for i, pic_url in enumerate(pic_urls):
        try:
            pic = requests.get(pic_url, timeout=15)
            string = savePath + str(i + 1) + '.jpg'
            with open(string, 'wb') as f:
                f.write(pic.content)
                print('成功下载第%s张图片: %s' % (str(i + 1), str(pic_url)))
        except Exception as e:
            print('下载第%s张图片时失败: %s' % (str(i + 1), str(pic_url)))
            print(e)
            continue


if __name__ == '__main__':
    keyword = '无人机'  # 关键词, 改为你想输入的词即可, 相当于在百度图片里搜索一样
    page_begin = 0
    image_number_per_page = 30
    how_many_page_you_want = 10000
    all_pic_urls = []
    while 1:
        if page_begin > how_many_page_you_want:
            break
        print("第%d次请求数据", [page_begin])
        url = getPage(keyword, page_begin, image_number_per_page)
        onepage_urls = get_onepage_urls(url)
        page_begin += 1

        all_pic_urls.extend(onepage_urls)

    print("All image count is ")
    print(len(all_pic_urls))
    down_pic(list(set(all_pic_urls)))
