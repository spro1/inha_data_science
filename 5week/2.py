# -*- coding: cp949 -*-
sum = 0
avg = 0
for i in range(1,6):
    num = float(input("%s 번째 숫자 입력 :"%i))
    sum += num
avg = sum/5

print("합계 : %s\n평균: %.2f"%(sum, avg))
