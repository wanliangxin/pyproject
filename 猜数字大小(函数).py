# -*- coding: utf-8 -*-
#go=1
import random
result=0 #猜对的次数
sum_name={}
cai_num = 4
lun = 1
def score():
    print '------------'
    print "猜对排行榜"
    print '------------'
    for key, value in sum_name.items():
        print '%s猜对了%d次' % (key, value)

print '请主持人确定猜数字的范围'
min_num = int(raw_input("请主持人输入开始的范围:"))
max_num = int(raw_input("请主持人输入结束的范围:"))
pk = int(raw_input("请主持人输入PK次数:"))
cai_num = int(raw_input("请主持人输入猜的次数:"))

while pk > 0:
    suiji = random.randint(min_num, max_num)
    print '~~~第', lun, '轮~~~'
    for i in range(pk):

        #print ("随机数为%s" %nums)
        # person = int(raw_input("请主持人输入数字:"))
        #打印随机数
        #print suiji
        for a in range(cai_num):
            name = raw_input('请输入你的名字:')
            if not (name in sum_name):
                sum_name[name] = 0
            guests=int(raw_input('请参赛者输入数字：'))
            if guests>suiji:
                print '太大了'
                print "这轮还有",cai_num-a-1,"次机会"
            elif guests<suiji:
                print  '太小了'
                print "这轮还有", cai_num-a-1, "次机会"
            else:
                print '猜对了'
                result=1 #0代表没猜对，1代表猜对，使得循环外的判断不成立
                if name in sum_name:   #判断玩家是否在字典内
                    sum_name[name]= sum_name[name] + 1   #如果猜对就加一
                suiji = random.randint(min_num, max_num)
                break
        if result==0:
            print '你输了'
            print ("上轮的随机数为%s" % suiji)
            suiji = random.randint(min_num, max_num)
    pk = pk -1
    if result == 1:
        break
    if pk > 0:
        lun = lun + 1

score() #调用排行榜函数
