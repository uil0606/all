# -*- coding: UTF-8 -*-

from aip import AipOcr
from aip import AipFace
import json

# 定义常量
APP_ID = '10882805'
API_KEY = 'UsSGNVR6x4ALjc1ZrHCClsLH'
SECRET_KEY = 'dyXqOIpqBcMaz0UhpgX6RLQCEuNTzg3p '

# 初始化AipFace对象
aipOcr = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "C:/Users/magfi/Desktop/test8.png"


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
    'detect_direction': 'true',
    'language_type': 'CHN_ENG',
}

# 调用通用文字识别接口
result = aipOcr.basicAccurate(get_file_content(filePath), options)
print(result)
