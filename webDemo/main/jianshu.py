# -*- coding: utf-8 -*-
# @Time    : 2019/1/13 19:14
# @Author  : Ming
import urllib

import requests
from bs4 import BeautifulSoup

main_url = 'http://www.jianshu.com'
requests.packages.urllib3.disable_warnings()

class Item_jianshu():
    '''
        获取信息
    '''

    def __init__(self, user_url):
        self.user_url = user_url

    def get_category(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        req = urllib.request.Request(url=self.user_url, headers=headers)  # 这里要注意，必须使用url=url，headers=headers的格式，否则回报错，无法连接字符
        html = urllib.request.urlopen(req).read()
        # html = requests.get(self.user_url).content
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        category_list = soup.find_all('a', class_='title')
        category_info = []
        for category in category_list:
            category_url = main_url + category['href']
            category_title = category.get_text()
            category_info.append([category_title, category_url])
        return category_info


class Body_jianshu():
    '''获取文章内容'''

    def __init__(self, article_url):
        self.article_url = article_url

    def get_body(self):
        # html = requests.get(self.article_url).content
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
        req = urllib.request.Request(url=self.article_url,
                                     headers=headers)  # 这里要注意，必须使用url=url，headers=headers的格式，否则回报错，无法连接字符
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
        article_content = soup.find_all('div', class_='show-content')

        body = str(article_content[0])
        # 将 body 中 " 转换为 \", ' 转换为 \'
        body = body.replace('"', '\\"')
        body = body.replace("'", "\\'")
        return body

