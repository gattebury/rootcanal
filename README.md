rootcanal
=========

Utility to make dealing with .root files less painful


Usage:
	./rootcanal -l <lfn>

	or

	./rootcanal -f <file with lfns>




hdfsscan
========

Scans through files reading 1 byte every defined blocksize (64MB default) with
the intention of forcing a read on every block on disk in an HDFS filesystem.

Can use multiple reader threads ( -t option ) for some performance gains.

Writes list of files with I/O errors to an output file.


Usage:

	./hdfsscan -v -t 5 -d <directory to start in>

