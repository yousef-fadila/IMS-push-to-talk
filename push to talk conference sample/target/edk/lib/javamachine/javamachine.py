########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Translate an abstract ECharts machine to Java.

from AbstractMachine import *

import string
import os
import types

True = 1
False = 0

# Global variable representing current line number of generated code.
lineNumber = 1

# generate transition state configuration structures - called by
# javasxn as part of generating static transition definitions

# cfg is the tree-based state configuration referenced by a transition
# source or target - i is the integer index of the transition -
# machineClass is the fully qualified classname of the machine in
# which the transition is defined - srctgt identifies whether cfg is a
# source config or a target config

def javascfg(cfg, i, machineClass, srctgt):
	cfgType = getConfigurationTreeType(cfg)
	if cfgType == DYNAMIC_CONFIG:
		rv = javasdynamiccfg(cfg, i, machineClass, srctgt)
	elif cfgType == VARIABLE_CONFIG:
		rv = "Machine.VARIABLE_CONFIG"
	elif cfgType == MULTI_CONFIG:
		rv = javasmulticfg(cfg, i, machineClass, srctgt)
	elif cfgType == BASIC_CONFIG:
		rv = "Machine.BASIC_CONFIG"
	elif isPseudoState(cfgType):
		rv = "Machine." + cfgType + "_CONFIG"
	else:
		raise "Unrecognized state configuration: %s" % cfg
	return rv

# auxilliary function called by javascfg

def javascfglist(cfglist, i, machineClass, srctgt):
	subcfglist = []
	for subcfg in cfglist:
		subcfglist = subcfglist + [ javascfg(subcfg, i, machineClass, srctgt) ]
	rv = reduce(lambda x, s: "%s, " % x + s, subcfglist)
	return rv

# auxilliary function called by javascfg

def javasmulticfg(cfg, i, machineClass, srctgt):
	subcfgs = "new StateConfiguration[]{" + javascfglist(getSubconfigurationTree(cfg), i, machineClass, srctgt) + "}"
	isMachineBindingDefined = []
	for binding in getMultiSubconfigurationMachineBindings(cfg):
		if binding == []:
			isMachineBindingDefined.append("false")
		else:
			isMachineBindingDefined.append("true")
	if srctgt == "src":
		machineBindingGettor = "null"
	else:
		machineBindingGettor = "new SubmachineBindingGettor() { public final Machine getSubmachine(final int cfgIndex, final Machine machine) throws Exception { return ((%s) machine).get_transition_%s_%s_machine_binding(cfgIndex); }}" % (machineClass, i, srctgt)
	rv = "new MultiStateConfiguration(%s, %s, new boolean[] {%s}, new int[] {%s}, %s)" % \
		 (cfg[1], subcfgs,
		  reduce(lambda x, y: "%s, " % x + y, isMachineBindingDefined),
		  reduce(lambda x, y: "%s, " % x + y, map(lambda x: str(x), getMultiSubconfigurationIndices(cfg))),
		  machineBindingGettor)
	return rv
	
# auxilliary function called by javascfg

def javasdynamiccfg(cfg, i, machineClass, srctgt):
	isGettorDefined = []
	isSettorDefined = []
	javaSubCfgs = []
	subCfgIndexAccessors = getDynamicSubconfigurationIndexAccessors(cfg)
	subCfgs = getDynamicSubconfigurations(cfg)
	for j in range(len(subCfgs)):
		javaSubCfgs.append(javascfg(subCfgs[j], i, machineClass, srctgt))
		indexType = getDynamicSubconfigurationIndexAccessorType(subCfgIndexAccessors[j])
		if indexType == GET_INDEX:
			isGettorDefined.append("true")
			isSettorDefined.append("false")
		elif indexType == SET_INDEX:
			isGettorDefined.append("false")
			isSettorDefined.append("true")
		else:
			isGettorDefined.append("false")
			isSettorDefined.append("false")
	cachedGettor = "new DynamicSubmachineIndexGettor() { public final int getIndex(final int cfgIndex, final Machine machine) throws Exception { return ((%s) machine).get_transition_%s_%s_cached_index(cfgIndex); }}" % (machineClass, i, srctgt)
	cachedSettor = "new DynamicSubmachineIndexSettor() { public final void setIndex(final int cfgIndex, final Machine machine, final int index) throws Exception { ((%s) machine).set_transition_%s_%s_cached_index(cfgIndex, index); }}" % (machineClass, i, srctgt)
	userGettor = "new DynamicSubmachineIndexGettor() { public final int getIndex(final int cfgIndex, final Machine machine) throws Exception { return ((%s) machine).get_transition_%s_%s_user_index(cfgIndex); }}" % (machineClass, i, srctgt)
	userSettor = "new DynamicSubmachineIndexSettor() { public final void setIndex(final int cfgIndex, final Machine machine, final int index) throws Exception { ((%s) machine).set_transition_%s_%s_user_index(cfgIndex, index); }}" % (machineClass, i, srctgt)
	rv = "new DynamicStateConfiguration(new StateConfiguration[]{%s}, new int[]{%s}, new boolean[]{%s}, new boolean[]{%s}, %s, %s, %s, %s)" % \
		 (reduce(lambda x, y: "%s, " % x + y, javaSubCfgs),
		  reduce(lambda x, y: "%s, %s" % (x, y), getDynamicSubconfigurationIndices(cfg)),
		  reduce(lambda x, y: "%s, " % x + y, isGettorDefined),
		  reduce(lambda x, y: "%s, " % x + y, isSettorDefined),
		  cachedGettor, cachedSettor, userGettor, userSettor)
	return rv

# generate a static state declaration for a machine state - called by
# javastatic()

# state is the (post-processed abstract) state object, 'i' is the
# state's index in its machine, stateName is name of state containing
# the machine, machineClass is fully-qualified machine's classname

