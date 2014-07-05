#!/usr/bin/env python

########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

import sys, string, os, types, os.path
import antlr
import echarts_l, echarts_p, echarts_w
from echarts_w import *

import warnings
# need to change how AbstractMachineExceptions are raised but in the meantime...
warnings.filterwarnings(action="ignore", message="raising a string exception is deprecated", category=DeprecationWarning)

_version = "1.3.1-beta"

def getVersion():
	return "ECharts AbstractMachine version " + _version

True = 1
False = 0

# AbstractMachine class and supporting methods. See comments below for
# AbstractMachine class.

AbstractMachineException = "AbstractMachineException"

# constants

DEEP_HISTORY = "DEEP_HISTORY"
TERMINAL = "TERMINAL"
NEW = "NEW"
DEFAULT_INITIAL = "DEFAULT_INITIAL"
ANY = "ANY"

# Methods for operating on abstract machine structure returned by
# echarts ast walker. Helps to hide the underlying structure of the
# list from the programmer. The general philosophy behind these
# methods is that if the returned list represents a primitive type
# i.e. has no leaf nodes in the ast, then any token type identifier is
# removed from the list e.g. see getImports().

def getHostBlocks(machine):
	return getMachineBody(machine)[3][1:]

# Returns delimited commment, if defined.
def getMachineComment(machine):
	if machine[0] == MACHINE_DEF:
		return machine[6]
	else:
		raise AbstractMachineException( "Not a machine definition %s" % indent(machine) )

# Returns (line, column) pair identifying location of machine
# definition in source file.
def getMachineLineColumn(machine):
	if machine[0] == MACHINE_DEF:
		return (machine[7][1], machine[7][2])
	else:
		raise AbstractMachineException( "Not a machine definition %s" % indent(machine)		)

def getExtendsClause(machine):
	if machine[0] == MACHINE_DEF:
		if len(machine[4]) > 1:
			return machine[4][1]
		else:
			return None
	else:
		raise AbstractMachineException( "Not a machine definition %s" % indent(machine)		)

def getImplementsClause(machine):
	if machine[0] == MACHINE_DEF:
		if len(machine[5]) > 1:
			return machine[5][1:]
		else:
			return None
	else:
		raise AbstractMachineException( "Not a machine definition %s" % indent(machine)		)

def getStates(machine):
	# exclude STATES token
	return getMachineBody(machine)[1][1:]

def setStates(machine, states):
	body = getMachineBody(machine)
	body[1] = [ STATES ] + states
	setMachineBody(machine, body)

def getStateName(state):
	if state[0] == STATE_DEF:
		return state[3][0]
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def getStateComment(state):
	if state[0] == STATE_DEF:
		return state[6]
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

# Returns (line, column) pair identifying location of state
# definition in source file.
def getStateLineColumn(state):
	if state[0] == STATE_DEF:
		return (state[7][1], state[7][2])
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def getStateArrayBound(state):
	if state[0] == STATE_DEF:
		if len(state[3]) == 1:
			return 0
		else:
			return state[3][1]
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def getStateModifiers(state):
	if state[0] == STATE_DEF:
		return state[2][1:]
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def setStateModifiers(state, modifiers):
	if state[0] == STATE_DEF:
		state[2][1:] = modifiers
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def isAndState(state):
	if state[0] == STATE_DEF:
		return 'concurrent' in getStateModifiers(state)
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def getStateAccessModifiers(state):
	if state[0] == STATE_DEF:
		return state[1][1:]
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def getStateEntry(state):
	if state[0] == STATE_DEF:
		return state[4]
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def getStateExit(state):
	if state[0] == STATE_DEF:
		return state[5]
	else:
		raise AbstractMachineException( "Not a state definition %s" % indent(state))

def getActionBlock(item):
	if item[0] in [EXIT, ENTRY]:
		if len(item) > 1:
			return item[1]
		else:
			# no action block defined 
			return []
	else:
		raise AbstractMachineException( "No action block defined for %s" % indent(item))

def getActions(actionBlock):
	if actionBlock[0] == ACTION_BLOCK:
		return actionBlock[1:]
	else:
		raise AbstractMachineException( "Not an action block %s" % indent(actionBlock))

def getActionType(action):
	if type(action) == types.ListType:
		if action[0] == PORT_SEND:
			return action[0]
		else:
			return EXPR
	else:
		raise AbstractMachineException( "Not an action %s" % indent(action))

def getPortReferenceType(portRef):
	return portRef[0]

def getPortReference(portOp):
	if portOp[0] in [ PORT_SEND, PORT_RECEIVE ]:
		return portOp[1]
	else:
		raise AbstractMachineException( "Not a port send/receive operation %s" % indent(portOp))

def getMessageSendReference(portSend):
	if portSend[0] == PORT_SEND:
		return portSend[2]
	else:
		raise AbstractMachineException( "Not a port send operation %s" % indent(portSend))

def getConstructorReferenceClass(messageConstructorRef):
	if messageConstructorRef[0] == CONSTRUCTOR_REF:
		return messageConstructorRef[1]
	else:
		raise AbstractMachineException( 
			  "Not a message constructor reference %s" % indent(messageConstructorRef))

def getConstructorReferenceArguments(messageConstructorRef):
	if messageConstructorRef[0] == CONSTRUCTOR_REF:
		return messageConstructorRef[2]
	else:
		raise AbstractMachineException( 
			  "Not a message constructor reference %s" % indent(messageConstructorRef))

def getHostConstructorReferenceClass(messageHostConstructorRef):
	if messageHostConstructorRef[0] == HOST_CONSTRUCTOR_REF:
		return messageHostConstructorRef[1]
	else:
		raise AbstractMachineException( 
			  "Not a host message constructor reference %s" % indent(messageHostConstructorRef))

def getHostConstructorReferenceHostBlock(messageHostConstructorRef):
	if messageHostConstructorRef[0] == HOST_CONSTRUCTOR_REF:
		return messageHostConstructorRef[2]
	else:
		raise AbstractMachineException( 
			  "Not a host message constructor reference %s" % indent(messageHostConstructorRef))

def getInitialState(machine):
	for state in getStates(machine):
		if isInitialState(state):
			return state
	return None

def isInitialStateDefined(machine):
	return getInitialState(machine) != None

def isInitialState(state):
	return "initial" in getStateModifiers(state)

def isNonTerminalState(state):
	return "nonterminal" in getStateModifiers(state)

def getConstructors(machine):
	return getMachineBody(machine)[4][1:]

def getConstructorName(constructor):
	if constructor[0] == CONSTRUCTOR_DEF:
		return constructor[2]
	else:
		raise AbstractMachineException( "Not a constructor definition %s" % indent(constructor))

def getConstructorAccessModifiers(constructor):
	if constructor[0] == CONSTRUCTOR_DEF:
		return constructor[1][1:]
	else:
		raise AbstractMachineException( "Not a constructor definition %s" % indent(constructor))

def getConstructorParameters(constructor):
	if constructor[0] == CONSTRUCTOR_DEF:
		return constructor[3][1:]
	else:
		raise AbstractMachineException( "Not a constructor definition %s" % indent(constructor))

# Returns comment with comment delimiters.
def getConstructorComment(constructor):
	if constructor[0] == CONSTRUCTOR_DEF:
		return constructor[5]
	else:
		raise AbstractMachineException( "Not a constructor definition %s" % indent(constructor))

# Returns (line, column) pair identifying location of constructor
# definition in source file.
def getConstructorLineColumn(constructor):
	if constructor[0] == CONSTRUCTOR_DEF:
		return (constructor[6][1], constructor[6][2])
	else:
		raise AbstractMachineException( "Not a constructor definition %s" % indent(constructor))

def getConstructorActionBlock(constructor):
	if constructor[0] == CONSTRUCTOR_DEF:
		return constructor[4]
	else:
		raise AbstractMachineException( "Not a constructor definition %s" % indent(constructor))

def getTypeIdentifier(type):
	if type[0] == TYPE:
		return type[1][-1]
	else:
		raise AbstractMachineException( "Not a type definition %s" % indent(type))

def getTypeArrayDeclarator(type):
	if type[0] == TYPE:
		return type[1][:-1]
	else:
		raise AbstractMachineException( "Not a type definition %s" % indent(type))

def getDelimitedHostCode(hostBlock):
	if hostBlock[0] == HOST_BLOCK:
		# do not strip off escape delimiters "<*" and "*>"
		return hostBlock[1]
	else:
		raise AbstractMachineException( "Not a host block %s" % indent(hostBlock))

# Returns (line, column) pair identifying location of host block
# definition in source file.
def getHostBlockLineColumn(hostBlock):
	if hostBlock[0] == HOST_BLOCK:
		return (hostBlock[2][1], hostBlock[2][2])
	else:
		raise AbstractMachineException( "Not a host block %s" % indent(hostBlock))

# Returns delimited comment, if one exists.
def getHostBlockComment(hostBlock):
	if hostBlock[0] == HOST_BLOCK:
		if len(hostBlock) == 4:
			return hostBlock[3]
		else:
			return ''
	else:
		raise AbstractMachineException( "Not a host block %s" % indent(hostBlock))

def getHostCode(hostBlock):
	if hostBlock[0] == HOST_BLOCK:
		# strip off escape delimiters "<*" and "*>"
		return hostBlock[1][2:-2]
	else:
		raise AbstractMachineException( "Not a host block %s" % indent(hostBlock))

def getTransitions(machine):
	# exclude TRANSITIONS token
	return getMachineBody(machine)[2][1:]

def setTransitions(machine, transitions):
	body = getMachineBody(machine)
	body[2] = [ TRANSITIONS ] + transitions
	setMachineBody(machine, body)

def isMessagelessTransition(transition):
	return getTransitionPort(transition) == None

def isMessageTransition(transition):
	return not isMessagelessTransition(transition)

def isDelayTransition(transition):
	return getTransitionPort(transition) == "delay"

def isAnyPortTransition(transition):
	return getTransitionPort(transition) == "*"

# Returns (line, column) pair identifying location of transition
# definition in source file.
def getTransitionLineColumn(transition):
	if transition[0] == TRANSITION_DEF:
		return (transition[-1][1], transition[-1][2])
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def getTransitionComment(transition):
	if transition[0] == TRANSITION_DEF:
		return transition[-2]
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def getTransitionModifiers(transition):
	if transition[0] == TRANSITION_DEF:
		return transition[1][1:]
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def getTransitionPort(transition):
	if transition[0] == TRANSITION_DEF:
		if len(transition[4][1]) > 1:
			return transition[4][1][0]
		else:
			return None
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def getTransitionMessageClass(transition):
	if transition[0] == TRANSITION_DEF:
		if len(transition[4][1]) > 1:
			return transition[4][1][1]
		else:
			return None
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def getTransitionTargets(transition):
	if transition[0] == TRANSITION_DEF:
		return transition[3]
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def isCompoundTarget(target):
	return target[0] == COMPOUND_TGT

def isBasicTarget(target):
	return target[0] == BASIC_TGT

def getCompoundTargets(target):
	if target[0] == COMPOUND_TGT:
		return target[1]
	else:
		raise AbstractMachineException( "Not a compound transition target %s" % indent(target))

