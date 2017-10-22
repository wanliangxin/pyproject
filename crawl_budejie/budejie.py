#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File: budejie.py
# @Author: Haocheng

import urllib
import os
import requests
import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_response(url):
    response = requests.get(url).text
    return response     # 返回网页源代码

def get_content(html):  # 在这个函数里面解析出来包含视频的html，并返回
    reg = re.compile(r'(<div class="j-r-list-c">.*?</div>.*?</div>)',re.S)
    return re.findall(reg,html)

def get_mp4_url(response):      # 获取视频的URL地址
    reg = r'data-mp4="(.*?)"'
    return re.findall(reg,response)

def get_mp4_name(response):     # 获取视频的名字
    reg = re.compile('<a href="/detail-.{8}.html">(.*?)</a>')
    return re.findall(reg,response)     # findall返回的是一个列表

def download_mp4(mp4_url,path):
    path = ''.join(path.split())
    path = 'C:\\pyproject\\crawl_budejie\\{}.mp4'.format(path.decode('utf-8').encode('gbk'))     # 视频的存储路径
    if not os.path.exists(path):
        urllib.urlretrieve(mp4_url,path)        # 下载视频
        print 'OK!!!'
    else:
        print 'No!!!'


def get_url_name(start_url):
    content = get_content(get_response(start_url))
    for i in content:
        mp4_url = get_mp4_url(i)
        if mp4_url:
            mp4_name = get_mp4_name(i)
            try:
                download_mp4(mp4_url[0],mp4_name[0])
            except:
                pass
                continue


def main():
    # for start_url in start_urls:
    #     get_url_name(start_url)
    [get_url_name(start_url) for start_url in start_urls]




if __name__ == '__main__':      # 判断是不是当前文件执行
    start_urls = ['http://www.budejie.com/{}'.format(i) for i in range(1,10)]
    main()
