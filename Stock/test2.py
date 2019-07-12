# -*- coding:UTF-8 -*-
import urllib
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#context = ssl._create_unverified_context()

ssl._create_default_https_context = ssl._create_unverified_context

#stockItem = '005930'
#url = 'http://finance.naver.com/item/sise_day.nhn?code='+ stockItem

#html = urlopen(url, context=context)
#source = BeautifulSoup(html.read(), "html.parser") 

#maxPage=source.find_all("table",align="center")
#mp = maxPage[0].find_all("td",class_="pgRR")
#mpNum = int(mp[0].a.get('href')[-3:])


#tt = source.find_all("a", class_="title")
#for page in tt:
#	print( page)


for i in range(1, 32):	# 1 to 31
	url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='+str(i)
	with urlopen(url) as response:
		html = response.read().decode('euc-kr','replace')
		#soup = BeautifulSoup(html, 'html.parser')
		soup = BeautifulSoup( html, 'html.parser')
		#td = soup.find_all('a')
		td = soup.find_all('a', {'class':'tltle'})
		
		for t in td:
			#print( t)
			#print( t.attrs['href'])
			stock_code = str( t.attrs['href'].split('code=')[1])
			name = str( t.text)	#, 'utf-8')
			print( stock_code, name)


for i in range(1, 29):	# 1 to 28
	url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page='+str(i)
	with urlopen(url) as response:
		html = response.read().decode('euc-kr','replace')
		soup = BeautifulSoup( html, 'html.parser')
		td = soup.find_all('a', {'class':'tltle'})
		
		for t in td:
			stock_code = str( t.attrs['href'].split('code=')[1])
			name = str( t.text)	#, 'utf-8')
			print( stock_code, name)





'''
for page in range(1, mpNum+1):
	print (str(page) )
	url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem +'&page='+ str(page)
	html = urlopen(url, context=context)
	source = BeautifulSoup(html.read(), "html.parser")
	srlists=source.find_all("tr")
	isCheckNone = None
	
	if((page % 1) == 0):
		time.sleep(1.50)
	
	for i in range(1,len(srlists)-1):
		if(srlists[i].span != isCheckNone):
			srlists[i].td.text
			print( srlists[i].find_all("td",align="center")[0].text, srlists[i].find_all("td",class_="num")[0].text )
'''


