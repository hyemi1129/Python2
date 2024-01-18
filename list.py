han = ["가", "나", "다"]
print(han.index("나"))

# "라" 추가
han.append("라")
print(han)

# "마" 가, 나 사이에 추가
han.insert(1, "마")
print(han)

# 하나씩 꺼냄
print(han.pop())
print(han)

# 같은 이름 몇 명?
han.append("가")
print(han)
print(han.count("가"))

# 정렬 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort()
print(num_list)

# 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
""" num_list.clear()
print(num_list) """

# 다양한 자료형 함께
mix_list = ["가", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)