def javasstate(state, i, stateName, machineClass):
	submachineType = getSubmachineType(getSubmachine(state))
	submachine = getSubmachine(state)
	if submachineType == NO_SUBMACHINE:
		# basic
		eval = "BasicMachineConstructor.BASIC_MACHINE_CONSTRUCTOR"
	elif submachineType == VARIABLE_SUBMACHINE:
		submachineClass = getVariableSubmachineClassName(submachine)
		eval = "new VariableMachineConstructor() { public void setInstance(final Machine parentMachine, final Machine submachine) throws Exception { ((%s) parentMachine).setState_%s((%s) submachine); }}" % (machineClass, getStateName(state), submachineClass)
	else:
		eval = "new MachineConstructor() { public Machine newInstance(final Machine parentMachine, final int machineIndex, final MachineCode machineCode) throws Exception { return ((%s) parentMachine).state_%s(parentMachine, machineIndex, machineCode); }}" % (machineClass, getStateName(state))
		if isDynamicMachine(submachine):
			eval = "new MachineConstructor() { public Machine newInstance(final Machine parentMachine, final int machineIndex, final MachineCode machineCode) throws Exception { return ((%s) parentMachine).state_%s(parentMachine, machineIndex, machineCode); }}" % (machineClass, getStateName(state))
	if getActionBlock(getStateEntry(state)) == []:
		entry = "null"
	else:
		entry = "new EntryMethod() { public void invoke(final Machine machine) throws Exception { ((%s) machine).state_%s_onEntry(); }}" % (machineClass, getStateName(state))
	if getActionBlock(getStateExit(state)) == []:
		exit = "null"
	else:
		exit = "new ExitMethod() { public void invoke(final Machine machine) throws Exception { ((%s) machine).state_%s_onExit(); }}" % (machineClass, getStateName(state))
	if isNonTerminalState(state):
		nonterminal = "true"
	else:
		nonterminal = "false"
	if isAndState(state):
		type = "And"
	else:
		type = "Or"
	rv = "%s_states[%s] = new %sState(\"%s\", %s, %s, %s, %s);\n" % (stateName, i, type, getStateName(state), eval, entry, exit, nonterminal)
	return rv

# generate a static transition declaration for a machine transition -
# called by javastatic()

# machine is the post-processed abstract machine, 'i' is the
# transition's index in it machine, stateName is name of state
# containing the machine, machineClass is fully-qualified machine's
# classname

def javasxn(xn, machine, i, stateName, machineClass):
	src = javasxnsrc(xn, i, machineClass)
	tgt = javasxntgt(xn, i, machineClass, [], getTransitionTargets(xn))
	index = getConfigurationIndex(getConfigurationTree(getSourceConfiguration(xn)))
	if isMessagelessTransition(xn):
		rv = "addMessagelessTransition(%s_messagelessTransitions, new MessagelessTransition(%s, %s), %s);\n" % \
			 (stateName, src, tgt, index)
	else:
		# message transition
		port = "new PortMethod() { public LocalPort invoke(final Machine machine) { return ((%s) machine).transition_%s_port(); }}" % \
			   (machineClass, i)
		if isDelayTransition(xn):
			rv = "addMessageTransition(%s_messageTransitions, new TimedTransition(%s, %s, %s), %s);\n" % \
				 (stateName, port, src, tgt, index)
		elif  isAnyPortTransition(xn):
			rv = "addMessageTransition(%s_messageTransitions, new AnyPortTransition(%s, %s.class, %s, %s), %s);\n" % \
				 (stateName, port, javatype(getTransitionMessageClass(xn)), src, tgt, index)
		else:
			# message transition with port explicitly specified by
			# programmer
			if "constport" in getTransitionModifiers(xn):
				varport = "false"
			else:
				varport = "true"
			rv = "addMessageTransition(%s_messageTransitions, new MessageTransition(%s, %s.class, %s, %s, %s), %s);\n" % \
				 (stateName, port, javatype(getTransitionMessageClass(xn)), src, tgt, varport, index)
	return rv

# generate a transition source declaration to be used by the
# transition's static declaration - called by javasxn

# machine is the post-processed abstract machine, 'i' is the
# transition's index in it machine, stateName is name of state
# containing the machine, machineClass is fully-qualified machine's
# classname

def javasxnsrc(xn, i, machineClass):
	srccfg = getSourceConfiguration(xn)
	srcimg = "\"" + getConfigurationImage(srccfg) + "\""
	javasrccfg = javascfg(getConfigurationTree(srccfg), i, machineClass, "src")
	rv = "new TransitionSource(%s, %s)" % (javasrccfg, srcimg)
	return rv

# generate a transition target declaration to be used by the
# transition's static declaration - called by javasxn

# machine is the post-processed abstract machine, 'i' is the
# transition's index in it machine, stateName is name of state
# containing the machine, machineClass is fully-qualified machine's
# classname, guard is the guard associated with the specified
# transtion target

def javasxntgt(xn, i, machineClass, guard, tgt):
	if isCompoundTarget(tgt):
		javatgts = []
		# concatenate results returned by recursively invoking
		# this method for each transition target
		j = 1
		for subtgt in getCompoundTargets(tgt):
			subi = "%s_%s" % (i, j)
			j = j + 1
			javatgts = javatgts + [ javasxntgt(xn, subi, machineClass,
											   getGuardedTargetGuard(subtgt),
											   getGuardedTargetTarget(subtgt)) ]
		rv = "new CompoundTransitionTarget(%s, new TransitionTarget[]{%s})" % (javasxnguard(xn, i, machineClass, guard),
																			   string.joinfields(javatgts, ", "))
	else:
		# tgt is a basic tgt
		tgtcfg = getTargetConfiguration(tgt)
		tgtimg = "\"" + getConfigurationImage(tgtcfg) + "\""
		# generate java representation of src/tgt configs
		javatgtcfg = javascfg(getConfigurationTree(tgtcfg), i, machineClass, "tgt")
		rv = "new BasicTransitionTarget(%s, %s, %s, %s)" % (javatgtcfg, tgtimg,
															javasxnguard(xn, i, machineClass, guard),
															javasxnaction(xn, i, machineClass, getTargetAction(tgt)))
	return rv

def javasxnguard(xn, i, machineClass, guard):
	if guard == []:
		return "null"
	if isMessagelessTransition(xn):
		# messageless transition
		return "new MessagelessGuardMethod() { public boolean invoke(final Machine machine) throws Exception { return ((%s) machine).transition_%s_guard(); }}" % (machineClass, i)
	else:
		# message transition
		if isDelayTransition(xn):
			# ignore port and message for timed transition
			return "new MessageGuardMethod() { public boolean invoke(final Machine machine, final LocalPort port, final Object message) throws Exception { return ((%s) machine).transition_%s_guard(); }}" % (machineClass, i)
		elif isAnyPortTransition(xn):
				return "new MessageGuardMethod() { public boolean invoke(final Machine machine, final LocalPort port, final Object message) throws Exception { return ((%s) machine).transition_%s_guard(port, (%s) message); }}" % (machineClass, i, javatype(getTransitionMessageClass(xn)))
		else:
			# message transition with port explicitly specified by
			# programmer
			return "new MessageGuardMethod() { public boolean invoke(final Machine machine, final LocalPort port, final Object message) throws Exception { return ((%s) machine).transition_%s_guard(port, (%s) message); }}" % \
						(machineClass, i, javatype(getTransitionMessageClass(xn)))

