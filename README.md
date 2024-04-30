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

For a better video compatibility an reduced size, use `ffmpeg`.
```sh
ffmpeg -i some_video_blurred.mp4 some_video_blurred_final.mp4
```

To include also the original audio into the final video
```sh
ffmpeg -i some_video.mp4 -i some_video_blurred.mp4 -c:a copy -map 1:v:0 -map 0:a:0 some_video_blurred_final.mp4
```
or use the shell funcion `remix_audio` (which have some limitations)
```sh
remix_audio some_video
```

## Future features
- [ ] Retain bluring around some extra frames to avoid face exposures.
- [ ] Tracking faces for an even improved privacy.
- [ ] Smooth eliptical blurring (instead of a rectangle).
