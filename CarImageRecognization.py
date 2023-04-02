# Importing OPENCV libary
import cv2

# Using the pretrained cascade classifer that holds all shapes of cars
car_cascade = cv2.CascadeClassifier("configurations/cars.xml")

# read the image and convert to gray scale
img = cv2.imread("images/cars.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# detect cars
carsIdentified = car_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangles around the cars
for (x, y, w, h) in carsIdentified:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

cv2.imshow('cars', img)
cv2.waitKey(0)
