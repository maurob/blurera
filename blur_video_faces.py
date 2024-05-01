import sys

from blurera.video import Video, video_writer
from blurera.detectors.yolo import detector
from blurera.filters.passthrough import temporal_filter
from blurera.image import blur_faces
from blurera.misc import trim_ext
from blurera.types import FrameWithBoxes


def main():
    videofiles = sys.argv[1:]
    for videofile in videofiles:
        print(f"Processing video {videofile!r}")
        process_video(videofile)


def process_video(videofile):
    video = Video(videofile)
    for frame in video:
        if frame.first:
            output_video = video_writer(f"{trim_ext(videofile)}_blurred.mp4", frame.size, video.fps)

        boxes = detector(frame.img)
        print(f"frame={frame.id} {boxes=}")
        current_frame = FrameWithBoxes(*frame, boxes)
        output_frame = temporal_filter(current_frame)
        if output_frame:
            blur_faces(output_frame)
            output_video.write(output_frame.img)


if __name__ == "__main__":
    main()
