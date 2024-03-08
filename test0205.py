# # import logging
# import json
# import os
import json
import sys
import time
# # import os
# # from common.read_file import ReadFile
# # import pytest
# # import requests
#
# # @pytest.mark.parametrize("id,status_code",[["1",200],["字符",404],["zifu",404]])
# # def testData(id,status_code):
# #     url = "http://127.0.0.1:81/zentao/api.php/v1/departments/" + str(id)
# #     # params = {
# #     #     "id": id
# #     # }
# #     headers = {
# #         "Token": "9ee384c2332ed9d844ea9ad40e0b1433"
# #     }
# #     logging.info("测试开始。。。")
# #     res = requests.get(url, headers=headers)
# #     print(res.text)
# #     assert res.status_code == status_code
# #     logging.info("测试结束。。。")
#
# # import logging
# # logging.basicConfig(level=logging.INFO,
# #                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
# #                     datefmt='[%Y-%m_%d %H:%M:%S]',
# #                     filename='./my.log',
# #                     filemode='a')
# # logging.critical('logging critical message.')
# # logging.error('logging error message')
# # logging.warning('logging warning message')
# # logging.info('logging info message')
# # logging.debug('logging debug message')
# import allure
# import pytest
# import yaml
#
# # print(time.strftime("%Y%m%d"))
#
# #
# # BASE_PATH = os.path.dirname(os.path.realpath(__file__))
# # print("BASE_PATH:"+BASE_PATH)
# # data_file = os.path.join(BASE_PATH,"data","base_data.yml")
# # print("data_file:"+data_file)
# # data = ReadFile().read_data_yml(data_file)
# # print(data,type(data))
# # print(data["login_info"]["username"])
#
# # dict_test = {
# #     "name": "sxj",
# #     "age": 18,
# #     "addr": "杭州市"
# # }
# # dt = dict(**dict_test)
# # print(dt["name"])
# """
# leetcode算法题：
# 最长连续序列
# 示例 2：
# 输入：nums = [0,3,7,2,5,8,4,6,0,1]
# 输出：9
# """
# #
# # def longestConsecutive(nums):
# #     #最长len
# #     max_len = 0
# #     dic = {}
# #     while len(nums)>0:
# #         key = nums[0]
# #         while key in nums:
# #             dic[key] = [].append(key)
# #             nums.remove(key)
# #             key = key+1
# #     for value in dic.values():
# #         le = len(value)
# #         if le>max_len:
# #             max_len = le
# #     return max_len
#
#
# # class Solution:
# #     def longestConsecutive(self, nums):
# #         res = 0     # 记录最长连续序列的长度
# #         num_set = set(nums)     # 记录nums中的所有数值
# #         for num in num_set:
# #             # 如果当前的数是一个连续序列的起点，统计这个连续序列的长度
# #             if (num - 1) not in num_set:
# #                 seq_len = 1     # 连续序列的长度，初始为1
# #                 while (num + 1) in num_set:
# #                     seq_len += 1
# #                     num += 1    # 不断查找连续序列，直到num的下一个数不存在于数组中
# #                 res = max(res, seq_len)     # 更新最长连续序列长度
# #         return res
#
#
# # nums = [0,3,7,2,5,8,4,6,0,1]
# # print(set(nums))
# # max = Solution().longestConsecutive(nums)
# # print(max)
#
# """
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法来解决此问题，且该算法只使用常量额外空间。
#
# 示例 1 ：
#
# 输入：nums = [2,2,1]
# 输出：1
# 示例 2 ：
#
# 输入：nums = [4,1,2,1,2]
# 输出：4
# 示例 3 ：
#
# 输入：nums = [1]
# 输出：1
# """
# # class Solution:
# #     def singleNumber(self, nums):
# #         # pr = nums[0]
# #         # nums.remove(pr)
# #         # while pr in nums:
# #         #     nums.remove(pr)
# #         #     pr = nums[0]
# #         #     nums.remove(pr)
# #         # return pr
# #         """
# #         解法二:异或运算
# #         :param nums:
# #         :return:
# #         """
# #         result = 0
# #         for i in nums:
# #             result ^= i
# #         return result
# #
# #
# # nums = [4,1,2,1,2]
# # n = Solution().singleNumber(nums)
# # print(n)
# from common.client import Client
# # name = "http://"
# # json_p = {
# # 	"page": 1,
# # 	"total": 1,
# # 	"limit": 1,
# # 	"users": [{
# # 		"id": 1,
# # 		"dept": 0,
# # 		"account": "admin",
# # 		"realname": "admin",
# # 		"role": "",
# # 		"pinyin": "admin a",
# # 		"email": "",
# # 		"group": {
# # 			"13": {
# # 				"id": 13,
# # 				"project": 0,
# # 				"vision": "rnd",
# # 				"name": "\u9879\u76ee\u7ba1\u7406\u5458",
# # 				"role": "projectAdmin",
# # 				"desc": "\u9879\u76ee\u7ba1\u7406\u5458\u53ef\u4ee5\u7ef4\u62a4\u9879\u76ee\u7684\u6743\u9650",
# # 				"acl": "",
# # 				"developer": "1"
# # 			}
# # 		}
# # 	}]
# # }
# # json_t = json.dumps(json_p)
# #
# # di = json.loads(json_t)
# # li = di["users"]
# # id = [i['id'] for i in li]
# # print(id)
# # 给定一个大小为
# # n
# # 的数组
# # nums ，返回其中的多数元素。多数元素是指在数组中出现次数
# # 大于 ⌊ n / 2 ⌋ 的元素。
# #
# # 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# #
# #
# #
# # 示例
# # 1：
# #
# # 输入：nums = [3, 2, 3]
# # 输出：3
# # 示例
# # 2：
# #
# # 输入：nums = [2, 2, 1, 1, 1, 2, 2]
# # 输出：2
# # def majorityElement(nums):
# # 	max = 0
# # 	max_num = nums[0]
# # 	nums_set = set(nums)
# # 	for i in nums_set:
# # 		num = nums.count(i)
# # 		if num > max:
# # 			max = num
# # 			max_num = i
# # 	return max_num
# # nums = [3,2,3]
# # max = majorityElement(nums)
# # print(max)
# """
# 20. 有效的括号
# 提示
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
#
# 有效字符串需满足：
#
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 每个右括号都有一个对应的相同类型的左括号。
#
#
# 示例 1：
#
# 输入：s = "()"
# 输出：true
# 示例 2：
#
# 输入：s = "()[]{}"
# 输出：true
# 示例 3：
#
# 输入：s = "(]"
# 输出：false
# """
#
#
# # def isValid(s):
# # 	dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
# # 	stack = ['?']
# # 	for num in s:
# # 		if num in dic.keys():
# # 			stack.append(num)
# # 		elif dic[stack.pop()] != num:
# # 			return False
# #
# # 	return len(stack) == 1
# #
# #
# # di = "(())"
# # # for i in di.keys():
# # # 	print(i)
# # bo = isValid(di)
# # print(bo)
# # from common.read_file import read_file
# #
# # base_path = os.path.dirname(os.path.realpath(__file__))
# # file_path = os.path.join(base_path,"data/user_info.yml")
# # print(file_path)
# #
# # data = read_file.read_data_yml(file_path)
# # print(data,"\n",type(data))
# # print(data["user_info"],len(data["user_info"]))
#
# # js = {
# #   "headers": {
# #     "Accept": "*/*",
# #     "Accept-Encoding": "gzip, deflate",
# #     "Connection": "keep-alive",
# #     "Content-Type": "application/json;charset=UTF-8",
# #     "Cache-Control": "no-cache",
# #     "X-163-AcceptLanguage": "zh",
# #     "Accept-Language": "zh-CN,zh;q=0.9",
# #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36",
# #     "Pragma": "no-cache"
# #   }
# # }
# # print()
# # {**read_data.load_yaml("configs/chrome.yml")["headers"], **headers}
# # import requests
# # import json
# #
# # url = "http://127.0.0.1:81/zentao/api.php/v1/users/1"
# #
# # payload = json.dumps({
# #   "realname": "123"
# # })
# # headers = {
# #   'token': '3427ec62bfbe8526c4823fffd9814204',
# #   'Content-Type': 'application/json',
# #   'Cookie': 'device=desktop; lang=zh-cn; theme=default; zentaosid=3427ec62bfbe8526c4823fffd9814204'
# # }
# #
# # response = requests.request("PUT", url, headers=headers, data=payload)
# #
# # print(response.text)
#
# """
# 链表的学习：
# 	1、单链表:
# 		两个属性+增删改查
# """
# #
#
# """
# error和assert失败的区别，以及exception
#
# """
#
# # import pytest
# #
# #
# # def test_case01():
# # 	print("我是测试用例1")
# #
# #
# # @pytest.mark.skip(reason="不执行该用例！！因为没写好！！")
# # def test_case02():
# # 	print("我是测试用例2")
# #
# #
# # flag = 1
# #
# #
# # @pytest.mark.skipif(flag == 1, reason="按条件忽略测试文件")
# # def test_case03():
# # 	print("我是测试用例3")
# #
# # @pytest.mark.xfail()
# # def test_case04():
# # 	# assert 1==0
# # 	print("我是测试用例4")
# # if __name__ == '__main__':
# # 	pytest.main(['-s', '-v', "-q", 'test_skip.py'])
# # from string import Template
# #
# # def readfile(path):
# # 	with open(path,encoding="UTF-8") as f:
# # 		data_yml = f.read()
# # 		temp = Template(data_yml)
# # 		temp1 = temp.safe_substitute({"username":"sxj{}".format(timestamp),"realname":"测试用户{}".format(timestamp)})
# # 		data = yaml.safe_load(temp1)
# # 	return data
# # timestamp = time.strftime("%y%m%d%H%M%S", time.localtime())[:-1]
# # Base_path = os.path.dirname(os.path.realpath(__file__))
# # path_file = os.path.join(Base_path,"data","user_info.yml")
# # print(path_file)
# # data = readfile(path_file)
# # @pytest.fixture(scope="function")
# # def login():
# # 	return "token"
# # def setup_function():
# # 	print("前置准备。。。")
# # def test_01():
# # 	# print("返回什么{}".format(login))
# # 	pass
# #
# # def test_02():
# # 	assert 1==1
# #
# # def test_03():
# # 	# print("返回什么{}".format(login))
# # 	pass
# """
# 单例模式：
# 1、使用装饰器
# 2、使用元类
# """
# # from functools import wraps
# #
# #
# # def singleton(cls):
# #     """单例类装饰器"""
# #     instances = {}
# #
# #     @wraps(cls)
# #     def wrapper(*args, **kwargs):
# #         if cls not in instances:
# #             instances[cls] = cls(*args, **kwargs)
# #         return instances[cls]
# #
# #     return wrapper
# #
# #
# # @singleton  #President = singleton(President)
# # class President:
# #     def __init__(self):
# #         print("被装饰的类")
# #
# # P = President()
# # p2 = President()
# # P3 = President()
# #使用元类
#
#
#
# # class MyMeta(type):
# #
# #     def __init__(self, *args, **kwargs):
# #         self.__instance = None
# #         super(MyMeta, self).__init__(*args, **kwargs)
# #
# #     def __call__(self, *args, **kwargs):
# #         if self.__instance is None:
# #             self.__instance = super(MyMeta, self).__call__(*args, **kwargs)
# #         return self.__instance
# #
# #
# # class MyClass(metaclass=MyMeta):
# #     pass
# #
# #
# # m = MyClass()
# # m2 = MyClass()
# # print(m2 == m)
#
# #
# # class p(type):
# #
# #     def __init__(self,*args,**kwargs):
# #         print("这是一个__Init__方法")
# #
# #     def __call__(self, *args, **kwargs):
# #         print("这是一个__call__方法")
# #
# # class pp(metaclass=p):
# #     pass
# # o = pp()
# # from collections.abc import Iterable,Iterator
# # class MyNumber(object):
# #
# #     def __init__(self):
# #         self.a = 0
# #     def __iter__(self):
# #         return self
# #     def __next__(self):
# #         self.a += 1
# #         if self.a >10:
# #             raise StopIteration
# #         return self.a
# #
# # m = MyNumber()
# # print(isinstance(m,Iterable))
# # print(isinstance(m,Iterator))
# # def mypow(x,y=2):	# y的默认值为2，不添加参数y时默认以y=2计算
# #     print(x ** y)
# # mypow(2,3)
# # mypow(2)
# # try:
# #     int(a)
# # except Exception:
# #     pass
# # try:
# #     print("开始只执行")
# #     int(a)
# # except Exception as e:
# #     print("发生异常")
# # raise Exception
# #
# # print("结束。。。。")
#
# # from copy import deepcopy
# #
# # a = [1,2,[1,2]]
# # b = a.copy()
# # c = deepcopy(a)
# # a[2].append(3)
# #
# # print(a)
# # print(b)
# # print(c)
#
# """
# 装饰器：
#
# """
# from functools import wraps
# # def decorator(fun):
# #
# #     def inner():
# #         print("装饰开始")
# #         fun()
# #         print("装饰结束")
# #     return inner
# #
# # @decorator
# # def addNum():
# #     print("被装饰的函数")
# #
# # addNum()
# # print(addNum.__name__)
# # import pytest
# # num1 = 2
# #
# # pytestmark = pytest.mark.order
# # url = "https://blog.csdn.net/weixin_60870637/article/details/126974874"
# # # 标记测试函数
# # @allure.issue(url,name="bug地址")
# # @pytest.mark.skipif(num1>1,reason="满足{}>1".format(num1))
# # @pytest.mark.run(order=1)
# # def test_01():
# #     print("执行test_01")
# #
# # @allure.testcase(url,name="csdn地址")
# # @pytest.mark.xfail(num1<1,reason="不满足条件，需要标记为失败")
# # @pytest.mark.run(order=2)
# # def test_02():
# #     print("执行test_02")
# #     # assert 1 == 0
# #
# # @allure.link("https://zhuanlan.zhihu.com/p/675147797",name="知乎链接")
# # @pytest.mark.login
# # @pytest.mark.flaky(reruns=5,reruns_delay=60)
# # def test_03():
# #     print("执行test_03")
# #     assert 1 == 1
from multiprocessing import Process
# from threading import Thread
# def dance():
#     print("正在跳舞。。。")
#     time.sleep(5)
#     print("跳舞结束。。。。")
#
# def sing():
#     print("正在唱歌。。。")
#     time.sleep(10)
#     print("唱歌结束。。。")
#
#
#
# if __name__ == "__main__":
#     p1 = Thread(target=dance)
#     p2 = Thread(target=sing)
#     p1.start()
#     p2.start()
#     # print(p.name)
#     # print(p.pid)
#
#     # print(p.name)
#     # print(p.pid)
#     p1.join()
#     print("主进程。。。。")
# class prot(object):
#     def __init__(self):
#         print("对象初始化.....")
#     def __enter__(self):
#         print("我是上下文管理器的上文。")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("我是上下文管理器的下文。")
#        # return True
#
#     def add(self,a,b):
#         print(a+b)
#
# g = prot()
# with g as v:
#     g.add(1,2)

