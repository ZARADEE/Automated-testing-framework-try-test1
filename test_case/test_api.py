#使用unittest进行一个用例的执行


import unittest
from ddt import ddt, file_data
from api_keys.keys import ApiKeys
from conf import set_conf


#假设用例为对一个特定的url请求用户登录，格式为json方式为post
#url为http://fecsshop.appapi.fancyecommerce.com/v1/account/login
#DDT还支持从外部文件加载测试数据，这可以通过@file_data装饰器实现。支持的文件格式包括JSON和YAML。这使得管理大量测试数据变得更加方便
@ddt
class  TestApi(unittest.TestCase):
    #接下来进行第一次优化，优化前api=ApiKeys()
    @classmethod
    def setUpClass(cls) -> None:
        cls.api=ApiKeys()
        #cls.access_token=None这里是全局变量设置位置
        #此处改动为使用配置文件代替全局变量
    
    #此处因为是测试用例，所以具有编号
    @file_data('../test_data/login.yaml')
    def test_01_loogin(self,**kwargs):
        #api=ApiKeys()
        res=self.api.do_post(path=kwargs['path'],data=kwargs['data'])
        print(res.text)
        #全局变量形态实现关联数据的传递
        #TestApi.access_token = res.json()['access-token']
        #通过写入文件实现关联数据的传递
        set_conf.write('headers','access-token',res.json()['access-token'])

    #基于登录的数据进行关联，获取多语言列表
    #此时的languages需要一个token
    @file_data('../test_data/languages.yaml')
    def test_02_languages(self,**kwargs):
        #api=ApiKeys()
        #print(self.access_token)
        #接下来将topken加入headers中，token是通过全局变量的方式置入
        #kwargs['headers']={'access-token':self.access_token}
        #读取文件中的headers信息
        #通过keys.py文件的55，56行对手动读取文件token进行自动化
        #kwargs['headers']={'access-token':set_conf.read('headers','access-token')}
        res=self.api.do_get(path=kwargs['path'],data=kwargs['data'])
        print(res.text)
if __name__=='__main__':
    unittest.main()

    #根据不同的网站进行修改与不同环境下的测试