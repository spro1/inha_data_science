# -*- coding: cp949 -*-
sum = 0
avg = 0
for i in range(1,6):
    num = float(input("%s ��° ���� �Է� :"%i))
    if num == 999:
        break
    sum += num
if num == 999:
    print("����ڿ� ���� ���α׷��� ���� �����մϴ�.")
else:
    avg = sum/5
    print("�հ� : %s\n���: %.2f"%(sum, avg))

