import cv2

img = cv2.imread("hanumanart.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.GaussianBlur(gray, (5,5), 0)

edges = cv2.Canny(gray,120,220)

cv2.imwrite("outline.png",edges)

cv2.imshow("Outline",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()