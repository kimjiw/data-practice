import urllib
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
from pymongo import MongoClient
import sys, re
import stock_ranks



def check_code_in_db (coll, code, name):

	res = coll.find_one( {'code':str(code)})
	if res is None:
		try:
			kospi.insert_one( {'code':str(code), 'name':name, 'trades':[]} )
		except:
			print( 'Failed to insert a new stock code info: code \''+ str(code) +'\'')
			sys.exit(0)

	else:
		print( 'Already registered: code \''+ str(code) +'\'')
	
	print( 'Complete to register the new code:'+ str(code))

	return




mongo = MongoClient('localhost', 27017)
db = mongo ['Stock']
kospi = db ['KOSPI']	# KOSPI collection

kospi_coms = stock_ranks.kospi_codes()

#url = 'http://finance.naver.com/item/sise_day.nhn?code='+ stockItem
#html = urlopen(url, context=context)
#source = BeautifulSoup(html.read(), "html.parser") 

for code, name in kospi_coms.items():	
	check_code_in_db(kospi, code, name)



sys.exit(0)


context = ssl._create_unverified_context()

maxPage=source.find_all("table",align="center")
mp = maxPage[0].find_all("td",class_="pgRR")
mpNum = int(mp[0].a.get('href')[-3:])


for page in range(1, mpNum+1):
	#print (str(page) )
	url = 'http://finance.naver.com/item/sise_day.nhn?code=' + stockItem +'&page='+ str(page)
	html = urlopen(url, context=context)
	source = BeautifulSoup(html.read(), "html.parser")
	srlists=source.find_all("tr")
	isCheckNone = None
	
	#if((page % 1) == 0):
	#	time.sleep(1.50)
	
	for i in range(1,len(srlists)-1):
		if(srlists[i].span != isCheckNone):
			srlists[i].td.text
			#print( srlists[i].find_all("td",align="center")[0].text, srlists[i].find_all("td",class_="num")[0].text )
			
			date = re.sub( '\.', '-', srlists[i].find_all("td",align="center")[0].text)
			price = int( re.sub( ',', '', srlists[i].find_all("td",class_="num")[0].text))
			vol = int( re.sub( ',', '', srlists[i].find_all("td",class_="num")[5].text))
			
			#print( date, price, vol)
			#sys.exit(0)
			try:
				#print( 'date:%s'%(date), 'price:%s'%(price), 'vol:%s'%(vol) )
				kospi.update_one( {'code':str(stockItem)}, {'$push': {'trades': {'date':'%s'%(date), 'price':price, 'vol':vol} } } )
			except:
				print( 'Failed to update the price info: code\''+ str(stockItem) +'\'')
				sys.exit(0)
				

