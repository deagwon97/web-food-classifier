# Web Food Classifier
청년취업사관학교(새싹)의 보조강사로 활동하면서 진행했던 코드와 강의 자료를 공유합니다.
flask, tensorflow를 활용한 인공지능 음식 분류 서비스입니다. 

## Screen
<div align="center">
    <img  style="width : 30% ;" src="/asset/sample_page.png"/>
</div>

## Start
```bash
>> git clone https://github.com/deagwon97/web-food-classifier.git

>> cd web-food-classifier

>> sh install-docker.sh

>> docker-compose up

>> docker exec -it server /bin/bash

(container)>> python3 main.py
```

## Reference 
- https://github.com/roytuts/flask/tree/master/python-flask-upload-display-multiple-images
- https://tfhub.dev/google/aiy/vision/classifier/food_V1/1

## Other
- 청년취업사관학교(새싹), "Python을 활용한 실전 AI 모델 개발" - 인공지능 모델 배포하기 과정의 실습 자료입니다.
- 강의자료 - <a href="/asset/인공지능 모델 배포하기.pdf">인공지능 모델 배포하기.pdf</a>