def javasxnaction(xn, i, machineClass, action):
	if action == []:
		return "null"
	if isMessagelessTransition(xn):
		# messageless transition
		return "new MessagelessActionMethod() { public void invoke(final Machine machine) throws Exception { ((%s) machine).transition_%s_action(); }}" % (machineClass, i)
	else:
		# message transition
		if isDelayTransition(xn):
			return "new DelayActionMethod() { public void invoke(final Machine machine, final long duration, final long activationTime, final long expiryTime) throws Exception { ((%s) machine).transition_%s_action(duration, activationTime, expiryTime); }}" % (machineClass, i)
		elif isAnyPortTransition(xn):
			return "new MessageActionMethod() { public void invoke(final Machine machine, final LocalPort port, final Object message) throws Exception { ((%s) machine).transition_%s_action(port, (%s) message); }}" %\
				   (machineClass, i, javatype(getTransitionMessageClass(xn)))
		else:
			# message transition with port explicitly specified by
			# programmer
			return "new MessageActionMethod() { public void invoke(final Machine machine, final LocalPort port, final Object message) throws Exception { ((%s) machine).transition_%s_action(port, (%s) message); }}" % \
				   (machineClass, i, javatype(getTransitionMessageClass(xn)))

# generates static code for machine's states, transitions and
# submachine (machine's class declaration and constructor generated in
# javatop() or javasub())

# stateName is name of parent state containing the machine,
# machineClass is fully-qualified machine classname, machine is the
# post-processed abstract machine

def javastatic(machine, stateName, machineClass):
	# maximum number of state or transition declarations per static
	# code block - the JVM imposes a static block code length limit of
	# 65536 bytes (see
	# http://java.sun.com/docs/books/jvms/second_edition/html/ClassFile.doc.html)
	# so we split up the declarations into separate methods containing
	# maxStaticGroupSize state/transition declarations - then we
	# declare a static initializer that calls these methods in sequence
	MAX_STATIC_GROUP_SIZE = 25
	rv = "// Static declarations for %s\n" % machineClass
	# declare states
	numStates = len(getStates(machine))
	rv = rv + "private static final int %s_NUM_STATES = %s;\n" % (stateName, numStates)
	rv = rv + "private static State[] %s_states = new State[%s_NUM_STATES];\n" % (stateName, stateName)
	count = 0
	groupCount = 0
	for state in getStates(machine):
		if count % MAX_STATIC_GROUP_SIZE == 0:
			if groupCount > 0:
				# close off previous group declaration before creating
				# next one
				rv = rv + "}\n"
			rv = rv + "private static void initialize_%s_states_%s() {\n" % (stateName, groupCount)
			groupCount = groupCount + 1
		rv = rv + javasstate(state, count, stateName, machineClass)
		count = count + 1
	if groupCount > 0:
		# close off previous group declaration
		rv = rv + "}\n"
		# static initializer to invoke each group declaration
		rv = rv + "static {\n"
		for group in range(0, groupCount):
			rv = rv + "    initialize_%s_states_%s();\n" % (stateName, group)
		rv = rv + "}\n"
	if isTransitionMachine(machine):
		xnArraySize = "%s_NUM_STATES" % stateName
		rv = rv + "private static MachineMessageTransitions[] %s_messageTransitions = initializeMessageTransitions(new MachineMessageTransitions[%s]);\n" % (stateName, xnArraySize)
		rv = rv + "private static MachineMessagelessTransitions[] %s_messagelessTransitions = initializeMessagelessTransitions(new MachineMessagelessTransitions[%s]);\n" % (stateName, xnArraySize)
		count = 1
		groupCount = 0
		for xn in getTransitions(machine):
			if (count - 1) % MAX_STATIC_GROUP_SIZE == 0:
				if groupCount > 0:
					# close off previous group declaration before creating
					# next one
					rv = rv + "}\n"
				rv = rv + "private static void initialize_%s_transitions_%s() {\n" % (stateName, groupCount)
				groupCount = groupCount + 1
			rv = rv + javasxn(xn, machine, count, stateName, machineClass)
			count = count + 1
		if groupCount > 0:
			# close off previous group declaration
			rv = rv + "}\n"
			# static initializer to invoke each group declaration
			rv = rv + "static {\n"
			for group in range(0, groupCount):
				rv = rv + "    initialize_%s_transitions_%s();\n" % (stateName, group)
			rv = rv + "}\n"
	# recurse to generate static code for inner submachines
	for state in getStates(machine):
		submachineName = getStateName(state)
		submachineClass = "%s.%s" % (machineClass, submachineName)
		submachine = getSubmachine(state)
		if isDynamicMachine(submachine):
			if getDynamicSubmachineType(submachine) == INNER_SUBMACHINE:
				# don't generate declarations for dynamic machine
				# itself but recurse to generate static code for inner
				# submachine wrapped by the dynamic machine
				rv = rv + javastatic(getDynamicSubmachine(submachine), submachineName, submachineClass)
		elif getSubmachineType(submachine) == INNER_SUBMACHINE:
			rv = rv + javastatic(submachine, submachineName, submachineClass)
	return rv

# generate method to return submachine instance for a given state -
# also generate submachine reference variable declaration for the
# state

