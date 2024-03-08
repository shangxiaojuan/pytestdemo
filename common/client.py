import requests
from common.logger import logger
import json as complexjson
class Client:
    def __init__(self, api_root_url):
        self.api_root_url = api_root_url
        self.session = requests.session()

    def get(self, url, **kwargs):
        result = self.request(url, "GET", **kwargs)
        # logger.info(f"GET请求地址{url}")
        logger.info(f"GET的响应码 ==>> {result.status_code}")
        logger.info(f"GET的响应内容 ==>> {result.text}")
        return result


    def post(self, url, data=None, json=None, **kwargs):
        result = self.request(url, "POST", data, json, **kwargs)
        # logger.info(f"POST请求地址{url}")
        logger.info(f"POST的响应码 ==>> {result.status_code}")
        logger.info(f"POST的响应内容 ==>> {result.text}")
        return result

    def put(self, url, data=None, **kwargs):
        result = self.request(url, "PUT", data, **kwargs)
        # logger.info(f"PUT请求地址{url}")
        logger.info(f"PUT的响应码 ==>> {result.status_code}")
        logger.info(f"PUT的响应内容 ==>> {result.text}")
        return result

    def delete(self, url, **kwargs):
        result = self.request(url, "DELETE", **kwargs)
        logger.info(f"DELETE的响应码 ==>> {result.status_code}")
        logger.info(f"DELETE的响应内容 ==>> {result.text}")
        return result

    def patch(self, url, data=None, **kwargs):
        result = self.request(url, "PATCH", data, **kwargs)
        logger.info(f"PATCH的响应码 ==>> {result.status_code}")
        logger.info(f"PATCH的响应内容 ==>> {result.text}")
        return result


    def request(self, url, method, data=None, json=None, **kwargs):
        url = self.api_root_url + url
        headers = dict(**kwargs).get("headers")
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        if method == "GET":
            return self.session.get(url, **kwargs)
        if method == "POST":
            return requests.post(url, data, json, **kwargs)
        if method == "PUT":
            if json:
                # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                data = complexjson.dumps(json)
            return self.session.put(url, data, **kwargs)
        if method == "DELETE":
            return self.session.delete(url, **kwargs)
        if method == "PATCH":
            if json:
                data = complexjson.dumps(json)
            return self.session.patch(url, data, **kwargs)

    @staticmethod
    def request_log(url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):
        logger.info("接口请求地址 ==>> {}".format(url))
        logger.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        logger.info("接口请求头 ==>> {}".format(complexjson.dumps(headers, indent=4, ensure_ascii=False)))
        logger.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 data 参数 ==>> {}".format(complexjson.dumps(data, indent=4, ensure_ascii=False)))
        logger.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, indent=4, ensure_ascii=False)))
        logger.info("接口上传附件 files 参数 ==>> {}".format(files))
        logger.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies, indent=4, ensure_ascii=False)))


