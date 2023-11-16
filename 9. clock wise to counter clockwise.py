import cv2
path = "E:\Computer Vision\computer vision input and output\9.counter clock wise.png"
src = cv2.imread(path)
cv2.imshow("original image",src)
cv2.waitKey(0)
window_name = 'Image'
image = cv2.rotate(src, cv2.ROTATE_180)
cv2.imshow(window_name, image)
cv2.waitKey(0)
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE) 
cv2.imshow(window_name, image)
cv2.waitKey(0)
image = cv2.rotate(src, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow(window_name, image)
cv2.waitKey(0) 
