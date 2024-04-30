image=blurera

build() {
    docker build -t $image dockerfiles/py312
}

blur_video_faces() {
    docker run --rm -it -v $PWD:/repo -w /repo $image python blur_video_faces.py $@
}

remix_audio() {
    ffmpeg -i $1.mp4 -i $1_blurred.mp4 -c:a copy -map 1:v:0 -map 0:a:0 $1_blurred_final.mp4
}
