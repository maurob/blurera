import os
import cv2
from collections.abc import Iterator
from .types import Frame


class Video:
    def __init__(self, filename):
        self.filename = filename

    @property
    def fps(self):
        cap = cv2.VideoCapture(self.filename)
        try:
            return cap.get(cv2.CAP_PROP_FPS)
        finally:
            cap.release()

    def __iter__(self) -> Iterator[Frame]:
        cap = cv2.VideoCapture(self.filename)
        ii = 0
        try:
            while True:
                success, img = cap.read()
                if not success:
                    break
                yield Frame(ii, img)
                ii += 1
        finally:
            cap.release()


def video_writer(videofile, size: tuple, fps: float):
    return cv2.VideoWriter(
        videofile,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        size,
    )
