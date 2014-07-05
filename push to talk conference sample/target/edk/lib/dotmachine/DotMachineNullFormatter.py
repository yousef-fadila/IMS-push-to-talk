########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Formatter subclass for dotmachine translator that returns empty strings.

import DotMachineFormatter

class DotMachineNullFormatter(DotMachineFormatter.DotMachineFormatter):

	def dotportreceive(self, xn):
		return ""

	def dotstate(self, state, statePath):
		return ""
		
	def dotrootmachine(self, compilationUnit):
		return ""
