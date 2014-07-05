########################################################################
#                                                                      #
#               This software is part of the ECharts package           #
#                  Copyright (c) 2006 AT&T Corp.                       #
#                      and is licensed under the                       #
#                  Common Public License, Version 1.0                  #
#                            by AT&T Corp.                             #
#                                                                      #
########################################################################

# Common front-end invoked by various ECharts machine translators
# e.g. ech2java. Processes command line arguments. Determines machine
# dependencies and relative modification dates between an '.ech' file
# and its translated file in order to decide if translator should be
# invoked for a machine or not.

import sys, getopt, string, os, os.path, stat, imp

binPath = os.path.dirname(os.path.abspath(sys.argv[0]))
translatorPath = os.path.dirname(binPath)
libPath = translatorPath + os.sep + "lib"

# add lib dir to python path
sys.path.insert(0, libPath)
import AbstractMachine

# add lib sudirectories to python path
for name in os.listdir(libPath):
	path = libPath + os.sep + name
	if os.path.isdir(path):
		sys.path.insert(0, path)

import versioncheck
# Check python version
#
if not versioncheck.versioncheck(min='2.2', max='2.6.99'):
    print "Unsupported version of python"
    print "Use a version between 2.2.x and 2.6.x"
    sys.exit(1)

_version = "1.3.1-beta"

def getVersion():
	return '%s version %s' % (ech2x, _version)

# globals - see main()
True = 1
False = 0
ech2x = "ech2x"
ext = ""
translator = ""
echartsPath = ""
translateDependencies = True
printDependencies = False
opts = []
targetBase = ""
packageSubdirectory = ""

# Used to represent set of echarts files that have already been
# translated or that are in the process of being translated. Key is
# absolute file path of echarts file. Value is the file's associated
# AbstractMachine instance.
translationDict = {}

# Translate specified ECharts machine file to X machine file using
# specified echartsPath to locate ECharts machine files on which this
# specified ECharts machine file depends. Translates any ECharts
# machine files on which specified machine file depends if
# necessary. A X machine file is created if no machine file currently
# exists for the specified ECharts machine file, or if a ECharts
# machine file upon which the specified ECharts machine file depends
# has been modified more recently than the specified ECharts machine
# file, or if the specified ECharts machine file has been modified
# more recently than its X machine file. Returns AbstractMachine
# instance if a new X machine file created for the specified ECharts
# machine file, otherwise returns None.
def translateMachine(machineFilePath):
	global ech2x, ext, translator, echartsPath,\
		   translateDependencies, translationDict
	absoluteMachineFilePath = os.path.abspath(machineFilePath)
	try:
		# check if we're already translating/translated
		machine = translationDict[absoluteMachineFilePath]
		# we are, so nothing to do
		return None
	except KeyError:
		# first time we've encountered the file so obtain its
		# AbstractMachine instance and make note of it in
		# translationDict
		try:
			machine = AbstractMachine.AbstractMachine(absoluteMachineFilePath, echartsPath)
			postProcessedCompilationUnit = machine.postProcess()
		except Exception, message:
			# exception encountered parsing or post-processing the
			# ECharts machine file so exit
			sys.stderr.write("%s\n" % message)
			# comment next line out for production
			raise
			sys.exit(1)
		except AbstractMachine.AbstractMachineException, message:
			# exception encountered parsing or post-processing the
			# ECharts machine file so exit
			sys.stderr.write("%s\n" % message)
			# comment next line out for production
			raise
			sys.exit(1)
		translationDict[absoluteMachineFilePath] = machine
		echFileModTime = os.stat(absoluteMachineFilePath)[stat.ST_MTIME]
		xFilePath = getTargetFilePath(machine, ext)
		if os.path.exists(xFilePath):
			xFileModTime = os.stat(xFilePath)[stat.ST_MTIME]
		else:
			xFileModTime = 0
		dependencyModified = False
		if translateDependencies:
			# recursively translate dependencies before translating
			# specified machine
			dependencies = machine.getDependencies()
			for depMachine in dependencies:
				if not translateMachine(depMachine.absoluteMachineFilePath) == None:
					dependencyModified = True
				elif not dependencyModified:
					# dependency not modified but check that its X file
					# modification date is earlier than modification date
					# of X file associated with specified ECharts
					# machine file
					depXFilePath = getTargetFilePath(depMachine, ext)
