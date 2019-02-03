# channels test

一直很想玩玩django的ebsocket，google找到channels，所以就來玩玩看

## Pre environment setup

Redis: `docker run --name some-redis  -p 6379:6379  -d redis redis-server --appendonly yes`


## Note
如果系統是Windows要多裝win32api: `pip install pywin32` (這次練習時是裝224版)

## Reference
[Django Channels](https://channels.readthedocs.io/en/latest/)  
[twtrubiks/django-channels2-tutorial](https://github.com/twtrubiks/django-channels2-tutorial)  
[跟著 Vue 闖蕩前端世界](https://dotblogs.com.tw/wasichris/2017/03/01/172049)  
