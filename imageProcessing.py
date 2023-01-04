## Image Flip
import cv2

img = cv2.imread("./doc/imgs/2.jpg")
img2 = cv2.flip(img, 1)  # 参数设为1，表示左右翻转，参数设为0，则表示上下翻转
cv2.imshow("img2", img2)
cv2.waitKey(0)


# ## Image Correction
# import cv2
# import numpy as np
#
# img = cv2.imread('input.jpg')
# result1 = img.copy()
# result2 = img.copy()
# result3 = img.copy()
#
# img = cv2.GaussianBlur(img,(3,3),0)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# cv2.imwrite("canny.jpg", edges)
# #hough transform
# lines = cv2.HoughLinesP(edges,1,np.pi/180,50,minLineLength=90,maxLineGap=10)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(result1,(x1,y1),(x2,y2),(0,0,255),1)
#     print (x1,y1)
#     print (x2,y2)
# cv2.circle(result2,(207,151),5,(0,255,0),5)
# cv2.circle(result2,(517,285),5,(0,255,0),5)
# cv2.circle(result2,(17,601),5,(0,255,0),5)
# cv2.circle(result2,(343,731),5,(0,255,0),5)
#
# cv2.imwrite("result1.jpg", result1)
# cv2.imwrite("result2.jpg", result2)
#
# src = np.float32([[207, 151], [517, 285], [17, 601], [343, 731]])
# dst = np.float32([[0, 0], [337, 0], [0, 488], [337, 488]])
# m = cv2.getPerspectiveTransform(src, dst)
# result = cv2.warpPerspective(result3, m, (337, 488))
# cv2.imwrite("result.jpg", result)
# cv2.imshow("result", result)
# cv2.waitKey(0)




# ## Image Enhancement
# import cv2
# import random
# # import imutils
# import numpy as np
#
# # 彩色图像每个像素值是[x,y,z], 灰度图像每个像素值便是一个np.uint8
# path = './doc/imgs/2.jpg'  # 路径二维码
# image = cv2.imread(path)
# gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
#
# # a<0 and b=0: 图像的亮区域变暗，暗区域变亮
# a, b = -0.5, 0
# new_img1 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
# for i in range(new_img1.shape[0]):
#     for j in range(new_img1.shape[1]):
#         new_img1[i][j] = gray_img[i][j] * a + b
#
# # a>1: 增强图像的对比度,图像看起来更加清晰
# a, b = 1.5, 20
# new_img2 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
# for i in range(new_img2.shape[0]):
#     for j in range(new_img2.shape[1]):
#         if gray_img[i][j] * a + b > 255:
#             new_img2[i][j] = 255
#         else:
#             new_img2[i][j] = gray_img[i][j] * a + b
#
# # a<1: 减小了图像的对比度, 图像看起来变暗
# a, b = 0.5, 0
# new_img3 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
# for i in range(new_img3.shape[0]):
#     for j in range(new_img3.shape[1]):
#         new_img3[i][j] = gray_img[i][j] * a + b
#
# # a=1且b≠0, 图像整体的灰度值上移或者下移, 也就是图像整体变亮或者变暗, 不会改变图像的对比度
# a, b = 1, -50
# new_img4 = np.ones((gray_img.shape[0], gray_img.shape[1]), dtype=np.uint8)
# for i in range(new_img4.shape[0]):
#     for j in range(new_img4.shape[1]):
#         pix = gray_img[i][j] * a + b
#         if pix > 255:
#             new_img4[i][j] = 255
#         elif pix < 0:
#             new_img4[i][j] = 0
#         else:
#             new_img4[i][j] = pix
#
# # a=-1, b=255, 图像翻转
# new_img5 = 255 - gray_img
#
# cv2.imshow('origin', image)
# cv2.imshow('gray', gray_img)
# cv2.imshow('a<0 and b=0', new_img1)
# cv2.imshow('a>1 and b>=0',new_img2)
# cv2.imshow('a<1 and b>=0',new_img3)
# cv2.imshow('a=1 and b><0',new_img4)
# cv2.imshow('a=-1 and b=255',new_img5)
# cv2.imwrite('a.jpg',new_img5)
# if cv2.waitKey(0) == 27:
#     cv2.destroyAllWindows()


