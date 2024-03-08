from common.logger import logger
import yaml
import json

class ReadFile:
    def read_data_yml(self, data_file):
        logger.info("加载{}文件.......".format(data_file))
        with open(data_file,encoding="UTF-8") as f:
            data = yaml.safe_load(f)
            logger.info("读取到数据==> {}".format(data))
        return data

    def read_data_json(self, data_file):
        logger.info("加载{}文件.......".format(data_file))
        with open(data_file,encoding="UTF-8") as f:
            data = json.load(f)
            logger.info("读取到数据==> {}".format(data))
        return data



read_file = ReadFile()
