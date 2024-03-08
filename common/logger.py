import logging
import os
import time
BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
path_name = os.path.join(BASE_PATH,"log")
if not os.path.exists(path_name):
    os.mkdir(path_name)
name = os.path.join(path_name,"{}.log".format(time.strftime("%Y%m%d")))
print(name)


class Logger:

    def __init__(self):
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.INFO)
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 初始化日志文件对象
        self.handler = logging.FileHandler(name, mode='a', encoding="UTF-8")
        self.handler.setLevel(logging.INFO)
        self.handler.setFormatter(self.formatter)

        # 初始化控制台对象
        # self.console = logging.StreamHandler()
        # self.console.setLevel(logging.DEBUG)
        # self.console.setFormatter(self.formatter)

        # 添加日志文件和控制台对象
        self.logger.addHandler(self.handler)
        # self.logger.addHandler(self.console)

logger = Logger().logger