def getSourceConfiguration(transition):
	if transition[0] == TRANSITION_DEF:
		return transition[2][1]
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def getGuardedTargetGuard(target):
	if target[0] == GUARDED_TGT:
		return target[1][1]
	else:
		raise AbstractMachineException( "Not a transition target %s" % indent(target))

def getGuardedTargetTarget(target):
	if target[0] == GUARDED_TGT:
		return target[2]
	else:
		raise AbstractMachineException( "Not a transition target %s" % indent(target))

def getTargetAction(target):
	if target[0] == BASIC_TGT:
		return target[1][1]
	else:
		raise AbstractMachineException( "Not a basic transition target %s" % indent(target))

def getTargetConfiguration(target):
	if target[0] == BASIC_TGT:
		return target[2][1]
	else:
		raise AbstractMachineException( "Not a basic transition target %s" % indent(target))

def setSourceConfiguration(transition, config):
	if transition[0] == TRANSITION_DEF:
		transition[2] = [ SRC_CONFIG ] + [ config ]
	else:
		raise AbstractMachineException( "Not a transition %s" % indent(transition))

def setTargetConfiguration(target, config):
	if target[0] == BASIC_TGT:
		target[2] = [ TGT_CONFIG ] + [ config ]
	else:
		raise AbstractMachineException( "Not a basic transition target %s" % indent(target))

def getConfigurationTreeType(config):
	return config[0]

# Return state path list from machine in which transition associated
# with config is defined to submachine referenced by root of specified
# config tree.
def getConfigurationTreeAncestorStatePath(config):
	return config[-2]

# Return parent state name of submachine referenced by root
# of specified config tree, or return empty string if root machine
# referenced by config tree.
def getConfigurationTreeParentStateName(config):
	path = getConfigurationTreeAncestorStatePath(config)
	if len(path) == 0:
		return ""
	else:
		return path[-1]

# Returns one of [ MACHINE_DEF, EXTERNAL_SUBMACHINE, INNER_SUBMACHINE,
# NO_SUBMACHINE, REFLECT_SUBMACHINE ] indicating the type (sub)machine
# referenced by root of the specified config tree.
def getConfigurationTreeMachineReferenceType(config):
	return config[-1][0]

def getSubconfigurationTree(config):
	if getConfigurationTreeType(config) in [ MULTI_CONFIG, DYNAMIC_CONFIG ]:
		return config[2]
	else:
		return None

def getMultiSubconfigurationIndices(config):
	if getConfigurationTreeType(config) == MULTI_CONFIG:
		return config[4]
	else:
		raise AbstractMachineException( "Not a multi configuration %s" % config)

def getMultiSubconfigurationMachineBindings(config):
	if getConfigurationTreeType(config) == MULTI_CONFIG:
		return config[3]
	else:
		raise AbstractMachineException( "Not a multi configuration %s" % config)

# Return machine array subconfigs for specified dynamic config.
def getDynamicSubconfigurations(config):
	if getConfigurationTreeType(config) == DYNAMIC_CONFIG:
		return config[2]
	else:
		raise AbstractMachineException( "Not a dynamic configuration %s" % config)

# Return machine array index accessors for specified dynamic config.
def getDynamicSubconfigurationIndexAccessors(config):
	if getConfigurationTreeType(config) == DYNAMIC_CONFIG:
		return config[1]
	else:
		raise AbstractMachineException( "Not a dynamic configuration %s" % config)

def getDynamicSubconfigurationIndices(config):
	if getConfigurationTreeType(config) == DYNAMIC_CONFIG:
		return config[3]
	else:
		raise AbstractMachineException( "Not a dynamic configuration %s" % config)

def getDynamicSubconfigurationMachineBindings(config):
	if getConfigurationTreeType(config) == DYNAMIC_CONFIG:
		return config[4]
	else:
		raise AbstractMachineException( "Not a dynamic configuration %s" % config)

# Return machine array index accesor type for specified array index.
def getDynamicSubconfigurationIndexAccessorType(index):
	if index == []:
		return None
	else:
		return index[0]

# Return machine array index accessor expression for specified array
# index.
def getDynamicSubconfigurationIndexAccessorExpression(index):
	if index == []:
		return None
	else:
		return index[1]

# Return current state index for specified config.
def getConfigurationIndex(config):
	if getConfigurationTreeType(config) == MULTI_CONFIG:
		return config[1]
	else:
		return -1

def getConfigurationTree(config):
	return config[0]

def toConfigurationImage(config):
	pathImages = []
	for path in config:
		pathImages = pathImages + [ toConfigurationPathImage(path) ]
	return "[" + string.joinfields(pathImages, ", ") + "]"

def toConfigurationPathImage(configPath):
	return string.joinfields(map(toConfigurationNodeImage, configPath), ".")	

def toConfigurationNodeImage(configNode):
	index = ""
	if isMachineBindingConfigurationNode(configNode):
		index = index + ":...:"
	if isMachineArrayIndexedConfigurationNode(configNode):
		indexType = getConfigurationNodeMachineArrayIndexType(configNode)
		if indexType == SET_INDEX:
			index = index + "[?...]"
		elif indexType == GET_INDEX:
			index = index + "[...]"
		elif indexType == EMPTY_INDEX:
			index = index + "[]"
	return "%s%s" % (getConfigurationNodeName(configNode), index)

def getConfigurationImage(config):
	return config[1]

def getConfigurationNodeName(configNode):
	return configNode[0]

def getConfigurationNodeMachineArrayIndex(configNode):
	return configNode[1]

def getConfigurationNodeMachineArrayIndexType(configNode):
	return configNode[1][0]

def isMachineArrayIndexedConfigurationNode(configNode):
	return configNode[1] != []

def getConfigurationNodeMachineBinding(configNode):
	if len(configNode) == 3:
		# assume we are dealing with a target reference
		return configNode[2]
	else:
		# assume we are dealing with a source reference (which doesn't
		# include machine bindings)
		return []

def isMachineBindingConfigurationNode(configNode):
	return len(configNode) == 3 and configNode[2] != []

def isPseudoState(stateIdentifier):
	return stateIdentifier in [ DEEP_HISTORY,
								TERMINAL,
								NEW,
								DEFAULT_INITIAL,
								ANY ]

def getMachine(compilationUnit):
	if compilationUnit[0] == COMPILATION_UNIT:
		# return machine definition from a compilation unit
		return compilationUnit[3]
	else:
		raise AbstractMachineException( "Not a compilation unit: %s" % indent(compilationUnit))

def getSubmachine(state):
	if state[0] == STATE_DEF:
		# return submachine definition from a state definition
		return state[-1]
	else:
		raise AbstractMachineException( "Not a state: %s" % indent(state))

def setSubmachine(state, submachine):
	if state[0] == STATE_DEF:
		# return submachine definition from a state definition
		state[-1] = submachine
	else:
		raise AbstractMachineException( "Not a state: %s" % indent(state))

def isTopMachine(machine):
	return not machine == [] and machine[0] == MACHINE_DEF

def isSubmachine(machine):
	return machine == [] or machine[0] in [ EXTERNAL_SUBMACHINE, VARIABLE_SUBMACHINE,
											INNER_SUBMACHINE, REFLECT_SUBMACHINE ]

def getMachineName(compilationUnit):
	if len(compilationUnit) > 0 and compilationUnit[0] == COMPILATION_UNIT:
		return compilationUnit[3][3]
	else:
		raise AbstractMachineException( "Not a compilation unit: %s" % indent(compilationUnit))

def getImports(compilationUnit):
	if len(compilationUnit) > 0 and compilationUnit[0] == COMPILATION_UNIT:
		return compilationUnit[2][1:]
	else:
		raise AbstractMachineException( "Not a compilation unit: %s" % indent(compilationUnit))

def getImportPackage(importStruct):
	if importStruct[0] == IMPORT_DEF:
		return importStruct[1]
	else:
		raise AbstractMachineException( "Not an import: %s" % indent(importStruct))

def getImportModifiers(importStruct):
	if importStruct[0] == IMPORT_DEF:
		return importStruct[2][1:]
	else:
		raise AbstractMachineException( "Not an import: %s" % indent(importStruct))

def getImportLineColumn(importStruct):
	if importStruct[0] == IMPORT_DEF:
		return (importStruct[-1][1], importStruct[-1][2])
	else:
		raise AbstractMachineException( "Not an import: %s" % indent(importStruct))

def getPackage(compilationUnit):
	if len(compilationUnit) > 0 and compilationUnit[0] == COMPILATION_UNIT:
		return compilationUnit[1][1]
	else:
		raise AbstractMachineException( "Not a compilation unit: %s" % indent(compilationUnit))

def getPackageLineColumn(compilationUnit):
	if len(compilationUnit) > 0 and compilationUnit[0] == COMPILATION_UNIT:
		return (compilationUnit[1][-1][1], compilationUnit[1][-1][2])
	else:
		raise AbstractMachineException( "Not a compilation unit: %s" % indent(compilationUnit))

def getSubmachineType(submachine):
	if submachine == []:
		return NO_SUBMACHINE
	elif submachine[0] in [ EXTERNAL_SUBMACHINE, VARIABLE_SUBMACHINE, INNER_SUBMACHINE, REFLECT_SUBMACHINE ]:
		return submachine[0]
	else:
		raise AbstractMachineException( "Not a submachine: %s" % indent(submachine))

# return unqualified machine class name
def getReflectSubmachineClassName(submachine):
	if len(submachine) > 0 and submachine[0] == REFLECT_SUBMACHINE:
		return submachine[2]
	else:
		raise AbstractMachineException( "Not a 'reflect' submachine: %s" % indent(submachine))

def getReflectSubmachineArguments(submachine):
	if len(submachine) > 0 and submachine[0] == REFLECT_SUBMACHINE:
		return submachine[3]
	else:
		raise AbstractMachineException( "Not a 'reflect' submachine: %s" % indent(submachine))

# return unqualified machine class name
def getExternalSubmachineClassName(submachine):
	if len(submachine) > 0 and submachine[0] == EXTERNAL_SUBMACHINE:
		if submachine[2][-4:] == ".ech":
			# if machine name is a filepath then extract name from
			# path
			return string.split(submachine[2], os.sep)[-1][:-4]
		else:
			return submachine[2]
	else:
		raise AbstractMachineException( "Not an external submachine: %s" % indent(submachine))

# return unqualified machine class name
def getVariableSubmachineClassName(submachine):
	if len(submachine) > 0 and submachine[0] == VARIABLE_SUBMACHINE:
		if submachine[2][-4:] == ".ech":
			# if machine name is a filepath then extract name from
			# path
			return string.split(submachine[2], os.sep)[-1][:-4]
		else:
			return submachine[2]
	else:
		raise AbstractMachineException( "Not a variable submachine: %s" % indent(submachine))

def getSubmachineFilePath(submachine):
	if len(submachine) > 0:
		if submachine[0] == EXTERNAL_SUBMACHINE:
			return getExternalSubmachineFilePath(submachine)
		elif submachine[0] == VARIABLE_SUBMACHINE:
			return getVariableSubmachineFilePath(submachine)
		else:
			raise AbstractMachineException( "Not an externall defined submachine: %s" % indent(submachine))
	else:
		raise AbstractMachineException( "Not a submachine: %s" % indent(submachine))

