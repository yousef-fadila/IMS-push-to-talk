########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Formatter subclass for dotmachine translator that produces complete
# string representations of ECharts expressions.

import string
import DotMachineFormatter
from AbstractMachine import *

class DotMachineCompleteFormatter(DotMachineFormatter.DotMachineFormatter):

	def dotportreceive(self, xn):
		if isMessagelessTransition(xn):
			return ""
		portRef = getTransitionPort(xn)
		if isDelayTransition(xn):
			rv = "delay(%s)" % self.dotexpression(getTransitionMessageClass(xn))
		elif isAnyPortTransition(xn):
			rv = "* ? " + self.dottype(getTransitionMessageClass(xn))
		else:
			rv = self.dotexpression(portRef) + " ? " + self.dottype(getTransitionMessageClass(xn))
		return rv

	def dotxnguard(self, guard):
		if guard == []:
			return ""
		else: 
			return " [ " + self.dotexpression(guard) + " ]"

	def dotxnaction(self, action):
		return " / " + self.dotaction(action)

	# translate an abstract machine action block to dot
	def dotaction(self, actionBlock):
		if actionBlock == []: return ""
		actions = getActions(actionBlock)
		if len(actions) > 1:
			rv = "{\l"
		else:
			rv = ""
		for action in actions:
			# port send action
			if getActionType(action) == PORT_SEND:
				# translate port reference
				rv = rv + self.dotexpression(getPortReference(action))
				# translate message reference
				rv = rv + "!%s" % self.dotexpression(getMessageSendReference(action))
				# an expression
			else: 
				rv = rv + self.dotexpression(action)
			if len(actions) > 1:
				rv = rv + ";\l"
		if len(actions) > 1:
			rv = rv + "}\l"
		# escape double quotes
		return string.replace(rv, '"', '\\"')

	def dotextname(self, submachine):
		extName = getExternalSubmachineClassName(submachine)
		arglist = self.dotarglist(getExternalSubmachineArguments(submachine))
		return '%s(%s)' % (extName, arglist)
		
	def dotreflect(self, submachine):
		extName = self.dotexpression(getReflectSubmachineClassName(submachine))
		extArgs = self.dotexpression(getReflectSubmachineArguments(submachine))
		return 'reflect(%s, %s)' % (extName, extArgs)

	def dotmachinearraybound(self, submachine):
		[mod, bound] = getDynamicMachineModifier(submachine)
		return "[%s]" % self.dotexpression(bound)

	def dotrootmachine(self, compilationUnit):
		name = getMachineName(compilationUnit)
		package = getPackage(compilationUnit)
		return string.joinfields(package + [ name ], ".")
