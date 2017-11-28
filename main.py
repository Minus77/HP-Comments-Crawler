#encoding:utf-8
import csv
import re
import requests
import json
import codecs

s = requests.session()
url = 'https://club.jd.com/comment/productPageComments.action'
data = {
    'callback':'fetchJSON_comment98vv61',
    'productId':'971916',
    'score':1,
    'sortType':5,
    'pageSize':10,
    'isShadowSku':0,
    'page':0
}

myFile=codecs.open("test.csv" ,"w",encoding="utf_8_sig" )
myWriter=csv.writer(myFile,dialect='excel')

#    while i<10:
#        myWriter.writerow([7,'g'])
#        i=i+1
#    myWriter.writerow([8,'h'])
#    myList=[[1,2,3],[4,5,6]]
#    myWriter.writerow(myList)
for i in range(1):
        t = s.get(url,params = data).text

        try:
            t = re.search(r'(?<=fetchJSON_comment98vv61\().*(?=\);)',t).group(0)
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

myFile.close()
