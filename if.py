weather = input("오늘 날씨는 어때? ")

if weather == "비" or weather == "눈":
    print("우산을 챙겨")
elif weather == "미세먼지":
    print("마스크를 챙겨")
else:
    print("그냥 나가")


temp = int(input("기온은 어때? "))
if 30 <= temp:
    print("나가지마. 더워")
elif 10 <= temp and temp <= 30:
    print("나가도 돼")
elif 0 <= temp and temp < 10:
    print("겉옷 ㄱ")
else:
    print("나가지마. 추워")