import json

import allure
import pytest
from operation.user import user
from conftest import usr_info
from common.logger import logger
class TestUser:
    id = []

    @allure.step("获取用户个人信息")
    def test_get_personalInfo(self,post_token):
        response = user.get_user_personal_info(post_token)
        assert response.status_code == 200

    @allure.step("获取所有用户信息")
    def test_get_users(self,post_token):
        response = user.get_users(post_token=post_token)
        assert response.status_code == 200

    @allure.step("添加用户")
    @pytest.mark.parametrize("data1",usr_info["add_user_info"])
    def test_add_user(self,data1,post_token):
        realname = data1["realname"]
        data = json.dumps(data1)
        response = user.add_user(data=data,post_token=post_token)
        assert response.json()["realname"] == realname
        TestUser.id = response.json()["id"]

    def test_get_user_id(self,post_token):
        response = user.get_user_id(TestUser.id,post_token=post_token)
        assert response.status_code == 200

    @pytest.mark.parametrize("data1",usr_info["edit_user_info"])
    def test_edit_user_id(self,data1,post_token):
        realname = data1["realname"]
        data = json.dumps(data1)
        response = user.edit_user_id("1",data=data,post_token=post_token)
        assert response.json()["realname"] == realname

    def test_delete_users_id(self,post_token):
        response = user.delete_user(TestUser.id,post_token=post_token)
        assert response.json()["message"] == "success"