# strs = 'I like java'
# print(strs.replace('I','Yours'))
# print(strs.replace('a','*',2))
# print(strs)
#
# tmp = dict.fromkeys(['a','b'],{4,10})
# print(tmp)
# t = tmp.keys()
# print(t,type(t),iter(t))
# print(tmp["c"])

# class tt:
#     co = [1,2]
#     def __init__(self):
#         pass

# def is_odd(n):
#     return n % 2 == 1
#
#
# if __name__ == '__main__':
#     newlist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
#     print(list(newlist))
    # b1 = tt()
    # b2 = tt()
    # b1.co.append(3)
    # print(id(b1.co),id(b2.co),id(tt.co))
    # print(b1.co)
    # print(b2.co)
    # print(tt.co)
    # sets = {1,2,3,4,5}
    # li = list(sets)
    # print(sets,type(sets),li[1])
    #
    # a = [['1','2']for i in range(2)]
    # print(a)
    # b = [1,]*2
    # print(b)
    # c = '123'*2
    # print(c)


# import functools
# from operator import attrgetter,itemgetter
#
# oldlist = [32,33, 16, 40]
# newlist = sorted(oldlist)
# print(newlist,type(newlist))
#
# oldlist = [('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12),('john', 'B', 15)]
# #多级排序
# newlist = sorted(oldlist,key=itemgetter(0,1),reverse=True)
# print(newlist)
#
# oldlist = [{'age':14},{'age':15},{'age':16}]
# #多级排序
# newlist = sorted(oldlist,key=lambda x:x['age'],reverse=False)
# print(list(newlist))
#
# def cmp(a, b):
#   return b-a
# oldlist = [1, 2, 5, 4]
# #自定义排序规则 从大到小
# newlist = sorted(oldlist, key=functools.cmp_to_key(cmp))
# print(list(newlist))

