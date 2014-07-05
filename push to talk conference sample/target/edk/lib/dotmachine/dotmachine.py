########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Translate an abstract ECharts machine to dot.

from AbstractMachine import *
import DotMachineFormatter
import DotMachineCommentFormatter
import DotMachinePartialFormatter

import string
import os
import types
import imp

# Global variable that is instance of DotMachineFormatter class. Used
# to generate string representations of ECharts expressions for
# inclusion in dot tooltips.
TOOLTIP_FORMATTER = None

# Global variable that is instance of DotMachineFormatter class. Used
# to generate string representations of ECharts state and transition
# comments.
COMMENT_FORMATTER = None

# Global variable that is instance of DotMachineFormatter class. Used
# to generate complete string representations of ECharts expressions
# for inclusion in dot labels. Also used to format the root graph's
# title.
LABEL_FORMATTER = None

# Global variable that is instance of DotMachineFormatter class. Used
# to generate URLs for inclusion in dot hrefs.
URL_FORMATTER = None

# Global variable associating (sub)machines with pseudostates
# explcitly referenced by transitions. Key is "." delimited string of
# submachine's ancestor state names with top-level machine's name as
# first name. Value is table representing set of referenced
# pseudostate names. Key for this table is the pseudostate type
# (e.g. TERMINAL). Value is a list of dot node nodes representing
# instances of this pseudostate.
PSTATE_REFS = {}

# Global variable associating parent machines with child machines
# explicitly referenced by transitions. Key is "." delimited string of
# submachine's ancestor state names with top-level machine's name as
# first name. Value is table representing set of referenced child
# machine names.
SUBSTATE_REFS = {}

# Global variable associating a basic submachine with explicit
# transition references. Each reference is represented by a distinct
# node. Key is "." delimited string of submachine's ancestor state
# names with top-level machine's name as first name. Value is table
# representing set of distinct nodes.
BASICSTATE_REFS = {}

# Global variable associating machine transition with the individual
# arcs used in its dot representation. Key is a string comprising the
# transition's number prepended with the ("." delimited) state path of
# the machine in which the transition is defined. The transition
# number is delimited from the state path with a ".". Value is a table
# of dot arc identifier strings of the form: "NODENAMEX->NODENAMEY"
# where NODENAMEX and NODENAMEY are dot node names defining an arc's
# source and sink.
TRANSITION_ARCS = {}

# Global variable associating dot arc with its associated ECharts
# transition. Key is a dot arc identifier strings of the form:
# "NODENAMEX->NODENAMEY" where NODENAMEX and NODENAMEY are dot node
# names defining an arc's source and sink. Value is a string
# comprising the transition's number prepended with the ("."
# delimited) state path of the machine in which the transition is
# defined. The transition number is delimited from the state path with
# a ".".
ARC_TRANSITIONS = {}

# Global variable associating machine transition with the individual
# nodes used in its dot representation. Key is a string comprising the
# transition's number prepended with the ("." delimited) state path of
# the machine in which the transition is defined. The transition
# number is delimited from the state path with a ".". Value is a table
# of dot node names.
TRANSITION_NODES = {}

# Global variable associating dot node name with its machine state
# name. Key is a dot node name. Value is a machine state name.
NODE_STATES = {}

# Global variable associating machine transition with the transition's
# comment extracted from the machine source code. Key is a string
# comprising the transition's number prepended with the ("."
# delimited) state path of the machine in which the transition is
# defined. The transition number is delimited from the state path with
# a ".". Value is a string representing the comment text, possibly
# with newline '\n' characters.
TRANSITION_COMMENTS = {}

# Global variable associating machine state name with the state's
# comment extracted from the machine source code. Key is the machine
# state name. Value is a string representing the comment text,
# possibly with newline '\n' characters.
STATE_COMMENTS = {}

# Global variable whose value is comment associated with the machine
# class declaration extracted from the machine source code.
MACHINE_COMMENT = ""

# Global variable whose value is a list of machine state names of
# states that are external to but referenced by the current machine.
EXTERNAL_STATES = []

