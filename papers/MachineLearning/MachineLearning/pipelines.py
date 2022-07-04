# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import scrapy
import re,string
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline


class MachinelearningPipeline(object):
    def process_item(self, item, spider):
        with open(r"D:\0000\py\spider\papers\MachineLearning\result\paper.txt",'a') as fp:
            fp.write(item['name']+'\n')
        
        # 只获取某一方向的机器学习论文
        r = re.search(r"Deep|DNN|CNN|LSTM",item['name'])
        if r:
            return item
        
class DownloadPapersPipeline(FilesPipeline):
    def get_media_requests(self,item,info):
        for paper_url in item['url']:
            yield scrapy.Request(paper_url,meta={'item':item['name']})
    def file_path(self,request,response=None,info=None):
        paper_name = request.meta['item']
        paper_name = re.sub("[\*:\?<>\|/\\\"]+",'',str(paper_name))
        print(paper_name)
        return 'full/%s.pdf' % paper_name
