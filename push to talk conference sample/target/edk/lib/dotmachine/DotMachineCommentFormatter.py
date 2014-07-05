########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Formatter subclass for dotmachine translator that returns user
# comments associated with ECharts expressions.

import string, re
import DotMachineFormatter
from AbstractMachine import *

class DotMachineCommentFormatter(DotMachineFormatter.DotMachineFormatter):

	def dotportreceive(self, xn):
		return cleanup(getTransitionComment(xn))

	def dotstate(self, state, statePath):
		return cleanup(getStateComment(state))
		
	def dotrootmachine(self, compilationUnit):
		return cleanup(getMachineComment(getMachine(compilationUnit)))

def cleanup(comment):
	rv = ""
	# strip leading escape chars '/**'
	stripped = comment[3:]
	# strip trailing escape chars '*/'
	stripped = stripped[:-2]
	for line in string.split(stripped, '\n'):
		# strip leading and trailing space characters from each line
		line = string.strip(line)
		# strip leading '*' character if present and any following
		# whitespace
		line = re.sub("^\*\s*", "", line)
		if not line == "":
			if rv == "":
				# don't prepend newline for first line
				rv = line
			else:
				# escape subsequent newline chars
				rv = rv + '\\n' + line
	return rv
