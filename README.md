# Rectangular-Cell-Feature-Extract

### 维管束细胞图像特征提取

---

#### 输入

1. 在./Data文件夹内放入原始图片

#### 输出

1. 输出数据特征到./Out/Data.csv中
   
   样例（部分）
   
   | filename           | area      | height      | width       |
   | ------------------ | --------- | ----------- | ----------- |
   | 0829_131619_02.jpg | 1586909.5 | 930.5437012 | 1792.184692 |

2. 输出特征提取参照图片到./Out文件夹中

---

### 注意事项

1. 对于二值化有内置两种方法，自行选用，此处采用后一种
   
   ```python
   def autoBinaryImgL(img):
       img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       img_gray = cv2.blur(img_gray, (3, 3))  # 滤波
       ret, img_gray_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)  # 自适应
       return img_gray_binary
   ```
   
   ```python
   def delBlueBackground(img):
       img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
       img_gray = cv2.blur(img_gray, (3, 3))  # 滤波
       ret, img_gray_binary = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU + cv2.THRESH_BINARY)  # 自适应
       return img_gray_binary
   ```
