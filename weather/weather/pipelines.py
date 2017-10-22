# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

class WeatherPipeline(object):

    def process_item(self, item, spider):
        base_dir = os.getcwd()  # 获取当前工作目录
        filename = base_dir + r'\local_data\weather.txt'  # 文件存在本地local_data目录下的weather.txt文件内

        with open(filename, 'a') as f:  # 以追加的方式打开文件，并写入对应的数据
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['temperature'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n')
            f.write(item['img'] + '\n\n')

        return item

