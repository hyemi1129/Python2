# 슬라이싱 : 필요한 만큼 잘라내기

jumin = "071129-4113515"

print("성별 : " + jumin[7])
print("연도 : " + jumin[0:2])
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[:6])
print("뒤 7자리 : " + jumin[7:])
print("뒤 7자리 (뒤 부터) : " + jumin[-7:]) # 맨 뒤에서 7번째부터 끝까지