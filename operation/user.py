
from common.client import Client
# from functools import wraps
from conftest import post_token

api_root_url = "http://127.0.0.1:81/zentao/api.php/v1/"

#以下是装饰器实现的单例模式
# def decorator(cls):
#     instance = None
#     @wraps(cls)
#     def wrapper(*args,**kwargs):
#         if instance == None:
#             return cls(*args,**kwargs)
#     return wrapper
# @decorator
class RestUser(Client):

    headers = {}
    def __init__(self):
        super().__init__(api_root_url)
        # RestUser.headers = {
        #     "token": post_token
        # }

    def get_user_personal_info(self,**kwargs):
        url = "user"
        post_token = dict(**kwargs)["post_token"]
        RestUser.headers = {
            "token": post_token
        }
        return self.get(url,headers=RestUser.headers)

    def get_users(self,**kwargs):
        url = "users"
        post_token = dict(**kwargs)["post_token"]
        RestUser.headers = {
            "token": post_token
        }
        params = {
                "page": 0,
                "limit": 0
        }
        return self.get(url,params=params)

    def get_user_id(self,id):
        url = "users/{}".format(id)
        return self.get(url)
    def edit_user_id(self,id,**kwargs):
        url = "users/{}".format(id)
        RestUser.headers["Content-Type"] = "application/json"
        RestUser.headers["Cookie"] = "device=desktop; lang=zh-cn; theme=default; zentaosid={}".format(RestUser.headers["token"])
        data = dict(**kwargs)["data"]
        return self.put(url,data=data,headers=RestUser.headers)

    def add_user(self,**kwargs):
        url = "users"
        data = dict(**kwargs)["data"]
        return self.post(url,data=data,headers=RestUser.headers)

    def delete_user(self,id):
        url = "users/{}".format(id)
        return self.delete(url,headers=RestUser.headers)
user = RestUser()  #可以实现单例模式
#也可以通过装饰器的方式
"""
单例模式的使用场景：
"""