import random
import sys
def a10d():
	p1=random.randint(0,999)
	while p1==333 or p1==444 or p1==555 or p1==666 or p1==777 or p1==888 or p1==999:
		p1=random.randint(0,999)
	code1=str(p1)
	if p1<10:
		code1="0"+"0"+code1
	elif p1<100:
		code1="0"+code1	
	def rng():
		global p2
		global code2
		global p2sum
		p2=random.randint(1,9999999)
		code2=str(p2)
		p2sum=0
		for i in code2:
			cyfra1=int(i)
			p2sum+=cyfra1
		if p2<10:
			code2="0"+"0"+"0"+"0"+"0"+"0"+code2
		elif p2<100:
			code2="0"+"0"+"0"+"0"+"0"+code2
		elif p2<1000:
			code2="0"+"0"+"0"+"0"+code2
		elif p2<10000:
			code2="0"+"0"+"0"+code2
		elif p2<100000:
			code2="0"+"0"+code2
		elif p2<1000000:
			code2="0"+code2
	rng()
	while p2sum%7!=0 or int(code2[6])==0 or int(code2[6])>=8:
		rng()
	print(code1+"-"+code2)
def a11d():
	p1=random.randint(1,999)
	code1=str(p1)
	if p1<10:
		code1="0"+"0"+code1
	elif p1<100:
		code1="0"+code1
	rand=random.randint(1,2)
	p1ost=int(code1[2])+rand
	if p1ost==11:
		p1ost=1
	elif p1ost==10:
		p1ost=0
	code1+=str(p1ost)
	def rng():
		global p2
		global code2
		global p2sum
		p2=random.randint(1,9999999)
		code2=str(p2)
		p2sum=0
		for i in code2:
			cyfra1=int(i)
			p2sum+=cyfra1
		if p2<10:
			code2="0"+"0"+"0"+"0"+"0"+"0"+code2
		elif p2<100:
			code2="0"+"0"+"0"+"0"+"0"+code2
		elif p2<1000:
			code2="0"+"0"+"0"+"0"+code2
		elif p2<10000:
			code2="0"+"0"+"0"+code2
		elif p2<100000:
			code2="0"+"0"+code2
		elif p2<1000000:
			code2="0"+code2
	rng()
	while p2sum%7!=0 or int(code2[6])==0 or int(code2[6])>=8:
		rng()
	print(code1+"-"+code2)
def oem():
	p1p1=random.randint(1,366)
	p1p2=random.choice(['95','96','97','98','99','00','01','02','03'])
	code1=str(p1p1)+p1p2
	if p1p1<10:
		code1="0"+"0"+code1
	elif p1p1<100:
		code1="0"+code1
	def rng():
		global p2
		global code2
		global p2sum
		p2=random.randint(1,999999)
		code2=str(p2)
		p2sum=0
		for i in code2:
			cyfra1=int(i)
			p2sum+=cyfra1
		if p2<10:
			code2="0"+"0"+"0"+"0"+"0"+code2
		elif p2<100:
			code2="0"+"0"+"0"+"0"+code2
		elif p2<1000:
			code2="0"+"0"+"0"+code2
		elif p2<10000:
			code2="0"+"0"+code2
		elif p2<100000:
			code2="0"+code2
		code2="0"+code2
	rng()
	while p2sum%7!=0 or int(code2[5])==0 or int(code2[5])>=8:
		rng()
	p3=random.randint(1,99999)
	code3=str(p3)
	if p3<10:
		code3="0"+"0"+"0"+"0"+code3
	elif p3<100:
		code3="0"+"0"+"0"+code3
	elif p3<1000:
		code3="0"+"0"+code3
	elif p3<10000:
		code3="0"+code3
	print(code1+"-"+"OEM"+"-"+code2+"-"+code3)
if len(sys.argv)>1:	
	if sys.argv[1]=="-10d":
		if len(sys.argv)>2:
			for i in range(1, int(sys.argv[2])+1):
				a10d()
		else:
			a10d()
	elif sys.argv[1]=="-11d":
		if len(sys.argv)>2:
			for i in range(1, int(sys.argv[2])+1):
				a11d()
		else:
			a11d()
	elif sys.argv[1]=="-oem":
		if len(sys.argv)>2:
			for i in range(1, int(sys.argv[2])+1):
				oem()
		else:
			oem()
	elif sys.argv[1]=="-h":
		print("USAGE:")
		print("\twin95keygen [OPTION] [NUMBER]\n")
		print("[OPTION]")
		print("\tList of available options:\n")
		print("\t-10d - generates a 10-digits CD Key, used to activate Windows 95, Windows NT and other Microsoft programs")
		print("\tExample: XXX-NNNNNNN\n")
		print("\t-11d - generates a 11-digits CD Key, used to activate Office 97")
		print("\tExample: XXXX-NNNNNNN\n")
		print("\t-oem - generates an OEM Key, used to activate OEM versions of Windows 95, Windows NT and other Microsoft programs")
		print("\tExample: XXXXX-OEM-NNNNNNN-AAAAA\n")
		print("[NUMBER]")
		print("\tType the number of keys you want get (default is 1)")
		print("\tFor example:")
		print("\t\"win95keygen -10d 5\" will generate 5 10-digits keys\n")
		print("Type windows95keygen -a to see informations about this program\n")
	elif sys.argv[1]=="-a":
		print("This program was written by intru")
		print("Based on the article written by Daniel Gurney: https://gurney.dev/posts/mod7/\n")
		print("Written in Python 3.7")
		print("Compiled with PyInstaller 3.4\n")
		print("Check out the GitHub repo: https://github.com/intruzek3/win95keygen/")
	else:
		print("Unknown parameter. Type \"win95keygen -h\" to help.")
else:
	print("Unknown parameter. Type \"win95keygen -h\" to help.") 