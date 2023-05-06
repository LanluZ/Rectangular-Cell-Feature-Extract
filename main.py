import csv
import os

import cv2

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
        # 去除蓝底
        img_mask = delBlueBackground(img)
        # 二值化
        img_gray_binary = autoBinaryImgL(img_mask)

        # 轮廓拟合
        contours, hierarchy = cv2.findContours(img_gray_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        index = getMaxCounterIndex(contours)

        # 写入名字
        data_dic['filename'] = filename

        # 轮廓绘制
        cv2.drawContours(img, contours, index, (0, 0, 255), 3)
        cv2.imwrite('./Out/Draw-' + filename, img)

        # 最小矩形获取
        rect = cv2.minAreaRect(contours[index])
        data_dic['width'] = rect[1][0]
        data_dic['height'] = rect[1][1]

        # 面积获取
        data_dic['area'] = cv2.contourArea(contours[index])

        write.writerow(data_dic)


# 删除指定文件夹下所有文件
def delDirFile(path):
    for filename in os.listdir(path):
        os.remove(path + '/' + filename)


if __name__ == '__main__':
    main()
