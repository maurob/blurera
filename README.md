# Blurera

Automatic blur faces in videos.

Project based on https://github.com/elyha7/yoloface.git.


## Use case

Load a set of shell functions
```sh
source ./activate.sh
```

The first time execute `build`.

### Blur video faces

```sh
blur_video_faces some_video.mp4
```
For this example, it'll generate `some_video_blurred.mp4`.

> Copy your input video in the same repository path, in order to have it inside the docker container for processing.

The default output FPS is 60 Hz. To change it just define the `FPS` environ, like

```sh
FPS=30 blur_video_faces some_video.mp4
```

### Post proccessing

For a better video compatibility an reduce size, use `ffmpeg`.
```sh
ffmpeg -i some_video_blurred.mp4 some_video_blurred_final.mp4
```

> This current version doesn't include audio in the output video. So, figure out how to reinject the input video audio
> into the final video.
