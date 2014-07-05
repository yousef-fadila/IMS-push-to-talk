########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Abstract formatter class for dotmachine translator.

from AbstractMachine import *

import re
import string

class DotMachineFormatter:

	def dotxnguard(self, guard): return ""

	def dotxnaction(self, actionBlock): return ""

	def dotaction(self, actionBlock): return ""

	def dotportreceive(self, xn): return ""

	def dotxn(self, portguard, action):
		if portguard == "":
			if action == "":
				return ""
			else:
				return "/" + action
		else:
			if action == "":
				return portguard
			else:
				return portguard + " /\l" + action

	def dotextname(self, machine): return ""

	def dotreflect(self, submachine): return ""

	def dotmachinearraybound(self, submachine): return ""

	def dotrootmachine(self, compilationUnit): return ""

	def doturl(self, compilationUnit, statePath):
		return ""

	def dotstate(self, state, statePath):
		submachine = getSubmachine(state)
		submachineName = getStateName(state)
		stateModifiersList = getStateAccessModifiers(state) + getStateModifiers(state)
		if "initial" in stateModifiersList:
			stateModifiersList.remove("initial")
		elif "concurrent" in stateModifiersList:
			stateModifiersList.remove("concurrent")
		stateModifiers = string.joinfields(stateModifiersList, " ")
		if isDynamicMachine(submachine):
			stateBound = self.dotmachinearraybound(submachine)
			# substitute machine with submachine nested in only state
			# of dynamic machine since we don't want to include
			# dynamic machine itself
			state = getStates(submachine)[0]
			submachine = getSubmachine(state)
		else:
			stateBound = ""
		if not stateModifiers == "":
			stateModifiers = stateModifiers + "\l"
		stateName = submachineName + stateBound + "\l"
		entryAction = getActionBlock(getStateEntry(state))
		if entryAction == []:
			stateEntry = ""
		else:
			stateEntry = "entry " + self.dotaction(entryAction) + "\l"
		exitAction = getActionBlock(getStateExit(state))
		if exitAction == []:
			stateExit = ""
		else:
			stateExit = "exit " + self.dotaction(exitAction) + "\l"
		stateLabel = "%s%s%s%s" % (stateModifiers, stateName, stateEntry, stateExit)
		if getSubmachineType(submachine) == EXTERNAL_SUBMACHINE:
			# constant parameterized submachine reference of form fsm(p1,...)
			# label = submachine constructor reference
			stateLabelSuffix = ':' + self.dotextname(submachine) + "\l"
		elif getSubmachineType(submachine) == REFLECT_SUBMACHINE:
			# 'reflect' submachine reference of form reflect(arg1, arg2)
			stateLabelSuffix = ':' + self.dotreflect(submachine) + "\l"
		elif getSubmachineType(submachine) in [ NO_SUBMACHINE, INNER_SUBMACHINE ]:
			stateLabelSuffix = ""
		return stateLabel + stateLabelSuffix
		
	# Convert a variable type declaration to a string.
	def dottype(self, type):
		typeId = string.joinfields(getTypeIdentifier(type), ".")
		typeArray = reduce(lambda x,y: "%s%s" % (x, y), getTypeArrayDeclarator(type), "")
		return typeId + typeArray

	# Translates a list of arguments to a string.
	def dotarglist(self, args):
		argStrings = []
		for arg in args:
			argStrings = argStrings + [ self.dotexpression(arg) ]
		return string.joinfields(argStrings, ", ")

	# Convert an abstract machine expression to a string.
	def dotexpression(self, ex):
		# ex may be a list or a irreducible element like a string or a
		# constant - initial list element may be an operator or a
		# irreducible element
		if type(ex) == types.ListType:
			if len(ex) == 0:
				return ""
			elif ex[0] == ASSIGN:
				return "%s = %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == PLUS_ASSIGN:
				return "%s += %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == MINUS_ASSIGN:
				return "%s -= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == STAR_ASSIGN:
				return "%s *= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == DIV_ASSIGN:
				return "%s /= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == MOD_ASSIGN:
				return "%s %= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == SR_ASSIGN:
				return "%s >>= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BSR_ASSIGN:
				return "%s >>>= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == SL_ASSIGN:
				return "%s <<= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BAND_ASSIGN:
				return "%s &= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BXOR_ASSIGN:
				return "%s ^= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BOR_ASSIGN:
				return "%s |= %s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == LOR:
				return "(%s || %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == LAND:
				return "(%s && %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BOR:
				return "(%s | %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BXOR:
				return "(%s ^ %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BAND:
				return "(%s & %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == NOT_EQUAL:
				return "(%s != %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == EQUAL:
				return "(%s == %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == LT:
				return "(%s < %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == GT:
				return "(%s > %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == LE:
				return "(%s <= %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == GE:
				return "(%s >= %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == SL:
				return "(%s << %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == SR:
				return "(%s >> %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == BSR:
				return "(%s >>> %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == PLUS:
				return "(%s + %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == MINUS:
				return "(%s - %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == DIV:
				return "(%s / %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == MOD:
				return "(%s % %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == STAR:
				return "(%s * %s)" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == INC:
				return "++(%s)" % self.dotexpression(ex[1])
			elif ex[0] == DEC:
				return "--(%s)" % self.dotexpression(ex[1])
			elif ex[0] == POST_INC:
				return "(%s)++" % self.dotexpression(ex[1])
			elif ex[0] == POST_DEC:
				return "(%s)--" % self.dotexpression(ex[1])
			elif ex[0] == BNOT:
				return "~(%s)" % self.dotexpression(ex[1])
			elif ex[0] == LNOT:
				return "!(%s)" % self.dotexpression(ex[1])
			elif ex[0] == UNARY_MINUS:
				return "-(%s)" % self.dotexpression(ex[1])
			elif ex[0] == UNARY_PLUS:
				return "+(%s)" % self.dotexpression(ex[1])
			elif ex[0] == METHOD_CALL:
				return "%s%s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == ELIST:
				return "(%s)" % self.dotarglist(ex[1])
			elif ex[0] == NEW_EXPRESSION:
				rv = "new %s%s" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
				if len(ex) == 4:
					# optional array initializer
					rv = rv + self.dotexpression(ex[3])
				return rv
			elif ex[0] == TYPECAST:
				return "((%s) %s)" % (self.dottype(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == INDEX_OP:
				return "%s[%s]" % (self.dotexpression(ex[1]), self.dotexpression(ex[2]))
			elif ex[0] == ARRAY_DECLARATOR:
				return string.joinfields(map(lambda x: "[%s]" % self.dotexpression(x), ex[1]), "")
			elif ex[0] == ARRAY_INIT:
				return "{%s}" % string.joinfields(map(self.dotexpression, ex[1:]), ", ")
			elif ex[0] == HOST_BLOCK:
				# return host block with delimiters but substitute
				# newlines with \l
				return re.sub("\n", "\\l", string.strip(getDelimitedHostCode(ex)))
			else:
				# first element not a recognized (integer) operator so
				# treat as (dotted) identifier (i.e. primaryExpression)
				return string.joinfields(map(self.dotexpression, ex), ".")
		else:
			# irreducible element escape quotes if present, and
			# substitute newlines with \n
			return re.sub("\n", "\\l", re.sub('"', '\\"', ex))

