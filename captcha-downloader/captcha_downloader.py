#coding:utf-8
import requests
import json
import base64
import uuid
import random,time,os

'''
访问国税网站，下载验证码保存在当前目录下
key1 : 图片代码
key2 : 有效时间
key3 : index  
key4 : 
       00
       01 红色文字
       02 黄色文字  
       03 蓝色文字
####https://fpcy.gd-n-tax.gov.cn/WebQuery/yzmQuery?callback=jQuery110206562392569612712_1518159395093&fpdm=044001500111&r=0.10662946407683194&v=V1.0.04_001&nowtime=1518159526735&area=4400&publickey=3241266FBB942BFE968150E98F84B247&_=1518159395104"
'''

URL_P0 = "https://fpcy.gd-n-tax.gov.cn/WebQuery/yzmQuery"
URL_P1 = "jQuery110206562392569612712_1518159395093"
URL_P2= "fpdm=044001500111&r=0.10662946407683194&v=V1.0.04_001&nowtime=1518159526735&area=4400&publickey=3241266FBB942BFE968150E98F84B247&_=1518159395104"

url = '{0}?callback={1}&{2}'.format(URL_P0, URL_P1, URL_P2 )

def generate_captcha_image():

    r = requests.get(url)
    if r.status_code == 200 :
        #print r.content
        json_str = r.content[(len(URL_P1)+1):-1 ]
    #  print json_str
        data = json.loads(json_str)
    #    print data['key1']
    
        with open( '{0}/{1}.png'.format( data['key4'] , uuid.uuid4()) , "wb") as fh:
            fh.write(base64.decodestring(data['key1']))
     
if __name__ == '__main__':
	# 测试
    while(1):
    	generate_captcha_image()
    	print '... ',time.ctime()