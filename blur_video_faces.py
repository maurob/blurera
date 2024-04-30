import os
import sys
import cv2
from face_detector import YoloDetector
import numpy as np
from PIL import Image


model = YoloDetector(target_size=720, device="cpu", min_face=10)
fps = 60


def main():
    videofiles = sys.argv[1:]
    for videofile in videofiles:
        print(f"Processing video {videofile!r}")
        process_video(videofile)


def process_video(videofile):
    for ii, img in enumerate(frame_gen(videofile)):
        if ii == 0:
            output_video = video_writer(f"{trim_ext(videofile)}_blurred.mp4", size=(img.shape[1], img.shape[0]))
            next(output_video)

        bboxes, points = model.predict(img)
        print(f"frame={ii} {bboxes=} {points=}")
        blur_faces(img, bboxes)
        output_video.send(img)


def frame_gen(videofile):
    cap = cv2.VideoCapture(videofile)
    while True:
        success, img = cap.read()
        if not success:
            break
        yield img
    cap.release()


def video_writer(videofile, size: tuple):
    output_video = cv2.VideoWriter(
        videofile,
        cv2.VideoWriter_fourcc(*'MP4V'),
        fps,
        size,
    )
    while True:
        frame = yield
        output_video.write(frame)


def trim_ext(filename):
    name, ext = os.path.splitext(filename)
    return name


def blur_faces(img, bboxes):
    for (x, y, x2, y2) in bboxes[0]:
        w = x2 - x
        h = y2 - y
        size = int(max([w, h]) / 3)
        ROI = img[y:y2, x:x2]
        if size % 2 == 0:
            size += 1
        blur = cv2.GaussianBlur(ROI, (size, size), 0)
        img[y:y+h, x:x+w] = blur


if __name__ == "__main__":
    main()
