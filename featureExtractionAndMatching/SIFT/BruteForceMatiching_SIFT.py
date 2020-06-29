import cv2 as cv
import matplotlib.pyplot as plt
import csv
import math

img1 = cv.imread('../Images/0000000000.jpg',
                 cv.IMREAD_GRAYSCALE)  # queryImage
img2 = cv.imread('../Images/0000000001.jpg',
                 cv.IMREAD_GRAYSCALE)  # trainImage

sift = cv.xfeatures2d.SIFT_create()
# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)
# BFMatcher with default params

# create BFMatcher object
bf = cv.BFMatcher()
# Match descriptors.
match = bf.match(des1, des2)
# Sort them in the order of their distance.
matches = sorted(match, key=lambda x: x.distance)

# Draw first 10 matches.
num_matches = 133
# num_matches = len(matches)
img3 = cv.drawMatches(img1,
                      kp1,
                      img2,
                      kp2,
                      matches[:num_matches],
                      None,
                      flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

plt.imshow(img3), plt.show()
