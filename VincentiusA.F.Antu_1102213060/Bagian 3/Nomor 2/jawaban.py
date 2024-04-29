import cv2

ayon_path = 'ayon.jpg'
ayon_read = cv2.imread(ayon_path)

ayon_grayscale = cv2.cvtColor(ayon_read, cv2.COLOR_BGR2GRAY)

cv2.imwrite("ayon_grayscale.jpg", ayon_grayscale)