
import urllib
from xml.dom import minidom
from zlib import adler32

def getFileReplicasFromDataset(dataset):
	url = 'https://cmsweb.cern.ch/phedex/datasvc/xml/prod/FileReplicas?dataset=' + dataset
	return minidom.parse(urllib.urlopen(url))


def calcChecksum(file):
	""" return adler32 checksum for file """
	val = 1
	try:
		fp = open(file)
		while True:
			data = fp.read(4096)
			if not data:
				break
			val = adler32(data,val)
		if val < 0:
			val += 2**32
		return hex(val)[2:10].zfill(8).lower()
	except IOError as (errno, strerror):
		print "** I/O ERROR({0}): {1}".format(errno, strerror)
		return ""
