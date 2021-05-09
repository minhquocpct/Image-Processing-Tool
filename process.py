import cv2 as cv
import matplotlib.pyplot as plt
import ui as ui
import numpy as np
import io
from PIL import Image
def Histo():
    name = ui.filename
    img = cv.imread(name,0)
    img_equalized = cv.equalizeHist(img)
    imgbytes = cv.imencode(".png", img_equalized)[1].tobytes()
    ui.window["-IMAGEPROCESS-"].update(data=imgbytes)

def Process_Logarit(img, c):
    return float(c) * cv.log(1.0 + img)

def Loga():
    name = ui.filename
    img = cv.imread(name)
    y = Process_Logarit(img, 2)
    imgbytes = cv.imencode(".png", y)[1].tobytes()
    ui.window["-IMAGEPROCESS-"].update(data=imgbytes)

def Process_Gamma(img, gamma, c):
    return float(c) * pow(img, float(gamma))

def Gamma():
    name = ui.filename
    img = cv.imread(name,0)
    y1 = Process_Gamma(img, 3.0, 1.0)
    imgbytes = cv.imencode(".png", y1)[1].tobytes()
    ui.window["-IMAGEPROCESS-"].update(data=imgbytes)

def Thresholding(img, th):
    return img > th

def Archive():
    name = ui.filename
    img = cv.imread(name, 0)

    lst = []
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            lst.append(np.binary_repr(img[i][j], width=8))  # width số bit
    # Đã có 1 danh sách chứa chuỗi các bit
    # Để tạo ra các mặt phẳng bit chúng ta lặp qua các phần tử chuỗi các bit
    # Rút trích nó là lưu vào từng danh sách (mỗi danh sách là mặt phẳng bit)

    # Rút trích thành mặt phẳng bit thứ 8
    mp_bit_8 = []
    for i in lst:
        mp_bit_8.append(int(i[0]))

    # Rút trích thành mặt phẳng bit thứ 7
    mp_bit_7 = []
    for i in lst:
        mp_bit_7.append(int(i[1]))

    # Rút trích thành mặt phẳng bit thứ 6
    mp_bit_6 = []
    for i in lst:
        mp_bit_6.append(int(i[2]))

    # Rút trích thành mặt phẳng bit thứ 5
    mp_bit_5 = []
    for i in lst:
        mp_bit_5.append(int(i[3]))

    # Rút trích thành mặt phẳng bit thứ 4
    mp_bit_4 = []
    for i in lst:
        mp_bit_4.append(int(i[4]))

    # Rút trích thành mặt phẳng bit thứ 3
    mp_bit_3 = []
    for i in lst:
        mp_bit_3.append(int(i[5]))

    # Rút trích thành mặt phẳng bit thứ 2
    mp_bit_2 = []
    for i in lst:
        mp_bit_2.append(int(i[6]))

    # Rút trích thành mặt phẳng bit thứ 1
    mp_bit_1 = []
    for i in lst:
        mp_bit_1.append(int(i[7]))

    # Tái tạo ảnh
    # Nhân từng phần tử với 2^(n-1) để có ảnh tái tạo tương ứng với mỗi mặt phẳng bit
    # n là bit thứ n
    image_bit_8 = (np.array(mp_bit_8, dtype='uint8') * 128).reshape(img.shape[0], img.shape[1])
    image_bit_7 = (np.array(mp_bit_7, dtype='uint8') * 64).reshape(img.shape[0], img.shape[1])
    image_bit_6 = (np.array(mp_bit_6, dtype='uint8') * 32).reshape(img.shape[0], img.shape[1])
    image_bit_5 = (np.array(mp_bit_5, dtype='uint8') * 16).reshape(img.shape[0], img.shape[1])
    image_bit_4 = (np.array(mp_bit_4, dtype='uint8') * 8).reshape(img.shape[0], img.shape[1])
    image_bit_3 = (np.array(mp_bit_3, dtype='uint8') * 4).reshape(img.shape[0], img.shape[1])
    image_bit_2 = (np.array(mp_bit_2, dtype='uint8') * 2).reshape(img.shape[0], img.shape[1])
    image_bit_1 = (np.array(mp_bit_1, dtype='uint8') * 1).reshape(img.shape[0], img.shape[1])

    y2 = image_bit_8 + image_bit_6+image_bit_7
    imgbytes = cv.imencode(".png", y2)[1].tobytes()
    ui.window["-IMAGEPROCESS-"].update(data=imgbytes)