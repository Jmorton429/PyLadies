#this is going to rename files in batch. huzzah!
#!/usr/bin/env python
from os import rename, listdir

badprefix = "EX"
fnames = listdir('.')
newname = "ex"

for fname in fnames:
	if fname.startswith(badprefix):
		rename(fname, fname.replace(badprefix, newname))
