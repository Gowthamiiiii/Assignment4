import cv2
import numpy as np
image1 = cv2.imread('rgb_image0.jpg')  
image2 = cv2.imread('rgb_image15.jpg')

gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

gray_image1 = np.array(gray_image1)
gray_image2 = np.array(gray_image2)

sift = sift = cv2.SIFT_create()
keypoints_1, descriptors_1 = sift.detectAndCompute(gray_image1,None)
keypoints_2, descriptors_2 = sift.detectAndCompute(gray_image2,None)

bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

matches = bf.match(descriptors_1,descriptors_2)
matches = sorted(matches, key = lambda x:x.distance)
matched_img = cv2.drawMatches(image1, keypoints_1, image2, keypoints_2, matches[:50], image2, flags=2)
cv2.imshow('image', matched_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
