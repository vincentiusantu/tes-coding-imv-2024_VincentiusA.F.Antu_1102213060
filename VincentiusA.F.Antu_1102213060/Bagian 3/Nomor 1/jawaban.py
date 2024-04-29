import cv2

emma_path = 'emma.jpg'
emma_read = cv2.imread(emma_path)

emma_flip_vertical = cv2.flip(emma_read, 0)
emma_flip_horizontal = cv2.flip(emma_read, 1)
emma_transpose = cv2.rotate(emma_flip_horizontal, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imwrite("emma_flip_vertikal.jpg", emma_flip_vertical)
cv2.imwrite("emma_flip_horizontal.jpg", emma_flip_horizontal)
cv2.imwrite("emma_transpose.jpg", emma_transpose)