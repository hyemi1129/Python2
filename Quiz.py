# 변수 사용 퀴즈
# 변수명 : station / 변수값 : 사당, 신도림, 인천공항 / 출력문장 : XX행 열차가 들어오고 있습니다.

station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")



# 랜덤 날짜 뽑기

from random import *

date = randint(4, 28)
print("오프라인 스터디 모임 날짜는 매월 "+ str(date) + "일로 선정되었습니다.")


#비번 만들기

# 예) http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!"로 구성


url = "http://naver.com"
my_str = url.replace("http://", "") # 규칙 1
my_str = my_str[:my_str.index(".")] # 규칙 2
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" 
print("{0}의 비밀번호는 {1}입니다.".format(url, password))