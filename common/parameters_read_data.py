import os.path
import time
from string import Template
import yaml
from common.timestamp import timestamp
class ReadParamFile:
	def readfile(self,path,**sub_str):
		with open(path,encoding="UTF-8") as f:
			default_str = {
				"username": "sxj{}".format(timestamp),
				"realname": "测试用户{}".format(timestamp)
			}
			if sub_str:
				sub_str = {**default_str,**sub_str}
			else:
				sub_str = default_str
			data_yml = f.read()
			temp = Template(data_yml)
			temp1 = temp.safe_substitute(sub_str)
			data = yaml.safe_load(temp1)
		return data
parameters_read_data = ReadParamFile()
#
# if __name__ == "__main__":
# 	pass
	# parameters_read_data.readfile()