def javastate(state, machineClass):
	submachine = getSubmachine(state)
	submachineName = getStateName(state)
	submachineType = getSubmachineType(submachine)

	if getSubmachineType(submachine) == VARIABLE_SUBMACHINE:
		# variable submachines, including variable dynamic
		# submachines, use setState_*() method to initialize a new
		# submachine instance

		# gwb
		# should use declared submachine class not the submachineName as the machine's type
		submachineClass = getVariableSubmachineClassName(submachine)
		instance = "%s %s %s = null;\n" % (string.joinfields(getStateAccessModifiers(state), " "), submachineClass, submachineName)
		instance = instance + "public void setState_%s(final %s submachine) {\n" % (submachineName, submachineClass)
		instance = instance + "%s = submachine;\n" % submachineName
		instance = instance + "}\n"

	elif submachineType in [ EXTERNAL_SUBMACHINE, REFLECT_SUBMACHINE, INNER_SUBMACHINE ] or isDynamicMachine(submachine):
		# non-variable submachines use state_*() method to initialize
		# a new submachine instance
		if isDynamicMachine(submachine):
			# a dynamic machine 
			dynamicSubmachineClass = getDynamicSubmachineClass(submachine, submachineName)
			instance = "%s DynamicMachine<%s> %s = null;\n" % (string.joinfields(getStateAccessModifiers(state), " "), dynamicSubmachineClass, submachineName)
			# generate state_?_element() method for dynamic machine
			instance = instance + \
					   "public %s state_%s_element(final Machine parentMachine, final int machineIndex, final MachineCode machineCode) throws Exception {\n" % \
					   (dynamicSubmachineClass, submachineName)
			instance = instance + "return %s;\n" % javasubnewinstance(getDynamicSubmachine(submachine), submachineName)
			instance = instance + "}\n"
			# generate state_?_element_constructor field for machine
			# array - defines how new machine array elements are
			# created - this constructor is called by state_?() method
			# associated with a machine array
			instance = instance + "private final MachineConstructor state_%s_element_constructor = new MachineConstructor() {\n" % submachineName
			instance = instance + "public Machine newInstance(final Machine parentMachine, final int machineIndex, final MachineCode machineCode) throws Exception {\n"
			# note that we reference the parent of parent, the latter
			# being the dynamic machine - since the dynamic machine
			# doesn't actually wrap the element as a Java class, then
			# the element is created in the context of the dynamic
			# machine's parent, not in the context of the dynamic
			# machine
			instance = instance + "return ((%s) parentMachine.getParentMachine()).state_%s_element(parentMachine, machineIndex, machineCode);\n" %(machineClass, submachineName)
			instance = instance + "}\n"
			instance = instance + "};\n"
		elif getSubmachineType(submachine) == EXTERNAL_SUBMACHINE:
			# external submachine reference of form fsm(p1,...)
			submachineClass = getExternalSubmachineClassName(submachine)
			instance = "%s %s %s = null;\n" % (string.joinfields(getStateAccessModifiers(state), " "), submachineClass, submachineName)
		elif getSubmachineType(submachine) == REFLECT_SUBMACHINE:
			# 'reflect' submachine reference of form reflect(arg1, arg2)
			instance = "%s TransitionMachine %s = null;\n" % (string.joinfields(getStateAccessModifiers(state), " "), submachineName)
		elif getSubmachineType(submachine) == INNER_SUBMACHINE:
			# an inner machine of form {states; xns}
			# i'm pleasantly surprised that the following works: the
			# variable name is the same as the variable's class
			instance = "%s %s %s = null;\n" % (string.joinfields(getStateAccessModifiers(state), " "), submachineName, submachineName)
			
		instance = instance + "public Machine state_%s(final Machine parentMachine, final int machineIndex, final MachineCode machineCode) throws Exception {\n" % submachineName
		instance = instance + "%s = %s;\n" % (submachineName, javasubnewinstance(submachine, submachineName))
		instance = instance + "return %s;\n" % submachineName
		instance = instance + "}\n"
		
	elif getSubmachineType(submachine) == NO_SUBMACHINE:
		# a basic machine instance is created by the runtime
		instance = ""

	entryAction = getActionBlock(getStateEntry(state))
	if entryAction == []:
		entry = ""
	else:
		entry = "public void state_%s_onEntry() throws Exception {\n" % submachineName
		entry = entry + javaaction(entryAction)
		entry = entry + "}\n"
	exitAction = getActionBlock(getStateExit(state))
	if exitAction == []:
		exit = ""
	else:
		exit = "public void state_%s_onExit() throws Exception {\n" % submachineName
		exit = exit + javaaction(exitAction)
		exit = exit + "}\n"
	rv = instance + entry + exit
	return rv

# helper method for javastate() - returns java code
# fragment for creating a new instance of the specified submachine
# structure isub associated with parent state named stateName
def javasubnewinstance(isub, stateName):
	instance = ""
	submachineType = getSubmachineType(isub)
	if isDynamicMachine(isub):
		dynSubmachineClass = getDynamicSubmachineClass(isub, stateName)
		# get machine bounds - mod parm no longer used
		[mod, bound] = getDynamicMachineModifier(isub)
		# STATE_?_ELEMENT_CONSTRUCTOR is a static field generated by
		# javasstate
		instance = 'new DynamicMachine<%s>(state_%s_element_constructor, %s, "MachineArray<%s>", parentMachine, machineIndex, machineCode)' % \
				   (dynSubmachineClass, stateName, javaexpression(bound), dynSubmachineClass)
	elif submachineType == EXTERNAL_SUBMACHINE:
		# external submachine reference of form fsm(p1,...)
		submachineClass = getExternalSubmachineClassName(isub)
		arglist = javaarglist(getExternalSubmachineArguments(isub))
		if arglist == "":
			arglist = "parentMachine, machineIndex, machineCode"
		else:
			arglist = arglist + ", parentMachine, machineIndex, machineCode"
		instance = "new %s(%s)" % (submachineClass, arglist)
	elif submachineType == REFLECT_SUBMACHINE:
		# 'reflect' submachine reference of form reflect(arg1, arg2)
		submachineClass = javaexpression(getReflectSubmachineClassName(isub))
		extArgs = javaexpression(getReflectSubmachineArguments(isub))
		instance = "(TransitionMachine) MachineConstructor.newInstance(%s, %s, parentMachine, machineIndex, machineCode)" % \
				   (submachineClass, extArgs)
	elif submachineType == INNER_SUBMACHINE:
		instance = "new %s(parentMachine, machineIndex, machineCode)" % (stateName)
	return instance	

# translate an abstract machine action block to java
def javaaction(actionBlock):
	rv = ""
	for action in getActions(actionBlock):
		# port send action
		if getActionType(action) == PORT_SEND:
			# translate port reference
			rv = rv + "((OutputPort) %s)" % javaexpression(getPortReference(action))
			# translate message reference
			rv = rv + ".output(%s, this);\n" % javaexpression(getMessageSendReference(action))
		# an expression
		else: 
			rv = rv + javaexpression(action) + ";\n"
	return rv

