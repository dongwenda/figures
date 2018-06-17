from die import Die
import pygal

# 创建5个D6的骰子
die_1 = Die()
die_2 = Die()
die_3 = Die()
die_4 = Die()
die_5 = Die()

# 骰子出现的次数
dice_1 = [0, 0, 0, 0, 0]
dice_2 = [0, 0, 0, 0, 0]
dice_3 = [0, 0, 0, 0, 0]
dice_4 = [0, 0, 0, 0, 0]
dice_5 = [0, 0, 0, 0, 0]
dice_6 = [0, 0, 0, 0, 0]

# 统计每个数 出现了几次
def count_dice_num(dice, num, result):
    if result.count(num) >= 1:
        dice[0] += 1
    if result.count(num) >= 2:
        dice[1] += 1
    if result.count(num) >= 3:
        dice[2] += 1
    if result.count(num) >= 4:
        dice[3] += 1
    if result.count(num) >= 5:
        dice[4] += 1
    if result.count(num) >= 6:
        dice[5] += 1

    return dice



for n in range(100):
    result = [die_1.roll(), die_2.roll(), die_3.roll(), die_4.roll(), die_5.roll()]
    #results.append(result)
    #print(result)

    # 统计 1 出现的次数
    dice_1 = count_dice_num(dice_1, 1, result)
    # 统计 2 出现的次数
    dice_2 = count_dice_num(dice_2, 2, result)
    # 统计 3 出现的次数
    dice_3 = count_dice_num(dice_3, 3, result)
    # 统计 4 出现的次数
    dice_4 = count_dice_num(dice_4, 4, result)
    # 统计 5 出现的次数
    dice_5 = count_dice_num(dice_5, 5, result)
    # 统计 6 出现的次数
    dice_6 = count_dice_num(dice_6, 6, result)





print("1 的出现次数统计：")
print(dice_1)
print("2 的出现次数统计：")
print(dice_2)
print("3 的出现次数统计：")
print(dice_3)
print("4 的出现次数统计：")
print(dice_4)
print("5 的出现次数统计：")
print(dice_5)
print("6 的出现次数统计：")
print(dice_6)

#dice = [dice_1, dice_2, dice_3, dice_4, dice_5, dice_6]
#n_1 = int(input("几个？"))
#n_2 = int(input("几？"))
#m = dice[n_2-1][n_1-1]/10
#print("掷了1000次 骰子，" + str(n_1) + "个" + str(n_2) + "的概率为：%.3f%%"  %(m))
