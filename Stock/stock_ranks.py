# -*- coding:UTF-8 -*-
import urllib
import time
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

ssl._create_default_https_context = ssl._create_unverified_context


def kospi_codes():
	
	codes = {}
	for i in range(1, 32):	# 1 to 31
		url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page='+str(i)
		with urlopen(url) as response:
			html = response.read().decode('euc-kr','replace')
			soup = BeautifulSoup( html, 'html.parser')
			td = soup.find_all('a', {'class':'tltle'})
			
			for t in td:
				stock_code = str( t.attrs['href'].split('code=')[1])
				name = str( t.text)
				#print( stock_code, name)
				codes [stock_code] = name
				
	return codes


def kosdaq_codes():

	for i in range(1, 29):	# 1 to 28
		url = 'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=1&page='+str(i)
		with urlopen(url) as response:
			html = response.read().decode('euc-kr','replace')
			soup = BeautifulSoup( html, 'html.parser')
			td = soup.find_all('a', {'class':'tltle'})
			
			for t in td:
				stock_code = str( t.attrs['href'].split('code=')[1])
				name = str( t.text)
				#print( stock_code, name)
				codes [stock_code] = name

	return codes



