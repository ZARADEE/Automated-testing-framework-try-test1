import requests

#接口测试的示例
#一般三步走，1.准备测试数据
url='http://apihcc.fecmall.com/v1/account/login'
data={
    'username':'admin',
    'password':'admin123',
    }

#请求的模拟
res=requests.post(url=url,json=data)

#解析响应结果，并校验数据
print(res.text)
print('此处为http状态码:{}'.format(res.status_code))