import random

secret=random.randint(1,100)
print("猜数字游戏:1-100")

while True:
    guess=int(input("请输入你的猜测:"))

    if (guess<secret):
        print("太小了")
    if (guess>secret):
        print("太大了")
    if (guess==secret):
        print("恭喜你，猜对了")
        break

    
