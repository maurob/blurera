from face_detector import YoloDetector
from ..types import Box

model = YoloDetector(target_size=720, device="cpu", min_face=10)


def detector(img):
    bboxes, points = model.predict(img)
    return set(Box.from_(bbox) for bbox in bboxes[0])