# translate a machine expression to a java expression
def javaexpression(ex):
	# ex may be a list or a irreducible element like a string or a
	# constant - initial list element may be an operator or a
	# irreducible element
	if type(ex) == types.ListType:
		if len(ex) == 0:
			return ""
		elif ex[0] == ASSIGN:
			return "(%s) = (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == PLUS_ASSIGN:
			return "(%s) += (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == MINUS_ASSIGN:
			return "(%s) -= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == STAR_ASSIGN:
			return "(%s) *= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == DIV_ASSIGN:
			return "(%s) /= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == MOD_ASSIGN:
			return "(%s) %= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == SR_ASSIGN:
			return "(%s) >>= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BSR_ASSIGN:
			return "(%s) >>>= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == SL_ASSIGN:
			return "(%s) <<= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BAND_ASSIGN:
			return "(%s) &= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BXOR_ASSIGN:
			return "(%s) ^= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BOR_ASSIGN:
			return "(%s) |= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == LOR:
			return "(%s) || (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == LAND:
			return "(%s) && (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BOR:
			return "(%s) | (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BXOR:
			return "(%s) ^ (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BAND:
			return "(%s) & (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == NOT_EQUAL:
			return "(%s) != (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == EQUAL:
			return "(%s) == (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == LT:
			return "(%s) < (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == GT:
			return "(%s) > (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == LE:
			return "(%s) <= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == GE:
			return "(%s) >= (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == SL:
			return "(%s) << (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == SR:
			return "(%s) >> (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == BSR:
			return "(%s) >>> (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == PLUS:
			return "(%s) + (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == MINUS:
			return "(%s) - (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == DIV:
			return "(%s) / (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == MOD:
			return "(%s) %% (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == STAR:
			return "(%s) * (%s)" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == INC:
			return "++(%s)" % javaexpression(ex[1])
		elif ex[0] == DEC:
			return "--(%s)" % javaexpression(ex[1])
		elif ex[0] == POST_INC:
			return "(%s)++" % javaexpression(ex[1])
		elif ex[0] == POST_DEC:
			return "(%s)--" % javaexpression(ex[1])
		elif ex[0] == BNOT:
			return "~(%s)" % javaexpression(ex[1])
		elif ex[0] == LNOT:
			return "!(%s)" % javaexpression(ex[1])
		elif ex[0] == UNARY_MINUS:
			return "-(%s)" % javaexpression(ex[1])
		elif ex[0] == UNARY_PLUS:
			return "+(%s)" % javaexpression(ex[1])
		elif ex[0] == METHOD_CALL:
			return "%s%s" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == ELIST:
			return "(%s)" % javaarglist(ex[1])
		elif ex[0] == NEW_EXPRESSION:
			rv = "new %s%s" % (javaexpression(ex[1]), javaexpression(ex[2]))
			if len(ex) == 4:
				# optional array initializer
				rv = rv + javaexpression(ex[3])
			return rv
		elif ex[0] == TYPECAST:
			return "((%s) %s)" % (javatype(ex[1]), javaexpression(ex[2]))
		elif ex[0] == INDEX_OP:
			return "%s[%s]" % (javaexpression(ex[1]), javaexpression(ex[2]))
		elif ex[0] == ARRAY_DECLARATOR:
			return string.joinfields(map(lambda x: "[%s]" % javaexpression(x), ex[1]), "")
		elif ex[0] == ARRAY_INIT:
			return "{%s}" % string.joinfields(map(javaexpression, ex[1:]), ", ")
		elif ex[0] == HOST_BLOCK:
			return string.strip(getHostCode(ex))
		else:
			# first element not a recognized (integer) operator so
			# treat as (dotted) identifier (i.e. primaryExpression)
			return string.joinfields(map(javaexpression, ex), ".")
	else:
		# irreducible element
		return ex

# generate settor/gettor method declarations and array index field
# declarations associated with dynamic submachine transition
# configurations - called by javaxn as part of generating transition
# definitions

# cfg is the tree-based state configuration referenced by a transition
# source or target - i is the integer index of the transition - srctgt
# identifies whether cfg is a source config or a target config -
# returns a string with the method and field declarations

def javacfg(cfg, i, srctgt):
	rv = javaindexaccessors(cfg, i, srctgt)
	if srctgt == "tgt":
		# machine binding only relevant for target cfgs
		rv = rv + javamachinebindinggettors(cfg, i, srctgt)
	return rv


def javamachinebindinggettors(cfg, i, srctgt):
	(cfgIndices, cfgMachineBindings) = javamachinebindingscfg(cfg, i)
	machineBindingGettors = ""
	for j in range(len(cfgIndices)):
		cfgMachineBinding = cfgMachineBindings[j]
		cfgIndex = cfgIndices[j]
		if cfgIndex != -1 and cfgMachineBinding != []:
			machineBindingGettors = machineBindingGettors + '''
    case %s:
	    return %s; 
''' % (cfgIndex, javaexpression(cfgMachineBinding))
	machineBindingGettors = '''
final private Machine get_transition_%s_%s_machine_binding(final int cfgIndex) throws Exception {
	switch (cfgIndex) {
%s
    default:
        throw new MachineException("No subconfiguration machine binding defined for subconfiguration index " + cfgIndex);
	}
}
''' % (i, srctgt, machineBindingGettors)
	return machineBindingGettors

def javaindexaccessors(cfg, i, srctgt):
	rv = ""
	# get all index accessors from all dynamic sub cfgs in the
	# specified cfg - also get the cfg index values associated with
	# the dynamic sub cfgs - the index value is used to uniquely
	# identify its associated accessor
	(cfgIndices, cfgIndexAccessors) = javaindexaccessorscfg(cfg, i)
	# use another index value (not the cfg index) to map a cached
	# array index value to an int array that is part of the machine
	# state
	if len(cfgIndices) != 0:
		userGettors = ""
		userSettors = ""
		cachedGettors = ""
		cachedSettors = ""
		for j in range(len(cfgIndices)):
			cfgIndexAccessor = cfgIndexAccessors[j]
			cfgIndex = cfgIndices[j]
			indexType = getDynamicSubconfigurationIndexAccessorType(cfgIndexAccessor)
			if indexType == GET_INDEX:
				userGettors = userGettors + '''
    case %s:
	    return %s; 
''' % (cfgIndex, javaexpression(getDynamicSubconfigurationIndexAccessorExpression(cfgIndexAccessor)))
			elif indexType == SET_INDEX:
				userSettors = userSettors + '''
    case %s:
	    %s = submachineIndex; 
		break;
''' % (cfgIndex, javaexpression(getDynamicSubconfigurationIndexAccessorExpression(cfgIndexAccessor)))
			else:
				pass
			cachedGettors = cachedGettors + '''
    case %s:
	    return transition_%s_%s_cached_indices[%s];
''' % (cfgIndex, i, srctgt, j)
			cachedSettors = cachedSettors + '''
    case %s:
	    transition_%s_%s_cached_indices[%s] = submachineIndex;
		break;
''' % (cfgIndex, i, srctgt, j)
		userGettors = '''
final private int get_transition_%s_%s_user_index(final int cfgIndex) throws Exception {
	switch (cfgIndex) {
%s
    default:
        throw new MachineException("No dynamic subconfiguration gettor defined for subconfiguration index " + cfgIndex);
	}
}
''' % (i, srctgt, userGettors)
		userSettors = '''
final private void set_transition_%s_%s_user_index(final int cfgIndex, final int submachineIndex) throws Exception {
	switch (cfgIndex) {
%s
    default:
	    throw new MachineException("No dynamic subconfiguration settor defined for subconfiguration index " + cfgIndex);
    }
}
''' % (i, srctgt, userSettors)
		cachedGettors = '''
final private int get_transition_%s_%s_cached_index(final int cfgIndex) throws Exception {
    switch (cfgIndex) {
%s
    default:
        throw new MachineException("No dynamic subconfiguration gettor defined for subconfiguration index " + cfgIndex);
	}
}''' % (i, srctgt, cachedGettors)
		cachedSettors = '''
final private void set_transition_%s_%s_cached_index(final int cfgIndex, final int submachineIndex) throws Exception {
    switch (cfgIndex) {
%s
    default:
        throw new MachineException("No dynamic subconfiguration settor defined for subconfiguration index " + cfgIndex);
	}
}''' % (i, srctgt, cachedSettors)
		cache = '''
final private int[] transition_%s_%s_cached_indices = new int[%s];
''' % (i, srctgt, len(cfgIndices))
		rv = cache + cachedGettors + cachedSettors + userGettors + userSettors
	return rv

