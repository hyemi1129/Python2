# 중복 X, 순서 X
my_set = {1,2,3,3,3}
print(my_set)

java = {"김철수", "신짱구", "이훈이"}
python = set(["김철수", "맹구"])

# 교집합 
print(java & python)
print(java.intersection(python))

# 합집합
print(java | python)
print(java.union(python))

# 차집합 (java O python X)
print(java - python)
print(java.difference(python))

# python 할 수 있는 사람 늚
python.add("유리")
print(python)

# java 까먹음
java.remove("이훈이")
print(java)