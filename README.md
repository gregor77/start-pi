# Raspberry-pi start with Python3
[모두의 라즈베리파이 with Python](http://www.kyobobook.co.kr/product/detailViewKor.laf?ejkGb=KOR&mallGb=KOR&barcode=9791187345190) 베타테스팅 리뷰를 위한 프로젝트

## 총평
 라즈베리파이 처음 시작할 때 "어떤 부속품을 사용해야 하고, 어떻게 회로를 구성해야 하는지"가 걱정된다 생각합니다.
이 책은 실습을 진행하는데 필요한 부품 목록이 정리되어 있고, 데이터 시트를 보는 법을 알려줘서 처음 회로를 잘못 구성해
부속품이 고장나는 상황을 미리 방지할 수 있게 해줘 좋았습니다.
 특히 실제 배선도 그림을 따라 회로를 구성하고, 코드를 따라하다보면 실제 동작하는 것을 눈으로 확인할 수 있었던 점이
가장 만족스러웠습니다.


#### 개선점
개선점은 독자 입장에서 실제로 실습을 진행할때 불편할 수 있는 점에 대해서 작성하였습니다.

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
