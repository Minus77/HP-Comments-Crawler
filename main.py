#encoding:utf-8
import csv
import re
import requests
import json
import codecs

print("请输入产品ID")
productId=input()
print("请输入所需评论种类\n0为全部评论、1为差评、2为好评")
kindNum=input()
s = requests.session()
url = 'https://club.jd.com/comment/skuProductPageComments.action'
data = {
    'callback' : 'fetchJSON_comment98vv1941',
    'productId' : productId,
    'score' : kindNum,
    'sortType' : 5,
    'pageSize' : 10,
    'isShadowSku' : 0,
    'page' : 0,
    'fold' : 1
}
print("正在爬取评论数据")
myFile=codecs.open(productId+".csv" ,"w",encoding="utf_8_sig" )
myWriter=csv.writer(myFile,dialect='excel')
title=['用户名','评论时间','用户终端','评论内容']
myWriter.writerow(title)
#    while i<10:
#        myWriter.writerow([7,'g'])
#        i=i+1
#    myWriter.writerow([8,'h'])
#    myList=[[1,2,3],[4,5,6]]
#    myWriter.writerow(myList)
for i in range(100):
        t = s.get(url,params = data).text

        try:
            t = re.search(r'(?<=fetchJSON_comment98vv1941\().*(?=\);)',t).group(0)
        except Exception as e:
            break

        j=json.loads(t)
        commentSummary = j['comments']
        for comment in commentSummary:
            c_content = comment['content']
            c_time = comment['referenceTime']
            c_name = comment['nickname']
            c_client = comment['userClientShow']
            info=[]
            info.append(c_name)
            info.append(c_time)
            info.append(c_client)
            info.append(c_content)
            myWriter.writerow(info)
            #print('{}  {}  {}\n{}\n'.format(c_name,c_time,c_client,c_content))
        data['page'] += 1
print("数据抓取完成")
while(0):
    stop=input()
myFile.close()
