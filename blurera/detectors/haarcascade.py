import cv2

cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

settings = {
    'scaleFactor': 1.3,
    'minNeighbors': 3,
    'minSize': (50, 50),
    'flags': 4|8,  # cv2.CV_HAAR_FIND_BIGGEST_OBJECT|cv2.CV_HAAR_DO_ROUGH_SEARCH
}

def detector(img):
    return cascade.detectMultiScale(img, **settings)
