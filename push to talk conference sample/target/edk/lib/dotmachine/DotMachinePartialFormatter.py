########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Formatter subclass for dotmachine translator that produces partial
# string representations of ECharts expressions.

import DotMachineFormatter
from AbstractMachine import *

MAX_LENGTH = 15

class DotMachinePartialFormatter(DotMachineFormatter.DotMachineFormatter):

	def dotportreceive(self, xn):
		if isMessagelessTransition(xn):
			return ""
		portRef = getTransitionPort(xn)
		if isDelayTransition(xn):
			rv = "delay(...)" 
		elif isAnyPortTransition(xn):
			rv = "* ? " + self.dottype(getTransitionMessageClass(xn))
		else:
			rv = self.dotexpression(portRef) + " ? " + self.dottype(getTransitionMessageClass(xn))
		return self.trim(rv)

	def dotxnguard(self, guard):
		if guard == []:
			return ""
		else: 
			return " [...]"

	def dotxnaction(self, action):
		return self.dotaction(action)

	# translate an abstract machine action block to dot
	def dotaction(self, actionBlock):
		if actionBlock == []: return ""
		previousActionWasAPortSend = True
		actionStrings = []
		actions = getActions(actionBlock)
		for action in actions:
			# port send action
			if getActionType(action) == PORT_SEND:
				# translate port reference
				actionString = self.dotexpression(getPortReference(action))
				# translate message reference
				actionStrings = actionStrings + [ actionString + self.trim(" ! %s" % self.dotexpression(getMessageSendReference(action))) ]
				previousActionWasAPortSend = True
			else:
				if previousActionWasAPortSend:
					actionStrings = actionStrings + [ "..." ]
					previousActionWasAPortSend = False						
		if len(actionStrings) == 1:
			if actionStrings[0] == "...":
				if len(actions) == 1:
					rv = " ...\l"
				else:
					rv = " {...}\l"
			else:
				# single port send action
				rv = " " + actionStrings[0] + "\l"
		else:
			rv = " {\l"
			for actionString in actionStrings:
				rv = rv + actionString + "\l"
			rv = rv + "}\l"
		return rv

	def dotextname(self, machine):
		extName = getExternalSubmachineClassName(machine)
		if len(getExternalSubmachineArguments(machine)) == 0:
			arglist = ""
		else:
			arglist = "..."
		return '%s(%s)' % (extName, arglist)
		
	def dotreflect(self, submachine):
		return 'reflect(..., ...)'

	def dotmachinearraybound(self, submachine):
		return "[...]" 

	def dotrootmachine(self, compilationUnit):
		return getMachineName(compilationUnit)

	def trim(self, string):
		global MAX_LENGTH
		if len(string) > MAX_LENGTH:
			return string[:MAX_LENGTH] + "..."
		else:
			return string
