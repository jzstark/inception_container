docker build -t matrixanger/inception .

docker run --name inception -d -p 5000:5000 -v /tmp/inception_img:/tmp/inception_img matrixanger/inception

docker run -d --cpuset-cpus 1 --name inception -p 8000:8000 matrixanger/inception

jbuilder build inception_app.exe

python request_example.py
