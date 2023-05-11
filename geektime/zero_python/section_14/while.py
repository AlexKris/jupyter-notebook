chinese_zodiac = '猴鸡狗猪鼠牛虎兔龙蛇马羊'

import time

num = 5
while True:
    num = num + 1
    if num == 10:
        continue
    print(num)
    time.sleep(1)