# Global variable initialized in translate() method representing
# AbstractMachine instance associated with machine that is being
# translated.
ABSTRACT_MACHINE = None

# generate dot specification for a given state and its substates
def dotstate(state, statePath, external):
	global LABEL_FORMATTER
	global TOOLTIP_FORMATTER
	global COMMENT_FORMATTER
	global URL_FORMATTER
	global ABSTRACT_MACHINE
	global NODE_STATES
	global STATE_COMMENTS
	global EXTERNAL_STATES
	nodeStyle = ''
	if external:
		# style for external states
		nodeStyle = 'pencolor="LightGrey";\n'
	if isAndState(state):
		# dashed style for and-states
		nodeStyle = nodeStyle + 'style="dashed";\n'
	elif isInitialState(state):
		# bold style for initial or-state
		nodeStyle = nodeStyle + 'style="bold";\n'
	else:
		# solid style for or-states
		nodeStyle = nodeStyle + 'style="solid";\n'
	submachine = getSubmachine(state)
	submachineName = getStateName(state)
	submachineStatePath = statePath + [ submachineName ]
	href = ""
	nodeName = string.joinfields(submachineStatePath, ".")
	NODE_STATES[ "cluster_" + nodeName ] = nodeName
	if external:
		EXTERNAL_STATES.append(nodeName)
	STATE_COMMENTS[ nodeName ] = COMMENT_FORMATTER.dotstate(state, statePath)
	statelabel = LABEL_FORMATTER.dotstate(state, statePath)
	statetooltip = TOOLTIP_FORMATTER.dotstate(state, statePath)
	if isDynamicMachine(submachine):
		# substitute machine with submachine nested in only state
		# of dynamic machine since we don't want to include
		# dynamic machine itself
		state = getStates(submachine)[0]
		submachine = getSubmachine(state)
	if getSubmachineType(submachine) == EXTERNAL_SUBMACHINE:
		# constant parameterized submachine reference of form fsm(p1,...)
		external = True
		# substitute external submachine definition with current
		# submachine in order to recurse to external submachine states
		# if they happen to be referenced by transitions
		extCompilationUnit = ABSTRACT_MACHINE.getCompilationUnitForFile(getExternalSubmachineFilePath(submachine))
		package = getPackage(extCompilationUnit)
		submachine = getMachine(extCompilationUnit)
		href = URL_FORMATTER.doturl(extCompilationUnit, submachineStatePath)
	# recursively invoke this method
	body = dotsubmachine(submachine, submachineStatePath, external)
	# hidden node required to ensure subgraph is rendered when subgraph
	# is not referenced by transitions and has no submachines
	rv = '''subgraph "cluster_%s" {
"hidden_%s" [style=invis, height="0.01", width="0.01", label="", shape="circle", fixedsize="true"];
shape="box";
label = "%s";
labeljust="l";
tooltip="%s";
href="%s";
%s%s};
''' %  (nodeName, nodeName, statelabel, statetooltip, href, nodeStyle, body)
	return rv

def dotsubmachine(submachine, submachineStatePath, external):
	# add invisible nodes to subgraph in order to connect transitions
	# to node representing parent state
	rv = ""
	key = string.joinfields(submachineStatePath, ".")
	try:
		refs = BASICSTATE_REFS[ key ] 
	except KeyError:
		refs = {}
	for ref in refs.keys():
		rv = rv + '"%s" [label="", style=invis, shape=circle, height=0.01, width=0.01, fixedsize="true"];\n' % ref
	if isTopMachine(submachine) or \
	   (isSubmachine(submachine) and getSubmachineType(submachine) in [ INNER_SUBMACHINE, EXTERNAL_SUBMACHINE]):
		# recurse to submachines for non-leaf states
		rv = rv + dotbody(submachine, submachineStatePath, external)
	elif isSubmachine(submachine) and getSubmachineType(submachine) == REFLECT_SUBMACHINE:
		rv = rv + dotpstates(submachine, submachineStatePath)
	return rv

