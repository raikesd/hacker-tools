##################################################
#	File: NMAPScanner.py
#	Date:	05/08/2013
#	Author: Donald Raikes <don.raikes@gmail.com>
#
#	adapted from the book "Violent Python"
################################################
import nmap
import optparse

def nmapScan(tgthost,tgtport):
	nm = nmap.PortScanner()
	nm.scan(tgthost,tgtport)
	hostname=nm[tgthost].hostname()
	state=nm[tgthost]['tcp'][int(tgtport)]['state']
	print "\t[*] "+" TCP/"+tgtport+" "+state

def main():
	parser = optparse.OptionParser('Usage%prog '+\
		'-H <target host> -p <target port>')
	parser.add_option('-H',dest='tgthost',type='string',\
		help='Specify target host.')
	parser.add_option('-p',dest='tgtport',type='string',\
		help='Specify target port(s) separated by commas')
	(options,args) = parser.parse_args()
	tgthost=options.tgthost
	tgtports=str(options.tgtport).split(',')
	print "-----------------------------------"
	print 'Host:\t'+tgthost
	
	if (tgthost == None) | (tgtports[0] == None):
		print parser.usage
		exit(0)
	
	for tgtport in tgtports:
		nmapScan(tgthost,tgtport)
		
if __name__ == '__main__':
	main()
