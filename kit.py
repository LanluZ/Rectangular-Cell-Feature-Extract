import cv2

import numpy as np


# 自适应二值化
def autoBinaryImgL(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.blur(img_gray, (3, 3))  # 滤波
    ret, img_gray_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)  # 自适应
    return img_gray_binary


# 去除图片蓝底
def delBlueBackground(img):
    # 滤波
    img = cv2.medianBlur(img, 3)
    # 去除蓝底
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([100, 60, 46])
    upper_blue = np.array([124, 255, 255])
    img_gray_binary = cv2.inRange(img_hsv, lower_blue, upper_blue)
    img_mask = np.copy(img)
    img_mask[img_gray_binary != 0] = [0, 0, 0]
    return img_mask


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
