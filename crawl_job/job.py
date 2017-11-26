# -*- coding:utf-8 -*-

#导入模块
import MySQLdb
import re
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#创建数据库连接
conn = MySQLdb.connect(
    host='192.168.100.10',
    port=3306,
    user='craw123',
    passwd='craw123',
    db='db',
    charset='utf8')
cur = conn.cursor()

#获取源码
def get_info(page):
    url ='http://search.51job.com/list/000000,000000,0000,00,9,99,python,2,'+ str(page)+'.html'
    a = urllib2.urlopen(url)
    html = a.read().decode('gbk')       # 读取源代码并转为unicode
    return html

#获取爬取的内容
def get(html):
    #利用正则提取出需要的信息
    reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S) #匹配换行符
    items = re.findall(reg,html)
    return items

#将爬取的内容写进文件
for b in range(1,20):  #设置爬取的页数
    html = get_info(b)
    print ("正在爬取第" + str(b) + "页的内容......")
    for num in get(html):
        filename = u'51job招聘信息.txt'
        with open(filename,'a') as f:
            f.write(num[0] + '\t' + num[1] + '\t' + num[2] + '\t' + num[3] + '\t' + num[4] + '\n' )
            f.close

#将爬取的内容写进数据库
for b in range(1,20):  #设置爬取的页数
    html = get_info(b)
    for num in get(html):
        JobName = num[0].encode('utf-8')
        CompanyName = num[1].encode('utf-8')
        WorkPlace = num[2].encode('utf-8')
        Salary = num[3].encode('utf-8')
        Time1 = num[4].encode('utf-8')
        cur.execute("INSERT INTO pythonjobs(Jobname, CompanyName, WorkPlace, Salary, Time1) values(%s,%s,%s,%s,%s)",
        (JobName, CompanyName, WorkPlace, Salary, Time1))

#关闭连接
cur.close()
conn.commit()
conn.close()