def dotpstates(machine, statePath):
	global PSTATE_REFS
	key = string.joinfields(statePath, ".")
	# obtain list of pstate refs for this machine
	try:
		pstateRefs = PSTATE_REFS[ key ]
	except KeyError:
		pstateRefs = {}
	rv = ""
	for pstate in pstateRefs.keys():
		nodeLabel = dotpstatelabel(pstate)
		for nodeName in pstateRefs[pstate]:
			rv = rv + '"%s" %s;\n' % (nodeName, nodeLabel)
	return rv

def dotpstatelabel(pstate):
	if pstate == TERMINAL:
		return '[label="T", shape="circle", fontname="Helvetica", width="0.2", height="0.2", fixedsize="true"]'
	elif pstate == DEEP_HISTORY:
		return '[label="H", shape="circle", fontname="Helvetica", width="0.2", height="0.2", fixedsize="true"]'
	elif pstate == NEW:
		return '[label="N", shape="circle", fontname="Helvetica", width="0.2", height="0.2", fixedsize="true"]'
	elif pstate == DEFAULT_INITIAL:
		return '[label="I", shape="circle", fontname="Helvetica", width="0.2", height="0.2", fixedsize="true"]'
	elif pstate == ANY:
		return '[label="A", shape="circle", fontname="Helvetica", width="0.2", height="0.2", fixedsize="true"]'
	else:
		return ''

# Generate dot transition specification associated with a given
# message/messageless transition.
def dotxn(xn, i, machineClass):
	global LABEL_FORMATTER
	global TOOLTIP_FORMATTER
	global COMMENT_FORMATTER
	global TRANSITION_COMMENTS
	srcrefs = dotxnref(i, [], machineClass, getConfigurationTree(getSourceConfiguration(xn)))
	(joinspec, joinstate) = dotjoin(i, machineClass, srcrefs)									
	xnlabel = LABEL_FORMATTER.dotportreceive(xn)
	xntooltip = TOOLTIP_FORMATTER.dotportreceive(xn)
	TRANSITION_COMMENTS[ string.joinfields(machineClass + [ str(i) ], ".") ] = COMMENT_FORMATTER.dotportreceive(xn)
	return joinspec + dotxntgt(i, [], machineClass, [], getTransitionTargets(xn), joinstate, xnlabel, xntooltip)

# Generates dot code for joined transition or transition with empty
# source state reference. For a given list of source xn references,
# returns pair (joinspec, joinstate) where joinspec is string
# representing dot spec for any nodes/transitions required to join xn
# references, and joinstate is join node if xn references were
# joined. If source xn reference list is empty then treated as an
# empty source state reference. If source xn reference list has only
# one element then function effectively performs a noop.
def dotjoin(i, machineClass, xnrefs):
	global TRANSITION_ARCS
	global ARC_TRANSITIONS
	global TRANSITION_NODES
	if len(xnrefs) == 1:
		# no need for join if only one xn ref
		return ("", xnrefs[0])
	elif len(xnrefs) == 0:
		nodeShape = 'shape=box, width=".05", height=".05", fixedsize=true'
	else:
		nodeShape = 'style=filled, color=black, shape=circle, width=".05", height=".05", fixedsize=true'
	joinName = "JOIN.%s" % i
	joinNodeName = string.joinfields(machineClass + [ joinName ], ".")
	# join node declaration
	rv = '"%s" [label="", %s];\n' % (joinNodeName, nodeShape)
	joinRef = [ [], joinNodeName, "", "" ]
	key = string.joinfields(machineClass + [ str(i) ], ".")
	try:
		nodes = TRANSITION_NODES[key]
		arcs = TRANSITION_ARCS[key]
	except KeyError:
		arcs = {}
		nodes = {}
		TRANSITION_ARCS[key] = arcs
		TRANSITION_NODES[key] = nodes
	nodes[joinNodeName] = None
	for ref in xnrefs:
		arc = "%s->%s" % (ref[1], joinNodeName)
		ARC_TRANSITIONS[arc] = key
		arcs[arc] = None
		nodes[ref[1]] = None
		rv = rv + '"%s" -> "%s" [taillabel="%s", ltail="%s", label=""];\n' % (ref[1], joinNodeName, ref[2], ref[3])
	return (rv, joinRef)