# called by javaindexaccessors - recurses through the specified cfg in order to
# extract info related to all subconfigurations of all dynamic
# configurations occurring in the cfg - i is the integer index of the
# transition - srctgt identifies whether cfg is a source config or a
# target config - returns a pair (cfgIndices, cfgIndexAccessors) where
# cfgIndices is a list of index values that are assigned to
# subconfigurations of dynamic configurations (these indices are
# assigned in AbstractMachine.getDynamicStateConfiguration), and
# cfgIndexAccessors is an associated list of user-defined accessors for
# setting/getting a subconfiguration's array index

def javaindexaccessorscfg(cfg, i):
	cfgType = getConfigurationTreeType(cfg)
	cfgIndices = []
	cfgIndexAccessors = []
	if cfgType == DYNAMIC_CONFIG:
		cfgIndices += getDynamicSubconfigurationIndices(cfg)
		cfgIndexAccessors += getDynamicSubconfigurationIndexAccessors(cfg)
		(subCfgIndices, subCfgIndexAccessors) = javaindexaccessorscfglist(getDynamicSubconfigurations(cfg), i)
		cfgIndices += subCfgIndices
		cfgIndexAccessors += subCfgIndexAccessors
	elif cfgType in [ VARIABLE_CONFIG, BASIC_CONFIG ]:
		pass
	elif cfgType == MULTI_CONFIG:
		(subCfgIndices, subCfgIndexAccessors) = javaindexaccessorscfglist(getSubconfigurationTree(cfg), i)
		cfgIndices += subCfgIndices
		cfgIndexAccessors += subCfgIndexAccessors
	elif isPseudoState(cfgType):
		pass
	return (cfgIndices, cfgIndexAccessors)

# auxilliary function to support javaindexaccessorscfg

def javaindexaccessorscfglist(cfglist, i):
	cfgIndices = []
	cfgIndexAccessors = []
	for subcfg in cfglist:
		(subCfgIndices, subCfgIndexAccessors) = javaindexaccessorscfg(subcfg, i)
		cfgIndices += subCfgIndices
		cfgIndexAccessors += subCfgIndexAccessors
	return (cfgIndices, cfgIndexAccessors)

# called by javamachinebindings - recurses through the specified cfg
# in order to extract info related to all subconfigurations of all
# multistate configurations with machine binding gettors occurring in
# the cfg - i is the integer index of the transition - srctgt
# identifies whether cfg is a source config or a target config -
# returns a pair (cfgIndices, cfgMachinebindings) where cfgIndices is
# a list of index values that are assigned to subconfigurations of
# configurations (these indices are assigned in
# AbstractMachine.getMultiStateConfiguration), and cfgMachinebindings
# is an associated list of user-defined gettors for getting a
# subconfiguration's machine binding

def javamachinebindingscfg(cfg, i):
	cfgType = getConfigurationTreeType(cfg)
	cfgIndices = []
	cfgMachinebindings = []
	if cfgType == DYNAMIC_CONFIG:
		(subCfgIndices, subCfgMachinebindings) = javamachinebindingscfglist(getDynamicSubconfigurations(cfg), i)
		cfgIndices += subCfgIndices
		cfgMachinebindings += subCfgMachinebindings
	elif cfgType in [ VARIABLE_CONFIG, BASIC_CONFIG ]:
		pass
	elif cfgType == MULTI_CONFIG:
		cfgIndices += getMultiSubconfigurationIndices(cfg)
		cfgMachinebindings += getMultiSubconfigurationMachineBindings(cfg)
		(subCfgIndices, subCfgMachinebindings) = javamachinebindingscfglist(getSubconfigurationTree(cfg), i)
		cfgIndices += subCfgIndices
		cfgMachinebindings += subCfgMachinebindings
	elif isPseudoState(cfgType):
		pass
	return (cfgIndices, cfgMachinebindings)

# auxilliary function to support javamachinebindingscfg

def javamachinebindingscfglist(cfglist, i):
	cfgIndices = []
	cfgMachinebindings = []
	for subcfg in cfglist:
		(subCfgIndices, subCfgMachinebindings) = javamachinebindingscfg(subcfg, i)
		cfgIndices += subCfgIndices
		cfgMachinebindings += subCfgMachinebindings
	return (cfgIndices, cfgMachinebindings)

# generate methods associated with a given message/messageless
# transition
def javaxn(xn, i, machineClass):
	# get declarations for any src/tgt dynamic index methods and
	# initializers from transition src/tgt configs
	dynCfgDecls = javacfg(getConfigurationTree(getSourceConfiguration(xn)), i, "src")
	return dynCfgDecls + javaport(xn, i, machineClass) + javaxntgt(xn, i, machineClass, [], getTransitionTargets(xn))

