python = "Python is Amazing"
print(python.lower()) # 다 소문자
print(python.upper()) # 다 대문자
print(python[0].isupper()) # 0번째 대문자면 True
print(len(python))
print(python.replace("Python", "Java")) # Python 찾아서 Java로 바꿈

index = python.index("n") # n이 몇 번째에 있는지
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("Java")) # Java가 없어서 -1 반환
# print(python.index("Java")) # 오류

print(python.count("n"))