# Generates dot code for forked transition or transition with empty
# target state reference. For a given list of target xn references,
# returns pair (forkspec, forkstate) where forkspec is string
# representing dot spec for any nodes/transitions required to fork xn
# references, and forkstate is fork node if xn references were
# forked. If target xn reference list is empty then treated as an
# empty target state reference. If target xn reference list has only
# one element then function effectively performs a noop.
def dotfork(i,b, machineClass, xnrefs):
	global TRANSITION_ARCS
	global ARC_TRANSITIONS
	global TRANSITION_NODES
	if len(xnrefs) == 1:
		# no need for fork if only one xn ref
		return ("", xnrefs[0])
	elif len(xnrefs) == 0:
		nodeShape = 'shape=box, width=".05", height=".05", fixedsize=true'
	else:
		nodeShape = 'style=filled, color=black, shape=circle, width=".05", height=".05", fixedsize=true'
	forkName = "FORK.%s" % string.joinfields(map(str, [ i ] + b), "_")
	forkNodeName = string.joinfields(machineClass + [ forkName ], ".")
	# fork node declaration
	rv = '"%s" [label="", %s];\n' % (forkNodeName, nodeShape)
	forkRef = [ [], forkNodeName, "", "" ] 
	key = string.joinfields(machineClass + [ str(i) ], ".")
	try:
		arcs = TRANSITION_ARCS[key]
		nodes = TRANSITION_NODES[key]
	except KeyError:
		arcs = {}
		nodes = {}
		TRANSITION_ARCS[key] = arcs
		TRANSITION_NODES[key] = nodes
	nodes[forkNodeName] = None
	for ref in xnrefs:
		arc = "%s->%s" % (forkNodeName, ref[1])
		ARC_TRANSITIONS[arc] = key
		arcs[arc] = None
		nodes[ref[1]] = None
		rv = rv + '"%s" -> "%s" [headlabel="%s", lhead="%s", label=""];\n' % (forkNodeName, ref[1], ref[2], ref[3])
	return (rv, forkRef)

# Returns list of node references of the form [ ancestorStatePath,
# nodeName, htlabel, lht ] corresponding to states referenced by the
# specified configuration tree, where ancestorStatePath is state path
# from machine in which transition associated with cfg is defined to
# (sub)machine referenced by the cfg root, nodeName is name of dot
# node associated with the reference, htlabel is the head/tail label
# string associated with any transitions to/from the node, and lht is
# the node's logical head/tail reference.
def dotxnref(i, b, machineClass, cfg):
	ancestorPath = getConfigurationTreeAncestorStatePath(cfg)
	referencedMachineType = getConfigurationTreeMachineReferenceType(cfg)
	cfgType = getConfigurationTreeType(cfg)
	refs = []
	if cfgType == VARIABLE_CONFIG:
		# if ancestorpath is null then we've got an empty ref - we
		# handle these in dotjoin/dotfork
		refs = []
	elif cfgType == BASIC_CONFIG:
		global BASICSTATE_REFS
		lht = "cluster_%s" % string.joinfields(machineClass + ancestorPath, ".")
		nodeName = "stub_%s.%s" % (string.joinfields(machineClass + ancestorPath, "."),
								   string.joinfields(map(str, [ i ] + b), "_"))
		htlabel = ""
		key = string.joinfields(machineClass + ancestorPath, ".")
		try:
			oldRefs = BASICSTATE_REFS[ key ]
		except KeyError:
			oldRefs = {}
			BASICSTATE_REFS[ key ] = oldRefs
		oldRefs[nodeName] = None
		refs = [ [ ancestorPath, nodeName, htlabel, lht ] ] 
	elif cfgType in [ DEFAULT_INITIAL, DEEP_HISTORY, TERMINAL, NEW, ANY ]:
		global PSTATE_REFS
		# pstate reference
		pstateName = cfgType
		newAncestorPath = ancestorPath + [ pstateName ]
		nodeName = string.joinfields(machineClass + newAncestorPath, ".")
		nodeName = nodeName + "." + string.joinfields(map(str, [ i ] + b), "_")
		htlabel = ""
		lht = ""
		# update global table of pstate ref's for referenced machine
		key = string.joinfields(machineClass + ancestorPath, ".")
		try:
			oldRefs = PSTATE_REFS[ key ]
		except KeyError:
			oldRefs = {}
			PSTATE_REFS[ key ] = oldRefs
		try:
			oldNodeNames = oldRefs[ cfgType ]
		except KeyError:
			oldNodeNames = []
			oldRefs[ cfgType ] = oldNodeNames
		oldNodeNames.append(nodeName)
		refs = [ [ newAncestorPath, nodeName, htlabel, lht ] ]
	elif cfgType == DYNAMIC_CONFIG:
		# extract the sub config from the dynamic config and recurse
		# since we want to ignore the dynamic config
		refs = []
		for subcfg in getDynamicSubconfigurations(cfg):
			refs = refs + dotxnref(i, b, machineClass, subcfg)
	else:
		# recurse for external machines or inner machines
		refs = []
		subrefs = []
		for subcfg in getSubconfigurationTree(cfg):
			newrefs = dotxnref(i, b, machineClass, subcfg)
			refs = refs + newrefs
			if not newrefs == []:
				subrefs = subrefs + [ getConfigurationTreeParentStateName(subcfg) ] 
		# add subrefs to table of subrefs for parent state
		key = string.joinfields(machineClass + ancestorPath, ".")
		try:
			oldsubrefs = SUBSTATE_REFS[ key ]
		except KeyError:
			oldsubrefs = {}
			SUBSTATE_REFS[ key ] = oldsubrefs
		for subref in subrefs:
			oldsubrefs[subref] = None
	return refs

