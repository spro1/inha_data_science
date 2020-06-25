scores = {"철수": 90, "민수": 85, "영희": 80} 
avg = 0
for value in scores.values():
    print (value)
    avg += value

print("평균 값 : %s"%(avg/len(scores)))
