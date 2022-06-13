#version 1.1
import random
import sys

#random 7 digits
def rng():
	while True:
		p2=random.randint(1,9999999)
		code2=str(p2).zfill(7)
		p2sum=0
		for i in code2:
			cyfra1=int(i)
			p2sum+=cyfra1
		if not (p2sum%7!=0 or int(code2[6])==0 or int(code2[6])>=8):
			return code2

#10-digits CD Key
def a10d():
	p1=random.randint(0,999)
	while p1==333 or p1==444 or p1==555 or p1==666 or p1==777 or p1==888 or p1==999:
		p1=random.randint(0,999)
	code1=str(p1).zfill(3)
	code2 = rng()
	print(code1+"-"+code2)

#11-Digits CD Key
def a11d():
	p1=random.randint(1,999)
	code1=str(p1).zfill(3)
	rand=random.randint(1,2)
	p1ost=int(code1[2])+rand
	if p1ost==11:
		p1ost=1
	elif p1ost==10:
		p1ost=0
	code1+=str(p1ost)
	code2 = rng()
	print(code1+"-"+code2)

#OEM Key
def oem():
	p1p1=random.randint(1,366)
	p1p2=random.choice(['95','96','97','98','99','00','01','02','03'])
	code1=(str(p1p1)+p1p2).zfill(5)
	code2 = rng()
	p3=random.randint(1,99999)
	code3=str(p3).zfill(5)
	print(code1+"-"+"OEM"+"-"+code2+"-"+code3)

if len(sys.argv)>1:	
	match sys.argv[1]:
		case "-10d":
			if len(sys.argv)>2:
				for i in range(1, int(sys.argv[2])+1):
					a10d()
			else:
				a10d()
		case "-11d":
			if len(sys.argv)>2:
				for i in range(1, int(sys.argv[2])+1):
					a11d()
			else:
				a11d()
		case "-oem":
			if len(sys.argv)>2:
				for i in range(1, int(sys.argv[2])+1):
					oem()
			else:
				oem()
		case "-h":
			print("USAGE:",
			"\twin95keygen [OPTION] [NUMBER]\n",
			"[OPTION]",
			"\tList of available options:\n",
			"\t-10d - generates a 10-digits CD Key, used to activate Windows 95, Windows NT and other Microsoft programs",
			"\tExample: XXX-NNNNNNN\n",
			"\t-11d - generates a 11-digits CD Key, used to activate Office 97",
			"\tExample: XXXX-NNNNNNN\n",
			"\t-oem - generates an OEM Key, used to activate OEM versions of Windows 95, Windows NT and other Microsoft programs",
			"\tExample: XXXXX-OEM-NNNNNNN-AAAAA\n",
			"[NUMBER]",
			"\tType the number of keys you want get (default is 1)",
			"\tFor example:",
			"\t\"win95keygen -10d 5\" will generate 5 10-digits keys\n",
			"Type windows95keygen -a to see informations about this program",
			sep='\n')
		case "-a":
			print("This program was written by intru",
			"Based on the article written by Daniel Gurney: https://gurney.dev/posts/mod7/\n",
			"Written in Python 3.7",
			"Compiled with PyInstaller 3.4\n",
			"Check out the GitHub repo: https://github.com/intruzek3/win95keygen/",
			sep='\n')
		case _:
			print("Unknown parameter. Type \"win95keygen -h\" to help.")
else:
	print("Not enough parameters. Type \"win95keygen -h\" to help.") 
