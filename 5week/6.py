class Machine:
    def __init__(self, coffee, sugar, milk, water):
        self.milk_coffee_cnt =0
        self.black_cnt = 0
        self.black_sugar_cnt = 0
        self.milk_cnt = 0
        self.money = 0
        self.coffee = coffee
        self.sugar = sugar
        self.milk = milk
        self.water = water

    def milk_coffee(self):
        self.milk_coffee_cnt += 1
        self.coffee -=10
        self.sugar -= 5
        self.milk -= 5
        self.water -= 15
        self.money += 400

    def black(self):
        self.black_cnt += 1
        self.coffee -=12
        self.water -= 15
        self.money += 400

    def black_sugar(self):
        self.black_sugar_cnt += 1
        self.coffee -=15
        self.sugar -= 5
        self.water -= 15
        self.money += 400

    def hot_milk(self):
        self.milk_cnt += 1
        self.milk -= 30
        self.money += 300

    def check(self):
        print("밀크 커피 판매 개수: %s"%(self.milk_coffee_cnt))
        print("블랙(설탕없음) 판매 개수 : %s"%(self.black_cnt))
        print("블랙(설탕있음) 판매 개수 : %s"%(self.black_sugar_cnt))
        print("우유 판매 개수 : %s"%(self.milk_cnt))
        print("총 매출은 %s 입니다"%(self.money))
        print("재료 잔량은 커피 : %sg, 설탕 : %sg, 우유 : %sml, 물 : %sml"%(self.coffee, self.sugar, self.milk, self.water))


myMachine = Machine(500, 200, 2000, 5000)
try:
    while True:
        menu = int(input("메뉴를 선택하세요 (1:밀크커피, 2:블랙(설탕x), 3:블랙(설탕), 4:우유, 0:현황, 999:종료) :"))
        if menu == 1: myMachine.milk_coffee()
        elif menu == 2: myMachine.black()
        elif menu == 3: myMachine.black_sugar()
        elif menu == 4: myMachine.hot_milk()
        elif menu == 0: myMachine.check()
        elif menu == 999: break
        else: pass
except:
    pass

print("종료했습니다.")