# Returns list of state paths for leaf states explicitly referenced by
# the specified cfg.
def dotxnpaths(cfg):
	cfgType = getConfigurationTreeType(cfg)
	if cfgType == BASIC_CONFIG:
		return [ getConfigurationTreeAncestorStatePath(cfg) ]
	elif cfgType in [ DEEP_HISTORY, DEFAULT_INITIAL, TERMINAL, NEW, ANY ]:
		return [ cfgType ]
	elif cfgType == VARIABLE_CONFIG:
		return []
	elif cfgType == DYNAMIC_CONFIG:
		return dotxnpaths(getSubconfigurationTree(cfg))
	else:
		rv = []
		for subcfg in getSubconfigurationTree(cfg):
			rv = rv + dotxnpaths(subcfg)
		return rv

# i is transition numbers, b is list of branch numbers for the
# transition, machine class is '.' qualified machine class name for
# the transition's machine
def dotxntgt(i, b, machineClass, guard, tgt, srcstate, xnlabel, xntooltip):
	global LABEL_FORMATTER
	global TOOLTIP_FORMATTER
	global TRANSITION_ARCS
	global TRANSITION_NODES
	rv = ""
	if isCompoundTarget(tgt):
		# concatenate results returned by recursively invoking
		# this method for each transition target
		subtgts = getCompoundTargets(tgt)
		if len(subtgts) == 1:
			# if we've only got one compund target member than
			# dispense with adding auxilliary node and use original
			# source node
			newsrcstate = srcstate
		else:
			# add auxilliary node and connect it to original source
			# node
			newsrcstateName = "BRANCH.%s" % string.joinfields(map(str, [ i ] + b), "_")
			# create new state path by replacing old parent state name
			# in src state ancestor state path with new aux state name
			newsrcstateAncestorPath = srcstate[0][:-1] + [ newsrcstateName ] 
			newsrcstateNode = string.joinfields(machineClass + newsrcstateAncestorPath, ".")
			newsrcstate = [ newsrcstateAncestorPath, newsrcstateNode, "", "", newsrcstateName ]
			rv = rv + '"%s" [label="", shape="circle", style="solid", height="0.05", width="0.05", fixedsize="true"];\n' % newsrcstateNode
			rv = rv + '"%s" -> "%s" [ltail="%s", taillabel="%s", label="%s", tooltip="%s"];\n' % \
				 (srcstate[1], newsrcstateNode, srcstate[3], srcstate[2], xnlabel, xntooltip)
			key = string.joinfields(machineClass + [ str(i) ], ".")
			try:
				arcs = TRANSITION_ARCS[key]
				nodes = TRANSITION_NODES[key]
			except KeyError:
				arcs = {}
				nodes = {}
				TRANSITION_ARCS[key] = arcs
				TRANSITION_NODES[key] = nodes
			arc = "%s->%s" % (srcstate[1], newsrcstateNode)
			ARC_TRANSITIONS[arc] = key
			arcs[arc] = None
			nodes[srcstate[1]] = None
			nodes[newsrcstateNode] = None
		j = 1
		for subtgt in subtgts:
			subguard = getGuardedTargetGuard(subtgt)
			if len(subtgts) == 1:
				newxnlabel = xnlabel + LABEL_FORMATTER.dotxnguard(subguard)
				newxntooltip = xntooltip + TOOLTIP_FORMATTER.dotxnguard(subguard)
			else:
				# add numeric taillabel for compound transitions when
				# more than one compound target member
				newsrcstate[2] = j
				newxnlabel = LABEL_FORMATTER.dotxnguard(subguard)
				newxntooltip = TOOLTIP_FORMATTER.dotxnguard(subguard)
			subb = b + [ j ] 
			j = j + 1
			rv = rv + dotxntgt(i, subb, machineClass, 
							   subguard,
							   getGuardedTargetTarget(subtgt),
							   newsrcstate,
							   newxnlabel,
							   newxntooltip)
	else:
		# tgt is a basic tgt
		tgtrefs = dotxnref(i, b, machineClass, getConfigurationTree(getTargetConfiguration(tgt)))
		(forkspec, forkstate) = dotfork(i, b, machineClass, tgtrefs)
		rv = rv + forkspec + '"%s" -> "%s" [ltail="%s", lhead="%s", taillabel="%s", headlabel="%s", label="%s", tooltip="%s"];\n' % \
			 (srcstate[1], forkstate[1], srcstate[3], forkstate[3], srcstate[2], forkstate[2], \
			  LABEL_FORMATTER.dotxn(xnlabel, LABEL_FORMATTER.dotxnaction(getTargetAction(tgt))), \
			  TOOLTIP_FORMATTER.dotxn(xntooltip, TOOLTIP_FORMATTER.dotxnaction(getTargetAction(tgt))))
		key = string.joinfields(machineClass + [ str(i) ], ".")
		try:
			arcs = TRANSITION_ARCS[key]
			nodes = TRANSITION_NODES[key]
		except KeyError:
			arcs = {}
			nodes = {}
			TRANSITION_ARCS[key] = arcs
			TRANSITION_NODES[key] = nodes
		arc = "%s->%s" % (srcstate[1], forkstate[1])
		ARC_TRANSITIONS[arc] = key
		arcs[arc] = None
		nodes[srcstate[1]] = None
		nodes[forkstate[1]] = None
	return rv

