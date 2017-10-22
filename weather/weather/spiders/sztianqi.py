# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem

class SztianqiSpider(scrapy.Spider):
    name = 'sztianqi'
    allowed_domains = ['suzhou.tianqi.com']
    start_urls = ['http://suzhou.tianqi.com/']


    def parse(self, response):
        items = []  #定义一个空的items列表，用来存放每天的信息
        sixday = response.xpath('//div[@class="tqshow1"]')   #找出包含着每天天气信息的DIV

        for day in sixday:  #先用for循环求出每天各自的信息
            item = WeatherItem()
            date = ''
            for datetitle in day.xpath('./h3//text()').extract():
                date += datetitle  #将for循环得出的文本叠加在一起

            item['date'] = date
            item['week'] = day.xpath('./p//text()').extract()[0]
            item['img'] = day.xpath('./ul/li[@class="tqpng"]/img/@src').extract()[0]

            tq = day.xpath('./ul/li[2]//text()').extract()

            item['temperature'] = ''.join(tq)   #使用join函数将元素以特定符号连接生成一个新的字符串
            item['weather'] = day.xpath('./ul/li[3]//text()').extract()[0]
            item['wind'] = day.xpath('./ul/li[4]//text()').extract()[0]
            items.append(item)

        return items

