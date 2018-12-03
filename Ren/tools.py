#!/home/s/ops/Python-3.5.6/python

import os
import sys
import yaml
from os.path import isfile


# Inspired by Perl module FindBin
Bin        = os.path.dirname(sys.argv[0])
Script     = os.path.basename(sys.argv[0])
RealBin    = os.path.dirname(os.path.realpath(sys.argv[0]))
RealScript = os.path.basename(os.path.realpath(sys.argv[0]))

# Load yaml config file
def load(conf=None):
	if conf is None:
		conf = RealBin + "/.config" if isfile(RealBin + "/.config") else RealBin + "/../.config"
		if not isfile(conf):
			print("Error: Not find config file.")
			exit(1)

	fin = open(conf)
	confDict = yaml.load(fin)
	fin.close()

	return confDict

def dict2yaml(dict_):
	print("---")

	if bool(dict_):
		print(yaml.dump(dict_, default_flow_style=False), end='')
