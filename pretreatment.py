import os
import cv2


# 图像特征归一化
def pretreatment():
    pos_path = './Train/Pos'
    origin_path = './Train/Origin'

    file_arr = os.listdir(origin_path)

    for filename in file_arr:
        img = cv2.imread(origin_path + '/' + filename, cv2.IMREAD_GRAYSCALE)
        img5050 = cv2.resize(img, (50, 50))
        cv2.imwrite(pos_path + '/' + filename, img5050)


# 生成正样本描述文件
def createPos():
    pos_path = './Train/Pos'
    neg_path = './Train/Neg'

    # 负样本描述文件
    for img in os.listdir(neg_path):
        line = neg_path + '/' + img + '\n'
        with open('./Train/neg.txt', 'a') as f:
            f.write(line)
    f.close()

    # 正样本描述文件
    for img in os.listdir(pos_path):
        line = pos_path + '/' + img + ' 1 0 0 50 50\n'
        with open('./Train/pos.txt', 'a') as f:
            f.write(line)
    f.close()


if __name__ == '__main__':
    pretreatment()
    createPos()
