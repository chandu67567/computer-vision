import cv2
path = "E:/Computer Vision/computer vision input and output/2.blurimage input.png"
img =cv2.imread(path)
cv2.imshow("original image",img)
cv2.waitKey(0)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Img Blur",imgBlur)
cv2.waitKey(0)
