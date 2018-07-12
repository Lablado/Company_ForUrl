import requests
from lxml import etree
user_agent = 'Mozilla/4.0(compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
url_1="http://roll.finance.sina.com.cn/finance/bx3/bxxw_xydt/index_"
url_2=".shtml"
urls=[]
# urls.append("http://news.jc001.cn/keyId-153749/")
for i in range(1,89):
    c=url_1+str(i)+url_2
    urls.append(c)

data=[]
n=0

for i in urls:
    n+=1
    res = requests.get(i,headers=headers)
    html = res.content
    html = etree.HTML(html)
    html_data = html.xpath('//*[@class="listBlk"]//@href')
    for z in html_data:
        if len(z)>20:
            data.append(z)
    print(len(data))
    
    
    
with open("d4p_jinrong_roll.txt","w") as f:
    k=""
    for i in data:
        if i!=k:
            f.write(""+i+"\r\n")
        k=i