# for jython
#					if True:
					if os.access(depXFilePath, os.F_OK):
						# file exists so check its mod time
						depXFileModTime = os.stat(depXFilePath)[stat.ST_MTIME]
						if depXFileModTime > xFileModTime:
							dependencyModified = True
		if printDependencies:
			depMachinePaths = []
			for depMachine in machine.getDependencies():
				depMachinePaths.append(depMachine.absoluteMachineFilePath)
			print "%s: dependencies for %s: %s" % (ech2x, absoluteMachineFilePath, string.joinfields(depMachinePaths, ","))
		# now that dependencies have been translated we can translate the
		# specified machine if necessary
		if not dependencyModified and xFileModTime > echFileModTime:
			# no need to create a new X machine file since
			# nothing has changed
			return None
		# dependencies were modified, or x machine file doesn't
		# exist, or x machine file older than its echarts file so
		# generate a new file
		ofd = open(xFilePath, 'w')
		print "%s: writing %s" % (ech2x, xFilePath)
		try:
			# load translator module if not already loaded, invoke its
			# translate function, and write result to file
			try: 
				mod = sys.modules[translator]
			except KeyError:
				(modfile, modpathname, moddescription) = imp.find_module(translator)
				mod = imp.load_module(translator, modfile, modpathname, moddescription)
			ofd.write(apply(getattr(mod, "translate"), [ postProcessedCompilationUnit, machine, \
														 os.path.dirname(xFilePath), opts ]))
		except Exception, message:
			# exception encountered parsing or post-processing the
			# ECharts machine file so remove file and exit
			sys.stderr.write("%s\n" % message)
			os.remove(xFilePath)
			# comment next line out for production
			raise
			sys.exit(1)
		ofd.close()
		return machine

# Return file path for translation target based on specified machine
# and target file extension. If target directory path specified on
# ech2x command line then return target file path relative to
# specified target directory, otherwise return file path in machine's
# source directory. If target directory doesn't exist then attempt to
# create it.
def getTargetFilePath(machine, tgtExt):
	global targetBase
	global packageSubdirectory
	sourceDirectoryPath = string.split(os.path.dirname(machine.absoluteMachineFilePath), os.sep)
	compilationUnit = machine.getCompilationUnit()
	name = AbstractMachine.getMachineName(compilationUnit)
	package = AbstractMachine.getPackage(compilationUnit)
	sourceBase = sourceDirectoryPath[:len(sourceDirectoryPath)-len(package)]
	if targetBase == "":
		targetBaseList = sourceBase
	else:
		targetBaseList = string.split(targetBase, os.sep)
	if packageSubdirectory == "":
		packageSubdirectoryList = []
	else:
		packageSubdirectoryList = [ packageSubdirectory ]
	targetDir = string.joinfields(targetBaseList + package + packageSubdirectoryList, os.sep)
	if not os.path.exists(targetDir):
		# if target dir doesn't exist then attempt to make it
		os.makedirs(targetDir)
	return targetDir + os.sep + name + "." + tgtExt

def appendMachine(machine, machines):
	if not machine == None:
		machines.append(machine)

# Return list of filepaths of echarts files found in specified
# package and in any subpackages of the package.
def getSubpackageFilepaths(pkgName):
	global echartsPath
	filepaths = []
	pkgSubpath = string.joinfields(string.split(pkgName, "."), os.sep)
	# find directory path for package
	for epath in string.split(echartsPath, os.pathsep):
		pkgPath = epath + os.sep + pkgSubpath
		if os.path.exists(pkgPath) and os.path.isdir(pkgPath):
			os.path.walk(pkgPath, getEchFilepaths, filepaths)
	return filepaths

# Return list of filepaths of echarts files found in specified
# package.
def getPackageFilepaths(pkgName):
	global echartsPath
	global ech2x
	filepaths = []
	pkgSubpath = string.joinfields(string.split(pkgName, "."), os.sep)
	# find directory path for package
	for epath in string.split(echartsPath, os.pathsep):
		pkgPath = epath + os.sep + pkgSubpath
		if os.path.exists(pkgPath) and os.path.isdir(pkgPath):
			getEchFilepaths(filepaths, pkgPath, os.listdir(pkgPath))
			if filepaths == []:
				sys.stderr.write("%s: error: no \".ech\" files found for package: %s\n" % (ech2x, pkgName))
				sys.exit(1)
			else:
				break
	if filepaths == []:
		sys.stderr.write("%s: error: package not found: %s\n" % (ech2x, pkgName))
		sys.exit(1)
	return filepaths

def getEchFilepaths(filepaths, pkgPath, dirlist):
	for entry in dirlist:
		if entry[-4:] == '.ech':
			filepaths.append(pkgPath + os.sep + entry)

def getWin32CommandPath(cmd):
	if not os.environ.has_key('PATH') or os.environ['PATH'] == '': 
		p = os.defpath 
	else: 
		p = os.environ['PATH'] 
	pathlist = p.split (os.pathsep) 
	for path in pathlist: 
		f = os.path.join(path, cmd + ".exe") 
		if os.access(f, os.X_OK): 
			return f 
	return None

