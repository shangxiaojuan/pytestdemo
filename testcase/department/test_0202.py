import time

import allure
import pytest

@pytest.fixture(scope = "function", params=["test01","test02","test03"])
def myfixture(request):
    print("这是一个装饰器函数前置")
    yield request.param
    print("这是一个装饰器函数后置")

class TestAutotest1():

    def setup(self):
        print("方法之前执行。。。。")

    def setup_class(self):
        print("类之前执行。。。")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.run(order=1)
    def test_A(self, myfixture):
        print("hello+"+myfixture)
    # @pytest.mark.xfail(reason="测试一下")
    @pytest.mark.run(order=2)
    def test_B(self):
        print("这是B。。。。。")

    @pytest.mark.module02
    @pytest.mark.run(order=3)
    # @pytest.mark.skip("跳过")
    def test_C(self):
        assert 1 == 1

    def teardown(self):
        print("方法执行结束后。。。。")
    def teardown_class(self):
        print("类之后执行。。。")
