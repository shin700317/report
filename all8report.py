소프트웨어기초코딩 과제
신제윤 2018775037
김주현 교수님

8장 연습문제

1. 문자열을 입력 받아 문자열의 길이를 구하고, 문자열의 첫 번째 문자, 두번째 문자, 마지막 문자를 출력해보자.

문자열 : Python Programming
문자열 길이 : 18
첫 번째 문자 : P
두 번째 문자 : y
마지막 문자 : g

index = input("문자열 : ")
for i in index:
    print("문자열 길이 : ", len(index))
    print("첫 번째 문자 : ", str(index)[0])
    print("두 번째 문자 : ", str(index)[1])
    print("마지막 문자 : ", str(index)[len(index)-1])
    break


2. 문자열을 입력 받아 for 문을 이용하여 개별 문자로 출력해보자. 그리고 for 문을 이용하여 입력 받은 문자열의 역순으로 개별 문자를 출력해보자.

문자열 : Python Programming
개별 문자 출력 : Python Programming
역순 개별 문자 출력 : gnimmargorP nohtyP

index = input("문자열 : ")

def rev(seq):
    seq_rev = "".join(reversed(seq))
    return seq_rev

for i in index:
    print("개별 문자 출력 : ", str(index))
    print("역순 개별 문자 출력 : ", rev(index))
    break


3. 0~100 사이의 점수를 입력 받아 입력한 점수가 0~100인 경우 점수에 대한 A, B, C, D, F 등급을 출력하고, 범위에 해당하지 않은 경우 "입력 가능한 점수
   범위는 0~100입니다."를 출력해보자. 점수에 대한 등급 판정은 if-elif-else 문을 이용하여 점수가 90~100일때 "A"이고, 점수가 80~89일때 "B"이고, 70
   ~79일때 "C", 60~69일때 "D", 0~59일때 "F"로 판정한다.

점수 : 85
85 : B
점수 : 50
50 : F
점수 : -5
입력 가능한 점수 범위는 0~100입니다.

score = int(input("점수 : "))

if score < 100 and score > 90:
    print(score, ": A")
elif score < 100 and score > 80:
    print(score, ": B")
elif score < 100 and score > 70:
    print(score, ": C")
elif score < 100 and score > 60:
    print(score, ": D")
elif score < 100 and score > 0:
    print(score, ": F")
else:
    print("입력 가능한 점수 범위는 0~100입니다.")


4. 문제 3을 if-elif-else 문 대신에 딕셔너리를 이용하여 점수에 대한 등급을 출력해보자.

점수 : 85
85 : B
점수 : 55
55 : F

