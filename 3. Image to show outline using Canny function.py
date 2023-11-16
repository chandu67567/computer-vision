import cv2
path = "E:/Computer Vision/computer vision input and output/3.Image to show outline using Canny function input.png"
img =cv2.imread(path)
cv2.imshow("original image",img)
cv2.waitKey(0)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
imgCanny = cv2.Canny(imgBlur,100,200)
cv2.imshow("Img Canny",imgCanny)
cv2.waitKey(0)
