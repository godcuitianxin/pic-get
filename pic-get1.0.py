#coding:utf-8

import requests as r
import re 
import time
import os

browser = 'https://image.baidu.com/search/flip?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=utf-8&word={}&ala=1&alatpl=adress&pos=0&hs=2&xthttps=111111'
name = input('请输入想查找的名称：')
number = int(input('请输入想要张数：'))
header = {'User-Agent':' Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66'}
def urlGet():
    try:
        url = browser
        pic_url = url.format(name)
        html = r.get(pic_url,header)
        html.encoding = 'utf-8'
        html_text = html.text
        
        return html_text
    except:
        print('网页html爬取失败\n请重试')
        return 0
def pic_urlGet(html_text):
    try:
        each_pic = re.findall(r' "objURL":"(.*?)"',html_text)#each_pic是一个列表
        return each_pic      
    except:
        print('网址爬取失误\n请重试')
        return 0
def downLoad(each_pic):
    n=1
    try:
        os.mkdir('e:\\{}_picture'.format(name))
        while n<=number:
            pic = r.get(each_pic[n-1],header)
            time.sleep(0.5)
            with open('e:\\{}_picture\\{}_picture{}.jpg'.format(name,name,n),'wb') as f:#文件保存到E盘
                f.write(pic.content)            
                print('{}/{}'.format(n,number))
                n+=1
        print('下载完成')
        f.close()
    except:
        print('文件夹已存在或下载失败')
        
if __name__ == '__main__':        
    downLoad(pic_urlGet(urlGet()))
    
    
    

    

    
    