score = int(input("점수 : "))
deg = { 10:'A', 9:'A', 8:'B', 7:'C', 6:'D', 5:'F', 4:'F', 3:'F', 2:'F', 1:'F', 0:'F'}
print(score, ":", deg[score//10])


5. 딕셔너리를 이용하여 제품:값의 형태로 items = {"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}을 선언해보자. while 문을 이용
   하여 무한 반복하면서 제품을 입력 받아 제품에 대한 값들의 합계를 구해 출력해보자. 아무 것도 입력을 하지 않은 채로 Enter키를 눌러 빈 물자열이 입
   력되면 무한 반복ㅇ르 멈추고 전체 합계를 출력한다.

제품명 : 우유
[우유:1100] > 1100
제품명 : 콜라
[콜라:1200] > 2300
제품명 : 라면
[라면:650] > 2950
제품명 : 라면
[라면:650] > 3600
제품명 : 과자
[과자:700] > 4300
제품명 : 딸기
딸기 는 미등록 제품입니다.
제품명 :
총 금액 : 4300

items = {"라면":650, "우유":1100, "콜라":1200, "캔커피":500, "과자":700}
prize = 0

while True:
    item = input("제품명 : ")
    if item == "":
        print("총 금액 :", prize)
        break
    elif item =='라면':
        prize += 650
        print("[라면:650] >", prize)
    elif item == '우유':
        prize += 1100
        print("[우유:1100] >", prize)
    elif item == '콜라':
        prize += 1200
        print("[콜라:1200] >", prize)
    elif item == '캔커피':
        prize += 500
        print("[캔커피:500] >", prize)
    elif item == '과자':
        prize += 700
        print("[과자:700] >", prize)
    else:
        print(item, "는 미등록 제품입니다.")
    continue


6. 딕셔너리를 이용하여 비어 있는 영한사전에 단어를 등록해보자. while 문을 이용하여 무한 반복하면서 영어 단어와 한글 단어를 입력 받아 등록하고, 아무
   것도 입력을 하지 않은 채로 Enter 키를 눌러 영어 단어와 한글 단어에 빈 문자열이 입력되면 무한 반복을 멈추고 딕셔너리에 등록된 모든 키와 값들을 출
   력한다.
   
영어 단어 : Python
한글 단어 : 파이썬
영어 단어 : string
한글 단어 : 문자열
영어 단어 : interation
한글 단어 : 반복
영어 단어 : selection
한글 단어 : 선택
영어 단어 :
한글 단어 :
{'Python':'파이썬', 'string':'문자열', 'interation':'반복', 'selection':'선택'}

engkor_dict = dict()

while True:
    eng = input("영어 단어 : ")
    kor = input("한글 단어 : ")
    if eng == "" and kor == "":
        print(engkor_dict)
        break
    engkor_dict[eng] = kor
    continue


7. 문제 6번의 딕셔너리 engkor_dict을 활용하여 영어 단어를 입력할 경우 해당하는 한글 단얼르 표시하도록 수정해보자. 만약 딕셔너리가 비어 있을 경우
   "사전이 비어 있습니다."를 출력하고, 비어 있지 않을 경우 검색을 하여 단어를 표시한다. 만약 영어 단어가 등록되어 있지 않을 경우 "단어가 등록되어
   있지 않습니다."를 출력하고, 한글 단어를 추가로 입력받아 딕셔너리에 추가로 등록한다. while 문에 의한 무한 반복의 종료는 영어 단어가 빈 문자열로
   입력되었을 경우 종료하고 딕셔너리에 등록된 모든 키와 값들을 출력한다.
   
영어 단어 : Python
사전이 비어 있습니다.
단어를 추가합니다.
한글 단어 : 파이썬
영어 단어 : string
string 단어가 등록되어 있지 않습니다.
단어를 추가합니다.
한글 단어 : 문자열
영어 단어 : interation
interation 단어가 등록되어 있지 않습니다.
단어를 추가합니다.
한글 단어 : 반복
영어 단어 : selection
selection 단어가 등록되어 있지 않습니다.
단어를 추가합니다.
한글 단어 : 선택
영어 단어 : string
string : 문자열
영어 단어 :interation
interation : 반복
영어 단어 :
{'Python':'파이썬', 'string':'문자열', 'interation':'반복', 'selection':'선택'}

engkor_dict = dict()

while True:
    eng = input("영어 단어 : ")
    if eng == "":
        print(engkor_dict)
        break
    if (not eng in engkor_dict) and (len(engkor_dict) > 0):
        print(eng, "단어가 등록되어 있지 않습니다.")
        print("단어를 추가합니다.")
        kor = input("한글 단어 : ")
    elif eng in engkor_dict:
        print(eng, ":", kor)
    else:
        print("사전이 비어있습니다.")
        print("단어를 추가합니다.")
        kor = input("한글 단어 : ")
    engkor_dict[eng] = kor
    continue


8. time 모듈을 import한 후, for 문을 이용하여 1부터 5까지의 숫자를 출력해보자. 각 숫자를 출력한 후 sleep() 함수를 이용하여 프로그램을 1초간 멈추게
   해보자.
   
1 2 3 4 5

import time
for i in (1, 2, 3, 4, 5):
    print(i, end=" ")
    time.sleep(1)


9. math 모듈을 import한 후, 실수 값을 입력 받아 ceil() 함수, floor() 함수, trunc() 함수 연산의 결과를 출력해보자.

실수 : 3.14
3.14 : 4
3.14 : 3
3.14 : 3

import math
num = float(input("실수 : "))
print(num, ":", math.ceil(num))
print(num, ":", math.floor(num))
print(num, ":", math.trunc(num))
