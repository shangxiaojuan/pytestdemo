"""
今日学习计划：
1、自动化项目学习，看完4个视频
pytest：
·依赖安装：放在根目录下，reqiurements.txt文件中，直接在terminal中，执行pip install -r requirements.txt
文件中的内容如下：
pytest
pytest-html
pytest-xdist
pytest-ordering
pytest-rerunfailures
allure-pytest

运行规则：
·需要以test_开头或者以_test结尾的
·类以Test开头
·方法以test开头
运行方式：
①命令行
②主函数
③pytest.ini

2、leetcode算法题：刷两题
"""
import os
import pytest

if __name__ == '__main__':
    pytest.main(["-vs","-n",'2'])
    os.system("allure generate ./results -o ./report1 --clean")