import pytest
import requests
import os
from common.read_file import read_file
from common.parameters_read_data import parameters_read_data
def get_file_path(filename):
    BASE_PATH = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(BASE_PATH,"data",filename)
data_yaml = get_file_path("base_data.yml")
departments_data_yml = get_file_path("departments_data.yml")
user_yaml = get_file_path("user_info.yml")

data_info = read_file.read_data_yml(data_yaml)
get_departments_data = read_file.read_data_yml(departments_data_yml)
usr_info = parameters_read_data.readfile(user_yaml)
# print(usr_info)



@pytest.fixture(scope="session")
def post_token():
    path = "http://"+data_info["env_info"]["ip"]+":"+ str(data_info["env_info"]["port"])+"/zentao/api.php/v1/"
    url = path + "tokens"
    data = {
        "account": data_info["login_info"]["username"],
        "password": data_info["login_info"]["password"]
    }
    res = requests.post(url=url, json=data)
    token = res.json()["token"]
    return token

