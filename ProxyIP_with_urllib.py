


import urllib.request
import chardet
import re

def open_url(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39')
    response = urllib.request.urlopen(req)
    page = response.read()

    encoding = chardet.detect(page)['encoding']
    if encoding == 'GB2312':
        html = page.decode('GBK')
    else:
        html = page.decode(encoding)
    return html
def get_ip(html):
    p = r'(?:(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}(?:[01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])'
    iplist = re.findall(p,html)

    for each in iplist:
        print(each)

if __name__=='__main__':
    url = "http://cn-proxy.com/"
    get_ip(open_url(url))
    