# Generates dot state and transition specifications for the machine
# and its submachines.

# machine is the post-processed abstract machine, statePath is list of
# state names to the current machine starting with root machine name,
# external is a boolean indicating whether or not specified machine is
# externally defined relative to the root machine we are translating

def dotbody(machine, statePath, external):
	rv = ""
	if external:
		# get set of states in this machine that have been referenced
		# by transitions
		key = string.joinfields(statePath, ".")
		try:
			subrefs = SUBSTATE_REFS[ key ]
		except KeyError:
			subrefs = {}
		states = getStates(machine)
		# generate declarations only for states that are explicitly
		# referenced by transitions
		for subref in subrefs.keys():
			index = map(getStateName, states).index(subref)
			rv = rv + dotstate(states[index], statePath, external)
	else:
		# generate transition declarations for non-external
		# machines
		count = 1
		for xn in getTransitions(machine):
			rv = rv + dotxn(xn, count, statePath)
			count = count + 1
		# generate state declarations
		for state in getStates(machine):
			rv = rv + dotstate(state, statePath, external)
	# generate pstate nodes
	rv = rv + dotpstates(machine, statePath)
	return rv

# Generate dot for top-level machine class and its submachine
# classes.
def dottop(machine, machineName):
	machineClass = [ machineName ]
	rv = dotbody(machine, machineClass, False)
	return rv