def commonOptionsUsage(commonOptions, hiddenCommonOptions):
	rv = ""
	for option in commonOptions.keys():
		if not option in hiddenCommonOptions:
			rv = rv + string.ljust("--%s" % option, 25) + commonOptions[option] + "\n"
	return rv

def processCommandLine(ech2xp, extp, translatorp, xlongoptspec, xusagesummary,
					   xusageoptions, xhiddencommonoptions):

	global opts
	global ech2x
	global ext
	global translator
	global echartsPath
	global translateDependencies
	global printDependencies
	global targetBase
	global packageSubdirectory

	targetBase = ""
	translateDependencies = True
	ech2x = ech2xp
	ext = extp
	subpackages = []
	packageSubdirectory = ""

	commonoptions = {}
	commonoptions["echartspath"] = "'%s' separated list specifying directories searched for .ech files and packages" % os.pathsep
	commonoptions["no-dependencies"] = "Do not translate .ech files upon which the specified .ech files depend"
	commonoptions["target-directory"] = "Directory path specifying where to write translated files to"
	commonoptions["package-subdirectory"] = "Package subdirectory name specifying where to write translated files to"
	commonoptions["subpackages"] = "'%s' separated list specifying package names recursively searched for .ech files" % os.pathsep
	commonoptions["version"] = "Print translator version and exit"
	commonoptions["help"] = "Print this message and exit"

	# initialize name of translator module
	if translatorp == "":
		translator = ext + "machine"
	else:
		translator = translatorp

	# combine xlongopts with common longopts
	longoptspec = xlongoptspec + ['echartspath=', 'no-dependencies', \
								  'target-directory=', 'subpackages=', \
								  'print-dependencies', \
								  'package-subdirectory=', 'version', 'help']

	# combine xusage with common usage
	usage = """Usage: %s [options] [echartsfilenames] [echartspackagenames]
%s
options:
%s
%s
""" % (ech2x, xusagesummary, xusageoptions, commonOptionsUsage(commonoptions, xhiddencommonoptions))

	if len(sys.argv) == 1:
		sys.stderr
		sys.stderr.write(usage + '\n')
		sys.exit(1)

	# use ECHARTSPATH from process environment by default
	try:
		echartsPath = os.environ['ECHARTSPATH']
	except KeyError:
		# no problem if ECHARTSPATH undefined
		echartsPath = ""

	try:
		opts, args = getopt.getopt(sys.argv[1:], '', longoptspec)
	except getopt.GetoptError, message:
		sys.stderr.write(usage + "\n")
		sys.exit(1)
	for arg, val in opts:
		if arg == '--echartspath':
			# overwrite default echartsPath value
			echartsPath = val
		elif arg == '--no-dependencies':
			translateDependencies = False
		elif arg == '--print-dependencies':
			printDependencies = True
		elif arg == '--target-directory':
			targetBase = val
		elif arg == '--subpackages':
			subpackages = string.split(val, os.pathsep)
		elif arg == '--package-subdirectory':
			packageSubdirectory = val
		elif arg == '--version':
			print getVersion()
			print AbstractMachine.getVersion()
			sys.exit(0)
		elif arg == '--help':
			print usage
			sys.exit(0)

	# ensure files to translate are specified
	if len(args) == 0  and subpackages == []:
		sys.stderr.write("%s: must specify files or packages to translate\n" % ech2x)
		sys.exit(1)

	return (subpackages, args)

# Invoked by translator front-end e.g. ech2java. 'ech2px' specifies
# translator command e.g. 'ech2java', 'extp' specifies file extension
# of translated file e.g. 'java', 'translatorp' specifies name of
# translator module to use when translating machine, 'xoptspec' and
# 'xlongoptspec' specify Python getopt() arguments specific to the
# front-end, 'xusagesummary' is the usage summary string for the
# front-end. 'xusageoptions' is a string explaining the translator's
# common line options, and xhiddenoptions is a list of the ech2x
# common options (without the leading '--') that should not be
# included in the usage summary e.g. ech2javadoc hides the
# 'package-subdirectory' and 'no-dependencies' common options because
# it uses them internally.
def main(ech2xp, extp, translatorp, xlongoptspec, xusagesummary,
		 xusageoptions, xhiddencommonoptions):

	(subpackages, args) = processCommandLine(ech2xp, extp, translatorp, xlongoptspec,
											 xusagesummary, xusageoptions, xhiddencommonoptions)
	machines = []

	for pkg in subpackages:
		for filepath in getSubpackageFilepaths(pkg):
			appendMachine(translateMachine(filepath), machines)

	for arg in args:
		if arg[-4:] == ".ech":
			# arg specifies an echarts filepath
			appendMachine(translateMachine(arg), machines)
		else:
			# arg specifies a package
			for filepath in getPackageFilepaths(arg):
				appendMachine(translateMachine(filepath), machines)

	return machines

