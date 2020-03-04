# from bs4 import BeautifulSoup
# 
# with open("D:\\text.txt","r", encoding = "utf-8") as f:
#     mystr = f.read()
# 
# def request_download(url):
#     import requests
#     import hashlib
#     r = requests.get(url)
#     picname = hashlib.md5(url.encode("UTF-8")).hexdigest()
# 
#     with open(picname +'.png', 'wb') as f:
#         f.write(r.content)
# 
# soup = BeautifulSoup(mystr,'lxml')
# for item in soup.find_all("img"):
# 
#     request_download(item.get("src"))


import requests
import time

def picdown(url, i):
    r = requests.get(url)
    picname = 'bgm' + str(i).zfill(3)
    with open(picname +'.mp3', 'wb') as f:
        f.write(r.content)

for i in range(193, 227):
    num = str(i).zfill(3)
    url = 'https://bestdori.com/assets/cn/sound/bgm' + num + '_rip/bgm' + num + '.mp3'
    print(url)
    picdown(url, i)
    time.sleep(1)