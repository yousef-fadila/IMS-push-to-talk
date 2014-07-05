########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006-2009 AT&T Corp.                  #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################


import string
import sys

def versioncheck(min='0', max='99'):
	min_version = string.split(min, ".")
	max_version = string.split(max, ".")
	current_version = string.split(string.split(sys.version)[0], ".")
	if map(int, current_version) < map(int, min_version) or map(int, current_version) > map(int, max_version):
		return False
	else:
		return True
