image=blurera

build() {
    docker build -t $image dockerfiles/py312
}

blur_video_faces() {
    docker run --rm -it -v $PWD:/repo -w /repo $image python blur_video_faces.py $@
}
