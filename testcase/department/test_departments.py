import logging
import os

import allure
import pytest
import requests
from common.client import Client

from common.logger import logger


from conftest import get_departments_data
class TestDepartments:

    BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    # print("BASE_PATH:" + BASE_PATH)
    """获取token"""
    path = "http://127.0.0.1:81/zentao/api.php/v1/"
    id = None
    headers = {}
    @allure.feature("禅道")
    @allure.story("部门")
    @allure.title("获取部门列表")
    def test_get_departments(self,post_token):
        url = TestDepartments.path + "departments"
        TestDepartments.headers = {
            "Token": post_token
        }
        res = requests.get(url,headers=TestDepartments.headers)
        if res.text:
            TestDepartments.id = res.json()[0]["id"]
        logger.info("url:{}\n status_code:{}\n Response:{}".format(url,res.status_code,res.json()))
        assert res.status_code == 200

    @pytest.mark.parametrize("id,status_code",get_departments_data["get_departments_id"])
    # @pytest.mark.xfail(reason="功能预期有问题")
    @allure.feature("禅道")
    @allure.story("部门")
    @allure.title("获取部门id={id}的详情")
    def test_get_department_id(self,post_token,id,status_code):
        url = "departments/" + str(id)
        res = Client(TestDepartments.path).get(url,headers=TestDepartments.headers)
        logger.info("url:{}\n status_code:{}\n Response:{}".format(res.url, res.status_code, res.json()))
        assert res.status_code == status_code

