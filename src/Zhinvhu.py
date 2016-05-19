#! /usr/bin/env python3
#-*- coding:utf-8 -*-
import os
from bs4 import BeautifulSoup
from PIL import Image
import requests
import json
import time

sum = 1;

headers_base = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
    'Connection': 'keep-alive',
    'Host': 'www.zhihu.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.130 Safari/537.36', 
    'Referer': 'https://www.zhihu.com/',
}

path = "e:\\zhihu\\"
file = "e:\\pic.txt"
base = "https://www.zhihu.com"

def is_path_exist():
    if not os.path.exists(path):
        os.mkdir(path)

def is_file_exist():
    if not os.access(file, os.F_OK):
        try:
            f = open(file,'w')
        except IOError:
            os.mkdir(os.path.dirname(file))
            f = open(file,'w')
        finally:
            f.close()  


#define  find_what
def download(url):
    print(url)
    d = requests.get(url,headers=headers_base)
    if d.status_code == 200:
        #print(d.text)
        spoon = BeautifulSoup(d.text,"lxml")
        pics = spoon.find_all('img',class_="origin_image")
        for pic in pics:
            with open(file,"at",encoding="utf-8") as f:
                print(pic['data-original'], file=f)
            save_img(pic['data-original'])

def save_img(url):
    img = requests.get(url)
    if img.status_code == 200:
        with open(path+url.split('/')[-1],'wb' ) as f:
            f.write(img.content)
            f.close()
    else:
        print(url+" 404 not founded")
     



def has(tag):
    return tag.has_attr("href") and tag.has_attr("class")

def main(url):
    is_path_exist()
    is_file_exist()
    r = requests.get(url,headers = headers_base)
    if r.status_code == 200:
        #r.decode("utf-8")
        #print(t.text)
        soup = BeautifulSoup(r.text,"lxml")
        tag = soup.find_all(href=True,class_="toggle-expand")
        for x in tag:
            #time.sleep(5)
            download(base+x['href'])
    
if __name__ == '__main__':
    main("https://www.zhihu.com/collection/26815754")
    