def javaport(xn, i, machineClass):
	if isMessagelessTransition(xn):
		return ""
	portRef = getTransitionPort(xn)
	if isDelayTransition(xn):
		rv = "TransitionTimerPort transition_%s_port = null;\n" % i
		rv = rv + "public TransitionTimerPort transition_%s_port() {\n" % i
		rv = rv + "if (transition_%s_port == null) transition_%s_port = new TransitionTimerPort(this, new TransitionTimerPortDurationMethod() { public final long invoke(final Machine machine) throws Exception { return ((%s) machine).transition_%s_port_duration(); } });\n" % (i, i, machineClass, i)
		rv = rv + "return transition_%s_port;\n" % i
		rv = rv + "}\n"
		rv = rv + "public long transition_%s_port_duration() throws Exception {\n" % i
		rv = rv + "return %s;\n" % javaexpression(getTransitionMessageClass(xn))
		rv = rv + "}\n"
	elif isAnyPortTransition(xn):
		rv = "public AnyPort transition_%s_port() {\n" % i
		rv = rv + "return AnyPort.ANY_PORT;\n"
		rv = rv + "}\n"
	else:
		rv = "public LocalPort transition_%s_port() {\n" % i
		rv = rv + "return " + javaexpression(portRef) + ";\n"
		rv = rv + "}\n"
	return rv

def javaxntgt(xn, i, machineClass, guard, tgt):
	if isCompoundTarget(tgt):
		rv = ""
		# concatenate results returned by recursively invoking
		# this method for each transition target
		j = 1
		for subtgt in getCompoundTargets(tgt):
			subi = "%s_%s" % (i, j)
			j = j + 1
			rv = rv + javaxntgt(xn, subi, machineClass, 
								getGuardedTargetGuard(subtgt),
								getGuardedTargetTarget(subtgt))
		rv = rv + javaxnguard(xn, i, guard)
	else:
		# tgt is a basic tgt
		dynCfgDecls =  javacfg(getConfigurationTree(getTargetConfiguration(tgt)), i, "tgt")
		# can ignore dynTgtInit since guaranteed to be empty string
		# for a tgt cfg
		rv = dynCfgDecls + javaxnguard(xn, i, guard) + javaxnaction(xn, i, getTargetAction(tgt))
	return rv

def javaxnguard(xn, i, guard):
	if guard == []:
		return ""
	if isMessagelessTransition(xn):
		# messageless transition
		rv = "public boolean transition_%s_guard() throws Exception {\n" % i
		rv = rv + "return " + javaexpression(guard) + ";\n"
		rv = rv + "}\n"
	else:
		# message transition
		if isDelayTransition(xn):
			rv = "public boolean transition_%s_guard() throws Exception {\n" % i
		else:
			rv = "public boolean transition_%s_guard(final LocalPort port, final %s message) throws Exception {\n" % \
					(i, javatype(getTransitionMessageClass(xn)))
		rv = rv + "return " + javaexpression(guard) + ";\n"
		rv = rv + "}\n"
	return rv

def javaxnaction(xn, i, action):
	if action == []:
		return ""
	if isMessagelessTransition(xn):
		# messageless transition
			rv = "public void transition_%s_action() throws Exception {\n" % i
			rv = rv + javaaction(action)
			rv = rv + "}\n"
	else:
		# message transition
		if isDelayTransition(xn):
			rv = "public void transition_%s_action(final long duration, final long activationTime, final long expiryTime) throws Exception {\n" % i
		else:
			rv = "public void transition_%s_action(final LocalPort port, final %s message) throws Exception {\n" % \
					 (i, javatype(getTransitionMessageClass(xn)))
		rv = rv + javaaction(action) + ";\n"
		rv = rv + "}\n"
	return rv

# declares a submachine's class declaration and constructor - calls
# javabody to declare a submachine's methods and variables

# stateName is name of parent state containing the machine,
# machineClass is fully-qualified parent machine's classname, isub is
# the post-processed abstract submachine

def javasub(isub, stateName, machineClass):
	submachineType = getSubmachineType(isub)
	if isDynamicMachine(isub):
		if getDynamicSubmachineType(isub) == INNER_SUBMACHINE:
			# generate inner class definition for inner submachine wrapped
			# by dynamic submachine
			rv = javasubinnermachine(getDynamicSubmachine(isub), stateName, machineClass)
		else:
			rv = ""
	elif submachineType in [ EXTERNAL_SUBMACHINE, REFLECT_SUBMACHINE, VARIABLE_SUBMACHINE ]:
		# do nothing 
		rv = ""
	elif submachineType == NO_SUBMACHINE:
		# do nothing for a basic (primitive) machine
		rv = ""
	elif submachineType == INNER_SUBMACHINE:
		# generate inner class definition for inner submachine
		rv = javasubinnermachine(isub, stateName, machineClass)
	return rv

# helper method for javasub() that returns java inner class definition
# for the specified inner submachine isub with parent state named
# stateName and parent state class machineClass - recursively calls
# javabody()
def javasubinnermachine(isub, stateName, machineClass):
	submachineName = stateName
	submachineClass = "%s.%s" % (machineClass, submachineName)
	rv = "// Declarations for %s\n" % submachineClass
	# transition machine
	rv = rv + "public class %s extends TransitionMachine {\n" % submachineName
	rv = rv + "public %s(final Machine parentMachine, final int machineIndex, final MachineCode machineCode) throws Exception {\n" % submachineName
	rv = rv + "super(%s_states, %s_messageTransitions, %s_messagelessTransitions, %s.class.getName(), parentMachine, machineIndex, machineCode);\n" % \
		 (stateName, stateName, stateName, submachineClass)
	rv = rv + "}\n"
	# generate body for inner machine
	rv = rv + javabody(isub, stateName, submachineClass)
	rv = rv + "}\n"
	return rv

# generates method to clear a variable referencing a specified
# submachine instance - these variables are declared and set by
# methods declared in javastate

def javaclearstateref(states):
	rv = "final protected void clearSubmachineReference(final int index) {\n"
	rv = rv + "switch(index) {\n"
	index = 0
	for state in states:
		if getSubmachineType(getSubmachine(state)) != NO_SUBMACHINE:
			rv = rv + "case %s: %s = null; break;\n" % (index, getStateName(state))
		index = index + 1
	rv = rv + "default: break;\n}\n"
	return rv + "}\n"	

# generates methods and date members for the machine and its
# submachines - a (sub)machine's class declaration and constructor are
# generated in javatop() or javasub()

# machine is the post-processed abstract machine, stateName is name of
# parent state containing the machine, machineClass is fully-qualified
# machine classname,

