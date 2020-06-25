# -*- coding: cp949 -*-
sum = 0
avg = 0
for i in range(1,6):
    num = float(input("%s 번째 숫자 입력 :"%i))
    if num == 999:
        break
    sum += num
if num == 999:
    print("사용자에 의해 프로그램을 강제 종료합니다.")
else:
    avg = sum/5
    print("합계 : %s\n평균: %.2f"%(sum, avg))

