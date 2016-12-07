import sys
if __name__=='__main__':
	print str(sys.argv[1]) +' <<right'
	fr=open('here_read.txt','r')
	fw=open('here_write.txt','w+')
	fw.write(fr.readline())
	fr.close()
	fw.close()