def javabody(machine, stateName, machineClass):
	rv = ""
	# generate host blocks
	for hostBlock in getHostBlocks(machine):
		rv = rv + getHostBlockComment(hostBlock) + "\n"
		rv = rv + echartsLineReference(getHostBlockLineColumn(hostBlock), getHostCode(hostBlock) + ";\n")
	# generate state methods
	for state in getStates(machine):
		rv = rv + echartsLineReference(getStateLineColumn(state), javastate(state, machineClass))
	rv = rv + javaclearstateref(getStates(machine))
	# generate transition methods
	count = 1
	for xn in getTransitions(machine):
		rv = rv + echartsLineReference(getTransitionLineColumn(xn), javaxn(xn, count, machineClass))
		count = count + 1
	# declare submachines
	for state in getStates(machine):
		rv = rv + javasub(getSubmachine(state), getStateName(state), machineClass)
	return rv

# translates a list of arguments from abstract machine to java
def javaarglist(args):
	argStrings = []
	for arg in args:
		argStrings = argStrings + [ javaexpression(arg) ]
	return string.joinfields(argStrings, ", ")

def echartsLineReference(topLineColumn, javaCode):
	if javaCode == "":
		return ""
	else:
		topTag = "// ECharts source top line tag: %s\n" % topLineColumn[0]
		bottomTag = "// ECharts source bottom line tag: %s\n" % topLineColumn[0]
		return topTag + javaCode + bottomTag

# Generate java for top-level machine class and its submachine
# classes.
def javatop(machine, machineName):
	machineClass = machineName
	if getExtendsClause(machine) == None:
		extends = "TransitionMachine"
	else:
		extends = string.joinfields(getExtendsClause(machine), ".")
	if getImplementsClause(machine) == None:
		implements = ""
	else:
		implementsClasses = []
		for interface in getImplementsClause(machine):
			implementsClasses = implementsClasses + [ string.joinfields(interface, ".") ]
		implements = " implements %s" % string.joinfields(implementsClasses, ", ")
	rv = getMachineComment(machine) + "\n"
	rv = rv + "public class %s extends %s%s {\n" % (machineClass, extends, implements)
	# Define static members and methods for top-level machine and its
	# submachines
	rv = rv + javastatic(machine, machineName, machineClass)
	rv = rv + "// Declarations for %s\n" % machineClass
	# Define top-level machine constructors
	rv = rv + javaconstructors(machine, machineName, machineClass)
	# Define instance members, methods and subclasses for top-level
	# machine and its submachines
	rv = rv + javabody(machine, machineName, machineClass)
	return rv

def javaconstructors(machine, machineName, machineClass):
	rv = ""
	constructors = getConstructors(machine)
	if len(constructors) > 0:
		# generate user defined constructors
		for constructor in getConstructors(machine):
			rv = rv + echartsLineReference(getConstructorLineColumn(constructor), javaconstructor(constructor, machineName, machineClass))
	else:
		# no user-defined constructors so generate default
		# constructors
		rv = "public %s(final Machine parentMachine, final int machineIndex, final MachineCode machineCode) throws Exception {\n" % machineClass
		rv = rv + "super(%s_states, %s_messageTransitions, %s_messagelessTransitions, %s.class.getName(), parentMachine, machineIndex, machineCode);\n" % \
			 (machineName, machineName, machineName, machineClass)
		rv = rv + "}\n"
		# constructor called when creating machine as top-level machine
		rv = rv + "public %s() throws Exception {\n" % machineClass
		rv = rv + "this(null, -1, null);\n"
		rv = rv + "}\n"
	return rv			 

# Generate machine constructors given an abstract machine
# constructor.
def javaconstructor(constructor, machineName, machineClass):
	# constructor header
	accessString = string.joinfields(getConstructorAccessModifiers(constructor), " ")
	rv = "%s %s(" % (accessString, machineClass)
	userParamStrings = []
	for param in getConstructorParameters(constructor):
		userParamStrings = userParamStrings + [ javatype(param[0]) + " " + param[1] ]
	paramStrings = userParamStrings + [ "final Machine parentMachine", "final int machineIndex",
									"final MachineCode machineCode" ]
	rv = rv + string.joinfields(paramStrings, ", ") + ") throws Exception {\n"
	rv = rv + "super(%s_states, %s_messageTransitions, %s_messagelessTransitions, %s.class.getName(), parentMachine, machineIndex, machineCode);\n" % \
		 (machineName, machineName, machineName, machineClass)
	# constructor body
	rv = rv + javaaction(getConstructorActionBlock(constructor)) + "}\n"
	# constructor called when creating machine as top-level machine
	rv = rv + getConstructorComment(constructor) + "\n"
	rv = rv + "%s %s(" % (accessString, machineClass)
	rv = rv + string.joinfields(userParamStrings, ", ") + ") throws Exception {\n"
	rv = rv + "this("
	userParamStrings = []
	for param in getConstructorParameters(constructor):
		userParamStrings = userParamStrings + [ param[1] ]
	paramStrings = userParamStrings + [ "null", "-1", "null" ]
	rv = rv + string.joinfields(paramStrings, ", ") + ");\n"
	return rv + "}\n"
	
# Convert a variable type declaration to a string.
def javatype(type):
	typeId = string.joinfields(getTypeIdentifier(type), ".")
	typeArray = reduce(lambda x,y: "%s%s" % (x, y), getTypeArrayDeclarator(type), "")
	return typeId + typeArray

def javamachine(compilationUnit):
	machine = getMachine(compilationUnit)
	name = getMachineName(compilationUnit)
	return javatop(machine, name) + "}\n"

# Translate an abstract machine to a string constituting a Java
# program.
def translate(compilationUnit, machine, targetDirectory, opts):
	header = """//
// This file was generated by ech2java. Do not modify.
//

"""
	# package declaration
	package = ""
	if len(getPackage(compilationUnit)) > 0:
		packageString = "package " + string.joinfields(getPackage(compilationUnit), ".") + ";\n"
		package = echartsLineReference(getPackageLineColumn(compilationUnit), packageString) + "\n"
	# imports
	imports = "import org.echarts.*;\n"
	imports = imports + "import org.echarts.monitor.*;\n"
	for imported in getImports(compilationUnit):
		importedPackage = getImportPackage(imported)
		importModifiers = getImportModifiers(imported)
		importString = "import %s %s;\n" % (string.joinfields(importModifiers, " "), string.joinfields(importedPackage, ".") )
		imports = imports + echartsLineReference(getImportLineColumn(imported), importString)
	imports = imports + "\n"
	# the machine itself
	machine = javamachine(compilationUnit)
	# the translated program
	rv = header + package + imports + machine
	# return the program
	return rv
