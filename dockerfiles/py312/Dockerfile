from python:3.12
run apt update
run apt install build-essential cmake libgl1-mesa-glx -y
run pip install --upgrade pip
workdir /app
env PYTHONPATH=/app/yoloface
run git clone https://github.com/elyha7/yoloface.git
run cd yoloface && git checkout 04bfe3459db5b1254e805eeaa3ec660afa52f899
copy ./requirements.txt /app
run pip install -r requirements.txt
run pip install ipython
workdir /repo
cmd bash