def dotmachine(compilationUnit):
	global LABEL_FORMATTER
	global COMMENT_FORMATTER
	global MACHINE_COMMENT
	machine = getMachine(compilationUnit)
	name = getMachineName(compilationUnit)
	MACHINE_COMMENT = COMMENT_FORMATTER.dotrootmachine(compilationUnit)
	dotinitstring = """digraph G {
    graph [
        remincross="true",
        nodesep="0.1",
        ranksep="0.5",
        clusterrank="local",
        size="8,10.5",
        compound="true",
        center="true",
        ratio="fill",
        fontsize="8",
        fontname="Courier New Bold",
		fontcolor="black",
		margin="0,0",
		label="%s",
    ];
    node [
        shape="box",
        fontsize="8",
        fontname="Courier New Bold",
		fontcolor="black",
    ];
    edge [
        fontsize="8",
        fontname="Courier New Bold",
		fontcolor="black",
		labelfontsize="6",
        labelfontname="Courier New Bold",
		labelfontcolor="black",
    ];
""" % LABEL_FORMATTER.dotrootmachine(compilationUnit)
	return dotinitstring + dottop(machine, name) + "\n}"

# Load formatter class specified on ech2dot command line (if not
# already loaded) and return a new class instance.
def dotFormatterInstance(qualifiedClassName):
	splitClassName = string.split(qualifiedClassName, ".")
	className = splitClassName[-1]
	moduleName = string.joinfields(splitClassName[:-1], ".")
	try:
		module = sys.modules[moduleName]
	except KeyError:
		(modfile, modpathname, moddescription) = imp.find_module(moduleName)
		module = imp.load_module(moduleName, modfile, modpathname, moddescription)
	return apply(getattr(module, className), [])
	
# Reset global tables.
def dotResetTables():
	global PSTATE_REFS
	global SUBSTATE_REFS
	global BASICSTATE_REFS
	global TRANSITION_ARCS
	global ARC_TRANSITIONS
	global TRANSITION_NODES
	global NODE_STATES
	global TRANSITION_COMMENTS
	global STATE_COMMENTS
	global EXTERNAL_STATES
	PSTATE_REFS = {}
	SUBSTATE_REFS = {}
	BASICSTATE_REFS = {}
	TRANSITION_ARCS = {}
	ARC_TRANSITIONS = {}
	TRANSITION_NODES = {}
	NODE_STATES = {}
	TRANSITION_COMMENTS = {}
	STATE_COMMENTS = {}
	MACHINE_COMMENT = ""
	EXTERNAL_STATES = []

# Translate an abstract machine to a string constituting a dot
# specification.
def translate(compilationUnit, machine, targetDirectory, opts):
	global ABSTRACT_MACHINE
	global LABEL_FORMATTER
	global TOOLTIP_FORMATTER
	global COMMENT_FORMATTER
	global URL_FORMATTER
	ABSTRACT_MACHINE = machine
	COMMENT_FORMATTER = DotMachineCommentFormatter.DotMachineCommentFormatter()
	TOOLTIP_FORMATTER = COMMENT_FORMATTER
	LABEL_FORMATTER = DotMachinePartialFormatter.DotMachinePartialFormatter()
	URL_FORMATTER = DotMachineFormatter.DotMachineFormatter()
	dotResetTables()
	for arg, val in opts:
		if arg == '--label-formatter':
			LABEL_FORMATTER = dotFormatterInstance(val)
		elif arg == '--tooltip-formatter':
			TOOLTIP_FORMATTER = dotFormatterInstance(val)
		elif arg == '--url-formatter':
			URL_FORMATTER = dotFormatterInstance(val)
		elif arg == '--comment-formatter':
			COMMENT_FORMATTER = dotFormatterInstance(val)
	header = """//
// This file was generated by ech2dot. Do not modify.
//

"""
	# the machine itself
	machine = dotmachine(compilationUnit)
	# return the string
	return header + machine
