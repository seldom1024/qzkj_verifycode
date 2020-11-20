import io

import requests
from PIL import Image
import sys
from io import BytesIO
import base64
import re

from char_lists import chars


def identify(img):
    identification_code_temp = []
    identification_code = [''] * 4
    diff_min = [144] * 4
    for i in range(4):
        identification_code_temp.append(img.crop((i * 10, 0, i * 10 + 13, 12)).getdata())
    for char in chars:
        diff = [0] * 4
        for i in range(4):
            for j in range(156):
                if identification_code_temp[i][j] ^ chars[char][j]:
                    diff[i] += 1
        for i in range(4):
            if diff[i] < diff_min[i]:
                diff_min[i] = diff[i]
                identification_code[i] = char
    return ''.join(identification_code)


def identificationCodeHandle(img):
    rect_box = (3, 4, 46, 16)  # crop rectangle,(left, upper, right, lower)
    img = img.crop(rect_box)
    img = img.convert('1')
    return img


if __name__ == '__main__':
    # url = sys.argv[0]
    # img = Image.open(requests.get("http://jwxt.gdufe.edu.cn/jsxsd/verifycode.servlet", stream=True).raw)
    # img = identificationCodeHandle(img)
    # identification_code = identify(img)
    # print(identification_code)

    # base64_data = re.sub('^data:image/.+;base64,', '', sys.argv[1])

    # byte_data = base64.b64decode(sys.argv[1])
    # print("====")
    # print(sys.argv[1])
    # image_data = BytesIO(byte_data)
    # img = Image.open(image_data)
    # img.save("test.jpeg")


    # tem1 = bytes(sys.argv[1], encoding='utf8')
    # tem = base64.decodebytes(tem1)
    # img = Image.open(tem)
    # img = identificationCodeHandle(img)


    # img = Image.open("test.jpeg")
    # identification_code = identify(img)
    # print(identification_code)


    # for i in range(10):
    #     img = Image.open('verifycode/' + str(i) + 's.jpeg')
    #     img = identificationCodeHandle(img)
    #     identification_code = identify(img)
    #     print(identification_code)

    img = Image.open(BytesIO(base64.b64decode(sys.argv[1])))
    img = identificationCodeHandle(img)
    identification_code = identify(img)
    print(identification_code)


