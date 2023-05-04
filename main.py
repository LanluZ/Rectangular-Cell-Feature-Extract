import csv
import numpy as np
import os
from kit import *


def main():
    current_path = os.getcwd().replace('\\', '/')
    # 删除上次处理后数据与图片
    delDirFile(current_path + '/Out')
    # 获取目录下预处理图片文件名
    filename_arr = os.listdir(current_path + '/Data')

    # 数据存储对象
    csvfile = open('./Out/Data.csv', mode='w', newline='')
    fieldnames = ['filename', 'area', 'height', 'width']
    write = csv.DictWriter(csvfile, fieldnames=fieldnames)
    write.writeheader()

    # 遍历图片
    for filename in filename_arr:
        data_dic = dict()

        # 预处理图片
        img = cv2.imread('./Data/' + filename)
        # 选择其中一种二值化方式
        img_gray_binary = delBlueBackground(img)

        # 轮廓拟合
        contours, hierarchy = cv2.findContours(img_gray_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        index = getMaxCounterIndex(contours)
        cv2.drawContours(img, contours, index, (0, 0, 255), 3)
        cv2.imwrite('./Out/Draw-' + filename, img)

        # 写入名字
        data_dic['filename'] = filename

        # 最小矩形获取
        rect = cv2.minAreaRect(contours[index])
        data_dic['width'] = rect[1][0]
        data_dic['height'] = rect[1][1]

        # 面积获取
        data_dic['area'] = cv2.contourArea(contours[index])

        write.writerow(data_dic)


# 二值化方式一
def autoBinaryImgL(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.blur(img_gray, (3, 3))  # 滤波
    ret, img_gray_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)  # 自适应
    return img_gray_binary


# 二值化方式二
def delBlueBackground(img):
    # 滤波
    img = cv2.medianBlur(img, 3)
    # 去除蓝底
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 60, 46])
    upper_blue = np.array([124, 255, 255])
    img_gray_binary = cv2.inRange(img_hsv, lower_blue, upper_blue)
    img_gray_binary = cv2.bitwise_not(img_gray_binary)  # 反色
    return img_gray_binary


# 寻找图像中最大的轮廓
def getMaxCounterIndex(contours):
    index = 0
    max_area = 0
    max_index = 0
    for i in contours:
        current_area = cv2.contourArea(i)
        if current_area > max_area:
            max_area = current_area
            max_index = index
        index += 1

    return max_index


# 删除指定文件夹下所有文件
def delDirFile(path):
    for filename in os.listdir(path):
        os.remove(path + '/' + filename)


if __name__ == '__main__':
    main()
