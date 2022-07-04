import scrapy
import re
from MachineLearning.items import MachinelearningItem


class ArxivSpider(scrapy.Spider):
    name = 'arxiv'
    allowed_domains = ['arxiv.org']
    start_urls = ['https://arxiv.org/list/cs.LG/pastweek?show=300']

    def parse(self, response):
        MonthPapers = response.xpath('//*[@id="dlpage"]/dl')
        for each_month_papers in MonthPapers:
            paperName = each_month_papers.xpath('//*[@id="dlpage"]/dl/dd')
            paperUrl = each_month_papers.xpath('//*[@id="dlpage"]/dl/dt')
            papers = zip(paperName,paperUrl)
            for each_paper_name,each_paper_url in papers:
                item = MachinelearningItem()
                item['name'] = each_paper_name.xpath("./div/div[1]/text()").extract()[1][0:-1]
                item['url'] = ["https://arxiv.org" + each_paper_url.xpath("./span/a[2]/@href").get()+'.pdf']
                yield item