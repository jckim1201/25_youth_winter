<img src="./images/kisti_logo.jpg" width="100"> <img src="./images/unist_logo.jpg" width="100"> <img src="./images/kisti_mas.png" width="90"> <img src="./images/unist_mas.jpg" width="70">

# **2025년 겨울방학 AI 팀프로젝트 슈퍼컴퓨팅 청소년 캠프**

본 자료는 2025년도 KISTI-UNIST 겨울 청소년캠프 Edge 디바이스를 활용한 AI 실습 강의 자료 입니다.

---
## 준비물
1. Jetson Nano or Orin Nano
2. Pytorch 개발 환경

## 기본 jetpack 설치 및 연결
```
ssh jetson@192.168.55.1
```
password: jetson

## 실습파일 다운
```
git clone https://github.com/jckim1201/25_youth_winter
```

## 카메라 확인
```
ls /dev/video*
```
- 위 확인이 되는 video 장비를 이용해서 활용 해야 함. 장비 별 설정에 따라 수정해야 함. 현재 파일들은 video0를 기준으로 작성되어 있으며, 그 외의 장비인 경우, --device 연결 시 해당 장비에 맞는 번호로 작성해 주고, 노트북 파일 내의 device 번호도 수정해 주어야 함.
- usb 카메라의 지원 fps 가 낮은 경우에도 연결이 안될 경우가 있으며, 이 경우 노트북의 카메라 연결 부분의 capture_fps 값을 낮게 설정해야 함.

## 도커파일 다운 및 실행
```
echo sudo docker run --runtime nvidia -it --rm --network host --volume ~/25_youth_winter:/nvdli-nano/data --volume /tmp/argus_socket:/tmp/argus_socket --device /dev/video0 nvcr.io/nvidia/dli/dli-nano-ai:v2.0.3-r36.3.0kr >> docker_run.sh
```
```
chmod +x docker_run.sh
```
```
./docker_run.sh
```
또는
```
cp 25_youth_winter/docker_run.sh ./
```
```
./docker_run.sh
```

---
## 참고자료

1. [Jetson AI Fundamentals](https://youtu.be/rSqIvLQ8Meg?si=45sTk7O73CtzZnAX)
2. [Nvidia AI Lab](https://www.jetson-ai-lab.com)
3. [Jetson Community Projects](https://developer.nvidia.com/embedded/community/jetson-projects)
4. [Neural Network Visualization](https://www.youtube.com/watch?v=aircAruvnKk&ab_channel=3Blue1Brown)
