D=print
import time as A,gzip
def E(data):
	B=0;E=40;A=''
	for C in data:
		if B==40:B=0;A+='\n'
		B+=1
		if C==0:A+='  '
		else:A+='%%'
	D(A+'\x1b[30A')
F=A.time()
B=0
try:
	G=1200
	with gzip.open('baddestapple.dat.gz')as C:
		while B<6573:B=int((A.time()-F)*30)+1;C.seek(B*G);E(C.read(1200));A.sleep(.02)
except KeyboardInterrupt:D(''+'\x1b[30B')

    #this is the original version of my bad apple demo
    #the way i had audio working was really broken so nearly 3 years later i just said "fuck it" and completely removed it
    #we do not talk about it trust me!
    #created my AverageJuliet/