# from multiprocessing import Process
# import os, time
#
# class CustomProcess(Process):
#     def __init__(self, p_name, target=None):
#         # step 1: call base __init__ function()
#         super(CustomProcess, self).__init__(name=p_name, target=target, args=(p_name,))
#
#     def run(self):
#         # step 2:
#         # time.sleep(0.1)
#         print("Custom Process name: %s, pid: %s "%(self.name, os.getpid()))
#
# if __name__ == '__main__':
#     p1 = CustomProcess("process_1")
#     p1.start()
#     p1.join()
#     print("subprocess pid: %s"%p1.pid)
#     print("current process pid: %s" % os.getpid())
# class TT:
#     __name = "sss"
#     def __init__(self,age):
#         self.age = age
#
#
# t = TT(12)
# print(t.__dict__)

# n = 1
#
# def test():
#     global n  # 不加的话会报错
#     n += 5
#     print(n)
#
# test()
# print(n)
# def test():
#     print(n)  # 这么用没问题

# a = input("input:")
# print('haha',type(a))
# str = "hhhh"
# string = "hello"
# # substr = 'll'
# # t = str.find(substr, start=0 ,end=len(string)) #python找到第一个出现的
# # tt = str.rfind(substr, start=0 ,end=len(string)) #python找到最后一个出现的
#
# print('\n'.join(['a','b','c','d']))
# strs = 'abcd'
# print(strs.center(60,'*'))
# print([1,2,3] == [1,3,2])
import requests


