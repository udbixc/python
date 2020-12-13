#!/usr/bin/env python
# encoding: utf-8

import requests
import json

from selenium import webdriver
#from selenium.webdriver.chrome import webdriver

option = webdriver.ChromeOptions()


def get_music_name():

    song_name = input("输入歌曲名:》 ")
    #url = 'https://music.163.com/#/search/m/?s={}&type=1'.format('黄昏')
    url = 'https://music.163.com/#/search/m/?s={}&type=1'.format(song_name)

    """headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/search/'
    }"""

    driver = webdriver.Chrome()
    driver.get(url=url)
    driver.switch_to_frame('g_iframe')
    #获取歌曲id
    req = driver.find_element_by_id('m-search')

    a_id = req.find_element_by_xpath('.//div[@class="item f-cb h-flag  "]/div[2]//a').get_attribute('href')
    print(a_id)


    song_id = a_id.split('='[-1])
    #print(song_id[1])
    s_id = song_id[1]
    return s_id

if __name__ == '__main__':
    get_music_name()

