import os
import time
import chargeStatus

bat = chargeStatus.status()
voltOk = True
while (voltOk == True):
	time.sleep(5)
	print "detecting voltage.."
	curBat = chargeStatus.status()
	print ("bat", bat[0])
	print ("curBat[0]", curBat[0])
	diff = bat[0] - curBat[0]
	if diff > 0.01 :
		print "voltage loss detected!!!"
		voltOk = False
		os.system('sudo poweroff')
	bat = curBat
	print "--------------------------------"


