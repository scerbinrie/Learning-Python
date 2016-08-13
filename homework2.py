

def celsiustofarenheit(temp1):
	farenheit = (float(temp1) * 1.8 + 32)
	return farenheit

def farenheittocelsius(temp1):
	celsius = (float(temp1)-32)*5/9
	return celsius


# while True:
# 	temp = float(raw_input("Enter temperature: "))
# 	print celsiustofarenheit(temp)
# 	print farenheittocelsius(temp)








# print "If temperature "+str(temp)+" is celsius, then this would equal to "+str(temp * 1.8 + 32)+" Farenheit"
# print "If temperature",temp,"is farenheit, then this would equal to",(temp-32)*5/9 ,"Celsius"