import pytest
import requests
# import os
# from common.read_file import read_file
# from common.parameters_read_data import parameters_read_data
# def get_file_path(filename):
#     BASE_PATH = os.path.dirname(os.path.realpath(__file__))
#     return os.path.join(BASE_PATH,"data",filename)
# data_yaml = get_file_path("base_data.yml")
# departments_data_yml = get_file_path("departments_data.yml")
# user_yaml = get_file_path("user_info.yml")
#
# data_info = read_file.read_data_yml(data_yaml)
# with open(user_yaml,encoding='UTF-8') as f:
#     data = f.read()
#     print(data,type(data))
# from string import Template
#
#
# from string import Template
#
#
# tempTemplate  = Template("There $a and $b")
# d={'a':'apple','b':'banbana'}
# print(tempTemplate.substitute(d))
# def test_getcookie():
#     '''
#
#     此方法用于获取login接口中返回的cookie
#
#     :param url_header_list 类型是一个列表，列表一个元素是url，第二个是header
#
#     return cookie
#
#     rtype dict
#
#     '''
#     path = "http://" + data_info["env_info"]["ip"] + ":" + str(data_info["env_info"]["port"]) + "/zentao/api.php/v1/"
#     url = path + "tokens"
#     data = {
#         "account": data_info["login_info"]["username"],
#         "password": data_info["login_info"]["password"]
#     }
#     response = requests.post(url=url, json=data)
#     cookies = response.cookies.get_dict()
#     print(response.text)
#     print(cookies,type(cookies))
#     print("cookies:", cookies['zentaosid'])
#     os.environ["cookie"] = json.dumps(cookies["zentaosid"])
#     for key in os.environ:
#         print(f'环境变量{key}:{os.getenv(key)}')
from functools import reduce
# s = '192.168.1.10'
# ss = s.split('.',maxsplit=2)
# print('-'.join(ss))
#
# b = {}
# a = [1,2,2,3,3,4,5]
# c = b.fromkeys(a,[1,2,3])
# print(list(c),type(c),'\n',c)
#
# d = {'a':1,'b':2}
# print(list(d))

# import pytest
#
#
# # 定义一个用例级别的夹具
# @pytest.fixture
# def my_fixture():
#     print('------my_fixture---用例前置执行脚本--------')
#     yield
#     print('------my_fixture---用例后置执行脚本--------')
#
#
# # 函数用例 指定测试夹具
# def test_func__01(my_fixture):
#     print("测试用例----test_func__01----")
#
#
# class TestDome:
#     # 函数用例 指定测试夹具
#     def test_02(self, my_fixture):
#         print('----测试用例：test_02------')
#
#     # 函数用例 指定测试夹具
#     def test_03(self):
#         print('----测试用例：test_03------')

import pymysql