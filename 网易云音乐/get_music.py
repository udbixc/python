#!/usr/bin/env python
# encoding: utf-8

import requests
import json

#还是需要输入歌曲id

def get_songs(song_id):
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_%s' %(song_id)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        'Host': 'music.163.com',
        'Referer': 'http://music.163.com/search/'}
    response = requests.get(url=url, headers=headers)
    #print(response.text)

    # dict
    data = json.loads(response.text)
    # print(type(data))

    # print(data)
    for i in range(0, 15):
        print(data['hotComments'][i]['content'])
        print('####################')

#张学友-饿狼传说
#get_songs(190270)

#刘若英-后来
#get_songs(254574)