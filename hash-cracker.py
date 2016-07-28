#!/usr/bin/env python2
# Author : L0V3R IN MYANMAR
# Date : 26,7,2016


import hashlib,sys,random,string,itertools


version = 1

allstrings = string.ascii_letters+string.digits+string.punctuation

def logo():
	print """
	 _   _           _            ____                _             
	| | | | __ _ ___| |__        / ___|_ __ __ _  ___| | _____ _ __ 
	| |_| |/ _` / __| '_ \ _____| |   | '__/ _` |/ __| |/ / _ \ '__|
	|  _  | (_| \__ \ | | |_____| |___| | | (_| | (__|   <  __/ |   
	|_| |_|\__,_|___/_| |_|      \____|_|  \__,_|\___|_|\_\___|_|   
	                                                                
                                                      Version [ %d ]

	"""%version

def ran():
	return random.choice("""\/|.-""")
def crack(realhash,hash_arg):
	for r in range(1,len(allstrings)+1):
		now = 1
		for b in itertools.product(allstrings,repeat=r):
			wordlist = "".join([str(i) for i in b])

			tmp_hash = hashlib.new(hash_arg,string=wordlist)
			tmp_hash = tmp_hash.hexdigest()
			sys.stdout.write("\rCracking with [ %s / %d ] : %s       %s"%(wordlist,now,tmp_hash,"%s%s"%(" "*int(20-len(tmp_hash)),ran())))
			sys.stdout.flush()
			if realhash == tmp_hash:
				return [True,wordlist]
			now += 1
def main():
	hash_tmp = ",".join([str(i) for i in hashlib.algorithms_available]).split(",")
	hasharg = []
	# remove same hash algorithms
	for i in hash_tmp:

		if i not in hasharg:
			hasharg.append(i)
	# End
	
	hasharg = sorted(hasharg)

	for i,alg in enumerate(hasharg):
		print " %d ] %s"%(i+1,alg)
	try:
		choice = int(raw_input("\nChoice hash algorithms to Crack (1-%d) : "%(i+1)))
	except ValueError:
		main()
		exit(1)
	if int(choice) in range(1,i+2):

		found = False
		try:
			found,text = crack(realhash,hasharg[choice-1])
		except TypeError:
			pass
		except KeyboardInterrupt:
			print "\nKeyboardInterrupt dectet!!"
			exit(1)
		if found == True:
			print "\nPassword Found : ", text
		else:
			print "\nSorry Not Found!" 

if __name__ == '__main__':
	logo()
	realhash = raw_input("Hash : ")
	print "1  ) All Characters (A-Za-Z0-9+SC)"
	print "2  ) Lower Characters ( a-z )"
	print "3  ) Upper Characters ( A-Z ) "
	print "4  ) Only Digit ( 0-9 ) "
	print "5  ) Special Characters ( %s )"%("""!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~""")

	print "6  ) Lower Characters and Upper Characters ( A-Za-z )"
	print "7  ) Lower Characters and digits ( a-z0-9 )"
	print "8  ) Lower Characters and Special Characters (a-z+SC) "
	
	print "9  ) Upper Characters and digits (A-Z0-9) "
	print "10 ) Upper Characters and Special Characters ( A-Z+SC ) "
	
	print "11 ) Digit and Special Characters ( 0-9+SC )"
	
	print "12 ) Lower Characters and digits and Special Characters ( a-z0-9+SC ) "
	print "13 ) Upper Characters and digits and Special Characters ( A-Z0-9+SC )"
	
	print "14 ) Lower Characters and Upper Characters and digits (a-zZ-A0-9) "
	print "15 ) Lower Characters and Upper Characters and Special Characters ( a-zA-Z+SC ) "
	wl = raw_input("\nChoice : ")
	if wl == "1":
		allstrings = string.ascii_letters+string.digits+string.punctuation
	elif wl == "2":
		allstrings = string.ascii_lowercase
	elif wl == "3":
		allstrings = string.ascii_uppercase
	elif wl == "4":
		allstrings = string.digits
	elif wl == "5":
		allstrings = string.punctuation
	elif wl == "6":
		allstrings = string.letters
	elif wl == "7":
		allstrings = string.ascii_lowercase+string.digits
	elif wl == "8":
		allstrings = string.ascii_lowercase+string.punctuation
	elif wl == "9":
		allstrings = string.ascii_uppercase+string.digits
	elif wl == "10":
		allstrings = string.ascii_uppercase+string.punctuation
	elif wl == "11":
		allstrings = string.digits+string.punctuation
	elif wl == "12":
		allstrings = string.ascii_lowercase+string.digits+string.punctuation
	elif wl == "13":
		allstrings = string.ascii_uppercase+string.digits+string.punctuation
	elif wl == "14":
		allstrings = string.ascii_lowercase+string.ascii_uppercase+string.digits
	elif wl == "15":
		allstrings = string.ascii_lowercase+string.ascii_uppercase+string.punctuation
	print "+"*30
	main()