def getExternalSubmachineFilePath(submachine):
	if len(submachine) > 0 and submachine[0] == EXTERNAL_SUBMACHINE:
		if submachine[2][-4:] == ".ech":
			return submachine[2]
		else:
			raise AbstractMachineException( "No file path defined for submachine: %s" % indent(submachine[2]))
	else:
		raise AbstractMachineException( "Not an external submachine: %s" % indent(submachine))

def getVariableSubmachineFilePath(submachine):
	if len(submachine) > 0 and submachine[0] == VARIABLE_SUBMACHINE:
		if submachine[2][-4:] == ".ech":
			return submachine[2]
		else:
			raise AbstractMachineException( "No file path defined for submachine: %s" % indent(submachine[2]))
	else:
		raise AbstractMachineException( "Not a variable submachine: %s" % indent(submachine))

def setExternalSubmachineClassName(submachine, name):
	if len(submachine) > 0 and submachine[0] == EXTERNAL_SUBMACHINE:
		submachine[2] = name
	else:
		raise AbstractMachineException( "Not an external submachine: %s" % indent(submachine))

def setVariableSubmachineClassName(submachine, name):
	if len(submachine) > 0 and submachine[0] == VARIABLE_SUBMACHINE:
		submachine[2] = name
	else:
		raise AbstractMachineException( "Not a variable submachine: %s" % indent(submachine))

def getExternalSubmachineArguments(submachine):
	if len(submachine) > 0 and submachine[0] == EXTERNAL_SUBMACHINE:
		# return ELIST value
		return submachine[3][1]
	else:
		raise AbstractMachineException( "Not an external submachine: %s" % indent(submachine))

def getMachineModifiers(machine):
	if len(machine) > 0:
		if machine[0] == MACHINE_DEF:
			return machine[2][1:]
		elif machine[0] in [ VARIABLE_SUBMACHINE, EXTERNAL_SUBMACHINE, INNER_SUBMACHINE, REFLECT_SUBMACHINE ]:
			return machine[1][1:]
		else:
			raise AbstractMachineException( "No machine modifiers defined for %s" % indent(machine))
	else:
		raise AbstractMachineException( "Not a machine: %s" % indent(machine))

def setMachineModifiers(machine, modifiers):
	if len(machine) > 0:
		if machine[0] == MACHINE_DEF:
			machine[2] = [ MACHINE_MODIFIERS ] + modifiers
		elif machine[0] in [ VARIABLE_SUBMACHINE, EXTERNAL_SUBMACHINE, INNER_SUBMACHINE, REFLECT_SUBMACHINE ]:
			machine[1] = [ MACHINE_MODIFIERS ] + modifiers
		else:
			raise AbstractMachineException( "No machine modifiers defined for %s" % indent(machine))
	else:
		raise AbstractMachineException( "Not a machine: %s" % indent(machine))

def getDynamicMachineModifier(machine):
	for mod in getMachineModifiers(machine):
		# "shared_dynamic" no longer used - all dynamic machines are
		# "dynamic"
		if mod[0] in ["dynamic", "shared_dynamic"]:
			return mod
	return [None, -1]

def isTransitionMachine(machine):
	return not isDynamicMachine(machine) and not isBasicMachine(machine)

def isDynamicMachine(machine):
	# top-level machines can't be dynamic
	return not isTopMachine(machine) and \
		   getSubmachineType(machine) != NO_SUBMACHINE and \
		   getDynamicMachineModifier(machine)[0] != None

def getDynamicSubmachine(machine):
	if isDynamicMachine(machine):
		# return submachine that is wrapped by specified
		# (post-processed) dynamic machine
		return getSubmachine(getStates(machine)[0])
	else:
		raise AbstractMachineException( "Not a dynamic machine %s" % indent(machine))

def getDynamicSubmachineType(machine):
	if isDynamicMachine(machine):
		# get submachine wrapped by specfied dynamic machine
		submachine = getSubmachine(getStates(machine)[0])
		return getSubmachineType(submachine)
	else:
		raise AbstractMachineException( "Not a dynamic machine %s" % indent(machine))

def getDynamicSubmachineClass(machine, machineName):
	if isDynamicMachine(machine):
		# get submachine wrapped by specfied dynamic machine
		submachine = getSubmachine(getStates(machine)[0])
		type = getDynamicSubmachineType(machine)
		if type == REFLECT_SUBMACHINE:
			return "TransitionMachine"
		elif type == NO_SUBMACHINE:
			return "BasicMachine"
		elif type == EXTERNAL_SUBMACHINE:
			return getExternalSubmachineClassName(submachine)
		elif type == INNER_SUBMACHINE:
			return machineName
		else:
			raise AbstractMachineException( "Unknown dynamic submachine type %s for dynamic machine %s" \
				  % (type, indent(machine)))
	else:
		raise AbstractMachineException( "Not a dynamic machine %s" % indent(machine))

# deprecated - should use isTransitionMachine() - returns true if user
# declared machine to be 'concurrent' but will return false if all
# states are explicitly declared as 'concurrent'
def isAndMachine(machine):
	return [ "concurrent" ] in getMachineModifiers(machine)

# deprecated - should use isTransitionMachine() - define an or-machine
# to be a transition machine with at least one state that isn't
# declared to be an and-state
def isOrMachine(machine):
	if not isAndMachine(machine) and not isDynamicMachine(machine) and not isBasicMachine(machine):
		for state in getStates(machine):
			if not isAndState(state):
				return True
	return False

def isBasicMachine(machine):
	return not isTopMachine(machine) and getSubmachineType(machine) == NO_SUBMACHINE

def isTopMachine(machine):
	return len(machine) > 0 and machine[0] == MACHINE_DEF 

def getMachineModifierType(modifier):
	if type(modifier) == types.ListType and len(modifier) > 0:
		return modifier[0]
	else:
		raise AbstractMachineException( "Not a machine modifier: %s" % indent(modifier))

def getMachineBody(machine):
	if len(machine) > 0 and machine[0] in [ MACHINE_DEF, INNER_SUBMACHINE ]:
		return  machine[-1]
	else:
		raise AbstractMachineException( "Machine body not defined for machine: %s" % indent(machine))

def setMachineBody(machine, body):
	if len(machine) > 0 and machine[0] in [ MACHINE_DEF, INNER_SUBMACHINE ]:
		machine[-1] = body
	else:
		raise AbstractMachineException( "Machine body not defined for machine: %s" % indent(machine))

def getMachineAccessModifiers(machine):
	if len(machine) > 0 and machine[0] == MACHINE_DEF:
		return machine[1][1:]
	else:
		raise AbstractMachineException( "Not a machine: %s" % indent(machine))

# Returns True is accessingMachine can access item with specified
# accessedModifiers declared in accessedMachine, otherwise returns
# False. Here, accessedMachine and accessingMachine are fully
# qualified machine names i.e. the machine name appended to the
# machine's package name e.g. '[ "com", "att", "blah", "MachineName" ]'.
def isAccessible(accessedModifiers, accessedMachine, accessingMachine):
	if "private" in accessedModifiers:
		if accessedMachine == accessingMachine:
			return True
		else:
			return False
	elif "public" in accessedModifiers:
		return True
	elif "protected" in accessedModifiers:
		if accessedMachine == accessingMachine:
			return True
		else:
			return False
	else:
		# no explicit access specified so default 'package' access
		# applies
		if accessedMachine[:-1] == accessingMachine[:-1]:
			return True
		else:
			return False

# Make abstract machine more readable. Substitutes token identifiers
# with their string equivalents (as defined in echarts_w._tokenNames)
# for first element of every sub-list in specified list.
def tokenIdToString(list):
	if type(list) == types.ListType:
		# deal with first list item
		if list == []:
			return list
		elif type(list[0]) == types.IntType and list[0] < len(echarts_w._tokenNames):
			# first item looks like a token indentifier so
			# translate to a string
			firstItem = echarts_w._tokenNames[list[0]]
		elif type(list[0]) == types.ListType:
			# first item a list so recurse to first element
			firstItem = tokenIdToString(list[0])
		else:
			# first element not a list or a token identifier
			firstItem = list[0]
		# now deal with any remaining list items
		newList = [ firstItem ]
		for item in list[1:]:
			# recurse to next sibling
			newList = newList + [ tokenIdToString(item) ] 
		return newList
	else:
		return list

# Returns string representing "pretty-printed" abstract machine. Token
# id's are substituted with strings and submachine definitions are
# indented with tabs. See tokenIdToString() for comments.
def indent(list):
	return _indent(list, 0)

def _indent(list, indentLevel):
	if type(list) == types.ListType:
		if list == []:
			return "[]"
		elif type(list[0]) == types.IntType and list[0] < len(echarts_w._tokenNames):
			if list[0] in [INNER_SUBMACHINE, EXTERNAL_SUBMACHINE]:
				indentLevel = indentLevel + 1
				string = "[" + echarts_w._tokenNames[list[0]]
			elif list[0] in [STATE_DEF, TRANSITION_DEF, CONSTRUCTOR_DEF]:
				string = "\n" + indentLevel * "\t" + "[" + echarts_w._tokenNames[list[0]]
			elif list[0] in [STATES, TRANSITIONS, HOST, CONSTRUCTORS]:
				string = "\n" + indentLevel * "\t" + "[" + echarts_w._tokenNames[list[0]]
			else:
				string = "[" + echarts_w._tokenNames[list[0]]
		elif type(list[0]) == types.ListType:
			string = "[" + _indent(list[0], indentLevel)
		else:
			if type(list[0]) == types.StringType:
				string = "[\"%s\"" % list[0]
			else:
				string = "[%s" % list[0]
		for item in list[1:]:
			string = string + ", " + _indent(item, indentLevel)
		return string + "]"
	else:
		if type(list) == types.StringType:
			return "\"%s\"" % list
		else:
			return "%s" % list

# Global variable whose value is token stream for most recently parsed
# .ech file.
stream = 1
def setStream(s):
	import AbstractMachine
	AbstractMachine.stream = s

# Iterates through list of tokens, translating each one to its text
# representation. Called by echarts_w.py (the AST builder).
def getText(tokens):
	rv = []
	for t in tokens:
		# make sure list item is a token
		if type(t) == antlr.CommonASTWithHiddenTokens:
			rv = rv + [ t.getText() ]
		elif type(t) == types.ListType:
			# recursively invoke if list item is a list
			rv = rv + [ getText(t) ]
		else:
			# pass through non-tokens
			rv = rv + [ t ] 
	return rv

# Returns line and column number pair associated with first token in
# the specified list of tokens. Returns line = column = 1 if no tokens
# found. Called by echarts_w.py (the AST builder).
def getLineColumn(tokens):
	for t in tokens:
		if type(t) == antlr.CommonASTWithHiddenTokens:
			# list item is a token 
			return [echarts_w.LINECOLUMN, t.line, t.column]
		elif type(t) == types.ListType:
			# recursively invoke if item is a list
			return getLineColumn(t)
	return [echarts_w.LINECOLUMN, 1, 1 ]

# Iterates through list of tokens until encountering first hidden
# comment. Returns empty string if no comment encountered. Called by
# echarts_w.py (the AST builder).
def getComment(tokens):
	h = None
	rv = ''
	for t in tokens:
		if type(t) == antlr.CommonASTWithHiddenTokens:
			# list item is a token 
			h = stream.getHiddenBefore(t)
			if not h == None:
				rv = h.getText()
		elif type(t) == types.ListType:
			# recursively invoke if item is a list
			rv = getComment(t)
		if not rv == '':
			break
	return rv

