cabinet = {3:"감자", 100:"고구마"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
# print(cabinet(5)) 오류
print(cabinet.get(5))
print(cabinet.get(5, "사용 가능"))

print(3 in cabinet)