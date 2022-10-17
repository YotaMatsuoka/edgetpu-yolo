import cv2
image = cv2.imread("/home/edgetpu-yolo/data/images/zidane.jpg")

cv2.imshow("image", image)
cv2.waitKey(20000)
