# print(5/3)
# print(5//3)  # // 은 소숫점 계산을 하지 않고 몫만 출력하게 해준다.
# print(abs(-5))
# print(pow(4,2))
# print(round(5.8))

# from math import *
# print(sqrt(16))

from random import *

# print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random()* 10) # 0.0 ~ 10.0 미만의 임의의 값 생성 
# print(int(random()*10)) # 0 ~ 10 미만의 임의의 값 생성 
# print(int(random()* 10) +1) #1 ~ 10 이하의 임의의 값 생성 
# print(randrange(1, 10)) # 1 ~ 10 미만의 임의의 값 생성
# print(randint(1, 10)) # 1 ~ 10이하의 임의의 값 생성 

# print("오프라인 스터디 모임 날짜는 매월",randint(4, 28),"일로 선정되었습니다.")

# num = "991207-1234567"
# print("성별: " + num[7])
# print("연: "+ num[0:2]) # 두번째 전까지 슬라이스
# print("월: "+ num[2:4])
# print("일: "+num[4:6])
# print("생년월일: "+num[:6])
# print("뒷번호: "+num[7:]) # 7부터 끝까지
# print("뒤에서부터 :"+num[-7:]) #맨 마지막 숫자가 -1을 의미한다.
#
# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python","Java"))
#
# index = python.index("n")
# print(index)
# index = python.index("n",index + 1)
# print(index)
#
# print(python.find("n")) # index의 경우 찾는 내용이 없으면 오류가 발생하고 find의 경우 -1이 리텅이 된다.
# print(python.count("n"))

# print("나는 %d살입니다." % 20)
# print("나는 %s을 좋아합니다. " %'python')
# print("%c" %'A')
# print("나는 %s색과 %s색을 좋아합니다." %("파란", "빨강"))
#
# print("나는 {}살입니다.".format(20))
# print("나는 {1}색과 {0}색을 좋아합니다.".format("파란","빨강"))
#
# print("나는 {age}살이며 {color}색을 좋아합니다." .format(age =20, color="빨강"))
#
# age = 20
# color ="빨강"
# print(f"나는 {age}살이며 {color}색을 좋아합니다.")

# print("백문이 불여일견\n백건이 불여일타")
# print(" \" \" ")
#
# print("\\")
# print("Red Apple\rPine")
# print("Redd\bapple")
# print("i\tu")

# # url = "http://naver.com"
# url = "http://google.com"
# passward = url[7:-4]
# # passward = url.replace("http://", "")
# # passward = passward[:passward.index('.')]
# new = passward[:3] + str(len(passward))+ str(passward.count('e')) + '!'
# print("Your password is %s" %new)

























