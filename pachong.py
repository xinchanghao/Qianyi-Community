'''
#coding utf8
@author: Xinhao

'''
from urllib.request import Request # 寮曞叆urlrequest 妯″潡
from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
from urllib import parse # 寮曞叆parse 妯″潡
import pymysql.cursors



	req = Request("http://www.thsrc.com.tw/tw/TimeTable/SearchResult")

postDate = parse.urlencode([
("StartStation", "2f940836-cedc-41ef-8e28-c2336ac8fe68"),
("EndStation", "977abb69-413a-4ccf-a109-0272c24fd490"),
("SearchDate", "2016/08/31"),
("SearchTime", "21:30"),
("SearchWay", "DepartureInMandarin")

])
req.add_header("Origin", "http://www.thsrc.com.tw")
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0)")



resp = urlopen(req).read().decode('utf-8')
soup = bs(resp,"html.parser")
listUrls = soup.findAll("a", class_="f14 list-info-title")
for a in listUrls:
	{    
		print(a['href'],"<-->""http://localhost/",a['href'])

    }




#鑾峰彇鏁版嵁搴撹繛鎺�


connection = pymysql.connection(
			host="localhost",
			port='3306',
			user='root',
			password='',
			db='ptngo',
			charset='utf-8',
	)



try:
	#鑾峰彇浼氳瘽鎸囬拡
	with connection.cursor() as cursor
	#鍒涘缓sql璇彞
	sql=insert into `list`(`urlname`,`urlhref`) value(%s,%s)

	#鎵цsql
	cursor.execute(sql,(a.string,"http://localhost/"+a['href'])
	#鎻愪氦
	connection.commit()	
finally:
	#鍏抽棴鏁版嵁搴�
	connection.close()
