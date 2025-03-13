"""
    请求的关键字驱动类，封装常见的接口测试方法
    一般来说请求的url是根据环境决定的
"""
from urllib import response
from wsgiref import headers
import requests

from conf import set_conf

#封装常见的方法使用
#以下代码仅仅为最基本的结构，根据现实需要可进行修改
#也许有的时候path不需要参数，直接就是url网址的情况下
class ApiKeys:
    #get
    def do_get(self,path=None,headers=None,params=None,**kwargs):
        #url的组成应该是url+path的类型,方便后期维护所以写成一个方法
        url=self.set_url(path)
        #例如我们要通过文件的方式在headers里面加入一个token
        headers=self.set_headers(headers)
        return requests.get(url=url,headers=headers,params=params,**kwargs)

    #post:如果需要传递json格式的内容，需要进行二次处理
    def do_post(self,path=None,headers=None,data=None,json=1,**kwargs):
        #url的组成应该是url+path的类型,方便后期维护所以写成一个方法
        url=self.set_url(path)
        #例如我们要通过文件的方式在headers里面加入一个token
        headers=self.set_headers(headers)
        #判断是否输入json格式
        if json:
            response= requests.post(url=url,headers=headers,json=data,**kwargs)
        else:
            response=requests.post(url=url,headers=headers,data=data,**kwargs)
        return response

    #url拼接
    def set_url(self,path):
        #读取配置的环境信息，此处直接写死，后期还能修改
        base_url=set_conf.read('severs','DEV')
        if path:
            url=base_url+path
        return url

    #headers拼接
    def set_headers(self,headers=None):
        #定义通用的基础头信息,简化请求时候的参数定义与设置，一般在传入的时候都有一个简要的格式定义
        #简化测试用例的数据内容,以useragent为例子
        base_headers={
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
        }
        #如果有新的头信息加入，则在headers中继续补充
        if headers:
            base_headers.update(headers)
            #如果产生access-token字段则自动进行添加，是一种与test—api中的读取文件加入token相对的方式
        if set_conf.read('headers','access-token'):
            base_headers['access-token']=set_conf.read('headers','access-token')
        return base_headers 