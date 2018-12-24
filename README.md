# Raspberry-pi start with Python3
[모두의 라즈베리파이 with Python](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791187345190) 베타테스팅 리뷰를 위한 프로젝트

* 테스트 사양
  - Raspbian Stretch image, python 3

## 총평
 라즈베리파이를 처음 만나면 "어떤 부품을 사용해야 하고, 어떻게 회로를 구성해야 하는지" 익숙하지 않아서 주저하게 됩니다. 
이 책은 실습에 필요한 부품과 실제 배선도를 포함하고 있기 때문에 입문자 입장에서도 책을 따라하며 부담없이 시작할 수 있습니다.
 특히 실습을 쉽게 배울 수 있는 파이썬 언어를 사용했다는 점과, 실습에 필요한 파이썬 문법을 설명하고 라즈베리파이 설명 순으로
책이 구성되어 있어서 한 권의 책으로 라즈베리 파이를 동작할 수 있는 점이 가장 만족스러웠습니다.
 만약 교재에 있는 부품을 구할 수 없어서 다른 종류의 부품을 구입하여 실습을 진행하는 경우에는 모델명과 제품번호로 반드시 
데이터 시트를 확인하고 회로 구성을 해야합니다. 부품마다 동작하기 위한 사양이나 회로 구성이 달라질 수 있기 때문입니다. 
하지만 라즈베리파이 키워드와 함께 검색한다면 책을 따라하는데는 어려움이 없을 거라 생각합니다.


####  1. 리뷰 내용
실습 진행시, 실제로 코드가 동작하지 않거나, 책에서 변경되어야 하는 점을 정리했습니다.

* p.288 실습에 사용한 **버튼 스위치**가 책 그림에 있는 스위치와 동일하지 않아서, 회로를 구성할 때 혼란이 있을 수 있다.
  - 그림에 있는 것은 발이 2개짜리인데, 실제 전달받은 버튼 스위치는 발이 4개 짜리
  - 책 처럼 in/out 2군데에만 gpio를 연결하면 잘 동작하지만, 초보자가 실제 회로를 구성할때 버튼스위치의 발 4개에 다 gpio를
   연결해야하는지 혼란스러울 수 있다.
  
* p.301 **모터 드라이버 IC 모듈** 을 책에 있는 Tip처럼 납땜을 하지 않고 사용한다면, 칩을 그림 4-37과 반대로 뒤집어서 
 빵판에 연결해서 사용해야 한다.
  - 그렇게 된다면 그림 4-37의 배선도 그림과 반대로 회로를 연결해야 하기때문에 헷갈릴 수 있다. 

* p.306 첨부 코드대로 동작되지 않는다. 함수만 리팩토링 필요
  - 함수내에서 파라미터로 전달받은 변수 사용하는 것으로 변경
  - Scale에 variable에 매핑된 값의 경우 str 타입의 value만 들어오기 때문에 get() 메소드 사용할 필요가 없음
  - tk.Scale에서 variable로 전달받는 변수 타입의 경우, str이다. 따라서 각 함수에 맞는 int, float로 type 변환이 필요
```python
코드 4-8 tk_Motor_01.py 코드 변경
# 다른 부분은 동일하고, 함수 선언부분만 변경 필요하다.

def change_dir(dr):
    direction = int(dr) # str를 int로 타입변경
    if direction == 0:
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.HIGH)
    elif direction == 1:
        GPIO.output(AIN1, GPIO.LOW)
        GPIO.output(AIN2, GPIO.LOW)
    elif direction == 2:
        GPIO.output(AIN1, GPIO.HIGH)
        GPIO.output(AIN2, GPIO.LOW)


def change_pw(pw):
    p.ChangeDutyCycle(float(pw)) # str를 float로 타입변경

    
```

* p.311 코드 4-9 **step motor** 동일한 코드 2번 반복
  - 테스트로 전달받은 step motor 모델(28BYJ-48)과 교재 step motor 모델(ST-42BYG506H)이 다르다.
  - p.308에 그림 4-40 스테핑 모터 제어 신호 다르고, 그림 4-41 실체 배선도를 그대로 사용할 수 없다.
  - step motor 모델(28BYJ-48) : https://components101.com/motors/28byj-48-stepper-motor
  - 코드4-9, 코드 4-10 실제 동작확인하지 못함

* p.218 코드 4-11 **서보모터** 교재와 모델이 다르다. 실제 데이터시트 확인해서 배선연결 필요
  - **그림 4-44 배선도에거 전원을 건전지박스 대신에 라즈베리파이 2번핀 (5v)으로 전압 공급하도록 변경하는 것이 낫다.**
  - 1) SG90 모델은 4.8v ~ 5v 사이에서 동작 2) AA 3개 들어가는 건전지 박스가 없는 경우 입문자 입장에서는 왜 회로대로 연결했음에도
    동작하지 않는 원인을 파악하기 어렵다.
  - SG90 데이터시트 : http://www.ee.ic.ac.uk/pcheung/teaching/DE1_EE/stores/sg90_datasheet.pdf

* p.321 코드 4-12에 change_dc 함수 변경 필요
  - 함수 매개변수 오타 변경. dum -> deg
  - 입력 매개변수 deg의 타입은 str이기 때문에 float함수를 통해서 타입 변경필요.
  - str타입은 get 함수를 가지고 있지 않기 때문에 실제 테스트시에 에러 발생한다.
```python
def change_dc(deg):
    dc = ((float(deg) - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)
    p.ChangeDutyCycle(dc)
```

#### 2. 책에 추가로 작성되면 좋을 것 같은 내용
* 4.3, 4.4, 4.5에 모터 드라이버 IC 모듈을 사용시 주의하라고 알림 내용 추가
  - DC 모터와 step 모터를 사용할때 모터 드라이버 IC 모듈을 사용한다.
  - 회로를 잘못 구성하여 동작하지 않는 경우, 전원은 들어오지만 모터가 동작하지 않는다.
  - 이럴때 모터 드라이버 IC 모듈의 노출면을 손으로 잡는 경우 손가락 화상이 발생할 수 있다.
```python
[주의]
동작하지 않는 경우, 반드시 라즈베리 파이 전원이나 건전지 전원을 제거하고 회로 및 부품을 확인하시오.
손가락 화상의 우려가 있을 수 있습니다.
```
* p.331 코드 4-13. 파일명 작성 주의
  - 책 내용처럼 picamera_01.py로 하면 아무 문제 없지만, picamera.py로 잘못 입력하는 경우,
picamera 모듈에서 PiCamera()를 찾을 수 없다는 에러 메세지가 발생하면서 스크립트가 중단된다.
```python
# picamera FAQ(https://picamera.readthedocs.io/en/release-1.13/faq.html)
5.1. AttributeError: ‘module’ object has no attribute ‘PiCamera’
```