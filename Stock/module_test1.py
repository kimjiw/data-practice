import stock_ranks

codes = stock_ranks.kospi_codes()

#print( codes)

for code, name in codes.items():
	print( '\t'.join( [code, name]))


