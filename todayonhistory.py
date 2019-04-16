import requests
import csv
from pyquery import PyQuery as pq
response=requests.get('http://www.todayonhistory.com/12/31/16570.html')
response.encoding=response.apparent_encoding
doc=pq(response.text)
nian=doc('body > div.wrap.main.oh.pr.showarc > div.pos.moh > a:nth-child(2)').text()
riqi=doc('body > div.wrap.main.oh.pr.showarc > div.pos.moh > a:nth-child(3)').text()
title=doc('body > div.wrap.main.oh.pr.showarc > div.ml.box > div.content > h1').text()
tupian=doc('body > div.wrap.main.oh.pr.showarc > div.ml.box > div.content > div.body').text()
links=doc('body > div.wrap.main.oh.pr.showarc > div.ml.box > div.content > div.body > div:nth-child(1) > img')
for link in links.items():
    print(link.attr.src)
with open("0904.csv",'a',newline='') as f:
    csvwriter=csv.writer(f,dialect='excel')
    csvwriter.writerow([nian,riqi,title,tupian,link.attr.src])
