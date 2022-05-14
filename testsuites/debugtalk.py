import random
def choose():
    textList = ["我","的","天","啊","好","简","单","吧"]
    num1=random.randint(0,7)
    num2 = random.randint(0, 7)
    num3 = random.randint(0, 7)
    num4 = random.randint(0, 7)
    return textList[num1]+textList[num2]+textList[num3]+textList[num4]
def  ids():
    return str(random.randint(3001,900))
