""" # 반복문

customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비 되었습니다. {1}번 남았어요.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")


while True: # 무한 반복
    print("hello")

 """

list_name = ["감자", "고구마"]

while True:
    name = input("이름 입력 >> ")
    if name in list_name:
        print(f"{name} 멋지다!")
        break
    else:
        print(f"{name} 최고!")