# An abstract machine is a list that reflects the structure returned
# by the ECharts AST walker (see echarts_w.g). We operate on this list
# rather than on the AST itself because the list is easier to work
# with. This class is used to parse an echarts file ("compilation
# unit") and (recursively) resolve any dependencies it might have on
# other machines. Optionally, the postProcess() method may be called
# to post-process the machine in preparation for back-end translation
# to a target language.

class AbstractMachine:

	# instance variable - absolute file path for this machine - value
	# set in the constructor
	absoluteMachineFilePath = ""

	# instance variable - used to locate other echarts machine files
	# for linking with this machine - value set in the constructor
	echartsPaths = ""

	# instance variable - map that contains entries for all machine
	# files found in directories whose paths are constructed from a
	# machine's package name and import list - maps an unqualified
	# machine name to a dict that maps qualified machine names to a
	# dict that maps file paths to None (only this map's keys matter
	# here since it is being used to represent a set) - note that
	# until a file is parsed, it is not known if a file actually
	# defines a machine with the specified qualified machine name -
	# for this reason, an entry in this dict is not necessarily valid
	# until there is a compilation unit associated with the file in
	# the compilationUnitDict (indicating that the file has been
	# parsed) - see comments for updateImportEntries() and
	# getSubmachineCompilationUnit() for more information
	importDict = {}

	# class variable - map containing the (un)linked compilation units
	# of all machines parsed while creating AbstractMachine instances
	# - maps machine's absolute file path to the compilation unit
	# obtained by parsing the machine's file - when the compilation
	# unit is linked, the side effect is to update the dict entry from
	# an unlinked to a linked compilation unit
	compilationUnitDict = {}

	# class variable - maps a machine's absolute file path to a map of
	# AbstractMachine instances representing the machines upon which
	# the machine is immediately dependent - the latter maps are used
	# to represent sets of machines - as such, each such map keys is a
	# machine absolute file path and its value is a machine instance
	# for that file path - former map value is None when the
	# dependencies are being computed during the linking process
	dependencyDict = {}

	# class variable - maps a machine's absolute file path to a pair
	# (compilationUnit, pass) where compilationUnit is the machine's
	# post-processed compilation unit and pass is an integer
	# indicating how many post-processing passes have occurred/are
	# occurring for the machine so far - if the machine is in the
	# process of being post-processed then an entry's value is None
	postProcessedDict = {}

	def __init__(self, machineFilename, echartsPaths):
		self.absoluteMachineFilePath = os.path.abspath(machineFilename)
		self.echartsPaths = echartsPaths
		try:
			AbstractMachine.dependencyDict[self.absoluteMachineFilePath]
			#  entry for this filename already in dependency
			#  dict so nothing more to do
		except KeyError:
			# first time we've encountered this file so link it
			self.linkMachine()

	def getCompilationUnitForFile(self, filename):
		try:
			# check to see if we've already parsed this file 
			return AbstractMachine.compilationUnitDict[filename]
		except KeyError:
			# parse this file for the first time and enter it in the
			# compilation unit dict
			try:
				compilationUnit = self.parse(filename)
			except antlr.ANTLRException, message:
				raise AbstractMachineException( "%s: error: parse error: %s" % (filename, message))
			machineNameList = string.split(filename, os.sep)
			machineName = machineNameList[-1][:-4]
			if getMachineName(compilationUnit) != machineName:
				raise AbstractMachineException( "%s: error: does not define machine named %s" % (filename, machineName))
			AbstractMachine.compilationUnitDict[filename] = compilationUnit
			return compilationUnit
		
	# Returns unlinked compilation unit list constructed by ast's
	# walker for specified machine filename.
	def parse(self, filename):
		machineFile = None
		try:
			machineFile = open(filename, 'r')
		except IOError, message:
			raise AbstractMachineException( "error: cannot open file " + filename + ": %s" % message)
		lexer = echarts_l.Lexer(machineFile) 
		lexer.setTokenObjectClass(antlr.CommonHiddenStreamToken)
		stream = antlr.TokenStreamHiddenTokenFilter(lexer);
		setStream(stream)
		stream.hide(echarts_p.ML_COMMENT);
		parser = echarts_p.Parser(stream)
		parser.setFilename(os.path.abspath(filename))
		parser.setASTNodeClass(antlr.CommonASTWithHiddenTokens)
		# parse the file
		try:
			parser.compilationUnit()
		except antlr.ANTLRException, message:
			raise AbstractMachineException( "%s: error: parse error(s): %s" % (filename, message))
		if parser.errorsWereReported():
			raise AbstractMachineException( "%s: error: parse error(s)" % filename)
		ast = parser.getAST()
		if not ast:
			raise AbstractMachineException( "%s: error: no AST generated" % filename)
		walker = echarts_w.Walker()
		return walker.compilationUnit(ast)

	def linkMachine(self):
		compilationUnit = self.getCompilationUnitForFile(self.absoluteMachineFilePath)
		qualifiedMachineName = string.joinfields(getPackage(compilationUnit) + \
												 [ getMachineName(compilationUnit) ], ".")
		# create None entry in dependency dict to indicate that
		# machine is being linked
		AbstractMachine.dependencyDict[self.absoluteMachineFilePath] = None
		# initialize machine's machineFileDict with imports
		self.initializeImports(getPackage(compilationUnit),
							   getImports(compilationUnit))
		# link the compilation unit
		dependencies = {}
		try:
			self.linkSubmachines(getMachine(compilationUnit), dependencies)
		except AbstractMachineException, message:
			raise AbstractMachineException("%s: error: %s" % (self.absoluteMachineFilePath, message))
		# update entry in dependency dict to include linked
		# compilation unit
		AbstractMachine.dependencyDict[self.absoluteMachineFilePath] = dependencies

	# Update import dict for each implicitly/explicitly imported
	# machine.
	def initializeImports(self, package, imports):
		# update implicitly imported machines
		for echartsPath in string.split(self.echartsPaths, os.pathsep):
			self.updateImportEntries(echartsPath, package + [ "*" ])
		# update explicitly imported machines
		for imported in imports:
			importAsList = getImportPackage(imported)
			for echartsPath in string.split(self.echartsPaths, os.pathsep):
				self.updateImportEntries(echartsPath, importAsList)

	# Update imports dict for files found on the paths constructed
	# from the specified echartsPath and qualifiedMachineName. If an
	# entry already exists for specified file path then no additional
	# entry is created. The parm 'echartsPath' is directory path from
	# echartsPaths, and 'qualifiedMachineName' is a list representing a
	# machine identifier, or a 'starred' machine identifier where the
	# star represents any machine name. Note that since we don't
	# examine package declarations and machine names in files, then it
	# is possible that the aulified machine name we associate with the
	# file is incorrect. However, any existing incorrect entries will
	# gradually be pruned from the import dict as a side-effect of the
	# getLinkedCompilationUnit() method.
	def updateImportEntries(self, echartsPath, qualifiedMachineName):
		if qualifiedMachineName[-1] == '*':
			# refers to any machine in specified package
			partialDirPath = string.joinfields(qualifiedMachineName[:-1], os.sep)
			dirPath = string.joinfields([ echartsPath ] +  [ partialDirPath ], os.sep)
			if os.path.isdir(dirPath):
				for filename in os.listdir(dirPath):
					if filename[-4:] == ".ech":
						self.updateImportEntry(qualifiedMachineName[:-1] + [ filename[:-4] ],
											   dirPath + os.sep + filename)
		else:
			# refers to particular machine in specified package
			filePath = echartsPath + os.sep + \
					   string.joinfields(qualifiedMachineName, os.sep) + ".ech"
			if os.path.isfile(filePath):
				self.updateImportEntry(qualifiedMachineName, filePath)

	# Updates importDict with entry for specified qualifiedMachineName
	# and filePath.
	def updateImportEntry(self, qualifiedMachineName, filePath):
		dottedMachineName = string.joinfields(qualifiedMachineName, ".")
		absoluteFilePath = os.path.abspath(filePath)
		try:
			machineDict = self.importDict[qualifiedMachineName[-1]]
			# entry exists for this machine name try to add file path
			# to dict for the machine
			try:
				fileDict = machineDict[dottedMachineName]
				# entry exists for this machine so add file path to
				# dict for qualified machine name if entry not already
				# present for the file path
				try:
					compilationUnit = fileDict[absoluteFilePath]
				except KeyError:
					fileDict[absoluteFilePath] = None
			except KeyError:
				# haven't encountered this machine before so add a new
				# dict for the machine with the file path as its entry
				machineDict[dottedMachineName] = {absoluteFilePath:None}
		except KeyError:
			# haven't encountered this machine name before so add a
			# new dict for the machine name with machine dict as its
			# entry
			self.importDict[qualifiedMachineName[-1]] = {dottedMachineName:{absoluteFilePath:None}}

	# Returns a new machine whose external submachine references are
	# replaced with fully-qualified machine references (if they
	# weren't already).
	def linkSubmachines(self, machine, dependencies):
		for state in getStates(machine):
			self.linkSubmachine(getSubmachine(state), dependencies)

	# Returns a new submachine whose external submachine references
	# are replaced with fully qualified machine references (if they
	# weren't already). Side-effect is to populate the abstract
	# machine dict with compilation units of descendant machines.
	def linkSubmachine(self, submachine, dependencies):
		if getSubmachineType(submachine) == INNER_SUBMACHINE:
			# inner submachine
			self.linkSubmachines(submachine, dependencies)
		elif getSubmachineType(submachine) == EXTERNAL_SUBMACHINE:
			# submachine is externally defined (and not a 'reflect'
			# machine) so get its fully qualified machine name
			submachineFilePath = self.getMachineFilePath(getExternalSubmachineClassName(submachine))
			# substitute submachine name with machine's absolute file path
			setExternalSubmachineClassName(submachine, submachineFilePath)
			# now link submachine (if it hasn't already been linked)
			linkedSubmachine = AbstractMachine(submachineFilePath, self.echartsPaths)
			# returns submachine as a dependency
			dependencies[linkedSubmachine.absoluteMachineFilePath] = linkedSubmachine
		elif getSubmachineType(submachine) == VARIABLE_SUBMACHINE:
			# submachine is a variable submachine so get its fully
			# qualified machine name
			submachineFilePath = self.getMachineFilePath(getVariableSubmachineClassName(submachine))
			# substitute submachine name with machine's absolute file path
			setVariableSubmachineClassName(submachine, submachineFilePath)
			# now link submachine (if it hasn't already been linked)
			linkedSubmachine = AbstractMachine(submachineFilePath, self.echartsPaths)
			# returns submachine as a dependency
			dependencies[linkedSubmachine.absoluteMachineFilePath] = linkedSubmachine
		else:
			# no submachine so no linking necessary
			return []

	# Returns absolute machine file path for machine whose qualified
	# name matches the specified submachine name. Side-effect is that
	# importDict is pruned of any extraneous or invalid entries that
	# are encountered during search for a compilation unit.
	def getMachineFilePath(self, submachineName):
		dottedSubmachineName = string.joinfields(submachineName, ".")
		# looking for matching name in import dict keys
		try:
			machineDict = self.importDict[submachineName[-1]]
		except KeyError:
			raise AbstractMachineException( "unable to locate ECharts file defining machine: " + 
				  dottedSubmachineName )
		nameKeys = self.getMatchingMachineNameKeys(submachineName, machineDict)
		for nameKey in nameKeys:
			fileDict = machineDict[nameKey]
			for filePath in fileDict.keys():
				compilationUnit = self.getCompilationUnitForFile(filePath)
				# now that we've parsed the file, check to ensure that
				# the qualified machine name that we expect the file
				# to have (the nameKey the file is listed under in the
				# machineDict) is the same as the qualified machine
				# name that it declares itself to have
				fileMachineName = getMachineName(compilationUnit)
				filePackage = getPackage(compilationUnit)
				fileDottedMachineName = string.joinfields(filePackage + [ fileMachineName ], ".")
				if fileDottedMachineName == nameKey:
					# they're the same so delete any other
					# filepath entries from the dict
					machineDict[nameKey] = {filePath:None}
					# now return file path
					return filePath
				else:
					# not the same so remove this filepath entry from dict
					del fileDict[filePath]
					# now check if this file's compilation unit is
					# referenced by a different machineDict entry
					try:
						fileDict = machineDict[fileDottedMachineName]
						# there's an entry for this file's
						# qualified machine name so make it the
						# only entry in its file dict
						machineDict[fileDottedMachineName] = {filePath:None}
					except KeyError:
						# no import corresponds to this file so we
						# can ignore it
						pass
			# if we've made it to here, none of the file paths
			# have machines that match the qualified machine name
			# we expect them to have so delete the (now empty)
			# file dict for this keyName from the machine dict
			del machineDict[nameKey]
		# if we make it to here, there are no more matching name
		# keys so we're out of luck
		raise AbstractMachineException( "unable to locate ECharts file defining machine: " + 
			  dottedSubmachineName )

	# Returns list of qualified machine name keys in specified dict
	# that matches specified submachineName. 
	def getMatchingMachineNameKeys(self, submachineName, dict):
		matchingKeys = []
		if len(submachineName) == 1:
			# look for a match against name suffixes
			dottedSubmachineName = submachineName[0]
			for name in dict.keys():
				if string.split(name, ".")[-1] == dottedSubmachineName:
					matchingKeys = matchingKeys + [ name ]
		else:
			dottedSubmachineName = string.joinfields(submachineName, ".")
			# look for a exact match against complete name
			if dottedSubmachineName in dict.keys():
				matchingKeys = [ dottedSubmachineName ]
		return matchingKeys

	# Return list of absolute file paths of machines upon which this
	# machine *immediately* depends i.e. child external machines
	# referenced by this machine.
	def getDependencies(self):
		return AbstractMachine.dependencyDict[self.absoluteMachineFilePath].values()

	# Returns this machine's linked compilation unit.
	def getCompilationUnit(self):
		return AbstractMachine.compilationUnitDict[self.absoluteMachineFilePath]

	# Returns a pair (compilationUnit, completedPass) representing
	# this machine's post-processed compilation unit and the number of
	# post-processing passes it has undergone. Returns None if the
	# machine hasn't been post-processed yet.
	def getPostProcessedCompilationUnit(self):
		try:
			return AbstractMachine.postProcessedDict[self.absoluteMachineFilePath]
		except KeyError:
			return None

	# Post-processing the abstract machine consists of performing
	# semantic checks and transforming the machine for use by back-end
	# translators. Post-processing takes place in two
	# passes. Post-processed machines are added to the
	# postProcessedDict. A None value for a machine in this dict
	# indicates that the machine is in the process of being
	# post-processed. Returns post-processed compilation unit for this
	# machine.
	def postProcess(self):
		self.postProcessPass1()
		self.postProcessPass2()
		return self.getPostProcessedCompilationUnit()[0]

	def postProcessPass1(self):
		# check if this machine already post-processed
		if self.getPostProcessedCompilationUnit() == None:
			# it's not post-processed nor in the process of being
			# post-processed so indicate that we've initiated
			# processing pass 1 for this machine
			AbstractMachine.postProcessedDict[self.absoluteMachineFilePath] = (None, 1)
			# pass 1 of post processing
			compilationUnit = self.getCompilationUnit()
			self.checkMachineModifiers(compilationUnit)
			self.checkMachineConstructors(compilationUnit)
			self.checkStateAccessModifiers(getMachine(compilationUnit), [])
			(machineLine, machineColumn) = getMachineLineColumn(getMachine(compilationUnit))
			self.checkStateModifiers(getMachine(compilationUnit), machineLine, machineColumn, [])
			self.checkTransitionModifiers(getMachine(compilationUnit), [])
			self.checkStates(getMachine(compilationUnit), [])
			self.checkMachineAccessModifiers(getMachine(compilationUnit))
			self.checkExternalSubmachineAccess(getMachine(compilationUnit),
											   getMachineName(compilationUnit),
											   getPackage(compilationUnit), [])
			self.transformAndMachineStates(getMachine(compilationUnit))
			self.transformOrMachines(getMachine(compilationUnit))
			self.transformDynamicMachines(getMachine(compilationUnit))
			# update dict entry to indicate pass 1 complete
			AbstractMachine.postProcessedDict[self.absoluteMachineFilePath] = (compilationUnit, 1)
			# recurse to machines on which we depend
			for machine in self.getDependencies():
				machine.postProcessPass1()

	def postProcessPass2(self):
		try:
			(compilationUnit, completedPass) = self.getPostProcessedCompilationUnit()
			if (completedPass == 2):
				# we're already processing pass 2 or we've completed
				# processing pass 2 so do nothing
				return
			else:
				# indicate that we've initiated processing pass 2 for
				# this machine
				AbstractMachine.postProcessedDict[self.absoluteMachineFilePath] = (None, 2)
				# pass 2 of post-processing
				self.checkAndTransformStateConfigurations(getMachine(compilationUnit), [],
														  getMachineName(compilationUnit),
														  getPackage(compilationUnit))
				# update dict entry to indicate pass 2 complete
				AbstractMachine.postProcessedDict[self.absoluteMachineFilePath] = (compilationUnit, 2)
				# recurse to machines on which we depend
				for machine in self.getDependencies():
					machine.postProcessPass2()
		except KeyError:
			# shouldn't happen
			raise AbstractMachineException( "%s: error: invoking post-process pass 2 before pass 1" % 
				  self.absoluteMachineFilePath )

	# No duplicate mods.
	def checkMachineModifiers(self, compilationUnit):
		machine = getMachine(compilationUnit)
		# check top-level machine
		mods = []
		for mod in getMachineModifiers(machine):
			modType = getMachineModifierType(mod)
			if modType in mods:
				(line, column) = getMachineLineColumn(machine)
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: duplicate machine modifiers: %s" % \
					  (self.absoluteMachineFilePath, line, column, modType) )
			mods = mods + [ modType ]
		# now recursively check any submachines
		for state in getStates(machine):
			self.checkSubmachineModifiers(state, getStateName(state))

	# No duplicate mods, no concurrent external submachines.
	def checkSubmachineModifiers(self, state, stateName):
		submachine = getSubmachine(state)
		if getSubmachineType(submachine) == NO_SUBMACHINE:
			return
		else: 
			mods = []
			for mod in getMachineModifiers(submachine):
				modType = getMachineModifierType(mod)
				if modType in mods:
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s state %s: semantic error: duplicate inner submachine modifiers: %s" % \
						  (self.absoluteMachineFilePath, line, column, stateName, modType) )
				mods = mods + [ modType ]
			# recursively check inner submachines
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				for substate in getStates(submachine):
					self.checkSubmachineModifiers(substate,
												  string.joinfields([ stateName,
																	  getStateName(substate) ], "."))
			elif isAndMachine(submachine) and \
				 getSubmachineType(submachine) == EXTERNAL_SUBMACHINE:
				(line, column) = getStateLineColumn(state)
				raise AbstractMachineException( 
					  "%s:%s:%s state %s: semantic error: cannot declare external submachine to be concurrent" % \
					  (self.absoluteMachineFilePath, line, column, stateName) )

	# Ensure that constructors have same name as machine. Ensure that
	# constructor access modifiers are valid. Ensure that no
	# constructors defined for inner submachines. Note that we
	# don't check if a call to a constructor from an external machine
	# reference is valid because this depends on type-checking against
	# the constructor parameters, which can only be accomplished by
	# the host language compiler/interpreter.
	def checkMachineConstructors(self, compilationUnit):
		machineName = getMachineName(compilationUnit)
		# first ensure constructors and their access modifiers are valid
		for constructor in getConstructors(getMachine(compilationUnit)):
			if getConstructorName(constructor) != machineName:
				(line, column) = getConstructorLineColumn(constructor)
				raise AbstractMachineException( 
					  "%s:%s:%s semantic error: constructor name %s is not the same as machine name %s" % \
					  (self.absoluteMachineFilePath, line, column, getConstructorName(constructor), machineName) )
			mods = getConstructorAccessModifiers(constructor)
			for mod in mods:
				if mods.count(mod) > 1:
					(line, column) = getConstructorLineColumn(constructor)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: duplicate access modifiers for machine constructor: %s" % \
						  (self.absoluteMachineFilePath, line, column, mod) )
			if "abstract" in mods:
				(line, column) = getConstructorLineColumn(constructor)
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: \"abstract\" access modifier not permitted for machine constructor" % \
					  (self.absoluteMachineFilePath, line, column) )
			if "final" in mods:
				if len(mods) > 2:
					(line, column) = getConstructorLineColumn(constructor)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: illegal combination of access modifiers for machine constructor: %s" % \
						  (self.absoluteMachineFilePath, line, column, reduce(lambda y, z: "%s, " % y + z, mods)) )
			elif len(mods) > 1: 
				(line, column) = getConstructorLineColumn(constructor)
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: illegal combination of access modifiers for machine constructor: %s" % \
					  (self.absoluteMachineFilePath, line, column, reduce(lambda y, z: "%s, " % y + z, mods)) )
		# now check that anon submachine don't declare constructors
		self.checkSubmachineConstructors(getMachine(compilationUnit), [])

	def checkSubmachineConstructors(self, machine, ancestorStates):
		# recursively check any inner submachines defined by this
		# machine
		for state in getStates(machine):
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				if len(getConstructors(submachine)) != 0:
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: inner submachines cannot define constructors: %s" % \
						  (self.absoluteMachineFilePath, line, column, 
						   string.joinfields(ancestorStates + [ getStateName(state) ], ".")) )
				else:
					# recursively check this submachine's states
					self.checkSubmachineConstructors(submachine, ancestorStates + [ getStateName(state) ])

	# Check for valid state access modifiers.
	def checkStateAccessModifiers(self, machine, ancestorStates):
		for state in getStates(machine):
			mods = getStateAccessModifiers(state)
			for mod in mods:
				if mods.count(mod) > 1:
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: duplicate access modifiers for state %s: %s" % \
						  (self.absoluteMachineFilePath, line, column,
						   string.joinfields(ancestorStates + [ getStateName(state) ], "."),
						   mod) )
			if "abstract" in mods:
				(line, column) = getStateLineColumn(state)
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: \"abstract\" access modifier not permitted for state %s" % \
					  (self.absoluteMachineFilePath, line, column,
					   string.joinfields(ancestorStates + [ getStateName(state) ], ".")) )

			if "final" in mods:
				if len(mods) > 2:
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: illegal combination of access modifiers for state %s: %s" % \
						  (self.absoluteMachineFilePath, line, column,
						   string.joinfields(ancestorStates + [ getStateName(state) ], "."),
						   reduce(lambda y, z: "%s, " % y + z, mods)) )
			elif len(mods) > 1: 
				(line, column) = getStateLineColumn(state)
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: illegal combination of access modifiers for state %s: %s" % \
					  (self.absoluteMachineFilePath, line, column,
					   string.joinfields(ancestorStates + [ getStateName(state) ], "."),
					   reduce(lambda y, z: "%s, " % y + z, mods)) )
			# now recursively invoke for any anon submachines
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				self.checkStateAccessModifiers(submachine, ancestorStates + [ getStateName(state) ])

	# constport modifier only for message transitions.
	def checkTransitionModifiers(self, machine, ancestorStates):
		transitions = getTransitions(machine)
		for index in range(len(transitions)):
			if "constport" in getTransitionModifiers(transitions[index]) and isMessagelessTransition(transitions[index]):
				qualifiedStateName = string.joinfields(ancestorStates, ".")
				(line, column) = getTransitionLineColumn(transitions[index])
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: constport modifier cannot be applied to a messageless transition: transition %s in (sub)machine %s" % \
					  (self.absoluteMachineFilePath, line, column, index + 1, qualifiedStateName) )
		# recursively invoke for any anon submachines
		for state in getStates(machine):
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				self.checkTransitionModifiers(submachine, ancestorStates + [ getStateName(state) ])


	# No duplicates for a given state, warning if no init state for an
	# or-machine, no more than one init state per or-machine, exactly
	# zero init states for and-machine, no concurrent states declared
	# in a concurrent machine.
	def checkStateModifiers(self, machine, machineLine, machineColumn, ancestorStates):
		initialState = None
		for state in getStates(machine):
			submachine = getSubmachine(state)
			stateMods = getStateModifiers(state)
			qualifiedStateName = string.joinfields(ancestorStates + [ getStateName(state) ], ".")
			if "initial" in stateMods:
				if isAndMachine(machine):
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: concurrent machine cannot declare initial state: %s" % \
						  (self.absoluteMachineFilePath, line, column, qualifiedStateName) )
				if stateMods.count("initial") > 1:
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: duplicate initial state modifier for %s" % \
						  (self.absoluteMachineFilePath, line, column, qualifiedStateName) )
				if initialState != None:
					qualifiedInitialStateName = string.joinfields(ancestorStates + [ initialState ], ".")
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s semantic error: more than one initial state declared: %s, %s" % \
						  (self.absoluteMachineFilePath, line, column,
						   qualifiedInitialStateName,
						   qualifiedStateName) )
				initialState = getStateName(state)
			if "nonterminal" in stateMods:
				if stateMods.count("nonterminal") > 1:
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: duplicate nonterminal state modifier for %s" % \
						  (self.absoluteMachineFilePath, line, column, qualifiedStateName) )
			if "concurrent" in stateMods:
				if stateMods.count("concurrent") > 1:
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException(
						  "%s:%s:%s: semantic error: duplicate concurrent state modifier for %s" % \
						  (self.absoluteMachineFilePath, line, column, qualifiedStateName) )
			if isAndState(state) and isAndMachine(machine):
					(line, column) = getStateLineColumn(state)
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: redundant declaration of concurrent state %s in concurrent machine" % \
						  (self.absoluteMachineFilePath, line, column, qualifiedStateName) )
			# now check states of this state's submachine if it
			# defines an anon submachine
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				(line, column) = getStateLineColumn(state)
				self.checkStateModifiers(submachine, line, column, ancestorStates + [ getStateName(state) ])
		if isOrMachine(machine) and initialState == None:
			sys.stderr.write("%s:%s:%s: semantic warning: no initial state defined for (sub)machine %s\n" % \
							 (self.absoluteMachineFilePath, machineLine, machineColumn, string.joinfields(ancestorStates, ".")))

	# Ensure no inconsistent or duplicate modifiers for a machine.
	def checkMachineAccessModifiers(self, machine):
		mods = getMachineAccessModifiers(machine)
		(line, column) = getMachineLineColumn(machine)
		for mod in mods:
			if mods.count(mod) > 1:
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: duplicate access modifiers for machine: %s" % \
					  (self.absoluteMachineFilePath, line, column, mod) )
		if "private" in mods:
			raise AbstractMachineException(
				  "%s:%s:%s: semantic error: illegal access modifiers for machine: \"private\"" % \
				  (self.absoluteMachineFilePath, line, column) )
		if "protected" in mods:
			raise AbstractMachineException( 
				  "%s:%s:%s: semantic error: illegal access modifiers for machine: \"protected\"" % \
				  (self.absoluteMachineFilePath, line, column) )
		if "final" in mods and "abstract" in mods:
			raise AbstractMachineException( 
				  "%s:%s:%s: semantic error: illegal combination of access modifiers for machine: final and abstract" % \
				  (self.absoluteMachineFilePath, line, column) )
		if ("final" in mods or "abstract" in mods):
			if len(mods) > 2:
				raise AbstractMachineException( 
					  "%s:%s:%s: semantic error: illegal combination of access modifiers for machine: %s" % \
					  (self.absoluteMachineFilePath, line, column, reduce(lambda y, z: "%s, " % y + z, mods)) )
		elif len(mods) > 1: 
			raise AbstractMachineException( 
				  "%s:%s:%s: semantic error: illegal combination of access modifiers for machine: %s" % \
				  (self.absoluteMachineFilePath, line, column, reduce(lambda y, z: "%s, " % y + z, mods)) )

	# Ensure this machine can access referenced external submachines
	# by checking external submachine access modifiers.
	def checkExternalSubmachineAccess(self, machine, machineName, package, ancestorStates):
		for state in getStates(machine):
			(line, column) = getStateLineColumn(state)
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == EXTERNAL_SUBMACHINE:
				extCompilationUnit = self.getCompilationUnitForFile(getExternalSubmachineFilePath(submachine))
				accessedMachine = getPackage(extCompilationUnit) + [ getMachineName(extCompilationUnit) ]
				if not isAccessible(getMachineAccessModifiers(getMachine(extCompilationUnit)),
									accessedMachine,
									package + [ machineName ]):
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: illegal access of machine %s from state %s of (sub)machine %s" % \
						  (self.absoluteMachineFilePath, line, column, string.joinfields(accessedMachine, "."),
						   getStateName(state), string.joinfields(ancestorStates, ".")) )
				if "abstract" in getMachineAccessModifiers(getMachine(extCompilationUnit)):
					raise AbstractMachineException( 
						  "%s:%s:%s: semantic error: illegal to reference abstract machine %s from state %s of (sub)machine %s" % \
						  (self.absoluteMachineFilePath, line, column, getMachineName(extCompilationUnit),
						   getStateName(state), string.joinfields(ancestorStates, ".")) )
			elif getSubmachineType(submachine) == INNER_SUBMACHINE:
				# recurse to anon submachine
				self.checkExternalSubmachineAccess(submachine, machineName, package,
												   ancestorStates + [ getStateName(state) ])

	# Check for duplicate states.
	def checkStates(self, machine, ancestorStates):
		states = getStates(machine)
		statenames = map(getStateName, states)
		for state in states:
			if statenames.count(getStateName(state)) > 1:
				(line, column) = getStateLineColumn(state)
				raise AbstractMachineException( "%s:%s:%s: semantic error: duplicate states %s declared in (sub)machine %s" % 
					  (self.absoluteMachineFilePath, line, column, getStateName(state),
					   string.joinfields(ancestorStates + [ getStateName(state) ], ".")) )
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				self.checkStates(submachine, ancestorStates + [ getStateName(state) ])

	# Add 'concurrent' state modifier to and-machine states.
	def transformAndMachineStates(self, machine):
		states = getStates(machine)
		for state in states:
			if isAndMachine(machine):
				mods = getStateModifiers(state)
				mods.append('concurrent')
				setStateModifiers(state, mods)
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				self.transformAndMachineStates(submachine)

	# Re-orders state declarations in or-machines so that declared
	# initial state (if any) is first in list of declared states. We
	# assume semantic checks have been performed prior to calling this
	# method.
	def transformOrMachines(self, machine):
		states = getStates(machine)
		for state in states:
			# transform inner machines depth first then perform any
			# re-ordering to ensure we don't mess with iterator
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				self.transformOrMachines(submachine)
		initialState = getInitialState(machine)
		if initialState != None:
			initialStateIndex = states.index(initialState)
			if initialStateIndex != 0:
				# re-order states so that initial state first (if it
				# isn't already)
				del states[ initialStateIndex ]
				setStates(machine, [ initialState ] + states)

	# Recursively wraps submachines with non-zero array bounds in a
	# dynamic machine. A dynamic machine wrapper is simply an anon
	# machine with the same dyn machine modifier as the original
	# machine, and a single state "Dynamic[StateName]" that references
	# the original submachine, where "StateName" is parent state name
	# of the dynamic machine. We assume that semantics checks have
	# been performed prior to calling this method.
	def transformDynamicMachines(self, machine):
		for state in getStates(machine):
			submachine = getSubmachine(state)
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				self.transformDynamicMachines(submachine)
			if getSubmachineType(submachine) != NO_SUBMACHINE and getStateArrayBound(state) != 0:
				# dynamic submachine
				mod = [ "dynamic", getStateArrayBound(state) ]
				(line, column) = getStateLineColumn(state)
				dynMachine = [ INNER_SUBMACHINE,
					   [ MACHINE_MODIFIERS, mod ],
					   [ MACHINE_BODY, [ STATES,
										 [ STATE_DEF,
										   [ ACCESS_MODIFIERS, "private" ],
										   [ STATE_MODIFIERS ],
										   [ "Dynamic" + getStateName(state) ],
										   [ ENTRY ],
										   [ EXIT ],
										   "",
										   [LINECOLUMN, line, column],
										   submachine ],
										 ],
						 [ TRANSITIONS ], [ HOST ]]]
				setSubmachine(state, dynMachine)

	# Transforms linear (path-oriented) source and target state
	# configurations to branching (tree-oriented) configurations. Also
	# checks integrity of state configurations: referenced states
	# exist and are accessible, legal use of pstates, absence of state
	# reference conflicts. Note that we don't check if a call to a
	# constructor from an external machine reference is valid because
	# this depends on type-checking against the constructor
	# parameters, which can only be accomplished by the host language
	# compiler/interpreter. Linear target states are replaced with a
	# tuple [ branchConfig, linearConfigImage ] where branchConfig is
	# the transformed config, and linearConfigImage is a string
	# representation of the original config.
	def checkAndTransformStateConfigurations(self, machine, ancestorStates, machineName, package):
		transitions = getTransitions(machine)
		accessingMachine = package + [ machineName ]
		for transition in transitions:
			srcConfig = getConfigurationTree(getSourceConfiguration(transition))
			setSourceConfiguration(transition, [self.transformPathConfigurations(srcConfig,
																				 machine,
																				 ancestorStates,
																				 transition,
																				 "source",
																				 accessingMachine,
																				 accessingMachine),
														toConfigurationImage(srcConfig)])
			# have to perform same ops we performed for source config
			# on each tgt config in transition's targets
			self.checkAndTransformTargetStateConfigurations(machine, ancestorStates, machineName,
															package, transition,
															getCompoundTargets(getTransitionTargets(transition)))
		for state in getStates(machine):
			submachine = getSubmachine(state)
			# recursively  call for  any anon  submachines  defined in
			# this machine
			if getSubmachineType(submachine) == INNER_SUBMACHINE:
				if isDynamicMachine(submachine):
					# extract submachine wrapped by dynamic machine
					submachine = getSubmachine(getStates(submachine)[0])
					if getSubmachineType(submachine) == INNER_SUBMACHINE:
						# submachine wrapped by dynamic machine
						# is inner machine
						self.checkAndTransformStateConfigurations(submachine,
																  ancestorStates + [ getStateName(state) ],
																  machineName, package)
				else:
					self.checkAndTransformStateConfigurations(submachine,
															  ancestorStates + [ getStateName(state) ],
															  machineName, package)

	def	checkAndTransformTargetStateConfigurations(self, machine, ancestorStates, machineName, package, transition, targets):
		accessingMachine = package + [ machineName ]
		for t in targets:
			tgt = getGuardedTargetTarget(t)
			if isCompoundTarget(tgt):
				self.checkAndTransformTargetStateConfigurations(machine, ancestorStates, machineName, package,
																transition, getCompoundTargets(tgt))
			else:
				# tgt is a basic tgt
				tgtConfig = getConfigurationTree(getTargetConfiguration(tgt))
				setTargetConfiguration(tgt, [self.transformPathConfigurations(tgtConfig,
																			  machine,
																			  ancestorStates,
																			  transition,
																			  "target",
																			  accessingMachine,
																			  accessingMachine),
											 toConfigurationImage(tgtConfig)])
		
	# State config structures provided as input parameters for
	# following configuration path transformation methods are abstract
	# machine structures returned by the ECharts AST walker
	# representing a transition src or target configuration. These
	# configurations are specified linearly (path-oriented). They are
	# of the following form:
	
	# [ path1, path2, ... ]
	
	# where pathn, n => 0, is a list representing an individual
	# configuration path of the overall state configuration
	
	# and a state configuration path pathn is of the form:
	
	# [ s1, s2, .... ]
	
	# where sn, n > 0, are state configuration nodes of the form:

	# [ s, i, ii ]

	# where s is a state name or pseudostate name,

	# i is a machine array index of one of the following four forms:

	# [], [ SET_INDEX, expression ], [ GET_INDEX, expression ], [ EMPTY_INDEX, [] ]

	# the '[]' form represents no index specified

	# and ii is a machine instance identifier (for submachine binding)
	# of one of the following two forms:

	# [], [ expression ]

	# where the '[]' form represents no instance specified
	
	############
	
	# Transformed branching (tree-oriented) cfg structures are one of
	# three forms:
	
	# form 1: [ cfg-type, state-index, sub-cfg-list,
	#           sub-cfg-binding-list, sub-cfg-index-list,
	#           ancestor-state-path, referenced-machine-type ]
	
	# where
	
	# cfg-type is MULTI_CONFIG
	
	# state-index is an integer => 0 representing the index of the current/next
	# state referenced by the cfg - if no such state is referenced, then
	# the value is equal to -1
	
	# sub-cfg-list is a list of cfg representing sub-states referenced
	# by this cfg

	# sub-cfg-binding-list is a list of user-defined submachine
	# bindings corresponding to the sub-cfgs in the sub-cfg-list -
	# list element is empty if no binding defined for associated
	# sub-cfg

	# sub-cfg-index-list is a list of integer indices where each index
	# is assigned to its associated subcfg in the sub-cfg-list - index
	# value is => 0 for non-variable sub-cfgs, o.w. value is -1 -
	# index values and their relative orders are irrelevant

	# ancestor-state-path is a list of ancestor state names
	# constituting a path from the machine in which the transition
	# associated with the cfg is defined, to the (sub)machine to which
	# the cfg root refers - if the cfg refers to the same machine in
	# which the transition is defined, then ancestor-state-path is an
	# empty list

	# referenced-machine-type is a singleton list containing one of
	# MACHINE_DEF, INNER_SUBMACHINE, EXTERNAL_SUBMACHINE,
	# REFLECT_SUBMACHINE, NO_SUBMACHINE - this indicates the type of
	# (sub)machine referenced by the cfg root

	# form 2: [ leaf-cfg-type, ancestor-state-path, referenced-machine-type ]
	
	# where
	
	# leaf-cfg-type is BASIC_CONFIG, DEEP_HISTORY,
	# VARIABLE_CONFIG, NEW, TERMINAL, DEFAULT_INITIAL, ANY

	# form 3: [ DYNAMIC_CONFIG, sub-cfg-accessor-list, sub-cfg-list,
	#           sub-cfg-index-list, sub-cfg-binding-list,
	#			ancestor-state-path, referenced-machine-type ]
	
	# where 

	# sub-cfg-accessor-list is a list of user-defined index gettor/settor
	# accesors corresponding to the sub-cfgs in the sub-cfg-list -
	# list element is empty if no binding defined for associated
	# sub-cfg

	# sub-cfg-list is a list of subcfgs referenced by the cfg

	# sub-cfg-index-list is a list of integer indices (=> 0) where
	# each index is assigned to its associated subcfg in the
	# sub-cfg-list - index values and their relative orders are
	# irrelevant

	# sub-cfg-binding-list is a list of user-defined submachine
	# bindings corresponding to the sub-cfgs in the sub-cfg-list -
	# list element is empty if no binding defined for associated
	# sub-cfg

	# Global. Next value to be used as an index for a new multistate
	# or dynamic state subconfiguration. This ensures that each subcfg
	# associated with a top level config (regardless of how deeply
	# nested) has a unique index value. The index values and their
	# relative orders are irrelevant. This value is reset to 0 for a
	# each new top-level configuration in
	# transformPathConfigurations. The value is referenced/incremented
	# in getMultiStateConfiguration and getDynamicStateConfiguration.
	subCfgIndex = 0

	# Returns a cfg for the given path associated with the linked
	# machine 'machine'. The trick here is to create a sub-tree (state
	# configuration) from a set of state paths using trees (linked
	# machines) as constraints.
	def transformPathConfigurations(self, paths, machine, ancestorStates,
									transition, srctgt, accessedMachine, accessingMachine):
		global subCfgIndex
		subCfgIndex = 0
		# construct a partially populated tree config for each path in
		# the set of paths using previous partial config as starting
		# point for next path
		pcfg = [ VARIABLE_CONFIG, [], [ MACHINE_DEF ] ]
		for path in paths:
			try:
				pcfg = self.getMultiStateConfiguration(path, [], machine, pcfg, srctgt,
															  accessedMachine, accessingMachine)
			except AbstractMachineException, message:
				(line, column) = getTransitionLineColumn(transition)
				raise AbstractMachineException(
					  "%s:%s:%s: semantic error: in transition %s state configuration segment %s of state configuration %s of (sub)machine %s: %s" % \
					  (self.absoluteMachineFilePath, line, column, srctgt, toConfigurationPathImage(path),
					   toConfigurationImage(paths), 
					   string.joinfields(ancestorStates, "."), message) )
		return pcfg

	# Returns a partial populated tree config for the given path,
	# machine, and partial config. Recurses over the elements of
	# path. Raises exceptions for state reference conflicts or for
	# illegal external state access.
	#
	# path is the remaining path list to transform
	#
	# transformedPath is the path list that has already been
	# transformed i.e. transformedPath + path == completePath
	#
	# machine is the (unexpanded or expanded) transition machine
	# referenced by the head element of the path
	#
	# pcfg is the current value of the transformed configuration
	#
	# accessedMachine is the fully qualified class name (represented
	# as a list of strings) of the external machine referenced by the
	# head element of the path
	#
	# accessingMachine is the fully qualified class name (represented
	# as a list of strings) of the external machine in which the
	# transition associated with the path was declared -
	# accessingMachine is the same for any internal submachines
	def getMultiStateConfiguration(self, path, transformedPath,
								   machine, pcfg, srctgt,
								   accessedMachine, accessingMachine):

		global subCfgIndex

		if len(path) == 0:

			return  self.getBasicStateConfiguration(path, transformedPath, machine, pcfg,
													srctgt, accessedMachine, accessingMachine)
		else:
			# len(path) > 0

			if isPseudoState(getConfigurationNodeName(path[0])):
				# referencing a pstate
				return self.getPseudostateConfiguration(path, transformedPath,
														machine, pcfg, srctgt)
			else:
				if isSubmachine(machine):
					machineType = getSubmachineType(machine)
					if machineType == REFLECT_SUBMACHINE:
						# referencing non-pstate of a 'reflect' submachine or no submachine is
						# illegal - limited reference to non-pstates of 'reflect' submachines will
						# be possible once machine typing is supported
						raise AbstractMachineException( 
							  "Illegal to reference to a non-pseudostate in a basic or 'reflect' machine: %s" % \
							  toConfigurationNodeImage(path[0]) )
					elif machineType in [ EXTERNAL_SUBMACHINE, VARIABLE_SUBMACHINE ]:
						# this machine is externally defined so expand
						# it and update accessedMachine value
						filePath = getSubmachineFilePath(machine)
						extCompilationUnit = self.getCompilationUnitForFile(filePath)
						machine = getMachine(extCompilationUnit)
						accessedMachine = getPackage(extCompilationUnit) + [ getMachineName(extCompilationUnit) ]

				# identify accessed state
				states = getStates(machine)
				try:
					index = map(getStateName, states).index(getConfigurationNodeName(path[0]))
				except ValueError:
					raise AbstractMachineException( "State %s does not exist in machine %s" % \
						  (toConfigurationNodeImage(path[0]), string.joinfields(accessedMachine, ".")) )
				# check if access to referenced state is permitted
				if not isAccessible(getStateAccessModifiers(states[index]), accessedMachine, accessingMachine):
					raise AbstractMachineException( "Illegal access of state %s declared in machine %s" % \
						  (getStateName(states[index]), string.joinfields(accessedMachine, ".")) )

				# referenced state exists and is accessible

				# create or augment a partial config for referenced state

				subpcfgIndex = index
				numStates = len(states)

				if pcfg[0] == VARIABLE_CONFIG:
					# no existing partial config so create default config
					if (isAndState(states[index])):
						currentStateIndex = -1
					else:
						currentStateIndex = index
					defaultsubcfg = []
					for state in states:
						defaultsubcfg = defaultsubcfg + [ [ VARIABLE_CONFIG,
															pcfg[-2] + [ getStateName(state) ], # prepend substate to current ancestor state path
															[ getSubmachineType(getSubmachine(state)) ] ] ] # submachine type
					pcfg = [ MULTI_CONFIG,
							 currentStateIndex,
							 defaultsubcfg,
							 numStates * [ [] ], # initially empty list of submachine bindings
							 numStates * [ -1 ], # initially empty list of multistate cfg indices
							 pcfg[-2], # current ancestor state path
							 pcfg[-1] ] # current machine type
					
				elif pcfg[0] == MULTI_CONFIG:
					# existing config is a multi config
					if not isAndState(states[index]):
						# state is an or-state
						currentStateIndex = pcfg[1]
						if currentStateIndex == -1:
							# no existing reference to an or-state so
							# update cfg index to point to this
							# or-state
							pcfg[1] = index
						elif currentStateIndex != index:
							# already have a existing reference to a different or-state
							raise AbstractMachineException( 
								  "Illegal to reference more than one or-state: %s" % \
								  toConfigurationNodeImage(path[0]) )
				else:
					raise AbstractMachineException( 
						  "State reference conflicts with another reference: %s" % \
						  toConfigurationNodeImage(path[0]) )
					

				# in preparation for recursing, update submachine
				# associated with the referenced state
				machine = getSubmachine(states[index])
				submachineType = getSubmachineType(machine)
				# extract any machine index from current state reference
				machineArrayIndexAccessor = getConfigurationNodeMachineArrayIndex(path[0])
				# extract any machine binding from current state reference
				machineBinding = getConfigurationNodeMachineBinding(path[0])

				if isDynamicMachine(machine):

					# submachine declared as dynamic so may need to generate wrapper dyn cfg for the
					# sub-cfg (even if we're on the last path element since there may be a machine
					# array index)
					subpcfg = self.getDynamicStateConfiguration(path[1:],
																transformedPath + path[0],
																machineArrayIndexAccessor,
																machineBinding,
																machine,
																pcfg[2][index],
																srctgt, accessedMachine,
																accessingMachine)
				elif submachineType == NO_SUBMACHINE:
					
					if machineArrayIndexAccessor != []:
						# indexed reference to non-dynamic machine is illegal
						raise AbstractMachineException( "Illegal to use indexed reference to non-machine array for state %s declared in machine %s" % \
							  (getStateName(states[index]), string.joinfields(accessedMachine, ".")) )

					if machineBinding != []:
						# can't bind a submachine to a basic machine
						raise AbstractMachineException( "Illegal to bind a submachine to basic state %s declared in machine %s" % \
							  (getStateName(states[index]), string.joinfields(accessedMachine, ".")) )

					subpcfg = self.getBasicStateConfiguration(path[1:],
															  transformedPath + path[0],
															  machine,
															  pcfg[2][index],
															  srctgt, accessedMachine,
															  accessingMachine)
				else:
					
					if machineArrayIndexAccessor != []:
						# indexed reference to non-dynamic machine is illegal
						raise AbstractMachineException( "Illegal to use indexed reference to non-machine array for state %s declared in machine %s" % \
							  (getStateName(states[index]), string.joinfields(accessedMachine, ".")) )

					if machineBinding != [] and submachineType in [ EXTERNAL_SUBMACHINE, INNER_SUBMACHINE, REFLECT_SUBMACHINE ]:
						# can't bind a submachine to a basic machine
						raise AbstractMachineException( "Illegal to bind to non-variable submachine for state %s declared in machine %s" % \
							  (getStateName(states[index]), string.joinfields(accessedMachine, ".")) )


					# recurse to this method for internal submachine or external submachine
					# referenced by constructor, reflection, or binding
					subpcfg = self.getMultiStateConfiguration(path[1:],
															  transformedPath + path[0],
															  machine,
															  pcfg[2][index],
															  srctgt, accessedMachine,
															  accessingMachine)

				# insert result returned above into current cfg
				if pcfg[2][subpcfgIndex][0] == VARIABLE_CONFIG or \
					   (pcfg[2][subpcfgIndex][0] == subpcfg[0] and subpcfg[0] in [ DYNAMIC_CONFIG, MULTI_CONFIG ]):
					# substitute sub-cfg in cfg
					pcfg[2][subpcfgIndex] = subpcfg
					pcfg[3][subpcfgIndex] = machineBinding
					pcfg[4][subpcfgIndex] = subCfgIndex
				else:
					# can't overwrite a non-variable state
					# reference with basic state reference
					raise AbstractMachineException( "Conflicting access of state %s declared in machine %s" % \
						  (getStateName(states[index]), string.joinfields(accessedMachine, ".")) )

				# increment counter indicating number of submachines
				# referenced by config paths so far
				subCfgIndex += 1
				# all done - return the result
				return pcfg

	def getDynamicStateConfiguration(self, path, transformedPath, machineArrayIndexAccessor, machineBinding,
									 machine, pcfg, srctgt, accessedMachine, accessingMachine):
		global subCfgIndex

		# get submachine wrapped by dynamic machine
		submachine = getSubmachine(getStates(machine)[0])

		if len(path) == 0:
			if machineArrayIndexAccessor != []:
				# leaf state reference includes a machine array index
				# (e.g. S1.S2[?i] )
				indexAccessorType = getDynamicSubconfigurationIndexAccessorType(machineArrayIndexAccessor)
				if pcfg[0] == VARIABLE_CONFIG:
					subpcfg = [ BASIC_CONFIG, pcfg[-2], [ getSubmachineType(submachine) ] ]
					# insert subpcfg in dynamic cfg
					newpcfg = [DYNAMIC_CONFIG, [ machineArrayIndexAccessor ], [ subpcfg ], 
							   [ subCfgIndex ], [ machineBinding ], pcfg[-2], pcfg[-1]]
				else:
					raise AbstractMachineException( "Inconsistency encountered referencing machine array state: %s" % \
						  toConfigurationNodeImage(path[0]) )
			else:
				# no machine array index so no need to add an explicit dyn cfg reference because dyn
				# machine not explicitly referenced - return immediately because we don't need to
				# increment the dynamic submachine reference counter
				return [ BASIC_CONFIG, pcfg[-2], [ getSubmachineType(submachine) ] ]
		else:
			# len(path) > 0
			if pcfg[0] == VARIABLE_CONFIG:
				subpcfg = self.getMultiStateConfiguration(path, transformedPath, submachine,
														  [ VARIABLE_CONFIG, pcfg[-2], [ getSubmachineType(submachine) ] ],
														  srctgt, accessedMachine, accessingMachine)
				# insert subpcfg in dynamic cfg
				newpcfg = [DYNAMIC_CONFIG, [ machineArrayIndexAccessor ], [ subpcfg ], 
						   [ subCfgIndex ], [ machineBinding ], pcfg[-2], pcfg[-1]]
			elif pcfg[0] == DYNAMIC_CONFIG:
				# augment existing dynamic subcfg
				subpcfg = self.getMultiStateConfiguration(path, transformedPath, submachine, 
														  [ VARIABLE_CONFIG, pcfg[-2], [ getSubmachineType(submachine) ] ],
														  srctgt, accessedMachine, accessingMachine)
				newpcfg = [DYNAMIC_CONFIG, pcfg[1] + [ machineArrayIndexAccessor ], pcfg[2] + [ subpcfg ], 
						   pcfg[3] + [ subCfgIndex ], pcfg[4] + [ machineBinding ], pcfg[-2], pcfg[-1]]
			else:
				# shouldn't happen
				raise AbstractMachineException( "Inconsistency encountered referencing machine array state: %s" % \
					  toConfigurationNodeImage(path[0]) )
		
		# increment counter indicating number of dynamic submachines referenced by config paths so
		# far
		subCfgIndex += 1
		return newpcfg

	def getBasicStateConfiguration(self, path, transformedPath,
								   machine, pcfg, srctgt, accessedMachine, accessingMachine):
		if len(path) == 0:
			if pcfg[0] == VARIABLE_CONFIG:
				# leaf state reference
				subpcfg = [ BASIC_CONFIG, pcfg[-2], [ getSubmachineType(machine) ] ]
			else:
				raise AbstractMachineException( "Conflicting references to leaf state")
		else:
			# len(path) > 0
			if isPseudoState(getConfigurationNodeName(path[0])):
				# referencing a pstate
				subpcfg = self.getPseudostateConfiguration(path, transformedPath,
														   machine, pcfg, srctgt)
			else:
				raise AbstractMachineException( "Incorrect attempt to access substate of basic machine state: %s" % \
					  toConfigurationNodeImage(path[0]) )
		return subpcfg

	# Returns a pseudo-state cfg.
	def getPseudostateConfiguration(self, path, transformedPath, machine, pcfg, srctgt):
		if isMachineArrayIndexedConfigurationNode(path[0]):
			# indexed reference to non-dynamic machine is illegal
			raise AbstractMachineException( "Illegal indexed reference to pseudostate: %s" % \
				  toConfigurationNodeImage(path[0]) )
		if isMachineBindingConfigurationNode(path[0]):
			# binding a submachine to a pstate is illegal
			raise AbstractMachineException( "Illegal attempt to bind a submachine to a pseudostate: %s" % \
				  toConfigurationNodeImage(path[0]) )
		if len(path) > 1:
			raise AbstractMachineException( "Illegal reference to sub-state of a pseudo-state: %s" % \
				  toConfigurationNodeImage(path[0]) )
		if srctgt == "source" and getConfigurationNodeName(path[0]) in [DEEP_HISTORY, DEFAULT_INITIAL, NEW]:
			raise AbstractMachineException( "Pseudostate %s may not be referenced as a source state" % \
				  toConfigurationNodeImage(path[0]) )
		if getConfigurationNodeName(path[0]) in [TERMINAL, ANY]:
			if srctgt == "target":
				raise AbstractMachineException( "Pseudostate %s may not be referenced as a target state" % \
					  toConfigurationNodeImage(path[0]) )
			elif transformedPath == [] and getConfigurationNodeName(path[0]) in [TERMINAL]:
				raise AbstractMachineException( "Pseudostate %s can only be referenced by an ancestor machine" % \
					  toConfigurationNodeImage(path[0]) )
		if pcfg[0] == VARIABLE_CONFIG:
			# return pseudo-state name
			return [ getConfigurationNodeName(path[0]), pcfg[-2], pcfg[-1] ]
		else:
			# reference conflict
			raise AbstractMachineException( "Conflict encountered referencing: %s" % \
				  toConfigurationNodeImage(path[0]) )

	# Returns string representation of abstract machine such that
	# numeric token identifiers are substituted with their associated
	# strings. See indent() for an alternative.
	def __str__(self):
		return "%s" % tokenIdToString(self.getCompilationUnit())

	# Machines with the same file path have the same hash code.
	def __hash__(self):
		return hash(self.absoluteMachineFilePath)

# End of AbstractMachine class

class AbstractMachineException(Exception):

	# can't have an empty class so i added this
	def __bogus(self):
		pass

# End of AbstractMachineException class

def main():
	
	echartsPaths = ""
	try:
		echartsPaths = os.environ["ECHARTSPATH"]
	except KeyError:
		# no problem if no ECHARTSPATH defined
		pass
	print "ECHARTSPATH = ", echartsPaths
	m = AbstractMachine(sys.argv[1], echartsPaths)
	print "Dependency dict: \n", AbstractMachine.dependencyDict
	print "Import dict: \n", m.importDict
	print "Linked abstract machine:"
	print indent(m.getCompilationUnit())
	mpp = m.postProcess()
	print "Post-processed abstract machine:"
	print indent(m.getPostProcessedCompilationUnit()[0])

if __name__ == "__main__":
   main()

