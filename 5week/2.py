# -*- coding: cp949 -*-
sum = 0
avg = 0
for i in range(1,6):
    num = float(input("%s ��° ���� �Է� :"%i))
    sum += num
avg = sum/5

print("�հ� : %s\n���: %.2f"%(sum, avg))
