import os

dirs = next(os.walk('.'))[1]

for dir in dirs:
	d = dir.split(" -")[0]
	if not os.path.exists(d):
		os.mkdir(d)
