import cv2
from .types import Box, FrameWithBoxes


def blur_faces(frame: FrameWithBoxes):
    for box in frame.boxes:
        blur(frame.img, box)


def blur(img, box: Box):
    size = int(max([box.w, box.h]) / 3)
    ROI = box(img)
    if size % 2 == 0:
        size += 1
    ROI[:] = cv2.GaussianBlur(ROI, (size, size), 0)


