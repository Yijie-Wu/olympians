# -*- encoding:utf-8 -*-
"""
Author: Yijie.Wu
Email: 1694517106@qq.com
"""
import os
import sys
import json


def default_json_parser(json_path, func_name):
    """
    :param json_path: 要解析的json路径
    :param func_name: 测试函数的名称
    :return: 解析完的数据
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        json_content = json.load(f)
        return json_content.get(func_name)


def data_provider(default=True, data_path=None, parser=None):
    if data_path:
        default = False

    def decorator(test_func):
        frame = sys._getframe()
        test_func_path = frame.f_back.f_code.co_filename
        test_func_name = test_func.__name__

        def wrapper(self):
            if default:
                default_json_path = test_func_path.replace('testcase', 'testdata').replace('.py', '.json')
                if os.path.exists(default_json_path):
                    if parser:
                        data = parser(default_json_path)
                    else:
                        data = default_json_parser(default_json_path, test_func_name)
                    return test_func(self, data)
                else:
                    raise FileNotFoundError
            else:
                if parser:
                    if os.path.exists(data_path):
                        data = parser(data_path)
                    else:
                        raise FileNotFoundError
                else:
                    data = default_json_parser(data_path, test_func_name)
                return test_func(self, data)

        return wrapper

    return decorator