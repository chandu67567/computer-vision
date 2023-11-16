import cv2 
path = "E:/Computer Vision/computer vision input and output/1.grayscaleinput.png"
img =cv2.imread(path)
cv2.imshow("original image",img)
cv2.waitKey(0)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("GrayScale",imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()
